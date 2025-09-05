import requests
from bs4 import BeautifulSoup
import json
import modules.superpornVideo as superpornVideo

def download_from_superporn(url, output_file="videos.json"):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    videos = []

    for video in soup.select("div.thumb-video"):
        link_tag = video.select_one("a.thumb-duracion")
        # img_tag = video.select_one("img.lazy")
        title_tag = video.select_one("a.thumb-video__description")

        if not link_tag or not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag.get("href")
        # thumbnail = img_tag.get("src")

        videos.append({
            "title": title,
            "link": link if link.startswith("http") else "https://www.superporn.com" + link
            # "thumbnail": thumbnail if thumbnail.startswith("http") else "https:" + thumbnail
        })

    # Save results into a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=4, ensure_ascii=False)

    print(f"✅ Saved {len(videos)} items to {output_file}")
    checkOption()


def checkOption():
    while True:
        print("Want to extract video sources from IncestFlix? y/n") 
        option = input().lower()

        if option == 'y':
            # process the saved JSON
            superpornVideo.process_json("videos.json", "videolink.json")
            break
        elif option == 'n':
            print("Exiting...")
            exit()
        else:
            print("Invalid option. Please type y/n.")

