from typing import List
import whisper


class WhisperExtractor():
    def __init__(self, full_filepath: str):
        self.full_filepath = full_filepath

    def get_segments(self) -> List[str]:
        print("start")
        model = whisper.load_model("base")
        result = model.transcribe(self.full_filepath)
        print (result)
        return self.break_text_into_segments(result["text"])

    def break_text_into_segments(self, text, segment_length=500):
        words = text.split()
        segments = []
        segment = ""
        for word in words:
            if len(segment.split()) + len(word.split()) > segment_length:
                segments.append(segment)
                segment = ""
            segment += " " + word
            if word[-1] in [".", "!", "?"]:
                segments.append(segment)
                segment = ""
        segments.append(segment)
        return segments

