from typing import List

from Extractors.extractor import Extractor
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter

class PdfMinerExtractor(Extractor):

    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        text_segments = []

        with open(self.full_filepath, 'rb') as fp:
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
            for page in PDFPage.get_pages(fp):
                page_num += 1

                interpreter.process_page(page)
                layout = device.get_result()
                page_text = []
                for lt_obj in layout:
                    if isinstance(lt_obj, LTTextBox):
                        page_text.append(lt_obj.get_text().strip())
                text_segments.append("\n".join(page_text))

        return text_segments