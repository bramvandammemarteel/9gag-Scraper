import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- Scrape TikTok Hashtags ---
def scrape_tiktok_hashtags():
    print("Starting TikTok hashtag scraper...")
    hashtags = []

    try:
        # Set up the WebDriver with options to suppress errors
        options = Options()
        options.add_argument("--log-level=3")  # Suppress logging
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.tiktok.com/discover")
        print("Waiting 5 seconds for manual interaction...")
        time.sleep(5)  # Allow manual interaction for cookies

        # Scrape hashtags
        while True:
            # Locate hashtag elements by the data-e2e attribute
            elements = driver.find_elements(By.XPATH, "//h4[@data-e2e='explore-feed-title']")
            if elements:
                for element in elements:
                    text = element.text.strip()
                    if text.startswith("#") and text not in hashtags:
                        hashtags.append(text)
                        print(f"Found hashtag: {text}")

            # Scroll down to load more content
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for new content to load

            # Check if no new hashtags are loaded
            new_elements = driver.find_elements(By.XPATH, "//h4[@data-e2e='explore-feed-title']")
            if len(new_elements) == len(elements):
                print("Reached the end of the page.")
                break

        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        try:
            driver.quit()
        except:
            pass

    print(f"Scraped {len(hashtags)} hashtags.")
    return hashtags

# --- Save Hashtags to File ---
def save_hashtags(hashtags, filename):
    print(f"Saving hashtags to {filename}...")
    with open(filename, "w", encoding="utf-8") as file:
        for hashtag in hashtags:
            file.write(hashtag + "\n")
    print(f"Saved {len(hashtags)} hashtags to {filename}.")

# --- Main ---
def main():
    hashtags = scrape_tiktok_hashtags()
    if hashtags:
        current_date = time.strftime("%Y-%m-%d")
        save_hashtags(hashtags, f"tiktok_hashtags_{current_date}.txt")
    else:
        print("No hashtags scraped.")

# --- Run Script ---
if __name__ == "__main__":
    main()
