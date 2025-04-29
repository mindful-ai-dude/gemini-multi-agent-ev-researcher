from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncio
import os
import markdown
from ev_research.src.agents.research_agent import EVResearchAgent
from ev_research.src.utils.visualization import create_station_map
from ev_research.src.config.settings import NREL_API_KEY, GEMINI_API_KEY, GEMINI_MODEL, DEFAULT_TEMPERATURE
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/report")
async def generate_report(request: Request):
    try:
        body = await request.json()
        city = body.get("city")
        state = body.get("state")
        country = body.get("country", "USA")
        logging.info(f"Received input: city={city}, state={state}, country={country}")
        # Validate input
        if not city or not isinstance(city, str):
            return JSONResponse(status_code=400, content={"error": "Missing or invalid 'city' in request body."})
        if not state or not isinstance(state, str):
            return JSONResponse(status_code=400, content={"error": "Missing or invalid 'state' in request body."})
        if not country or not isinstance(country, str):
            return JSONResponse(status_code=400, content={"error": "Missing or invalid 'country' in request body."})
        agent = EVResearchAgent(NREL_API_KEY, GEMINI_API_KEY, GEMINI_MODEL, DEFAULT_TEMPERATURE)
        try:
            report = await agent.generate_report(city, state)
        except Exception as e:
            error_msg = str(e)
            if "Geocoding failed" in error_msg:
                return JSONResponse(status_code=400, content={"error": error_msg})
            raise  # re-raise for other backend errors
        # Always use root-level docs/output
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs', 'output'))
        os.makedirs(output_dir, exist_ok=True)
        base = os.path.join(output_dir, f"{city.lower()}_{state.lower()}_report")
        await agent.save_report(report, f"{base}.md", format="markdown")
        await agent.save_report(report, f"{base}.pdf", format="pdf")
        await agent.save_report(report, f"{base}.docx", format="docx")
        # HTML export (write HTML from markdown)
        html_path = f"{base}.html"
        if markdown:
            with open(f"{base}.md", "r") as f:
                html_content = markdown.markdown(f.read())
            with open(html_path, "w") as f:
                f.write(html_content)
        else:
            with open(html_path, "w") as f:
                f.write("<html><body><pre>Markdown not available. HTML export skipped.</pre></body></html>")
        # Map HTML
        map_obj = create_station_map(report.stations, report.city, report.state)
        map_path = os.path.join(output_dir, f"{city.lower()}_{state.lower()}_stations_map.html")
        map_obj.save(map_path)
        # Return summary and file paths
        return {
            "city": city,
            "state": state,
            "country": country,
            "summary": report.summary,
            "output_files": {
                "markdown": f"docs/output/{city.lower()}_{state.lower()}_report.md",
                "pdf": f"docs/output/{city.lower()}_{state.lower()}_report.pdf",
                "docx": f"docs/output/{city.lower()}_{state.lower()}_report.docx",
                "html": f"docs/output/{city.lower()}_{state.lower()}_report.html",
                "map_html": f"docs/output/{city.lower()}_{state.lower()}_stations_map.html"
            }
        }
    except Exception as e:
        import traceback
        logging.error(traceback.format_exc())
        return JSONResponse(status_code=500, content={"error": str(e)})

