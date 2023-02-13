from Extractors.Segmentors.segmentor import Segmentor

class ByWordCount(Segmentor):
    def __init__(self, max_words):
        self.max_words = max_words

    def break_text_into_segments(self, text):
        words = text.split()
        segments = []
        segment = ""
        for word in words:
            if len(segment.split()) + len(word.split()) > self.max_words:
                segments.append(segment)
                segment = ""
            segment += " " + word
            if word[-1] in [".", "!", "?"]:
                segments.append(segment)
                segment = ""
        segments.append(segment)
        return segments