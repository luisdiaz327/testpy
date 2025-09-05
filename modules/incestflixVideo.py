import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def get_video_src_selenium(url):
    options = Options()
    options.headless = True  # run without opening Firefox window

    driver = webdriver.Firefox(options=options)
    driver.get(url)

    time.sleep(3)  # wait for page to load properly

    try:
        video_element = driver.find_element(By.CSS_SELECTOR, "#incflix-stream video source")
        src = video_element.get_attribute("src")
        if src and src.startswith("//"):
            src = "https:" + src
        return src
    except Exception:
        return None
    finally:
        driver.quit()


def process_json(input_file="videos.json", output_file="videolink.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        videos = json.load(f)

    for item in videos:
        print(f"🔍 Scraping: {item['link']}")
        video_url = get_video_src_selenium(item["link"])
        item["video_url"] = video_url
        print(f"✅ Found: {video_url}")

    # Save updated results
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=4, ensure_ascii=False)

    print(f"🎬 All done! Saved to {output_file}")
