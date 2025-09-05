import requests
from bs4 import BeautifulSoup
import re
import json
import modules.incestflixVideo as incestflixVideo


def download_from_incestflix(url, output_file="videos.json"):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    videos = []

    for a in soup.select("a#videolink"):
        title = a.select_one(".text-heading").get_text(strip=True)
        link = a["href"]

        # Extract thumbnail from inline style
        style = a.select_one(".img-overflow").get("style", "")
        thumb_match = re.search(r'url\((.*?)\)', style)
        thumbnail = thumb_match.group(1) if thumb_match else None

        videos.append({
            "title": title,
            "link": "https:" + link,
            "thumbnail": "https:" + thumbnail if thumbnail else None
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
            incestflixVideo.process_json("videos.json", "videolink.json")
            break
        elif option == 'n':
            print("Exiting...")
            exit()
        else:
            print("Invalid option. Please type y/n.")
