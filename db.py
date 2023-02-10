import os

import numpy as np
import pandas as pd

from open_ai_api import get_embedding_batch
from constants import Config


def init_db():
    # Check if the database exists if not create it
    if not os.path.isfile(Config.DB_PATH):
        #Create the dataframe with columns for time and message
        df = pd.DataFrame(columns=["time","message", "ada_search"])
        # Save the dataframe to a csv file
        df.to_csv(Config.DB_PATH,index=False)

def return_most_similiar(question, df, top_n=3):
    # Get the embedding for the question
    question_embedding = get_embedding_batch([question])[0]["embedding"]
    # Get the embedding for the messages in the database
    df["ada_search"] = df["ada_search"].apply(eval).apply(np.array)
    # Get the similarity between the question and the messages in the database
    df['similarity'] = df.ada_search.apply(lambda x: cosine_similarity(x, question_embedding))
    # Get the index of the top 3 most similar message
    most_similiar = df.sort_values('similarity', ascending=False).head(top_n)
    return most_similiar


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
