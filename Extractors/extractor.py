import abc
from typing import List


class Extractor():
    @abc.abstractmethod
    def get_segments(self, full_filepath: str) -> List[str]:
        pass