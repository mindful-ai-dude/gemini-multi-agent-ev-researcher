# EV Researcher Web UI

A simple, modern web frontend for entering city, state, and country information to generate EV charging infrastructure reports.

## Features
- Enter location details via a form (city, state, optional country)
- Submit to backend Python API for report generation
- View results and download reports in various formats

## How to Use

1. From the project root:
   ```bash
   cd webui
   pnpm install
   pnpm dev
   ```
2. Open the local URL provided (e.g., http://localhost:3000) in your browser.
3. Enter city, state, and (optionally) country, then submit the form.
4. View the generated report and download outputs as needed.

## Folder Structure
- `webui/pages/` – Main UI pages (Next.js)
- `webui/components/` – UI components (form, results, etc.)
- `webui/utils/` – Helper functions
- `webui/styles/` – Tailwind CSS styles

## Backend Requirements
- The backend Python API (FastAPI or Flask recommended) must be running and accessible to the web UI.
- Update the API endpoint URL in `webui/utils/api.ts` if needed.

## International Support
- For Europe, Morocco, or other countries, ensure the backend API supports your chosen region and data source (see main README for details).

## Tech Stack
- Next.js App Router (React)
- TypeScript
- Tailwind CSS
- Shadcn UI, Radix UI
- pnpm for package management

---

For questions or to contribute, see the main project README.
