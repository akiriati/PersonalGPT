import numpy as np
import pandas as pd
from db import return_most_similiar
from open_ai_api import get_embedding_batch, get_completion
from constants import Config


def query(question, history=""):
    df = pd.read_csv(Config.DB_PATH)
    prompt = construct_prompt(question, df, history, top_n=3)
    # Get the answer
    response = get_completion(prompt)
    return (response["choices"][0]["text"])




def construct_prompt(question, df, history="", top_n=Config.NUMBER_OF_MOST_RELEVANT_SECTIONS):
    context = generate_context(question, df, top_n)
    header = """Answer the question in details, based on the provided context and the conversation history, and if the answer is not there, say I don't know."""
    context = """\n\nContext:\n\n""" + context
    conversation_prompt = ("""\n\nConversation History:\n\n""" + history) if history else ""
    return header + "".join(context) + "".join(conversation_prompt) + "Q: " + question + "\n A:"

def generate_context(question, df, top_n=Config.NUMBER_OF_MOST_RELEVANT_SECTIONS):
    most_similiar = return_most_similiar(question, df, top_n)
    # Get the top 3 most similar messages
    top_messages = most_similiar["message"].values
    # Concatenate the top 3 messages into a single string
    context = '\n '.join(top_messages)
    return context

