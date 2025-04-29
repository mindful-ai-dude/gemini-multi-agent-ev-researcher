"""Research agent for analyzing EV charging infrastructure."""

from datetime import datetime
from typing import List, Dict
from .base_agent import BaseAgent
from .synthesis_agent import SynthesisAgent
from ..api.nrel_api import NRELAPIClient
from ..models.data_models import ResearchReport, InfrastructureAnalysis, ChargingStation

class EVResearchAgent(BaseAgent):
    """Agent for researching and analyzing EV charging infrastructure."""
    
    def __init__(self, nrel_api_key: str, gemini_api_key: str, model_name: str, temperature: float = 0.7):
        """Initialize the research agent."""
        super().__init__(gemini_api_key, model_name, temperature)
        self.nrel_client = NRELAPIClient(nrel_api_key)
        self.synthesis_agent = SynthesisAgent(gemini_api_key, model_name, temperature)
    
    async def generate_report(self, city: str, state: str) -> ResearchReport:
        """
        Generate a comprehensive report about EV charging infrastructure in a city.
        
        Args:
            city: City name
            state: Two-letter state code
            
        Returns:
            ResearchReport object containing analysis and recommendations
        """
        # Geocode city/state to latitude/longitude
        latitude, longitude = await self.nrel_client.geocode_city_state(city, state)
        # Fetch charging station data
        stations = await self.nrel_client.get_stations(latitude, longitude)

        # Analyze infrastructure
        analysis = self._analyze_infrastructure(stations)
        
        # Generate summary and recommendations using Gemini AI
        summary_prompt = f"""
        Analyze the following EV charging infrastructure data for {city}, {state}:
        - Total stations: {analysis.total_stations}
        - Stations by type: {self._format_data_for_prompt(analysis.stations_by_type)}
        - Coverage score: {analysis.coverage_score:.2f}/10.0
        - Identified gaps: {', '.join(analysis.gaps_identified)}
        
        Provide a concise summary of the current state of EV charging infrastructure.
        """
        
        recommendations_prompt = f"""
        Based on the following EV charging infrastructure analysis for {city}, {state}:
        - Total stations: {analysis.total_stations}
        - Stations by type: {self._format_data_for_prompt(analysis.stations_by_type)}
        - Coverage score: {analysis.coverage_score:.2f}/10.0
        - Identified gaps: {', '.join(analysis.gaps_identified)}
        
        Provide 3-5 specific recommendations for improving the charging infrastructure.
        Format each recommendation as a bullet point.
        """
        
        summary = await self.generate_content_async(summary_prompt)
        recommendations_text = await self.generate_content_async(recommendations_prompt)
        recommendations = [r.strip('- ') for r in recommendations_text.split('\n') if r.strip()]
        
        # Create and return the report
        return ResearchReport(
            city=city,
            state=state,
            date_generated=datetime.now(),
            infrastructure_analysis=analysis,
            stations=stations,
            summary=summary,
            recommendations=recommendations
        )
    
    def _analyze_infrastructure(self, stations: List[ChargingStation]) -> InfrastructureAnalysis:
        """Analyze charging station infrastructure."""
        # Count stations by connector type
        stations_by_type = {}
        for station in stations:
            for connector in station.connector_types:
                stations_by_type[connector] = stations_by_type.get(connector, 0) + 1
        
        # Calculate coverage score (simple version)
        coverage_score = min(len(stations) / 10, 10)  # 1 point per 10 stations, max 10
        
        # Identify gaps
        gaps = []
        if len(stations) < 10:
            gaps.append("Insufficient number of charging stations")
        if not any(t.startswith("DC") for s in stations for t in s.connector_types):
            gaps.append("No DC fast charging stations available")
        if not any(s.access_type == "public" for s in stations):
            gaps.append("Limited public charging access")
        
        return InfrastructureAnalysis(
            total_stations=len(stations),
            stations_by_type=stations_by_type,
            coverage_score=coverage_score,
            recommendations=[],  # Will be filled by Gemini AI
            gaps_identified=gaps
        )
    
    async def save_report(self, report: ResearchReport, output_path: str, format: str = "markdown") -> None:
        """Save the report in the specified format."""
        if format == "markdown":
            with open(output_path, "w") as f:
                f.write(report.to_markdown())
        else:
            # Convert to other formats using the synthesis agent
            await self.synthesis_agent.convert_format(
                input_path=output_path.replace(f".{format}", ".md"),
                output_path=output_path,
                output_format=format
            )
