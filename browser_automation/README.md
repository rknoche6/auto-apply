# Browser Automation Project

This project demonstrates the use of browser-use package for automated web browsing tasks.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install playwright:
```bash
playwright install
```

3. Configure environment:
- Copy the `.env` file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Running the Script

To run the automation script:
```bash
python src/main.py
```

The script will:
1. Go to Reddit
2. Search for 'browser-use'
3. Click on the first post
4. Return the first comment
