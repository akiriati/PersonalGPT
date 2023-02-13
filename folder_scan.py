from Extractors.extractors_factory import get_extractor
import os


def extract_text_from_path(path):
    if os.path.isdir(path):
        return scan_all_files_in_path(path)
    else:
        return get_extractor(path).get_segments(path)


def scan_all_files_in_path(folder_path):
    all_segments=[]
    for filename in os.listdir(folder_path):
        full_filepath = os.path.join(folder_path, filename)
        extractor = get_extractor(full_filepath)
        all_segments.extend(extractor.get_segments(full_filepath))

    return all_segments