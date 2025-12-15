import tiktoken

def get_encoder(model_name: str):
    return tiktoken.encoding_for_model(model_name)

def count_tokens(text: str, encoder) -> int:
    return len(encoder.encode(text))

def chunk_text(text: str, encoder, max_tokens: int):
    tokens = encoder.encode(text)
    for i in range(0, len(tokens), max_tokens):
        yield encoder.decode(tokens[i:i + max_tokens])
