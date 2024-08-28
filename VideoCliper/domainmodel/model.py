




class Playlist:

    def __init__(self, name:str, cover_img_url:str):
        self.playlist = list()
        self.size = 0
        self.name = name
        self.cover_img_url = cover_img_url
        self.total_duration = 0
        self.playlist_id = id(self)