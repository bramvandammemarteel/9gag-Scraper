from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import subprocess

driver = webdriver.Chrome()
url = "https://9gag.com/trending"
posts_needed = 5
watermark_content = "9gag Scraper"

current_date = datetime.now().strftime("%Y-%m-%d")
output_folder = os.path.join(os.getcwd(), current_date)
os.makedirs(output_folder, exist_ok=True)

driver.get(url)
time.sleep(5)

try:
    cookies_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
    cookies_button.click()
    print("Cookies popup accepted.")
    time.sleep(2)
except Exception:
    print("No cookies popup found.")

scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    posts = driver.find_elements(By.XPATH, "//article")
    if len(posts) >= posts_needed:
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print(f"Found {len(posts)} posts. Proceeding to scrape the top {posts_needed}.")

def add_watermark(image_path, text):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", size=36)
        except IOError:
            font = ImageFont.load_default()
        
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

        width, height = img.size

        x = (width - text_width) / 2
        y = height - text_height - 50  

        shadow_offset = 2
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill="black")  
        draw.text((x, y), text, font=font, fill=(255, 218, 33))  

        img.save(image_path)
        print(f"Watermark added to: {image_path}")



def add_video_watermark(video_path, output_path, text):
    font_path = "C\\:/Windows/Fonts/arial.ttf"

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"drawtext=text='{text}':fontfile='{font_path}':fontcolor=yellow:fontsize=36:x=(w-text_w)/2:y=h-text_h-50:shadowx=2:shadowy=2:shadowcolor=black",
        "-codec:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Watermark added successfully: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error adding watermark: {e}")


for index, post in enumerate(posts[:posts_needed]):
    try:
        try:
            img_element = post.find_element(By.XPATH, ".//img[contains(@src, 'https://img-')]")
            img_url = img_element.get_attribute("src")
            if img_url and img_url.startswith("http"):
                img_data = requests.get(img_url).content
                img_path = os.path.join(output_folder, f"post_image_{index + 1}.jpg")
                with open(img_path, "wb") as file:
                    file.write(img_data)
                print(f"Downloaded: {img_path}")
                add_watermark(img_path, watermark_content)
        except Exception as e:
            print(f"No image found in post {index + 1}: {e}")

        try:
            video_element = post.find_element(By.XPATH, ".//video/source")
            video_url = video_element.get_attribute("src")
            if video_url and video_url.startswith("http"):
                video_data = requests.get(video_url).content
                video_path = os.path.join(output_folder, f"post_video_{index + 1}.mp4")
                with open(video_path, "wb") as file:
                    file.write(video_data)
                print(f"Downloaded: {video_path}")
                
                watermarked_video_path = os.path.join(output_folder, f"post_video_{index + 1}_watermarked.mp4")
                add_video_watermark(video_path, watermarked_video_path, watermark_content)
        except Exception as e:
            print(f"No video found in post {index + 1}: {e}")

    except Exception as e:
        print(f"Failed to download media from post {index + 1}: {e}")


driver.quit()
