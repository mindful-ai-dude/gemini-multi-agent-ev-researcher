"""Example script demonstrating the EV Research Agent."""

import asyncio
import os
from dotenv import load_dotenv
from src.config.settings import NREL_API_KEY, GEMINI_API_KEY, GEMINI_MODEL
from src.agents.research_agent import EVResearchAgent
from src.utils.visualization import create_station_map

async def main():
    """Run the example."""
    # Initialize the research agent
    agent = EVResearchAgent(
        nrel_api_key=NREL_API_KEY,
        gemini_api_key=GEMINI_API_KEY,
        model_name=GEMINI_MODEL,
        temperature=0.7
    )
    
    # Generate a report for Austin, TX
    print("Generating report for Austin, TX...")
    report = await agent.generate_report("Austin", "TX")
    
    # Create visualization
    print("\nCreating interactive map...")
    map_obj = create_station_map(report.stations, report.city, report.state)
    
    # Ensure output directory exists
    output_dir = os.path.join("docs", "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the visualization
    map_path = os.path.join(output_dir, "austin_stations_map.html")
    map_obj.save(map_path)
    
    # Save the report in different formats
    print("\nSaving report in different formats...")
    await agent.save_report(report, os.path.join(output_dir, "austin_report.md"), "markdown")
    await agent.save_report(report, os.path.join(output_dir, "austin_report.pdf"), "pdf")
    await agent.save_report(report, os.path.join(output_dir, "austin_report.docx"), "docx")
    
    print("\nReport generation complete! Files saved in", output_dir + ":")
    print("- austin_report.md")
    print("- austin_report.pdf")
    print("- austin_report.docx")
    print("- austin_stations_map.html")

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    asyncio.run(main())
