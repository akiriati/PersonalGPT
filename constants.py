import openai
import yaml


class Config():
    DB_PATH = None
    TIKTOKEN_ENCODING = None
    EMBEDDING_MODEL = None
    COMPLETIONS_MODEL = None
    QUESTION_COMPLETIONS_API_PARAMS = None
    NUMBER_OF_MOST_RELEVANT_SECTIONS = None


def init_constants_from_config():
    with open("config.yaml", 'r') as stream:
        yaml_config = yaml.safe_load(stream)
        Config.DB_PATH = yaml_config['DB_PATH']
        Config.TIKTOKEN_ENCODING = yaml_config['TIKTOKEN_ENCODING']
        Config.EMBEDDING_MODEL = yaml_config['EMBEDDING_MODEL']
        Config.COMPLETIONS_MODEL = yaml_config['COMPLETIONS_MODEL']
        Config.NUMBER_OF_MOST_RELEVANT_SECTIONS = yaml_config['NUMBER_OF_MOST_RELEVANT_SECTIONS']

        Config.QUESTION_COMPLETIONS_API_PARAMS = {
            # We use temperature of 0.0 because it gives the most predictable, factual answer.
            "temperature": yaml_config['TEMPERATURE'],
            "max_tokens": yaml_config['MAX_TOKENS'],
            "model": Config.COMPLETIONS_MODEL,
        }

    with open("config-secrets.yaml", 'r') as stream:
        secret_config = yaml.safe_load(stream)
        openai.api_key = secret_config['OPENAI_KEY']


