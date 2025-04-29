# EV Research Multi-Agent System

A powerful multi-agent system for analyzing EV charging infrastructure using Google's Gemini 2.0 AI. This application combines real-time data from the National Renewable Energy Laboratory (NREL) with advanced AI analysis to provide comprehensive insights into EV charging networks.

## 🚀 Features

### 🤖 Advanced AI Analysis
- **Gemini 2.5 Integration**: Leverages Google's latest `gemini-2.5-flash-preview-04-17` model for rapid, high-quality analysis
- **Intelligent Fallback**: Automatic fallback to `gemini-2.5-pro-preview-03-25` ensures uninterrupted operation
- **Natural Language Processing**: Generates human-readable insights and recommendations

### 📊 Data Analysis & Visualization
- **Real-time Data**: Direct integration with NREL's API for up-to-date charging station information
- **Interactive Maps**: Beautiful, interactive maps showing charging station locations and details
- **Comprehensive Analysis**: Coverage scores, gap analysis, and infrastructure recommendations

### 📝 Report Generation
- **Multiple Formats**: Generate reports in PDF, DOCX, and Markdown formats
- **Professional Styling**: Clean, well-formatted reports with consistent styling
- **Rich Content**: Detailed statistics, recommendations, and visualizations

## 🛠 Installation

### Prerequisites
1. Python 3.12 or higher
2. Conda package manager
3. MacTeX (for PDF generation)
4. API Keys:
   - NREL API Key (get it [here](https://developer.nrel.gov/signup/))
   - Google AI API Key (get it [here](https://ai.google.dev/))

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/trainnect-dev/gemini-multi-agent-ev-researcher.git
   cd gemini-multi-agent-ev-researcher
   ```

2. **Create and Activate Conda Environment**
   ```bash
   conda create -n ev_research python=3.12
   conda activate ev_research
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install MacTeX** (if not already installed)
   ```bash
   brew install --cask basictex
   ```

5. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```env
   NREL_API_KEY=your_nrel_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

## 🚀 Usage

### Location Requirements (April 2025 Update)

- **NREL API now requires latitude and longitude for all station queries.**

- This application automatically converts a provided city and state into latitude/longitude using OpenStreetMap's Nominatim geocoding service.

- **You only need to provide the city and state** (e.g., `Austin, TX`). The system will handle the conversion for you.
- If geocoding fails (e.g., invalid city/state), a clear error message will be shown.

### Example Usage

1. **Run the Example Script**
   ```bash
   cd ev_research
   python example.py
   ```

2. **Check Generated Output**
   The script will generate several files in `docs/output/`:
   - `austin_report.pdf`: PDF version of the report
   - `austin_report.docx`: Word version of the report
   - `austin_report.md`: Markdown version of the report
   - `austin_stations_map.html`: Interactive map of charging stations

### How Location Lookup Works
- The system uses an async geocoding helper to convert city/state to latitude/longitude.
- No manual latitude/longitude entry is required for typical use—just specify the city and state.
- This ensures compatibility with the latest NREL API requirements.

## 📊 Output Examples

### Interactive Map
- Displays all charging stations with detailed information
- Color-coded markers for station status
- Cluster view for better visualization
- Fullscreen mode for detailed exploration

### Analysis Report
- Comprehensive infrastructure analysis
- Coverage scores and statistics
- Identified gaps and opportunities
- Actionable recommendations

---

## 🌍 Using the System for Europe or Morocco

By default, this project uses the US-based NREL API, which only covers the United States. To analyze charging stations in other countries (such as Europe or Morocco):

1. **Find a suitable open API** for your country/region:
   - Europe: [Open Charge Map API](https://openchargemap.org/site/develop/api)
   - Morocco: Check for local government or open data sources.

2. **Update the API client code** in `ev_research/src/api/nrel_api.py` to fetch and parse data from the new source.
   - You may need to replace or extend the `get_stations` method.
   - Adjust the data parsing logic to match the new API’s response format.

3. **Adjust the geocoding call** to include the correct country name if required. The geocoding helper supports a `country` parameter.
4. **Update your `.env` file** with any new API keys or endpoints.
5. **Test** by running `python example.py` with your chosen city, region, and country.

**Files to update:**
- `ev_research/src/api/nrel_api.py` (API logic)
- `ev_research/src/models/data_models.py` (if the charging station data model changes)
- `ev_research/example.py` (for usage examples)
- `.env` (for new API keys)
- `README.md` (for documentation)

---

## 🖥️ Simple Web UI for City/State Entry

A simple web-based frontend is available for entering city and state information (and optionally country). This makes it easy for students to run analyses without editing code.

- **Location:** `webui/` directory
- **How to use:**
  1. From the project root, run:
     ```bash
     cd webui
     pnpm install
     pnpm dev
     ```
  2. Open the provided local URL in your browser.
  3. Enter the city, state, and (optionally) country, then submit to generate a report.
- The web UI communicates with the backend Python API to fetch and display results.
- For international support, ensure the backend is updated as described above.

---

## 🆕 What Was Added and Changed

### 1. FastAPI Backend (`backend/main.py`)
- Accepts POST requests at `/api/report` with `city`, `state`, and `country`.
- Runs your EVResearchAgent to generate a report.
- Saves outputs (Markdown, PDF, DOCX) to `docs/output/`.
- Returns a summary and file paths as JSON.

### 2. Frontend Proxy (`webui/pages/api/report.ts`)
- Proxies POST requests from the web UI to the FastAPI backend at `http://localhost:8000/api/report`.
- Returns the backend’s real response to the frontend UI.

### 3. Web UI
- Modern, student-friendly form for entering location info.
- Displays summary and can be extended to show download links or map previews.

---

## 🚦 How to Run the Full System

### 🟢 Recommended: Use the Provided Scripts

For a smooth experience, use the provided scripts to start the backend and frontend from anywhere in the project. These scripts set up the correct environment and paths automatically.

#### 1. Start the Backend
```bash
./run_backend.sh
```
- This script:
  - Sets the correct `PYTHONPATH` so all imports work.
  - Launches the FastAPI backend with live reload.
  - Works from any directory in the project.

#### 2. Start the Frontend
```bash
./run_frontend.sh
```
- This script:
  - Changes to the `webui` directory.
  - Installs dependencies with `pnpm` if needed.
  - Starts the Next.js dev server at [http://localhost:3000](http://localhost:3000).
  - Works from any directory in the project.

#### 3. Make Scripts Executable (First Time Only)
If you get a permissions error, run:
```bash
chmod +x run_backend.sh run_frontend.sh
```

#### 4. Use the Web UI
- Open [http://localhost:3000](http://localhost:3000) in your browser.
- Enter city, state, and (optionally) country.
- Submit the form.
- The backend will generate reports and save them to `docs/output/`.
- The UI will display the summary and can be extended to show download links.

---

### 🛠️ Manual Startup (Advanced)
If you prefer manual control, you can still start each service as described in earlier sections, but the scripts are recommended for beginners and classroom use.

---

**You now have a working, modern, student-friendly, full-stack EV research platform!**

If you want help with file download links, map previews, or international API integration, see the relevant sections above or ask your instructor.

---

## 🔧 Troubleshooting

### PDF Generation Issues
1. Ensure MacTeX is properly installed:
   ```bash
   which pdflatex
   ```
2. If pdflatex is not found, add it to your PATH:
   ```bash
   export PATH=$PATH:/Library/TeX/texbin
   ```
3. If you see errors about missing LaTeX packages, try running:
   ```bash
   sudo tlmgr install <package-name>
   ```

### API Connection Issues
1. Verify your API keys are correctly set in the `.env` file.
2. Check your internet connection.
3. Ensure you haven't exceeded API rate limits.
4. If you see CORS errors, make sure the FastAPI backend allows connections from your frontend.

### Backend/Frontend Connection Issues
1. Make sure the backend is running (`uvicorn main:app --reload`) on port 8000.
2. Make sure the frontend is running (`pnpm dev`) on port 3000.
3. If ports are in use, stop other apps or change the port in the relevant config.
4. If you get a 'Backend connection failed' error, check that the backend URL in `webui/pages/api/report.ts` matches your backend server.

### File Permissions
- If you see errors writing to `docs/output`, ensure the directory exists and you have write permissions.
- On Mac/Linux, you can run:
  ```bash
  mkdir -p docs/output
  chmod -R 755 docs/output
  ```

### International API Integration
- If you want to use a non-US data source, follow the instructions in the "Using the System for Europe or Morocco" section.
- Make sure to update the API client, geocoding helper, and `.env` as needed.

---

## ❓ FAQ

**Q: Where do I enter my API keys?**
A: In the `.env` file at the project root. You need both an NREL API key and a Gemini API key.

**Q: Where are my generated reports?**
A: In the `docs/output/` folder as Markdown, PDF, and DOCX files.

**Q: Can I use this for countries outside the USA?**
A: Yes! See the "Using the System for Europe or Morocco" section for instructions on updating the API client and geocoding logic.

**Q: The web UI loads but nothing happens when I submit a city/state. Why?**
A: Make sure the FastAPI backend is running and accessible at `http://localhost:8000`. Check the browser console and backend logs for errors.

**Q: How do I update the Gemini model version?**
A: Update the model names in `ev_research/src/config/settings.py` and make sure the README reflects the correct model versions:
```
GEMINI_MODEL = "gemini-2.5-flash-preview-04-17"
GEMINI_FALLBACK_MODEL = "gemini-2.5-pro-preview-03-25"
DEFAULT_TEMPERATURE = 0.7
```

**Q: How do I contribute or ask for help?**
A: Submit a GitHub issue or pull request, or ask your instructor for guidance.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- National Renewable Energy Laboratory (NREL) for providing the charging station data API
- Google AI for the Gemini AI models
- All contributors and users of this project

