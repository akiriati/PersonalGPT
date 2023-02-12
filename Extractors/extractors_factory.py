from Extractors.extractor import Extractor
from Extractors.ms_word_extractor import DocxExtractor
from Extractors.not_supported_extractor import NotSupportedExtractor
import os
from Extractors.pdf_extractor import PdfMinerExtractor
from Extractors.requests_extractor import RequestsExtractor
from Extractors.whisper_extractor import WhisperExtractor

extractor_registry = {
    "doc": DocxExtractor,
    "docx": DocxExtractor,
    "pdf": PdfMinerExtractor,
    "wav": WhisperExtractor,
    "mp3": WhisperExtractor,
    "mp4": WhisperExtractor,
    "avi": WhisperExtractor,
    "wmv": WhisperExtractor,
    "wma": WhisperExtractor,
    "web": RequestsExtractor,
    "url": RequestsExtractor,
    "webloc": RequestsExtractor,
}


def get_extractor(full_filepath: str) -> Extractor:
    _, ext = os.path.splitext(full_filepath)
    ext = ext[1:]
    extractor = extractor_registry.get(ext, NotSupportedExtractor)
    return extractor(full_filepath)