from .chunking import chunk_text, get_encoder
from .prompts import ZERO_SHOT, HIERARCHICAL_MERGE
from .openai_client import get_client

def _call_llm(client, model, prompt, temperature):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()

def summarize_text(text, model="gpt-4o-mini", max_tokens=30000, temperature=0.5):
    client = get_client()
    encoder = get_encoder(model)
    chunks = list(chunk_text(text, encoder, max_tokens))

    if len(chunks) == 1:
        return _call_llm(client, model, ZERO_SHOT.format(text=chunks[0]), temperature)

    partials = []
    for chunk in chunks:
        partials.append(
            _call_llm(client, model, ZERO_SHOT.format(text=chunk), temperature)
        )

    return _call_llm(
        client,
        model,
        HIERARCHICAL_MERGE.format(text="\n\n".join(partials)),
        temperature,
    )
