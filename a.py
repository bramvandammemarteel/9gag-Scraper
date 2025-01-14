from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
url = "https://9gag.com/trending"

# Open the webpage
driver.get(url)
time.sleep(5)  # Allow time for JavaScript to load

# Handle cookies popup
try:
    cookies_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
    cookies_button.click()
    print("Cookies popup accepted.")
    time.sleep(2)  # Allow time for the page to refresh after clicking
except Exception:
    print("No cookies popup found.")

# Scroll the page to load more posts
scroll_pause_time = 2
posts_needed = 10
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    posts = driver.find_elements(By.XPATH, "//article")
    if len(posts) >= posts_needed:
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down
    time.sleep(scroll_pause_time)  # Wait for new posts to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # Break if no new content is loaded
        break
    last_height = new_height

print(f"Found {len(posts)} posts. Proceeding to scrape the top {posts_needed}.")

# Scrape the top 10 posts
for index, post in enumerate(posts[:posts_needed]):  # Limit to the first 10 posts
    try:
        # Check if the post contains an image
        try:
            img_element = post.find_element(By.XPATH, ".//img[contains(@src, 'https://img-')]")
            img_url = img_element.get_attribute("src")
            if img_url and img_url.startswith("http"):
                img_data = requests.get(img_url).content
                with open(f"post_image_{index + 1}.jpg", "wb") as file:
                    file.write(img_data)
                print(f"Downloaded: post_image_{index + 1}.jpg")
        except Exception as e:
            print(f"No image found in post {index + 1}: {e}")

        # Check if the post contains a video
        try:
            video_element = post.find_element(By.XPATH, ".//video/source")
            video_url = video_element.get_attribute("src")
            if video_url and video_url.startswith("http"):
                video_data = requests.get(video_url).content
                with open(f"post_video_{index + 1}.mp4", "wb") as file:
                    file.write(video_data)
                print(f"Downloaded: post_video_{index + 1}.mp4")
        except Exception as e:
            print(f"No video found in post {index + 1}: {e}")

    except Exception as e:
        print(f"Failed to download media from post {index + 1}: {e}")

# Quit the driver
driver.quit()
