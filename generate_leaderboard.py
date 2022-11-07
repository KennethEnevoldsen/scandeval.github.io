"""Python script to generate the leaderboard(s)."""

from collections import defaultdict
from pathlib import Path
import json
from typing import Dict, List, Set
import logging

# Set up logging, which should display logs as "HH:MM:SS [LEVEL] MESSAGE"
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


LANGAUGE_MODEL_BENCHMARK_HTML_START = """---
layout: leaderboard
title: Language Model Benchmark
---

<center><i>Hover over the headings for more information</i></center>

<div class="table-wrapper centered">
<table id="language-model-benchmark" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of trainable parameters in the model">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Sequence length</span></th>
   <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score - Macro-average across tasks">DA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score - Macro-average across tasks">NO</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score - Macro-average across tasks">SV</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total named entity recognition score - Macro-average across languages">NER</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total sentiment classification tagging score - Macro-average across languages">SENT</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total linguistic acceptability score - Macro-average across languages">LA</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total question answering score - Macro-average across languages">QA</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">DaNE</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">AngryTweets</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-da</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish question answering - Exact match / F1-score">ScandiQA-da</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">NorNE-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Matthews correlation coefficient / Macro-average F1-score">NoReC</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nb</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-nn</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian question answering - Exact match / F1-score">ScandiQA-no</span></th>

   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish named entity recognition - Micro-average F1-score / Micro-average F1-score without MISC tags">SUC3</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish sentiment classification - Matthews correlation coefficient / Macro-average F1-score">ABSAbank-Imm</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish linguistic acceptability - Matthews correlation coefficient / Macro-average F1-score">ScaLA-sv</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish question answering - Exact match / F1-score">ScandiQA-sv</span></th>
  </tr>
 </thead>
 <tbody>"""


LANGAUGE_MODEL_BENCHMARK_HTML_END = """ </tbody>
</table>
</div>"""


LANGAUGE_MODEL_BENCHMARK_ENTRY = """  <tr>
   <td>{model_id}</td> <!-- Model ID -->
   <td class="num_model_parameters">{num_model_parameters}</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">{vocabulary_size}</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">{max_sequence_length}</td> <!-- Maximum sequence length of the model-->
   <td class="score"></td> <!-- ScandEval score -->
   <td class="da-score"></td> <!-- Danish score -->
   <td class="no-score"></td> <!-- Norwegian score -->
   <td class="sv-score"></td> <!-- Swedish score -->
   <td class="ner-score"></td> <!-- Mean named entity recognition score -->
   <td class="sent-score"></td> <!-- Mean sentiment classification score -->
   <td class="la-score"></td> <!-- Mean linguistic acceptability score -->
   <td class="qa-score"></td> <!-- Mean question answering score -->
   <td class="da ner">{da_ner}</td> <!-- DaNE -->
   <td class="da sent">{da_sent}</td> <!-- AngryTweets -->
   <td class="da la">{da_la}</td> <!-- ScaLA-da -->
   <td class="da qa">{da_qa}</td> <!-- ScandiQA-da -->
   <td class="no ner">{nb_ner}</td> <!-- NorNE-nb -->
   <td class="no ner">{nn_ner}</td> <!-- NorNE-nn -->
   <td class="no sent">{no_sent}</td> <!-- NoReC -->
   <td class="no la">{nb_la}</td> <!-- ScaLA-nb -->
   <td class="no la">{nn_la}</td> <!-- ScaLA-nn -->
   <td class="no qa">{no_qa}</td> <!-- ScandiQA-no -->
   <td class="sv ner">{sv_ner}</td> <!-- SUC3 -->
   <td class="sv sent">{sv_sent}</td> <!-- ABSAbank-Imm -->
   <td class="sv la">{sv_la}</td> <!-- ScaLA-sv -->
   <td class="sv qa">{sv_qa}</td> <!-- ScandiQA-sv -->
  </tr>"""


# Set up primary/secondary metrics
PRIMARY_METRICS = ["mcc", "em", "micro_f1"]
SECONDARY_METRICS = ["macro_f1", "f1", "micro_f1_no_misc"]


def main() -> None:
    """Generate the leaderboard(s)."""

    # Create path to the leaderboard, and ensure that it exists
    language_model_benchmark_path = Path("language-model-benchmark.md")
    language_model_benchmark_path.parent.mkdir(exist_ok=True, parents=True)
    language_model_benchmark_path.touch(exist_ok=True)

    # Create path to the scores JSONL file, and raise error if it doesn't exist
    scores_path = Path("scandeval_benchmark_results.jsonl")
    if not scores_path.exists():
        raise FileNotFoundError(f"Could not find {scores_path!r}")

    # Load in scores
    with scores_path.open() as f:
        scores = [json.loads(line) for line in f if line.strip()]

    # Reorganize the scores by each model
    model_scores: Dict[str, Dict[str, str]] = defaultdict(dict)
    for record in scores:
        model_id: str = record["model"]
        task: str = record["task"]
        languages: List[str] = record["dataset_languages"]

        # Extract the scores from the dict
        results: Dict[str, float] = record["results"]["total"]
        metrics: Set[str] = {
            key.replace('test_', '').replace('_se', '')
            for key in results.keys() if key.startswith("test_")
        }
        score_dict: Dict[str, str] = dict()
        for metric in metrics:

            # Raise error if the metric is unknown
            if metric not in PRIMARY_METRICS + SECONDARY_METRICS:
                raise ValueError(f"Unknown metric: {metric!r}")

            test_score = results[f"test_{metric}"]
            test_se = results[f"test_{metric}_se"]
            score_dict[metric] = f"{test_score:.2f} ± {test_se:.2f}"

        # Order the metric scores and generate final score string
        primary_metrics = [m for m in PRIMARY_METRICS if m in metrics]
        secondary_metrics = [m for m in SECONDARY_METRICS if m in metrics]
        score_list = primary_metrics + secondary_metrics
        score_str = " / ".join(score_dict[metric] for metric in score_list)

        # Extract single language from the languages
        if len(languages) == 1:
            language = languages[0]
        elif set(languages) == {"nb", "nn"}:
            language = "no"
        else:
            raise ValueError(
                f"Found a task ({task}) which has more than one language: {languages}. "
                "This is currently not supported by the language model benchmark."
            )

        # Extract shorthand notation for the task
        if task == "sentiment-classification":
            task_shorthand = "sent"
        elif task == "named-entity-recognition":
            task_shorthand = "ner"
        elif task == "linguistic-acceptability":
            task_shorthand = "la"
        elif task == "question-answering":
            task_shorthand = "qa"
        else:
            raise ValueError(f"Found invalid task: {task!r}")

        # Add the metrics to the model's score dict
        model_scores[model_id][f"{language} {task_shorthand}"] = score_str

        # Add the model metadata to the model's dict, if it hasn't previously been
        # entered
        for metadata in ["num_model_parameters", "vocabulary_size", "max_sequence_length"]:
            if metadata not in model_scores[model_id] and metadata in record:
                model_scores[model_id][metadata] = str(record[metadata])

    # Generate language model benchmark HTML
    models_to_remove = list()
    html_lines = [LANGAUGE_MODEL_BENCHMARK_HTML_START]
    for model_id, model_dict in model_scores.items():
        values = dict(
            model_id=model_id,
            num_model_parameters=model_dict.get("num_model_parameters", ""),
            vocabulary_size=model_dict.get("vocabulary_size", ""),
            max_sequence_length=model_dict.get("max_sequence_length", ""),
            da_ner=model_dict.get("da ner", ""),
            da_sent=model_dict.get("da sent", ""),
            da_la=model_dict.get("da la", ""),
            da_qa=model_dict.get("da qa", ""),
            nb_ner=model_dict.get("nb ner", ""),
            nn_ner=model_dict.get("nn ner", ""),
            no_sent=model_dict.get("no sent", ""),
            nb_la=model_dict.get("nb la", ""),
            nn_la=model_dict.get("nn la", ""),
            no_qa=model_dict.get("no qa", ""),
            sv_ner=model_dict.get("sv ner", ""),
            sv_sent=model_dict.get("sv sent", ""),
            sv_la=model_dict.get("sv la", ""),
            sv_qa=model_dict.get("sv qa", ""),
        )
        if all([value != "" for value in values.values()]):
            html_lines.append(LANGAUGE_MODEL_BENCHMARK_ENTRY.format(**values))
        else:
            models_to_remove.append(model_id)
    html_lines.append(LANGAUGE_MODEL_BENCHMARK_HTML_END)
    html = "\n".join(html_lines)

    # Remove the models not added to the leaderboard
    for model_id in models_to_remove:
        del model_scores[model_id]

    # Write table to the file
    with language_model_benchmark_path.open("w") as f:
        f.write(html)

    # Log status
    logging.info(
        f"Generated language model benchmark with results from {len(model_scores):,} "
        f"models, stored at {str(language_model_benchmark_path)!r}"
    )


if __name__ == "__main__":
    main()
