from Extractors.extractors_factory import get_extractor
import os


def extract_text_from_path(path):
    if os.path.isdir(path):
        return scan_all_files_in_path(path)
    else:
        return get_extractor(path).get_segments()


def scan_all_files_in_path(folder_path):
    all_segments=[]
    for filename in os.listdir(folder_path):
        extractor = get_extractor(os.path.join(folder_path, filename))
        all_segments.extend(extractor.get_segments())

    return all_segments