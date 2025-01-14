# 9GAG Media Scraper

A Python script that scrapes the top 10 trending posts from 9GAG's Trending page and downloads their images and videos into a folder named with the current date.

---

## Features

- Dynamically loads the trending page to ensure at least 10 posts are captured.
- Downloads both images and videos from the posts.
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
   git clone https://github.com/your-username/9gag-media-scraper.git
   cd 9gag-media-scraper
   ```

2. Install the required Python libraries:
   ```bash
   pip install selenium requests
   ```

---

## Usage

1. Run the script:

   ```bash
   python scraper.py
   ```

2. The script will:

   - Open the 9GAG Trending page in a Chrome browser.
   - Scroll to load the top 10 posts dynamically.
   - Download images and videos into a folder named with the current date (e.g., `2025-01-14`).

3. Check the output folder:
   - All downloaded media files will be saved in the folder created in the same directory as the script.

---

## Example Output

If the script is run on `2025-01-14`, the folder structure will look like this:

```
2025-01-14/
├── post_image_1.jpg
├── post_video_1.mp4
├── post_image_2.jpg
├── post_video_2.mp4
...
├── post_image_10.jpg
└── post_video_10.mp4
```

---

## Notes

1. Ensure that your ChromeDriver version matches your Google Chrome version.
2. The script is designed to scrape the first 10 posts only.
3. Please ensure your use of this script complies with 9GAG’s [terms of service](https://9gag.com/terms).

---

## Troubleshooting

1. **ChromeDriver not found**:

   - Ensure ChromeDriver is installed and added to your system's PATH.
   - Verify by running:
     ```bash
     chromedriver --version
     ```

2. **Selenium errors**:

   - Update Selenium to the latest version:
     ```bash
     pip install --upgrade selenium
     ```

3. **No posts downloaded**:
   - Ensure the 9GAG page structure hasn’t changed. Inspect the HTML structure and update the XPath selectors in the script if necessary.
