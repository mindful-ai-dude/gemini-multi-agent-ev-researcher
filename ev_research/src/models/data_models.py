"""Data models for the EV Research application."""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class ChargingStation:
    """Represents an EV charging station."""
    station_id: str
    name: str
    latitude: float
    longitude: float
    address: str
    city: str
    state: str
    zip_code: str
    status: str
    access_type: str
    connector_types: List[str]
    network: Optional[str] = None
    hours: Optional[str] = None
    pricing: Optional[str] = None

@dataclass
class InfrastructureAnalysis:
    """Analysis of EV charging infrastructure in a region."""
    total_stations: int
    stations_by_type: Dict[str, int]
    coverage_score: float
    recommendations: List[str]
    gaps_identified: List[str]

@dataclass
class ResearchReport:
    """Complete research report for a city's EV infrastructure."""
    city: str
    state: str
    date_generated: datetime
    infrastructure_analysis: InfrastructureAnalysis
    stations: List[ChargingStation]
    summary: str
    recommendations: List[str]
    
    def to_markdown(self) -> str:
        """Convert the report to markdown format."""
        md = f"""# EV Charging Infrastructure Report: {self.city}, {self.state}
Generated: {self.date_generated.strftime('%Y-%m-%d %H:%M:%S')}

## Summary
{self.summary}

## Infrastructure Analysis
- Total Charging Stations: {self.infrastructure_analysis.total_stations}
- Coverage Score: {self.infrastructure_analysis.coverage_score:.2f}/10.0

### Stations by Connector Type
"""
        
        for connector, count in self.infrastructure_analysis.stations_by_type.items():
            md += f"- {connector}: {count}\n"
            
        md += "\n### Identified Gaps\n"
        for gap in self.infrastructure_analysis.gaps_identified:
            md += f"- {gap}\n"
            
        md += "\n## Recommendations\n"
        for rec in self.recommendations:
            md += f"- {rec}\n"
            
        md += "\n## Charging Station Details\n"
        for station in self.stations:
            md += f"""
### {station.name}
- Address: {station.address}, {station.city}, {station.state} {station.zip_code}
- Status: {station.status}
- Access: {station.access_type}
- Network: {station.network or 'N/A'}
- Connector Types: {', '.join(station.connector_types)}
- Hours: {station.hours or 'N/A'}
- Pricing: {station.pricing or 'N/A'}
"""
        
        return md
