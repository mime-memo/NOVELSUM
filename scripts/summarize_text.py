import argparse
from pathlib import Path
from novelsum.summarization import summarize_text

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
parser.add_argument("--model", default="gpt-4o-mini")
parser.add_argument("--chunk-size", type=int, default=30000)
args = parser.parse_args()

text = Path(args.input).read_text(encoding="utf-8")
summary = summarize_text(text, args.model, args.chunk_size)
Path(args.output).write_text(summary, encoding="utf-8")
