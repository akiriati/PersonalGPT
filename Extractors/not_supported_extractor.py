from typing import List

from Extractors.extractor import Extractor


class NotSupportedExtractor(Extractor):
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        return []