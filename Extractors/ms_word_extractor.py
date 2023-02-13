from typing import List

from Extractors.extractor import Extractor
import docx

class DocxExtractor(Extractor):
    def get_segments(self, full_filepath: str) -> List[str]:
        doc = docx.Document(full_filepath)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return full_text
