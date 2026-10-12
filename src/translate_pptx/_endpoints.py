from functools import lru_cache

@lru_cache(maxsize=128)
def prompt_openai(message: str, model="gpt-4o-2024-11-20"):
    """A prompt helper function that sends a message to openAI
    and returns only the text response.
    Results are cached to optimize for repeated queries.
    """
    import os
    import openai

    message = [{"role": "user", "content": message}]

    base_url = os.environ.get("TRANSLATE_PPTX_BASE_URL", None)
    api_key = os.environ.get("TRANSLATE_PPTX_BASE_API_KEY", None)
    base_model = os.environ.get("TRANSLATE_PPTX_BASE_MODEL", None)

    if base_url or api_key:
        client = openai.OpenAI(base_url=base_url, api_key=api_key)
    else:
        client = openai.OpenAI()
    if base_model:
        model = base_model

    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    return response.choices[0].message.content

def prompt_nop(message:str):
    """A prompt helper function that does nothing but returns the contained json. This function is useful for testing."""
    return "```json" + message.split("```json")[1]
