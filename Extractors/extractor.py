import abc


class Extractor():
    @abc.abstractmethod
    def get_segments(self):
        pass