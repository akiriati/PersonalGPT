from typing import List
import whisper

from Extractors.segments import break_text_into_segments


class WhisperExtractor():
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        print("start")
        model = whisper.load_model("base")
        result = model.transcribe(self.full_filepath)
        print (result)
        return break_text_into_segments(result["text"])


