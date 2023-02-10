from Extractors.extractors_factory import get_extractor
import os


def scan_all_files_in_path(folder_path):
    all_segments=[]
    folder_path = os.path.expanduser(folder_path)
    for filename in os.listdir(folder_path):
        print(os.path.join(folder_path, filename))
        extractor = get_extractor(os.path.join(folder_path, filename))

        all_segments.extend(extractor.get_segments())

    return all_segments