def break_text_into_segments(text, segment_length=500):
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
