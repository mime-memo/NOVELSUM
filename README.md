# NOVELSUM: Evaluating Long-Form Summary Generation for Historical Scandinavian Novels

This repository contains code, data, and resources for the NOVELSUM project, which evaluates long-form summarization of late-19th-century Danish and Norwegian novels.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run summarization: `python code/summarization.py`
3. Evaluate results: `python code/evaluation.py`

## Dataset
The dataset includes 34 historical Scandinavian novels with:
- Full novel texts (public domain)
- Professional reference summaries (copyrighted, not distributed)
- Generated summaries from multiple models

## Models Evaluated
- Baseline: LED, LongT5, DanSumT5-large
- LLMs: DeepSeek-V3, Llama-3.2-3B, gemma-3n-E4B-it, GPT-4o-mini
- Evaluation: Qwen3-235B-A22B-Instruct-2507-FP8

## Citation
If you use this resource, please cite our LREC 2026 paper.
