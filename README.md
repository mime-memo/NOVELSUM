# NOVELSUM

**NOVELSUM** is a research framework for long-form summarization and evaluation of
historical Danish and Norwegian novels.



## Features
- Full-text & hierarchical LLM summarization
- Metadata-based summarization
- Evaluation with ROUGE, BERTScore, and SAS
- Reproducible CLI pipelines

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
export OPENAI_API_KEY=YOUR_KEY
python scripts/summarize_text.py --input data/novels/example.txt --output result.txt
```

## Citation
```
@inproceedings{novelsum2026,
  title={NOVELSUM: Evaluating Long-Form Summary Generation for Historical Scandinavian Novels},
  booktitle={Proceedings of LREC},
  year={2026}
}
```
