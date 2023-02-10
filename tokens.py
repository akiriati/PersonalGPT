
import tiktoken

from constants import Config


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(Config.TIKTOKEN_ENCODING)
    num_tokens = len(encoding.encode(string))
    return num_tokens