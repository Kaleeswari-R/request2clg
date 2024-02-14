import requests
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download("C:\\Users\\Admin\\Videos\\Captures")

        update_status_url = "https://kaleeswarir.pythonanywhere.com/update_status"
        data = {"url": url, "media": "yes"}
        response = requests.post(update_status_url, json=data)

        return "yes"
    except Exception as e:
        print("An error occurred:", str(e))
        return "no"

def main():
    get_not_downloaded_url = "https://kaleeswarir.pythonanywhere.com/get_not_downloaded"
    response = requests.get(get_not_downloaded_url)

    if response.status_code == 200:
        videos = response.json()

        for video in videos:
            video_url = video['url']
            download_status = download_video(video_url)

            print(f"Video {video_url} downloaded with status: {download_status}")

if __name__ == "__main__":
    main()
