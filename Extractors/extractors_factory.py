from Extractors.Scrappers.requests_scrapper import RequestsScrapper
from Extractors.Segmentors.by_word_count import ByWordCount
from Extractors.extractor import Extractor
from Extractors.link_extractor import LinkExtractor
from Extractors.ms_word_extractor import DocxExtractor
from Extractors.not_supported_extractor import NotSupportedExtractor
import os
from Extractors.pdf_extractor import PdfMinerExtractor
from Extractors.text_extractor import TextExtractor
from Extractors.whisper_extractor import WhisperExtractor

word_count_segmentor = ByWordCount(500)

scrapper = RequestsScrapper()

link_extractor = LinkExtractor(word_count_segmentor, scrapper)
transcript_extractor = WhisperExtractor(word_count_segmentor)
ms_doc_extracror = DocxExtractor()
pdf_extractor = PdfMinerExtractor()
text_extractor = TextExtractor(word_count_segmentor)

extractor_registry = {
    "txt": text_extractor,
    "md": text_extractor,
    "doc": ms_doc_extracror,
    "docx": ms_doc_extracror,
    "pdf": pdf_extractor,
    "wav": transcript_extractor,
    "mp3": transcript_extractor,
    "mp4": transcript_extractor,
    "avi": transcript_extractor,
    "wmv": transcript_extractor,
    "wma": transcript_extractor,
    "web": link_extractor,
    "url": link_extractor,
    "webloc": link_extractor,
}


def get_extractor(full_filepath: str) -> Extractor:
    _, ext = os.path.splitext(full_filepath)
    ext = ext[1:]
    return extractor_registry.get(ext, NotSupportedExtractor())