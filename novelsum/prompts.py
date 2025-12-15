ZERO_SHOT = """You are an attentive reader who is good at summarizing a long text.
Please provide a Danish summary of the following novel.
Mention fictional time, key places, main characters, and plot events.
Focus on facts rather than interpretation.

{text}
"""

HIERARCHICAL_MERGE = """You are an attentive reader who is good at summarizing a long text.
Here are summaries of different parts of a 19th-century Danish novel:

{text}

Please merge these into a single, well-structured Danish summary.
"""

METADATA = """You are an attentive reader who is good at summarizing a long text.
Title: {title}
Author: {author}

Write a factual Danish summary including time, place, characters, and plot.
"""
