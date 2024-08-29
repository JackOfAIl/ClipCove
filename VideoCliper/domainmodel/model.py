import typing
import datetime


class Video:
    #Static variable used to keep track of the total number
    #of videos the user has downloaded.
    total_number_of_videos:str = 0

    def __init__(self, video_url:str, website:str):
        self._video_url = video_url
        self._video_img: str = str()
        self._website = website
        self._video_duration: int = 0
        self._date_added: datetime.datetime = datetime.datetime.now()
        self._video_id = id(self)
        self.in_playlist: list[Playlist] = []
        self.video_name: str = ""


    @property
    def video_id(self) -> str:
        return self.video_id

    @property
    def video_url(self) -> str:
        return self.video_url

    @property
    def website(self) -> str:
        return self.website

    @property
    def video_duration(self) -> float:
        return self.video_duration

    @property
    def date_added(self) -> datetime.datetime:
        return self._date_added

    @property
    def video_name(self) -> str:
        return self.video_name

    @video_name.setter
    def video_name(self, name:str):
        self._video_name = name

    @property
    def video_img(self) -> str:
        return self._video_img

    @video_img.setter
    def video_img(self, img:str):
        self._video_img = img

    def __lt__(self, other) -> bool:
        return self.video_duration < other.video_duration

    def __hash__(self) -> int:
        return hash((self.video_url, self.website, self.video_id))

    def __eq__(self, other) -> bool:
        return (self.video_url == other.video_url
                and self.website == other.website
                and self.video_id == other.video_id)

    def __str__(self) -> str:
        return f"{self.video_url} {self.website} {self.video_duration} {self.date_added}"




class Playlist:
    number_of_playlists: int = 0

    def __init__(self, name:str, cover_img_url:str, description:str):
        self._playlist: dict[str, Video] = dict()
        self._size = 0
        self._name = name
        self.date_publised: datetime.datetime = datetime.datetime.now()
        self._cover_img_url = cover_img_url
        self.total_duration = 0
        self._playlist_id = id(self)
        self._description = description


    @property
    def size(self) -> int:
        return self.size

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name:str):
        self.name = name

    @property
    def cover_img_url(self) -> str:
        return self.cover_img_url

    @cover_img_url.setter
    def cover_img_url(self, new_img_url:str):
        self._cover_img_url = new_img_url

    @property
    def playlist_id(self) -> int:
        return self.playlist_id

    @property
    def description(self) -> str:
        return self.description

    @description.setter
    def description(self, description:str):
        self._description = description

    def add_video_to_playlist(self, video_obj:Video):
        if isinstance(video_obj, Video):
            self.playlist.append(video_obj)
        else:
            raise TypeError ("Could not add Video to Playlist")

    @property
    def playlist(self) -> list:
        return self.playlist


    def __hash__(self) -> int:
        return hash((self.playlist_id, self._name, self._cover_img_url, self._description))

    def __eq__(self, other) -> bool:
        return self.playlist_id == other.playlist_id

    def __str__(self) -> str:
        return f"Name: {self._name}\n" \
               f" Size: {self._size}\n" f" Description: {self._description}\n" \
               f"Playlist: {self.playlist}\n" \

    def __lt__(self, other) -> bool:
        return self.date_publised < other.date_publised



class RecentlyDownloaded:

    def __init__(self, video:Video):
        self._video = video
        self._video.video_name = Video.video_name
        self._video.total_duration = Video.video_duration
        self._video.total_number_of_videos = Video.total_number_of_videos
        

