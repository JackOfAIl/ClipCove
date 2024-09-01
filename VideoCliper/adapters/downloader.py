import pytube



class Downloader:

    def __init__(self, website: str, website_url: str):
        self.website = website
        self.website_url = website_url


    def download_video(self):

        try:
            yt = pytube.YouTube(self.website)

            video_stream = yt.streams.get_highest_resolution()

            print(f"Downloading: {yt.title}")
            video_stream.download()

        except Exception as e:
            print(f"An error {e} while downloading the video")








