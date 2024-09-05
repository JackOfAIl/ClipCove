import abc

repo_instance = None

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_video_clip(self, video):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_video(self, video_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_video_clip(self, video_id):
        #returns video object based on the given id
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_videos(self):
        #Returns a list of all recently downloaded videos
        raise NotImplementedError