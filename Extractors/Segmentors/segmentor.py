
import abc
from typing import List


class Segmentor():
    @abc.abstractmethod
    def break_text_into_segments(self, text: str) -> List[str]:
        pass