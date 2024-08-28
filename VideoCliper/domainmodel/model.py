import type


class Video:

    def __init__(self):
        pass




class Playlist:

    def __init__(self, name:str, cover_img_url:str, description:str):
        self.playlist: list[Video] = list()
        self.size = 0
        self.name = name
        self.cover_img_url = cover_img_url
        self.total_duration = 0
        self.playlist_id = id(self)
        self.description = description


    @property
    def size(self):
        return self.size

    @property
    def name(self):
        return self.name

    @property
    def cover_img_url(self):
        return self.cover_img_url

    @property
    def playlist_id(self):
        return self.playlist_id

    @property
    def description(self):
        return self.description

    def add_video_to_playlist(self, video_obj:Video):
        if isinstance(video_obj, Video):
            self.playlist.append(video_obj)
        else:
            raise TypeError ("Could not add Video to Playlist")