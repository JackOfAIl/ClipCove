import typing


class Video:
    #Static variable used to keep track of the total number
    #of videos the user has downloaded.
    total_number_of_videos:str = 0

    def __init__(self, video_url:str, website:str):
        self._video_url = video_url
        self._website = website
        self._video_duration: int = 0
        self._video_id = id(self)
        self.in_playlist: list[Playlist] = []
        self.video_name: str = ""

    @property
    def video_id(self):
        return self.video_id

    @property
    def video_url(self):
        return self.video_url

    @property
    def website(self):
        return self.website

    @property
    def video_duration(self):
        return self.video_duration

    def __hash__(self):
        return hash((self.video_url, self.website, self.video_id))





class Playlist:

    def __init__(self, name:str, cover_img_url:str, description:str):
        self._playlist: dict[str, Video] = dict()
        self._size = 0
        self._name = name
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

    @property
    def cover_img_url(self) -> str:
        return self.cover_img_url

    @property
    def playlist_id(self) -> int:
        return self.playlist_id

    @property
    def description(self) -> str:
        return self.description

    def add_video_to_playlist(self, video_obj:Video):
        if isinstance(video_obj, Video):
            self.playlist.append(video_obj)
        else:
            raise TypeError ("Could not add Video to Playlist")

    @property
    def playlist(self):
        return self.playlist


    @size.setter
    def size(self, value):
        self._size = value



