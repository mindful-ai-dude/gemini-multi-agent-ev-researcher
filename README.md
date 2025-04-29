# EV Research Multi-Agent System

A powerful multi-agent system for analyzing EV charging infrastructure using Google's Gemini 2.0 AI. This application combines real-time data from the National Renewable Energy Laboratory (NREL) with advanced AI analysis to provide comprehensive insights into EV charging networks.

## 🚀 Features

### 🤖 Advanced AI Analysis
- **Gemini 2.0 Integration**: Leverages Google's latest `gemini-2.0-flash-exp` model for rapid, high-quality analysis
- **Intelligent Fallback**: Automatic fallback to `gemini-1.5-pro` ensures uninterrupted operation
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

### API Connection Issues
1. Verify your API keys are correctly set in the `.env` file
2. Check your internet connection
3. Ensure you haven't exceeded API rate limits

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- National Renewable Energy Laboratory (NREL) for providing the charging station data API
- Google AI for the Gemini AI models
- All contributors and users of this project




