from typing import List
import whisper

from Extractors.Segmentors.segmentor import Segmentor


class WhisperExtractor():
    def __init__(self, segmentor: Segmentor):
        self.segmentor = segmentor

    def get_segments(self, full_filepath: str) -> List[str]:
        print("start")
        model = whisper.load_model("base")
        result = model.transcribe(full_filepath)
        print (result)
        return self.segmentor.break_text_into_segments(result["text"])


