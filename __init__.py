from VideoCliper.adapters.downloader import Downloader
from flask import Flask, render_template, request


create_app = Flask(__name__)

if __name__ == "__main__":
    url = input("Enter URL: ")
    yt_downloader = Downloader(url)
    yt_downloader.download_video()