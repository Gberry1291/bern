from openai import OpenAI
import os

# Initialize client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Model for embeddings
EMBEDDING_MODEL = "text-embedding-3-small"


def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding vector for a given text.
    Returns a list of floats.
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding
