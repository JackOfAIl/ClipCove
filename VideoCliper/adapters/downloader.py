import pytube

from VideoCliper.domainmodel.model import Video



class Downloader:
    recently_downloaded: list[Video] = list()

    def __init__(self, website: str, website_url: str):
        self.website = website
        self.website_url = website_url


    def download_video(self):

        try:
            yt = pytube.YouTube(self.website)

            video_stream = yt.streams.get_highest_resolution()

            print(f"Downloading: {yt.title}")
            video_stream.download()

            #Returns the video object which is the downloaded video
            return yt

        except Exception as e:
            print(f"An error {e} while downloading the video")


    def create_video(self,):








