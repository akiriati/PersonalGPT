from typing import List

from Extractors.extractor import Extractor


class NotSupportedExtractor(Extractor):

    def get_segments(self, full_filepath: str) -> List[str]:
        return []