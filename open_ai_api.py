import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential

from constants import Config

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_completion(prompt):
    return openai.Completion.create(prompt=prompt, **Config.QUESTION_COMPLETIONS_API_PARAMS)

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding_batch(texts):
    texts = [string.replace("\n", " ") for string in texts if string]

    embedding_list = openai.Embedding.create(input=texts, engine=Config.EMBEDDING_MODEL)["data"]

    embedding_with_text = []

    for embedding in embedding_list:
        embedding_with_text.append(
            {
                'text': texts[embedding["index"]],
                'embedding': embedding["embedding"]
            }
        )

    return embedding_with_text

