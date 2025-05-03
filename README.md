# Sputnik Music Artist Manager

A Python tool to help you discover and track new artists from Sputnik Music. The program allows you to scrape artists from Sputnik Music pages and keep track of which ones you've tried.

## Features

- Scrape artists from Sputnik Music pages
- Keep track of artists you want to try
- Randomly select artists to try
- Maintain a list of artists you've already checked

## Setup

1. Install Pipenv (if you haven't already):
```bash
pip install pipenv
```

2. Clone this repository and navigate to its directory:
```bash
cd SputnikArtistSearcherV2
```

3. Install dependencies using Pipenv:
```bash
pipenv install
```

## Usage

1. Activate the virtual environment and run the program:
```bash
pipenv run python main.py
```

2. Use the menu options:
   - Option 1: Add a Sputnik Music source URL (e.g., https://www.sputnikmusic.com/uservote.php?memberid=791704)
   - Option 2: Get a random artist to try
   - Option 3: Exit the program

## File Structure

- `main.py`: Main program file
- `scraper.py`: Module for scraping Sputnik Music pages
- `music-to-try.txt`: List of artists to try (created automatically)
- `music-to-ignore.txt`: List of artists you've already checked (created automatically)
- `Pipfile`: Project dependencies
- `Pipfile.lock`: Locked dependencies for reproducible builds

## Dependencies

- Python 3.x
- requests
- beautifulsoup4

All dependencies are managed through Pipenv and will be installed automatically when you run `pipenv install`. 