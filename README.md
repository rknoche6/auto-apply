# Browser Automation Project

This project demonstrates the use of browser-use package for automated web browsing tasks.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install playwright:
```bash
playwright install
```

4. Configure environment:
- Copy the `.env` file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Development Notes

- The project uses `.gitignore` to exclude:
  - Virtual environment (`venv/`)
  - Environment variables (`.env`)

## Running the Script

To run the automation script:
```bash
python src/main.py
```

The script will:
1. Connect to HolidayCheck's job website
2. Automatically search for software engineer positions
3. Fill out job applications with provided information
4. Request confirmation before submitting any application

Note: The script uses AI-powered automation to handle the application process but will always ask for confirmation before submitting any application.
