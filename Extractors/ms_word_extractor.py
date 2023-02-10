from typing import List

from Extractors.extractor import Extractor
import docx



class DocxExtractor(Extractor):
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        doc = docx.Document(self.full_filepath)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return full_text
