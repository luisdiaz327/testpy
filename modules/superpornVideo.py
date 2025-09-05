import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def get_video_src_selenium(url):
    options = Options()
    options.headless = True  # run without opening browser

    driver = webdriver.Firefox(options=options)
    driver.get(url)

    time.sleep(3)  # wait for page to load

    try:
        # locate the <video> element
        video_elem = driver.find_element(By.CSS_SELECTOR, "video")
        
        # extract the video source URL
        source_elem = video_elem.find_element(By.CSS_SELECTOR, "source")
        video_url = source_elem.get_attribute("src")
        if video_url and video_url.startswith("//"):
            video_url = "https:" + video_url
        
        # extract poster image
        poster_url = video_elem.get_attribute("poster")
        if poster_url and poster_url.startswith("//"):
            poster_url = "https:" + poster_url

        return {
            "video_url": video_url,
            "poster_url": poster_url
        }
    except Exception as e:
        print("Error:", e)
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


if __name__ == "__main__":
    process_json()
