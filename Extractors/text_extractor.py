from typing import List

from Extractors.Segmentors.segmentor import Segmentor
from Extractors.extractor import Extractor


class TextExtractor(Extractor):
    def __init__(self, segmentor: Segmentor):
        self.segmentor = segmentor

    def get_segments(self, full_filepath: str) -> List[str]:
        with open("filename.txt", "r") as file:
            contents = file.read()
            return self.segmentor.break_text_into_segments(contents)
