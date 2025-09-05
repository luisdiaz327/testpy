from modules.incestflix import download_from_incestflix
from modules.superporn import download_from_superporn

if __name__ == "__main__":
    print("🎬 Video Downloader")
    try:
        url = input("🔗 Enter video URL: \n").strip()
        checkUrl = url.split("/")[2]
        # print("🌐 Detected site: " + checkUrl)

        if checkUrl in ["hqporner.com", "www.hqporner.com"]:
            download_from_hqporner(url)
        elif checkUrl in ["incestflix.com", "www.incestflix.com", "tabooflix.ws", "www.tabooflix.ws"]:
            download_from_incestflix(url)
        elif checkUrl in ["superporn.com", "www.superporn.com"]:
            download_from_superporn(url)
        else:
            print("⚠️ Unrecognized site. Attempting with IncestFlix handler...")
            download_from_incestflix(url)

    except ValueError:
        print("❌ Invalid URL or site not supported.")
