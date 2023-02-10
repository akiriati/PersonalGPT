
from datetime import datetime
import pandas as pd

from open_ai_api import get_embedding_batch
from tokens import num_tokens_from_string
from constants import Config


def teach(segments):
    print("Reading DB...")
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    df = pd.read_csv(Config.DB_PATH)

    print("Learning...")

    segments_batch = []
    total_tokens = 0
    text_embedding_list = []

    for segment in segments:

        if total_tokens + num_tokens_from_string(segment) < 8000:
            total_tokens += num_tokens_from_string(segment)
            segments_batch.append(segment)
        else:

            text_embedding_list.extend(get_embedding_batch(segments_batch))
            total_tokens = 0
            segments_batch = []

    if segments_batch:
        text_embedding_list.extend(get_embedding_batch(segments_batch))

    print("Writing to db")

    for text_embedding in text_embedding_list:
        df = pd.concat([df, pd.DataFrame({
            "time": [dt_string],
            "message": [text_embedding["text"]],
            "ada_search": [text_embedding["embedding"]]
        })],
            ignore_index=True)


    df.to_csv(Config.DB_PATH,index=False)
    return "Message saved successfully!"