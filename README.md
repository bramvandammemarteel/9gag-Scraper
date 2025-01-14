# 9GAG Media Scraper

A Python script that scrapes the top trending posts from 9GAG's Trending page, downloads their images and videos into a folder named with the current date, and adds watermarks to both images and videos.

---

## Features

- Dynamically loads the trending page to ensure at least 10 posts are captured.
- Downloads both images and videos from the posts.
- Adds a watermark to all images and videos.
- Saves all media files into a folder named with the current date (e.g., `2025-01-14`).
- Handles cookies popups automatically.

---

## Prerequisites

1. **Python 3.x**:

   - Install Python 3.x from [python.org](https://www.python.org/downloads/).
   - Ensure `pip` (Python package manager) is installed.

2. **Google Chrome**:

   - Download and install [Google Chrome](https://www.google.com/chrome/).

3. **ChromeDriver**:
   - Download ChromeDriver compatible with your Chrome version from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).
   - Add the ChromeDriver executable to your system's PATH.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bramvandammemarteel/9gag-Scraper
   cd 9gag-scraper
   pip install -r requirements.txt
   python scraper.py

   ```
