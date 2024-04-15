---
layout: page
mathjax: true
title: ScandEval
subtitle: A Natural Language Processing Benchmark
use-site-title: true
meta-description: A Multilingual Robust Natural Language Processing Benchmark
---
The `ScandEval` benchmark can be used to compare pretrained language models on tasks in
Danish, Swedish, Norwegian Bokmål, Norwegian Nynorsk, Icelandic, Faroese, German, Dutch
and English.

When evaluating language models we also split "Natural Language Processing" (NLP) into
two groups. "Natural Language Understanding" (NLU) is concerned with an analysis of
input text, and being able to extract insights from it. "Natural Language Generation"
(NLG) is about *generating* text in a coherent and human-like way. ScandEval has both
NLU and NLG leaderboards, which you can access in the top menu.

The NLU benchmarks evaluate the models on a variety of tasks: named entity recognition,
sentiment classification, linguistic acceptability and question answering. For encoder
(i.e., BERT-style) models, the scores are the the result of finetuning the models 10
times and evaluating each of these 10 finetuned models on a bootstrapped version of the
test set of the given dataset (different bootstrap for each of the 10 runs). The mean
of these 10 scores for the given (model, dataset) pair are then presented in the
leaderboard, with an associated 95% confidence interval. For decoder (i.e., GPT-style)
models, the models are evaluated using in-context learning with few-shot prompts. The
few-shot examples are sampled randomly from the training split, and we again benchmark
the models 10 times with bootstrapped test sets and different few-shot examples in each
iteration.

All benchmark results have been computed using the associated [ScandEval Python
package](https://github.com/ScandEval/ScandEval), which you can use to replicate the
results as well. The methodology of the benchmark can be [found in the associated
research paper](https://aclanthology.org/2023.nodalida-1.20/).
