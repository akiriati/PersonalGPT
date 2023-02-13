from typing import List

from Extractors.Segmentors.segmentor import Segmentor
from Extractors.extractor import Extractor
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter


class PdfMinerExtractor(Extractor):

    def get_segments(self, full_filepath: str) -> List[str]:
        with open(full_filepath, 'rb') as fp:
            # Create a PDF resource manager and set parameters
            rsrcmgr = PDFResourceManager()
            laparams = LAParams()

            # Create a PDF page aggregator
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # List to store text segments
            text_segments = []

            # Loop through all the pages in the PDF
            page_num = 0
            all_texts = []
            for page in PDFPage.get_pages(fp):
                page_num += 1

                interpreter.process_page(page)
                layout = device.get_result()
                page_text = []
                for lt_obj in layout:
                    if isinstance(lt_obj, LTTextBox):
                        page_text.append(lt_obj.get_text().strip())

                all_texts.append(page_text)

            return all_texts