---
layout: leaderboard
title: Dutch NLG 🇳🇱
---

<center>Last updated: 28/10/2024 09:54:10 CET</center>

<div class="blocked centered">
  <input type="checkbox" id="merged-models-checkbox">
  <label for="merged-models-checkbox">Include merged models</label>
</div>

<div class="blocked table-wrapper centered">
<table id="dutch-nlg-test" class="sortable fixed centered small-font">
 <thead>
  <tr>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Hugging Face Hub Model ID">Model ID</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of parameters in the model, in millions">Parameters</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of unique tokens that the model has been trained on, in thousands">Vocabulary size</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="The maximum amount of tokens the model can process">Context</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Whether the model can be used commercially">Commercial</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Number of tokens processed per second / Number of tokens processed in small documents per second">Speed</span></th>

   <th id="rank-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="1 + the average number of standard deviations away from the best model">Rank</span></th>
    
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch named entity recognition - Micro-average F1-score without MISC tags / Micro-average F1-score with MISC tags">CoNLL-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch sentiment classification - Matthews Correlation Coefficient / Macro-average F1-score">Dutch Social</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch linguistic acceptability - Matthews Correlation Coefficient / Macro-average F1-score">ScaLA-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch reading comprehension - Exact Match / F1-score">SQuAD-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch summarization - BERTScore / ROUGE-L">Wiki-Lingua-NL</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch knowledge - Matthews Correlation Coefficient / Accuracy">MMLU-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Dutch common sense reasoning - Matthews Correlation Coefficient / Accuracy">HellaSwag-nl</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on CoNLL-nl">CoNLL-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Dutch Social">Dutch Social version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on ScaLA-nl">ScaLA-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on SQuAD-nl">SQuAD-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on Wiki-Lingua-NL">Wiki-Lingua-NL version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on MMLU-nl">MMLU-nl version</span></th>
   <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval version used to benchmark the model on HellaSwag-nl">HellaSwag-nl version</span></th>
  </tr>
 </thead>
 <tbody>
  <tr class="not-merged-model">
   <td>gpt-4-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8316</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">597 ± 197 / 93 ± 33</td> <!-- Model inference speed -->
   <td class="rank">1.19</td> <!-- ScandEval rank -->
   <td class="nl ner">73.35 ± 2.61 / 56.00 ± 2.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.92 ± 2.78 / 40.80 ± 2.43</td> <!-- Dutch Social -->
   <td class="nl la">76.70 ± 2.39 / 88.16 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.03 ± 1.96 / 76.47 ± 1.22</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.97 ± 0.41 / 22.66 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.71 ± 2.96 / 78.12 ± 2.24</td> <!-- MMLU-nl -->
   <td class="nl reason">90.07 ± 1.29 / 92.54 ± 0.98</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">312 ± 55 / 177 ± 51</td> <!-- Model inference speed -->
   <td class="rank">1.43</td> <!-- ScandEval rank -->
   <td class="nl ner">72.91 ± 3.24 / 68.06 ± 4.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">19.08 ± 3.37 / 42.04 ± 2.31</td> <!-- Dutch Social -->
   <td class="nl la">54.33 ± 3.49 / 75.54 ± 2.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.99 ± 2.07 / 77.63 ± 1.16</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.41 ± 0.97 / 25.41 ± 1.66</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.33 ± 1.92 / 73.98 ± 1.56</td> <!-- MMLU-nl -->
   <td class="nl reason">71.06 ± 2.82 / 78.16 ± 2.22</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4-1106-preview (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">576 ± 221 / 81 ± 28</td> <!-- Model inference speed -->
   <td class="rank">1.50</td> <!-- ScandEval rank -->
   <td class="nl ner">66.44 ± 2.18 / 56.97 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.22 ± 3.26 / 33.41 ± 3.24</td> <!-- Dutch Social -->
   <td class="nl la">72.30 ± 2.26 / 85.96 ± 1.13</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.81 ± 1.23 / 74.51 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.13 ± 0.50 / 17.61 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">70.04 ± 1.91 / 77.58 ± 1.42</td> <!-- MMLU-nl -->
   <td class="nl reason">88.29 ± 2.26 / 91.17 ± 1.70</td> <!-- HellaSwag-nl -->
   <td>12.3.2</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.3.2</td> <!-- SQuAD-nl version -->
   <td>12.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-70B-Instruct (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">70554</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,673 ± 583 / 275 ± 85</td> <!-- Model inference speed -->
   <td class="rank">1.61</td> <!-- ScandEval rank -->
   <td class="nl ner">74.64 ± 3.67 / 71.84 ± 4.01</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.90 ± 2.04 / 41.93 ± 1.60</td> <!-- Dutch Social -->
   <td class="nl la">49.54 ± 4.22 / 74.03 ± 2.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">44.77 ± 1.67 / 71.44 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">70.28 ± 0.65 / 22.72 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">65.80 ± 3.16 / 74.38 ± 2.37</td> <!-- MMLU-nl -->
   <td class="nl reason">76.21 ± 1.36 / 82.15 ± 1.01</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-2024-05-13 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128000</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">916 ± 329 / 114 ± 38</td> <!-- Model inference speed -->
   <td class="rank">1.65</td> <!-- ScandEval rank -->
   <td class="nl ner">76.75 ± 3.44 / 61.13 ± 4.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.80 ± 2.24 / 32.52 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">56.26 ± 4.51 / 73.83 ± 3.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.55 ± 2.54 / 76.28 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.86 ± 0.46 / 16.93 ± 0.91</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">73.11 ± 1.87 / 79.69 ± 1.46</td> <!-- MMLU-nl -->
   <td class="nl reason">92.69 ± 1.46 / 94.53 ± 1.09</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.2</td> <!-- Dutch Social version -->
   <td>12.10.2</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.2</td> <!-- MMLU-nl version -->
   <td>12.10.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>152334H/miqu-1-70b-sf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32889</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,126 ± 676 / 319 ± 104</td> <!-- Model inference speed -->
   <td class="rank">1.75</td> <!-- ScandEval rank -->
   <td class="nl ner">67.00 ± 3.69 / 56.41 ± 4.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.33 ± 4.14 / 36.14 ± 2.91</td> <!-- Dutch Social -->
   <td class="nl la">55.48 ± 4.37 / 77.55 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.02 ± 1.67 / 76.87 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.95 ± 0.75 / 21.31 ± 1.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">54.36 ± 1.61 / 65.70 ± 1.26</td> <!-- MMLU-nl -->
   <td class="nl reason">70.26 ± 3.64 / 77.62 ± 2.82</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-27b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">27227</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,516 ± 257 / 480 ± 148</td> <!-- Model inference speed -->
   <td class="rank">1.84</td> <!-- ScandEval rank -->
   <td class="nl ner">65.20 ± 1.76 / 53.16 ± 2.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.80 ± 0.93 / 36.86 ± 1.08</td> <!-- Dutch Social -->
   <td class="nl la">59.02 ± 1.53 / 79.44 ± 0.78</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.60 ± 1.51 / 74.99 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.03 ± 1.25 / 20.76 ± 1.31</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">59.71 ± 0.83 / 69.70 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">70.70 ± 1.31 / 77.81 ± 0.99</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,062 ± 397 / 589 ± 178</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="nl ner">52.62 ± 2.15 / 39.41 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.78 ± 1.31 / 32.80 ± 0.87</td> <!-- Dutch Social -->
   <td class="nl la">59.23 ± 1.58 / 79.42 ± 0.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.78 ± 0.87 / 72.71 ± 0.70</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.39 ± 0.71 / 20.04 ± 1.05</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.99 ± 0.77 / 65.31 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">65.58 ± 1.18 / 73.75 ± 0.94</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>upstage/SOLAR-10.7B-v1.0 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">10732</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,780 ± 906 / 799 ± 261</td> <!-- Model inference speed -->
   <td class="rank">2.08</td> <!-- ScandEval rank -->
   <td class="nl ner">65.37 ± 1.61 / 46.10 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.93 ± 1.80 / 34.67 ± 2.84</td> <!-- Dutch Social -->
   <td class="nl la">41.67 ± 1.53 / 69.81 ± 1.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">67.75 ± 0.62 / 78.01 ± 0.45</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.83 ± 0.35 / 26.12 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.18 ± 0.57 / 55.06 ± 0.44</td> <!-- MMLU-nl -->
   <td class="nl reason">65.34 ± 1.05 / 73.48 ± 0.83</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-9b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">9242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,038 ± 406 / 566 ± 172</td> <!-- Model inference speed -->
   <td class="rank">2.09</td> <!-- ScandEval rank -->
   <td class="nl ner">57.13 ± 2.73 / 36.21 ± 1.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">17.43 ± 2.17 / 40.83 ± 1.50</td> <!-- Dutch Social -->
   <td class="nl la">31.39 ± 5.53 / 56.70 ± 5.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.33 ± 1.35 / 73.56 ± 0.52</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.59 ± 1.21 / 21.08 ± 1.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">53.71 ± 0.86 / 65.15 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">53.26 ± 3.38 / 63.65 ± 2.84</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Ministral-8B-Instruct-2410 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8020</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,821 ± 1,090 / 1,561 ± 506</td> <!-- Model inference speed -->
   <td class="rank">2.13</td> <!-- ScandEval rank -->
   <td class="nl ner">66.51 ± 1.38 / 52.40 ± 2.62</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.55 ± 2.14 / 37.36 ± 1.32</td> <!-- Dutch Social -->
   <td class="nl la">34.46 ± 2.79 / 65.61 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.23 ± 1.16 / 72.56 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.87 ± 0.72 / 21.06 ± 1.13</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.81 ± 1.05 / 55.44 ± 0.80</td> <!-- MMLU-nl -->
   <td class="nl reason">60.68 ± 1.04 / 70.24 ± 0.85</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Nexusflow/Starling-LM-7B-beta (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,876 ± 1,021 / 1,677 ± 546</td> <!-- Model inference speed -->
   <td class="rank">2.15</td> <!-- ScandEval rank -->
   <td class="nl ner">64.47 ± 2.31 / 40.89 ± 2.81</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.83 ± 1.91 / 41.53 ± 1.23</td> <!-- Dutch Social -->
   <td class="nl la">45.69 ± 1.76 / 72.13 ± 1.39</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.03 ± 1.37 / 73.17 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.34 ± 0.77 / 22.22 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">37.60 ± 0.83 / 53.13 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">54.33 ± 0.84 / 65.41 ± 0.59</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-3.5-turbo-0613 (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4095</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">921 ± 293 / 113 ± 37</td> <!-- Model inference speed -->
   <td class="rank">2.16</td> <!-- ScandEval rank -->
   <td class="nl ner">68.96 ± 3.80 / 58.45 ± 3.71</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.81 ± 3.30 / 30.88 ± 2.25</td> <!-- Dutch Social -->
   <td class="nl la">58.95 ± 4.48 / 78.64 ± 2.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.57 ± 2.33 / 68.26 ± 1.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">69.13 ± 0.41 / 21.32 ± 0.75</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.28 ± 2.88 / 56.45 ± 2.26</td> <!-- MMLU-nl -->
   <td class="nl reason">61.52 ± 2.69 / 70.62 ± 2.20</td> <!-- HellaSwag-nl -->
   <td>0.0.0</td> <!-- CoNLL-nl version -->
   <td>0.0.0</td> <!-- Dutch Social version -->
   <td>0.0.0</td> <!-- ScaLA-nl version -->
   <td>0.0.0</td> <!-- SQuAD-nl version -->
   <td>0.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>0.0.0</td> <!-- MMLU-nl version -->
   <td>0.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,892 ± 650 / 318 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.21</td> <!-- ScandEval rank -->
   <td class="nl ner">66.50 ± 3.72 / 57.66 ± 3.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.82 ± 4.30 / 34.91 ± 2.53</td> <!-- Dutch Social -->
   <td class="nl la">49.55 ± 4.95 / 73.43 ± 3.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">65.26 ± 1.55 / 77.36 ± 1.41</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.28 ± 1.07 / 21.33 ± 1.39</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">49.41 ± 2.21 / 61.91 ± 1.74</td> <!-- MMLU-nl -->
   <td class="nl reason">54.50 ± 4.84 / 65.70 ± 3.64</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,116 ± 943 / 1,436 ± 472</td> <!-- Model inference speed -->
   <td class="rank">2.28</td> <!-- ScandEval rank -->
   <td class="nl ner">53.21 ± 1.37 / 42.13 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.72 ± 2.18 / 39.38 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">40.85 ± 4.16 / 67.34 ± 3.66</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.41 ± 0.99 / 74.19 ± 0.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.70 ± 0.37 / 19.34 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">39.74 ± 0.95 / 54.61 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">54.37 ± 0.74 / 65.48 ± 0.65</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-Nemo-Instruct-2407 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">12248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024128</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,095 ± 2,193 / 1,063 ± 344</td> <!-- Model inference speed -->
   <td class="rank">2.31</td> <!-- ScandEval rank -->
   <td class="nl ner">66.57 ± 1.86 / 48.40 ± 2.67</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.10 ± 1.55 / 33.62 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">40.31 ± 2.25 / 69.53 ± 1.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.99 ± 0.95 / 74.24 ± 0.63</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.68 / 20.75 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.50 ± 0.84 / 56.53 ± 0.62</td> <!-- MMLU-nl -->
   <td class="nl reason">48.51 ± 1.44 / 60.59 ± 1.34</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-70b-chat-hf (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">68977</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4221</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,979 ± 621 / 320 ± 105</td> <!-- Model inference speed -->
   <td class="rank">2.36</td> <!-- ScandEval rank -->
   <td class="nl ner">64.00 ± 3.52 / 48.94 ± 3.83</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.30 ± 3.75 / 30.50 ± 2.48</td> <!-- Dutch Social -->
   <td class="nl la">30.88 ± 4.62 / 59.62 ± 4.50</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.14 ± 1.55 / 70.96 ± 1.01</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.71 ± 0.70 / 19.82 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">45.47 ± 2.07 / 59.14 ± 1.69</td> <!-- MMLU-nl -->
   <td class="nl reason">42.91 ± 3.26 / 57.30 ± 2.39</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,411 ± 465 / 686 ± 215</td> <!-- Model inference speed -->
   <td class="rank">2.40</td> <!-- ScandEval rank -->
   <td class="nl ner">69.76 ± 1.36 / 57.66 ± 1.36</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.51 ± 1.59 / 39.71 ± 1.21</td> <!-- Dutch Social -->
   <td class="nl la">37.58 ± 3.42 / 66.98 ± 2.22</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.26 ± 2.09 / 65.63 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.84 ± 0.62 / 21.41 ± 1.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.98 ± 0.71 / 55.51 ± 0.59</td> <!-- MMLU-nl -->
   <td class="nl reason">39.98 ± 1.59 / 54.32 ± 1.27</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>senseable/WestLake-7B-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,993 ± 1,028 / 1,742 ± 561</td> <!-- Model inference speed -->
   <td class="rank">2.42</td> <!-- ScandEval rank -->
   <td class="nl ner">64.25 ± 2.23 / 46.52 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.66 ± 1.99 / 39.45 ± 1.52</td> <!-- Dutch Social -->
   <td class="nl la">28.59 ± 1.48 / 61.24 ± 1.46</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.64 ± 0.86 / 68.04 ± 0.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.66 ± 0.57 / 19.51 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.37 ± 1.30 / 51.43 ± 0.96</td> <!-- MMLU-nl -->
   <td class="nl reason">47.50 ± 1.75 / 60.41 ± 1.32</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>gpt-4o-mini-2024-07-18 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">200</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">128126</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,171 ± 378 / 120 ± 39</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="nl ner">68.20 ± 1.93 / 49.92 ± 2.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.65 ± 1.80 / 14.84 ± 2.18</td> <!-- Dutch Social -->
   <td class="nl la">31.15 ± 7.70 / 52.16 ± 7.03</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.17 ± 1.82 / 72.08 ± 0.90</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.45 / 18.21 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">54.56 ± 1.84 / 64.78 ± 1.89</td> <!-- MMLU-nl -->
   <td class="nl reason">65.27 ± 1.51 / 72.80 ± 1.37</td> <!-- HellaSwag-nl -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.11.0</td> <!-- MMLU-nl version -->
   <td>12.11.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3.1-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,439 ± 459 / 703 ± 219</td> <!-- Model inference speed -->
   <td class="rank">2.44</td> <!-- ScandEval rank -->
   <td class="nl ner">64.79 ± 1.96 / 45.48 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.95 ± 2.83 / 37.12 ± 2.19</td> <!-- Dutch Social -->
   <td class="nl la">32.97 ± 2.68 / 58.52 ± 2.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.89 ± 1.06 / 74.73 ± 1.02</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.29 ± 1.29 / 20.14 ± 1.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.44 ± 1.33 / 53.68 ± 1.01</td> <!-- MMLU-nl -->
   <td class="nl reason">30.88 ± 2.27 / 47.18 ± 1.81</td> <!-- HellaSwag-nl -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.11.0</td> <!-- Dutch Social version -->
   <td>12.11.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>CohereForAI/aya-23-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8028</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,608 ± 1,062 / 1,472 ± 479</td> <!-- Model inference speed -->
   <td class="rank">2.46</td> <!-- ScandEval rank -->
   <td class="nl ner">60.81 ± 1.94 / 46.59 ± 3.32</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.63 / 24.82 ± 0.95</td> <!-- Dutch Social -->
   <td class="nl la">31.12 ± 2.35 / 64.29 ± 1.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.00 ± 1.23 / 74.60 ± 0.67</td> <!-- SQuAD-nl -->
   <td class="nl summ">72.90 ± 0.24 / 30.63 ± 0.42</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.37 ± 1.09 / 48.63 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">53.32 ± 1.89 / 64.30 ± 1.72</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/NeuralBeagle14-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,549 ± 472 / 784 ± 245</td> <!-- Model inference speed -->
   <td class="rank">2.48</td> <!-- ScandEval rank -->
   <td class="nl ner">63.53 ± 3.80 / 50.43 ± 2.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 4.22 / 39.00 ± 3.14</td> <!-- Dutch Social -->
   <td class="nl la">27.76 ± 4.44 / 62.44 ± 2.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.94 ± 1.12 / 70.12 ± 0.96</td> <!-- SQuAD-nl -->
   <td class="nl summ">71.20 ± 0.46 / 23.47 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">40.23 ± 2.86 / 54.77 ± 2.16</td> <!-- MMLU-nl -->
   <td class="nl reason">47.87 ± 2.49 / 60.78 ± 1.85</td> <!-- HellaSwag-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>9.3.2</td> <!-- Dutch Social version -->
   <td>9.3.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.2</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,909 ± 1,215 / 978 ± 319</td> <!-- Model inference speed -->
   <td class="rank">2.53</td> <!-- ScandEval rank -->
   <td class="nl ner">68.72 ± 1.81 / 54.89 ± 2.10</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.67 ± 2.51 / 41.36 ± 2.04</td> <!-- Dutch Social -->
   <td class="nl la">32.91 ± 2.56 / 64.93 ± 1.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.36 ± 1.31 / 67.50 ± 0.69</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.62 ± 0.82 / 18.19 ± 1.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.18 ± 1.31 / 51.68 ± 1.05</td> <!-- MMLU-nl -->
   <td class="nl reason">33.91 ± 1.71 / 48.01 ± 1.47</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>skole-gpt (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,583 ± 977 / 686 ± 231</td> <!-- Model inference speed -->
   <td class="rank">2.56</td> <!-- ScandEval rank -->
   <td class="nl ner">62.16 ± 1.09 / 45.76 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.92 ± 1.08 / 24.28 ± 0.76</td> <!-- Dutch Social -->
   <td class="nl la">32.76 ± 2.94 / 65.17 ± 2.79</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.87 ± 0.92 / 72.57 ± 0.85</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.39 ± 0.73 / 20.83 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">46.17 ± 0.64 / 59.57 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">33.31 ± 1.83 / 49.12 ± 1.64</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="merged-model">
   <td>mlabonne/AlphaMonarch-7B (few-shot, val)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,340 ± 1,262 / 1,157 ± 375</td> <!-- Model inference speed -->
   <td class="rank">2.61</td> <!-- ScandEval rank -->
   <td class="nl ner">64.71 ± 5.15 / 53.58 ± 3.82</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.14 ± 3.37 / 38.64 ± 2.36</td> <!-- Dutch Social -->
   <td class="nl la">25.22 ± 5.45 / 61.28 ± 2.51</td> <!-- ScaLA-nl -->
   <td class="nl rc">46.34 ± 1.07 / 66.56 ± 1.49</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.71 ± 0.59 / 17.76 ± 0.71</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">38.49 ± 2.59 / 53.52 ± 2.03</td> <!-- MMLU-nl -->
   <td class="nl reason">47.66 ± 2.91 / 60.31 ± 2.30</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>yhavinga/Boreas-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,913 ± 459 / 1,129 ± 342</td> <!-- Model inference speed -->
   <td class="rank">2.62</td> <!-- ScandEval rank -->
   <td class="nl ner">60.22 ± 1.55 / 38.72 ± 1.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.97 ± 1.80 / 35.17 ± 3.03</td> <!-- Dutch Social -->
   <td class="nl la">30.94 ± 4.81 / 62.66 ± 3.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.19 ± 1.96 / 67.52 ± 1.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.60 ± 1.93 / 20.00 ± 1.35</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.34 ± 1.32 / 51.45 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">31.47 ± 2.90 / 47.64 ± 2.52</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Meta-Llama-3-8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,687 ± 1,121 / 967 ± 313</td> <!-- Model inference speed -->
   <td class="rank">2.63</td> <!-- ScandEval rank -->
   <td class="nl ner">62.26 ± 2.20 / 42.41 ± 2.02</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.45 ± 2.69 / 33.45 ± 1.99</td> <!-- Dutch Social -->
   <td class="nl la">30.30 ± 3.94 / 62.28 ± 2.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.99 ± 1.00 / 73.73 ± 0.98</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.17 ± 1.24 / 18.63 ± 1.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.38 ± 0.86 / 52.08 ± 0.66</td> <!-- MMLU-nl -->
   <td class="nl reason">28.33 ± 2.31 / 45.29 ± 1.78</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat-Sft-Bf16 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,413 ± 463 / 700 ± 220</td> <!-- Model inference speed -->
   <td class="rank">2.67</td> <!-- ScandEval rank -->
   <td class="nl ner">56.83 ± 2.31 / 46.81 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.79 ± 1.96 / 41.48 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">23.58 ± 2.69 / 50.85 ± 3.74</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.90 ± 1.80 / 70.07 ± 0.77</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.06 ± 1.20 / 18.45 ± 1.09</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.73 ± 0.75 / 50.05 ± 0.57</td> <!-- MMLU-nl -->
   <td class="nl reason">29.29 ± 1.83 / 45.90 ± 1.77</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>robinsmits/Qwen1.5-7B-Dutch-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7719</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,686 ± 1,131 / 996 ± 326</td> <!-- Model inference speed -->
   <td class="rank">2.72</td> <!-- ScandEval rank -->
   <td class="nl ner">57.81 ± 2.68 / 47.15 ± 2.77</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.62 ± 2.25 / 41.08 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">25.34 ± 2.37 / 54.46 ± 3.43</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.81 ± 1.44 / 70.49 ± 0.68</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.51 ± 2.40 / 15.62 ± 1.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.78 ± 0.80 / 50.83 ± 0.58</td> <!-- MMLU-nl -->
   <td class="nl reason">30.29 ± 1.78 / 46.74 ± 1.68</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Reynaerde-7B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,562 ± 487 / 782 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.73</td> <!-- ScandEval rank -->
   <td class="nl ner">59.16 ± 2.29 / 42.33 ± 2.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.39 ± 1.44 / 28.74 ± 1.05</td> <!-- Dutch Social -->
   <td class="nl la">19.50 ± 1.96 / 55.52 ± 3.92</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.96 ± 1.24 / 72.79 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.19 ± 0.63 / 20.85 ± 0.78</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.93 ± 0.63 / 49.37 ± 0.55</td> <!-- MMLU-nl -->
   <td class="nl reason">28.04 ± 1.54 / 45.48 ± 1.35</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Reynaerde-7B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,554 ± 483 / 781 ± 247</td> <!-- Model inference speed -->
   <td class="rank">2.75</td> <!-- ScandEval rank -->
   <td class="nl ner">56.22 ± 2.46 / 38.04 ± 1.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.22 ± 1.85 / 30.99 ± 1.36</td> <!-- Dutch Social -->
   <td class="nl la">20.04 ± 1.67 / 55.38 ± 3.62</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.15 ± 1.01 / 72.89 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.28 ± 0.61 / 20.97 ± 0.82</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">32.44 ± 0.61 / 49.05 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">31.24 ± 1.92 / 47.72 ± 1.69</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-8b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8171</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,090 ± 937 / 1,423 ± 466</td> <!-- Model inference speed -->
   <td class="rank">2.77</td> <!-- ScandEval rank -->
   <td class="nl ner">53.62 ± 2.29 / 40.51 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.37 ± 1.25 / 36.94 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">23.47 ± 1.79 / 60.17 ± 1.23</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.20 ± 1.02 / 72.98 ± 0.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.34 ± 3.24 / 18.49 ± 1.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.69 ± 0.59 / 50.59 ± 0.56</td> <!-- MMLU-nl -->
   <td class="nl reason">31.36 ± 1.90 / 46.78 ± 1.51</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ReBatch/Llama-3-8B-dutch (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,800 ± 1,275 / 566 ± 194</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="nl ner">60.14 ± 2.00 / 44.91 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.07 ± 1.98 / 34.77 ± 1.31</td> <!-- Dutch Social -->
   <td class="nl la">15.67 ± 3.75 / 40.14 ± 2.65</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.93 ± 1.17 / 71.20 ± 1.30</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.49 ± 1.40 / 18.40 ± 1.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">36.13 ± 1.24 / 51.76 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">28.25 ± 2.23 / 44.23 ± 2.03</td> <!-- HellaSwag-nl -->
   <td>12.7.0</td> <!-- CoNLL-nl version -->
   <td>12.7.0</td> <!-- Dutch Social version -->
   <td>12.7.0</td> <!-- ScaLA-nl version -->
   <td>12.7.0</td> <!-- SQuAD-nl version -->
   <td>12.7.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.7.0</td> <!-- MMLU-nl version -->
   <td>12.7.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,378 ± 260 / 387 ± 119</td> <!-- Model inference speed -->
   <td class="rank">2.81</td> <!-- ScandEval rank -->
   <td class="nl ner">47.75 ± 2.33 / 35.64 ± 1.89</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.68 ± 0.61 / 26.25 ± 1.18</td> <!-- Dutch Social -->
   <td class="nl la">28.28 ± 2.48 / 62.81 ± 1.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.49 ± 1.15 / 73.19 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.60 ± 1.18 / 19.95 ± 1.23</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">42.19 ± 0.97 / 55.52 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">31.45 ± 2.79 / 44.15 ± 3.09</td> <!-- HellaSwag-nl -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.9.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.9.1</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/Mistral-7B-v0.1-chat-nl (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,907 ± 1,028 / 1,695 ± 549</td> <!-- Model inference speed -->
   <td class="rank">2.86</td> <!-- ScandEval rank -->
   <td class="nl ner">56.73 ± 1.95 / 38.97 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.08 ± 1.46 / 32.20 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">19.41 ± 2.55 / 57.17 ± 2.38</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.91 ± 0.92 / 71.22 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.05 ± 0.39 / 21.26 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">31.39 ± 0.86 / 48.09 ± 0.72</td> <!-- MMLU-nl -->
   <td class="nl reason">16.49 ± 2.14 / 36.67 ± 1.72</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="nl ner">55.56 ± 2.66 / 39.56 ± 2.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.37 ± 1.64 / 37.37 ± 1.35</td> <!-- Dutch Social -->
   <td class="nl la">21.50 ± 1.70 / 59.10 ± 1.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">50.77 ± 0.95 / 66.54 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.99 ± 0.49 / 19.54 ± 0.55</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.86 ± 1.89 / 41.71 ± 1.45</td> <!-- MMLU-nl -->
   <td class="nl reason">24.80 ± 1.77 / 42.93 ± 1.38</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.2</td> <!-- MMLU-nl version -->
   <td>9.3.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,657 ± 524 / 880 ± 278</td> <!-- Model inference speed -->
   <td class="rank">2.88</td> <!-- ScandEval rank -->
   <td class="nl ner">58.15 ± 1.14 / 40.78 ± 1.91</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.94 ± 1.25 / 31.02 ± 3.45</td> <!-- Dutch Social -->
   <td class="nl la">25.41 ± 3.46 / 61.11 ± 2.36</td> <!-- ScaLA-nl -->
   <td class="nl rc">62.56 ± 1.10 / 73.16 ± 0.93</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.24 ± 0.91 / 17.54 ± 1.10</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">35.49 ± 0.57 / 51.51 ± 0.42</td> <!-- MMLU-nl -->
   <td class="nl reason">19.88 ± 1.80 / 39.13 ± 1.56</td> <!-- HellaSwag-nl -->
   <td>9.1.2</td> <!-- CoNLL-nl version -->
   <td>9.1.2</td> <!-- Dutch Social version -->
   <td>9.1.2</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>alpindale/Mistral-7B-v0.2-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,841 ± 297 / 651 ± 193</td> <!-- Model inference speed -->
   <td class="rank">2.90</td> <!-- ScandEval rank -->
   <td class="nl ner">56.76 ± 1.52 / 42.03 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.11 ± 1.17 / 26.36 ± 2.97</td> <!-- Dutch Social -->
   <td class="nl la">23.55 ± 2.76 / 59.14 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.89 ± 1.10 / 72.41 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.33 ± 0.72 / 17.66 ± 0.87</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.92 ± 1.07 / 51.02 ± 0.85</td> <!-- MMLU-nl -->
   <td class="nl reason">23.87 ± 1.80 / 42.03 ± 1.58</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2534</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,187 ± 2,363 / 2,204 ± 737</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="nl ner">47.28 ± 1.57 / 36.12 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.12 ± 1.92 / 35.44 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">12.74 ± 2.68 / 52.69 ± 2.88</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.36 ± 1.36 / 71.20 ± 0.77</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.26 ± 0.75 / 16.55 ± 0.76</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.88 ± 0.86 / 44.76 ± 0.70</td> <!-- MMLU-nl -->
   <td class="nl reason">34.05 ± 1.57 / 50.08 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-v0.3 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7248</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">33</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,120 ± 976 / 926 ± 306</td> <!-- Model inference speed -->
   <td class="rank">2.91</td> <!-- ScandEval rank -->
   <td class="nl ner">56.52 ± 1.42 / 41.84 ± 1.84</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.02 ± 1.21 / 26.40 ± 2.96</td> <!-- Dutch Social -->
   <td class="nl la">23.41 ± 2.91 / 59.14 ± 3.11</td> <!-- ScaLA-nl -->
   <td class="nl rc">61.90 ± 1.07 / 72.49 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.37 ± 0.74 / 17.69 ± 0.90</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">34.93 ± 1.11 / 51.02 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">23.73 ± 1.97 / 41.93 ± 1.68</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2634</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,194 ± 2,403 / 2,193 ± 731</td> <!-- Model inference speed -->
   <td class="rank">2.93</td> <!-- ScandEval rank -->
   <td class="nl ner">52.52 ± 1.62 / 44.69 ± 2.23</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.85 ± 1.90 / 36.43 ± 2.11</td> <!-- Dutch Social -->
   <td class="nl la">17.72 ± 1.86 / 57.31 ± 1.52</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.50 ± 1.16 / 67.02 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.23 ± 0.48 / 18.18 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.62 ± 0.65 / 43.32 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">15.79 ± 1.37 / 35.56 ± 1.11</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/GEITje-7B-ultra (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,475 ± 460 / 765 ± 238</td> <!-- Model inference speed -->
   <td class="rank">2.96</td> <!-- ScandEval rank -->
   <td class="nl ner">42.20 ± 2.20 / 27.85 ± 1.11</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.78 ± 2.52 / 42.17 ± 1.91</td> <!-- Dutch Social -->
   <td class="nl la">18.23 ± 1.91 / 50.04 ± 2.54</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.41 ± 1.11 / 66.45 ± 0.46</td> <!-- SQuAD-nl -->
   <td class="nl summ">68.30 ± 0.40 / 20.79 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.92 ± 1.09 / 44.44 ± 0.85</td> <!-- MMLU-nl -->
   <td class="nl reason">25.72 ± 1.01 / 43.74 ± 0.69</td> <!-- HellaSwag-nl -->
   <td>10.0.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>10.0.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>10.0.1</td> <!-- MMLU-nl version -->
   <td>10.0.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-4k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,224 ± 1,371 / 1,063 ± 358</td> <!-- Model inference speed -->
   <td class="rank">3.00</td> <!-- ScandEval rank -->
   <td class="nl ner">50.31 ± 1.94 / 41.54 ± 2.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.58 ± 1.62 / 36.56 ± 1.79</td> <!-- Dutch Social -->
   <td class="nl la">14.72 ± 1.84 / 50.23 ± 3.10</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.19 ± 0.80 / 66.72 ± 0.92</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.40 ± 0.77 / 17.47 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.31 ± 0.70 / 46.18 ± 0.50</td> <!-- MMLU-nl -->
   <td class="nl reason">21.25 ± 1.25 / 40.78 ± 1.02</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.5</td> <!-- MMLU-nl version -->
   <td>12.10.5</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,424 ± 2,641 / 2,081 ± 666</td> <!-- Model inference speed -->
   <td class="rank">3.01</td> <!-- ScandEval rank -->
   <td class="nl ner">43.66 ± 2.01 / 40.23 ± 1.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.87 ± 1.32 / 37.23 ± 1.55</td> <!-- Dutch Social -->
   <td class="nl la">17.94 ± 3.48 / 55.88 ± 3.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">47.77 ± 1.82 / 64.44 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.74 ± 1.00 / 18.33 ± 1.28</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">33.80 ± 0.84 / 50.30 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">21.02 ± 1.29 / 40.27 ± 1.09</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,088 ± 352 / 706 ± 214</td> <!-- Model inference speed -->
   <td class="rank">3.03</td> <!-- ScandEval rank -->
   <td class="nl ner">53.78 ± 1.86 / 41.29 ± 2.07</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.78 ± 1.43 / 24.33 ± 1.57</td> <!-- Dutch Social -->
   <td class="nl la">16.23 ± 2.49 / 55.09 ± 3.18</td> <!-- ScaLA-nl -->
   <td class="nl rc">63.09 ± 1.18 / 73.88 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.46 ± 0.67 / 19.49 ± 0.92</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.37 ± 0.99 / 45.81 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">15.25 ± 1.71 / 35.83 ± 1.42</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.2.0</td> <!-- Dutch Social version -->
   <td>12.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.3.1</td> <!-- MMLU-nl version -->
   <td>12.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B-chat-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,908 ± 1,022 / 1,694 ± 551</td> <!-- Model inference speed -->
   <td class="rank">3.05</td> <!-- ScandEval rank -->
   <td class="nl ner">42.12 ± 4.00 / 31.12 ± 1.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.06 ± 2.30 / 40.32 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">19.71 ± 3.65 / 49.65 ± 4.28</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.19 ± 0.91 / 70.06 ± 0.82</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.55 ± 0.49 / 19.18 ± 0.67</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.71 ± 0.91 / 45.01 ± 0.71</td> <!-- MMLU-nl -->
   <td class="nl reason">18.03 ± 1.77 / 36.82 ± 1.76</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,374 ± 1,233 / 1,193 ± 377</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="nl ner">40.58 ± 2.08 / 28.95 ± 1.56</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.17 ± 1.32 / 32.96 ± 1.96</td> <!-- Dutch Social -->
   <td class="nl la">19.63 ± 2.61 / 52.65 ± 2.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.30 ± 1.25 / 67.27 ± 0.73</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.83 ± 0.86 / 19.21 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.30 ± 1.02 / 46.88 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">31.43 ± 1.42 / 47.87 ± 1.30</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-8b-code-base-4k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8055</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,313 ± 423 / 682 ± 210</td> <!-- Model inference speed -->
   <td class="rank">3.06</td> <!-- ScandEval rank -->
   <td class="nl ner">63.29 ± 2.51 / 52.18 ± 4.31</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.81 ± 1.66 / 36.99 ± 2.58</td> <!-- Dutch Social -->
   <td class="nl la">8.16 ± 1.97 / 44.29 ± 4.25</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.64 ± 0.68 / 66.29 ± 0.71</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.08 ± 0.90 / 15.69 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">16.86 ± 1.16 / 37.54 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">6.24 ± 0.78 / 29.25 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,849 ± 622 / 723 ± 229</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="nl ner">57.80 ± 1.53 / 39.43 ± 1.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 1.27 / 29.84 ± 2.35</td> <!-- Dutch Social -->
   <td class="nl la">17.40 ± 1.54 / 57.26 ± 1.96</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.35 ± 0.85 / 69.69 ± 0.76</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.11 ± 0.58 / 18.31 ± 0.61</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.15 ± 1.09 / 44.95 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">19.18 ± 1.46 / 38.84 ± 1.26</td> <!-- HellaSwag-nl -->
   <td>12.11.0</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.11.0</td> <!-- SQuAD-nl version -->
   <td>12.11.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>microsoft/Phi-3-mini-128k-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3821</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131072</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,312 ± 1,668 / 1,609 ± 525</td> <!-- Model inference speed -->
   <td class="rank">3.08</td> <!-- ScandEval rank -->
   <td class="nl ner">44.27 ± 2.14 / 34.47 ± 2.48</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.84 ± 1.82 / 36.64 ± 1.13</td> <!-- Dutch Social -->
   <td class="nl la">10.44 ± 1.58 / 48.93 ± 3.41</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.40 ± 1.14 / 68.02 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.60 ± 0.62 / 15.63 ± 0.45</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.63 ± 0.84 / 46.39 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">22.58 ± 0.97 / 41.78 ± 0.71</td> <!-- HellaSwag-nl -->
   <td>12.9.1</td> <!-- CoNLL-nl version -->
   <td>12.9.1</td> <!-- Dutch Social version -->
   <td>12.9.1</td> <!-- ScaLA-nl version -->
   <td>12.9.1</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-13b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,254 ± 1,068 / 484 ± 173</td> <!-- Model inference speed -->
   <td class="rank">3.09</td> <!-- ScandEval rank -->
   <td class="nl ner">57.66 ± 1.29 / 43.77 ± 2.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.41 ± 1.47 / 25.59 ± 1.30</td> <!-- Dutch Social -->
   <td class="nl la">16.93 ± 2.60 / 55.72 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.29 ± 1.11 / 68.94 ± 0.81</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.22 ± 0.50 / 19.03 ± 0.51</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.70 ± 1.05 / 44.15 ± 0.82</td> <!-- MMLU-nl -->
   <td class="nl reason">17.92 ± 1.69 / 37.64 ± 1.43</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2775</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,710 ± 1,040 / 1,188 ± 383</td> <!-- Model inference speed -->
   <td class="rank">3.10</td> <!-- ScandEval rank -->
   <td class="nl ner">36.50 ± 2.72 / 28.73 ± 1.41</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.70 ± 2.29 / 40.77 ± 1.77</td> <!-- Dutch Social -->
   <td class="nl la">4.81 ± 2.20 / 43.19 ± 1.45</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.63 ± 0.62 / 71.62 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.01 ± 0.42 / 17.97 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.76 ± 1.00 / 44.94 ± 0.74</td> <!-- MMLU-nl -->
   <td class="nl reason">12.93 ± 1.54 / 34.12 ± 1.22</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,887 ± 1,087 / 1,600 ± 522</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="nl ner">47.53 ± 1.90 / 32.42 ± 1.99</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.36 ± 2.96 / 28.11 ± 4.71</td> <!-- Dutch Social -->
   <td class="nl la">30.67 ± 4.45 / 63.78 ± 2.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.55 ± 0.70 / 67.56 ± 0.60</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.58 ± 0.85 / 22.14 ± 1.21</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.12 ± 0.98 / 44.50 ± 0.93</td> <!-- MMLU-nl -->
   <td class="nl reason">11.70 ± 2.42 / 32.05 ± 1.90</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-7b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">8538</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8317</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,792 ± 249 / 668 ± 203</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="nl ner">53.93 ± 2.71 / 47.48 ± 2.09</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.83 ± 2.37 / 34.00 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">6.58 ± 3.36 / 48.51 ± 3.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.45 ± 2.52 / 67.47 ± 0.88</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.89 ± 0.38 / 17.99 ± 0.46</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">19.58 ± 1.24 / 38.76 ± 1.06</td> <!-- MMLU-nl -->
   <td class="nl reason">13.68 ± 1.08 / 32.30 ± 0.99</td> <!-- HellaSwag-nl -->
   <td>12.10.0</td> <!-- CoNLL-nl version -->
   <td>12.10.0</td> <!-- Dutch Social version -->
   <td>12.10.0</td> <!-- ScaLA-nl version -->
   <td>12.10.0</td> <!-- SQuAD-nl version -->
   <td>12.10.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.0</td> <!-- MMLU-nl version -->
   <td>12.10.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-13b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">13016</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,898 ± 637 / 736 ± 236</td> <!-- Model inference speed -->
   <td class="rank">3.11</td> <!-- ScandEval rank -->
   <td class="nl ner">52.55 ± 1.64 / 43.32 ± 1.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.26 ± 2.09 / 28.32 ± 2.68</td> <!-- Dutch Social -->
   <td class="nl la">24.57 ± 3.54 / 54.94 ± 5.33</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.99 ± 0.95 / 72.74 ± 0.78</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.02 ± 0.84 / 16.97 ± 0.98</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.73 ± 0.90 / 45.62 ± 0.64</td> <!-- MMLU-nl -->
   <td class="nl reason">19.43 ± 1.53 / 38.57 ± 1.39</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2775</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,704 ± 1,015 / 1,185 ± 375</td> <!-- Model inference speed -->
   <td class="rank">3.13</td> <!-- ScandEval rank -->
   <td class="nl ner">39.57 ± 2.74 / 31.81 ± 1.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.25 ± 2.12 / 39.92 ± 1.66</td> <!-- Dutch Social -->
   <td class="nl la">9.31 ± 1.92 / 50.99 ± 2.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">60.26 ± 0.62 / 71.03 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">65.37 ± 0.53 / 17.63 ± 0.74</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.63 ± 1.33 / 44.86 ± 1.00</td> <!-- MMLU-nl -->
   <td class="nl reason">11.62 ± 1.28 / 32.71 ± 1.00</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-chat-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,643 ± 455 / 800 ± 247</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="nl ner">50.23 ± 2.34 / 37.12 ± 3.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">10.07 ± 1.84 / 35.66 ± 2.24</td> <!-- Dutch Social -->
   <td class="nl la">14.73 ± 1.62 / 54.59 ± 2.24</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.42 ± 0.80 / 66.24 ± 0.84</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.59 ± 0.56 / 18.45 ± 0.65</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.19 ± 1.26 / 39.24 ± 1.03</td> <!-- MMLU-nl -->
   <td class="nl reason">11.42 ± 1.29 / 32.50 ± 1.10</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>occiglot/occiglot-7b-eu5 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,219 ± 427 / 717 ± 224</td> <!-- Model inference speed -->
   <td class="rank">3.16</td> <!-- ScandEval rank -->
   <td class="nl ner">51.31 ± 2.32 / 42.95 ± 2.58</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.41 ± 1.24 / 26.93 ± 1.56</td> <!-- Dutch Social -->
   <td class="nl la">13.04 ± 1.93 / 53.54 ± 2.70</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.28 ± 1.15 / 69.67 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.66 ± 0.74 / 18.22 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">27.12 ± 0.86 / 44.36 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">13.99 ± 2.04 / 34.45 ± 1.89</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.2.0</td> <!-- MMLU-nl version -->
   <td>12.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,347 ± 893 / 1,135 ± 365</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="nl ner">42.52 ± 2.25 / 37.46 ± 3.08</td> <!-- CoNLL-nl -->
   <td class="nl sent">14.68 ± 1.40 / 40.53 ± 1.64</td> <!-- Dutch Social -->
   <td class="nl la">4.07 ± 2.16 / 35.24 ± 1.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.18 ± 0.74 / 66.50 ± 0.80</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.75 ± 0.84 / 14.83 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.25 ± 1.22 / 43.08 ± 0.87</td> <!-- MMLU-nl -->
   <td class="nl reason">16.21 ± 1.51 / 37.11 ± 1.16</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Rijgersberg/GEITje-7B-chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,920 ± 1,028 / 1,696 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="nl ner">50.69 ± 1.67 / 35.96 ± 2.63</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.16 ± 1.68 / 27.37 ± 1.95</td> <!-- Dutch Social -->
   <td class="nl la">20.45 ± 2.12 / 59.00 ± 1.21</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.48 ± 0.86 / 66.71 ± 0.59</td> <!-- SQuAD-nl -->
   <td class="nl summ">66.92 ± 0.50 / 20.19 ± 0.69</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.89 ± 1.55 / 42.34 ± 1.14</td> <!-- MMLU-nl -->
   <td class="nl reason">9.84 ± 1.87 / 30.90 ± 1.58</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,246 ± 3,021 / 1,629 ± 550</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="nl ner">49.25 ± 2.57 / 36.48 ± 2.14</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.45 ± 1.76 / 39.66 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">11.87 ± 2.68 / 47.32 ± 3.85</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.20 ± 1.44 / 67.04 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.96 / 16.74 ± 0.86</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">21.52 ± 1.18 / 40.76 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">22.32 ± 2.02 / 39.89 ± 1.82</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>mistralai/Mistral-7B-Instruct-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">634 ± 179 / 110 ± 35</td> <!-- Model inference speed -->
   <td class="rank">3.17</td> <!-- ScandEval rank -->
   <td class="nl ner">52.72 ± 2.58 / 33.51 ± 1.22</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.91 ± 2.16 / 27.82 ± 1.97</td> <!-- Dutch Social -->
   <td class="nl la">18.14 ± 2.10 / 55.42 ± 3.05</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.75 ± 0.88 / 67.15 ± 1.08</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.77 ± 0.97 / 16.55 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">26.06 ± 0.77 / 44.08 ± 0.51</td> <!-- MMLU-nl -->
   <td class="nl reason">14.26 ± 1.48 / 35.14 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/GEITje-7B-ultra-sft (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,979 ± 1,044 / 1,724 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.26</td> <!-- ScandEval rank -->
   <td class="nl ner">39.41 ± 2.93 / 30.59 ± 1.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.00 ± 3.04 / 35.01 ± 3.72</td> <!-- Dutch Social -->
   <td class="nl la">16.10 ± 2.34 / 52.05 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">53.02 ± 0.97 / 65.63 ± 0.72</td> <!-- SQuAD-nl -->
   <td class="nl summ">67.74 ± 0.43 / 20.32 ± 0.57</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.80 ± 0.75 / 42.85 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">12.49 ± 2.15 / 33.04 ± 2.08</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-1.5-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,867 ± 550 / 793 ± 253</td> <!-- Model inference speed -->
   <td class="rank">3.29</td> <!-- ScandEval rank -->
   <td class="nl ner">51.18 ± 1.62 / 35.45 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.23 ± 2.84 / 19.38 ± 4.37</td> <!-- Dutch Social -->
   <td class="nl la">1.99 ± 2.56 / 34.69 ± 1.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.66 ± 1.25 / 65.31 ± 1.06</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.81 ± 1.16 / 15.41 ± 0.63</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">28.03 ± 1.02 / 45.90 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">23.64 ± 1.21 / 42.59 ± 0.96</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3.0-3b-a800m-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3374</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,504 ± 3,028 / 1,678 ± 559</td> <!-- Model inference speed -->
   <td class="rank">3.32</td> <!-- ScandEval rank -->
   <td class="nl ner">42.52 ± 3.31 / 33.08 ± 2.70</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.91 ± 1.71 / 35.24 ± 2.62</td> <!-- Dutch Social -->
   <td class="nl la">0.69 ± 2.82 / 36.10 ± 2.58</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.95 ± 1.18 / 66.87 ± 1.37</td> <!-- SQuAD-nl -->
   <td class="nl summ">63.71 ± 0.60 / 17.04 ± 0.70</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.93 ± 1.42 / 40.35 ± 1.23</td> <!-- MMLU-nl -->
   <td class="nl reason">24.42 ± 1.73 / 42.26 ± 1.49</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>BramVanroy/fietje-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2780</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">51</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,804 ± 1,045 / 1,220 ± 392</td> <!-- Model inference speed -->
   <td class="rank">3.34</td> <!-- ScandEval rank -->
   <td class="nl ner">33.92 ± 3.43 / 28.63 ± 2.42</td> <!-- CoNLL-nl -->
   <td class="nl sent">13.39 ± 1.64 / 41.03 ± 1.87</td> <!-- Dutch Social -->
   <td class="nl la">6.75 ± 2.55 / 41.28 ± 2.37</td> <!-- ScaLA-nl -->
   <td class="nl rc">58.57 ± 1.03 / 69.39 ± 0.79</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.49 ± 0.90 / 16.13 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">24.66 ± 0.67 / 42.68 ± 0.55</td> <!-- MMLU-nl -->
   <td class="nl reason">4.78 ± 1.80 / 27.19 ± 1.20</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>01-ai/Yi-6B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6061</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,435 ± 1,316 / 1,632 ± 549</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="nl ner">46.34 ± 2.00 / 33.30 ± 1.78</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.96 ± 1.44 / 18.10 ± 2.39</td> <!-- Dutch Social -->
   <td class="nl la">0.88 ± 1.23 / 33.53 ± 0.48</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.33 ± 1.28 / 66.50 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.35 ± 1.57 / 14.29 ± 0.85</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.33 ± 0.91 / 46.94 ± 0.68</td> <!-- MMLU-nl -->
   <td class="nl reason">20.27 ± 1.38 / 39.32 ± 1.12</td> <!-- HellaSwag-nl -->
   <td>9.3.2</td> <!-- CoNLL-nl version -->
   <td>10.0.0</td> <!-- Dutch Social version -->
   <td>10.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>12.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>10.0.1</td> <!-- MMLU-nl version -->
   <td>10.0.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-3B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3213</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,713 ± 877 / 836 ± 267</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="nl ner">47.40 ± 3.29 / 33.11 ± 2.04</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.90 ± 1.98 / 30.71 ± 1.89</td> <!-- Dutch Social -->
   <td class="nl la">3.10 ± 1.93 / 34.24 ± 0.73</td> <!-- ScaLA-nl -->
   <td class="nl rc">56.53 ± 1.48 / 68.47 ± 1.35</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.27 ± 2.04 / 16.54 ± 1.58</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">29.18 ± 0.87 / 46.04 ± 0.54</td> <!-- MMLU-nl -->
   <td class="nl reason">10.34 ± 1.08 / 32.08 ± 1.06</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>timpal0l/Mistral-7B-v0.1-flashback-v2 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,054 ± 1,200 / 1,056 ± 339</td> <!-- Model inference speed -->
   <td class="rank">3.36</td> <!-- ScandEval rank -->
   <td class="nl ner">54.56 ± 2.96 / 37.86 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.43 ± 1.27 / 24.23 ± 0.94</td> <!-- Dutch Social -->
   <td class="nl la">10.99 ± 2.55 / 50.46 ± 4.17</td> <!-- ScaLA-nl -->
   <td class="nl rc">55.91 ± 1.08 / 66.78 ± 1.13</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.88 ± 1.41 / 12.36 ± 1.30</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">25.12 ± 1.17 / 43.50 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">10.65 ± 1.55 / 31.51 ± 1.52</td> <!-- HellaSwag-nl -->
   <td>12.5.3</td> <!-- CoNLL-nl version -->
   <td>12.5.3</td> <!-- Dutch Social version -->
   <td>12.5.3</td> <!-- ScaLA-nl version -->
   <td>12.5.3</td> <!-- SQuAD-nl version -->
   <td>12.5.3</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.3</td> <!-- MMLU-nl version -->
   <td>12.5.3</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-2-7b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">930 ± 310 / 128 ± 43</td> <!-- Model inference speed -->
   <td class="rank">3.41</td> <!-- ScandEval rank -->
   <td class="nl ner">40.49 ± 4.32 / 30.86 ± 2.27</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.10 ± 1.85 / 27.42 ± 1.76</td> <!-- Dutch Social -->
   <td class="nl la">18.66 ± 2.39 / 55.25 ± 3.77</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.92 ± 0.61 / 70.24 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.58 ± 1.13 / 16.33 ± 0.81</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.36 ± 1.12 / 37.44 ± 0.99</td> <!-- MMLU-nl -->
   <td class="nl reason">6.68 ± 1.82 / 29.30 ± 1.02</td> <!-- HellaSwag-nl -->
   <td>9.2.0</td> <!-- CoNLL-nl version -->
   <td>9.2.0</td> <!-- Dutch Social version -->
   <td>9.2.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>11.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>9.2.0</td> <!-- MMLU-nl version -->
   <td>9.2.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-4B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3950</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,248 ± 739 / 761 ± 252</td> <!-- Model inference speed -->
   <td class="rank">3.45</td> <!-- ScandEval rank -->
   <td class="nl ner">35.74 ± 3.22 / 31.74 ± 2.24</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.55 ± 1.39 / 39.80 ± 1.38</td> <!-- Dutch Social -->
   <td class="nl la">0.23 ± 0.44 / 33.35 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">51.30 ± 1.63 / 64.17 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.90 ± 1.59 / 14.17 ± 0.80</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.20 ± 1.53 / 41.49 ± 1.08</td> <!-- MMLU-nl -->
   <td class="nl reason">13.11 ± 1.85 / 33.86 ± 1.69</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>TrustLLMeu/baseline-7-8b_1t-tokens_llama (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7800</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,197 ± 1,118 / 1,730 ± 577</td> <!-- Model inference speed -->
   <td class="rank">3.48</td> <!-- ScandEval rank -->
   <td class="nl ner">48.24 ± 2.28 / 40.24 ± 1.90</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.37 ± 1.34 / 33.54 ± 1.83</td> <!-- Dutch Social -->
   <td class="nl la">10.73 ± 1.76 / 48.26 ± 4.65</td> <!-- ScaLA-nl -->
   <td class="nl rc">54.83 ± 1.16 / 65.28 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">64.32 ± 0.90 / 18.12 ± 1.06</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.72 ± 1.25 / 24.90 ± 0.92</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.47 ± 0.87 / 24.28 ± 0.68</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,875 ± 673 / 261 ± 91</td> <!-- Model inference speed -->
   <td class="rank">3.51</td> <!-- ScandEval rank -->
   <td class="nl ner">35.30 ± 3.76 / 33.68 ± 1.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">15.67 ± 2.21 / 31.30 ± 4.51</td> <!-- Dutch Social -->
   <td class="nl la">1.76 ± 2.37 / 47.60 ± 1.68</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.05 ± 1.68 / 55.38 ± 1.66</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.15 ± 1.54 / 14.60 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">6.24 ± 1.54 / 29.02 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl reason">0.47 ± 1.20 / 24.89 ± 0.59</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1.7-7B-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,371 ± 876 / 561 ± 184</td> <!-- Model inference speed -->
   <td class="rank">3.57</td> <!-- ScandEval rank -->
   <td class="nl ner">46.95 ± 2.32 / 36.13 ± 1.88</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.34 ± 2.10 / 19.37 ± 2.08</td> <!-- Dutch Social -->
   <td class="nl la">3.46 ± 1.91 / 41.32 ± 3.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">57.07 ± 0.89 / 68.14 ± 0.65</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.31 ± 0.64 / 17.24 ± 0.72</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">18.21 ± 0.70 / 37.51 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">9.03 ± 1.04 / 29.35 ± 0.77</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-3b-code-base-2k (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">3483</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">49</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,732 ± 868 / 662 ± 238</td> <!-- Model inference speed -->
   <td class="rank">3.60</td> <!-- ScandEval rank -->
   <td class="nl ner">50.88 ± 3.41 / 39.51 ± 3.29</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.39 ± 1.50 / 30.05 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">3.31 ± 1.19 / 37.97 ± 4.40</td> <!-- ScaLA-nl -->
   <td class="nl rc">48.44 ± 1.06 / 58.85 ± 0.75</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.50 ± 2.95 / 10.11 ± 2.12</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">9.22 ± 0.79 / 31.06 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">4.45 ± 1.38 / 28.26 ± 1.08</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2614</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8320</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,235 ± 1,226 / 1,154 ± 366</td> <!-- Model inference speed -->
   <td class="rank">3.64</td> <!-- ScandEval rank -->
   <td class="nl ner">22.63 ± 4.98 / 22.71 ± 2.86</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.11 ± 1.55 / 28.07 ± 1.80</td> <!-- Dutch Social -->
   <td class="nl la">8.04 ± 1.79 / 48.95 ± 2.97</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.39 ± 2.14 / 65.22 ± 1.11</td> <!-- SQuAD-nl -->
   <td class="nl summ">61.90 ± 1.04 / 17.09 ± 0.93</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">22.76 ± 0.76 / 41.67 ± 0.80</td> <!-- MMLU-nl -->
   <td class="nl reason">8.50 ± 1.32 / 30.16 ± 1.11</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>MaLA-LM/emma-500-llama2-7b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,275 ± 1,193 / 1,755 ± 578</td> <!-- Model inference speed -->
   <td class="rank">3.68</td> <!-- ScandEval rank -->
   <td class="nl ner">36.61 ± 3.37 / 31.91 ± 2.20</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.77 ± 1.80 / 25.31 ± 1.42</td> <!-- Dutch Social -->
   <td class="nl la">3.52 ± 2.07 / 35.34 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">59.51 ± 0.97 / 70.33 ± 0.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.50 ± 5.78 / 15.01 ± 1.59</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.90 ± 1.44 / 35.20 ± 1.09</td> <!-- MMLU-nl -->
   <td class="nl reason">7.26 ± 1.56 / 29.91 ± 1.18</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B-Instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,436 ± 1,846 / 1,508 ± 479</td> <!-- Model inference speed -->
   <td class="rank">3.72</td> <!-- ScandEval rank -->
   <td class="nl ner">42.01 ± 2.06 / 37.16 ± 1.98</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.15 ± 1.70 / 32.55 ± 2.69</td> <!-- Dutch Social -->
   <td class="nl la">1.11 ± 2.15 / 36.71 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">40.04 ± 1.61 / 53.75 ± 1.10</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.72 ± 1.05 / 12.47 ± 0.62</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">17.71 ± 0.69 / 38.01 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.98 ± 1.11 / 28.05 ± 1.00</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ibm-granite/granite-7b-base (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6738</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,405 ± 1,098 / 1,032 ± 345</td> <!-- Model inference speed -->
   <td class="rank">3.73</td> <!-- ScandEval rank -->
   <td class="nl ner">37.39 ± 3.37 / 32.77 ± 1.97</td> <!-- CoNLL-nl -->
   <td class="nl sent">7.51 ± 1.57 / 19.22 ± 1.72</td> <!-- Dutch Social -->
   <td class="nl la">3.11 ± 0.88 / 50.54 ± 0.90</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.60 ± 1.28 / 61.06 ± 0.94</td> <!-- SQuAD-nl -->
   <td class="nl summ">57.63 ± 1.86 / 12.27 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">14.52 ± 1.25 / 35.34 ± 0.95</td> <!-- MMLU-nl -->
   <td class="nl reason">6.60 ± 1.13 / 29.30 ± 0.97</td> <!-- HellaSwag-nl -->
   <td>12.10.5</td> <!-- CoNLL-nl version -->
   <td>12.10.5</td> <!-- Dutch Social version -->
   <td>12.10.5</td> <!-- ScaLA-nl version -->
   <td>12.10.5</td> <!-- SQuAD-nl version -->
   <td>12.10.5</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>AI-Sweden-Models/gpt-sw3-20b-instruct (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">20918</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">64</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2048</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">1,831 ± 587 / 268 ± 90</td> <!-- Model inference speed -->
   <td class="rank">3.75</td> <!-- ScandEval rank -->
   <td class="nl ner">24.44 ± 1.62 / 25.02 ± 1.72</td> <!-- CoNLL-nl -->
   <td class="nl sent">18.40 ± 2.14 / 40.21 ± 2.51</td> <!-- Dutch Social -->
   <td class="nl la">4.85 ± 2.01 / 49.10 ± 2.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">39.83 ± 1.08 / 52.69 ± 1.15</td> <!-- SQuAD-nl -->
   <td class="nl summ">54.89 ± 1.27 / 13.01 ± 0.47</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">4.38 ± 1.45 / 27.07 ± 1.30</td> <!-- MMLU-nl -->
   <td class="nl reason">1.95 ± 0.83 / 24.88 ± 0.71</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>9.3.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RuterNorway/Llama-2-7b-chat-norwegian (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">10,890 ± 2,686 / 2,186 ± 750</td> <!-- Model inference speed -->
   <td class="rank">3.81</td> <!-- ScandEval rank -->
   <td class="nl ner">35.49 ± 3.10 / 29.35 ± 2.75</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.36 ± 1.56 / 30.66 ± 3.68</td> <!-- Dutch Social -->
   <td class="nl la">2.52 ± 2.14 / 42.60 ± 4.80</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.49 ± 1.37 / 47.34 ± 1.53</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.24 ± 0.86 / 15.62 ± 0.60</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.41 ± 1.15 / 27.75 ± 0.75</td> <!-- MMLU-nl -->
   <td class="nl reason">0.15 ± 0.98 / 25.59 ± 0.57</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b-it (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,471 ± 1,142 / 1,961 ± 584</td> <!-- Model inference speed -->
   <td class="rank">3.90</td> <!-- ScandEval rank -->
   <td class="nl ner">38.85 ± 3.77 / 32.18 ± 2.49</td> <!-- CoNLL-nl -->
   <td class="nl sent">11.25 ± 1.90 / 28.36 ± 1.81</td> <!-- Dutch Social -->
   <td class="nl la">-2.27 ± 1.37 / 37.91 ± 2.26</td> <!-- ScaLA-nl -->
   <td class="nl rc">45.95 ± 1.11 / 56.54 ± 0.95</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.99 ± 8.25 / 12.75 ± 2.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.97 ± 0.92 / 32.28 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">1.45 ± 1.15 / 24.79 ± 0.52</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.4.0</td> <!-- SQuAD-nl version -->
   <td>12.4.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>google/gemma-2b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2506</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">256</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">8192</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">6,087 ± 1,046 / 1,902 ± 563</td> <!-- Model inference speed -->
   <td class="rank">3.93</td> <!-- ScandEval rank -->
   <td class="nl ner">16.90 ± 4.91 / 17.38 ± 4.30</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.95 ± 0.78 / 27.94 ± 1.43</td> <!-- Dutch Social -->
   <td class="nl la">0.41 ± 1.03 / 33.54 ± 0.32</td> <!-- ScaLA-nl -->
   <td class="nl rc">49.15 ± 1.55 / 59.16 ± 1.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.61 ± 2.22 / 13.67 ± 1.15</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.94 ± 0.50 / 31.87 ± 0.76</td> <!-- MMLU-nl -->
   <td class="nl reason">3.29 ± 0.95 / 26.85 ± 0.49</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>stabilityai/stablelm-2-1_6b (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1645</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,259 ± 2,120 / 1,240 ± 432</td> <!-- Model inference speed -->
   <td class="rank">3.96</td> <!-- ScandEval rank -->
   <td class="nl ner">36.58 ± 3.88 / 33.82 ± 2.87</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.32 ± 1.30 / 24.04 ± 1.14</td> <!-- Dutch Social -->
   <td class="nl la">4.01 ± 2.01 / 36.03 ± 1.61</td> <!-- ScaLA-nl -->
   <td class="nl rc">52.81 ± 0.81 / 63.87 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">52.24 ± 1.79 / 10.76 ± 0.68</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">10.24 ± 1.06 / 31.02 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">6.75 ± 0.83 / 28.50 ± 0.84</td> <!-- HellaSwag-nl -->
   <td>12.10.8</td> <!-- CoNLL-nl version -->
   <td>12.10.8</td> <!-- Dutch Social version -->
   <td>12.10.8</td> <!-- ScaLA-nl version -->
   <td>12.10.8</td> <!-- SQuAD-nl version -->
   <td>12.10.8</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.8</td> <!-- MMLU-nl version -->
   <td>12.10.8</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,304 ± 1,846 / 1,933 ± 617</td> <!-- Model inference speed -->
   <td class="rank">3.98</td> <!-- ScandEval rank -->
   <td class="nl ner">23.44 ± 5.09 / 25.00 ± 2.33</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.82 ± 1.82 / 30.97 ± 2.65</td> <!-- Dutch Social -->
   <td class="nl la">4.11 ± 1.73 / 43.70 ± 3.47</td> <!-- ScaLA-nl -->
   <td class="nl rc">33.16 ± 1.61 / 46.66 ± 1.27</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.91 ± 0.99 / 12.65 ± 0.41</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">12.11 ± 0.90 / 33.62 ± 0.61</td> <!-- MMLU-nl -->
   <td class="nl reason">6.41 ± 1.13 / 29.73 ± 0.82</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Tweeties/tweety-7b-dutch-v24a (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7391</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,971 ± 423 / 1,351 ± 410</td> <!-- Model inference speed -->
   <td class="rank">4.04</td> <!-- ScandEval rank -->
   <td class="nl ner">35.83 ± 3.06 / 29.15 ± 2.80</td> <!-- CoNLL-nl -->
   <td class="nl sent">12.47 ± 2.51 / 40.41 ± 2.26</td> <!-- Dutch Social -->
   <td class="nl la">16.81 ± 3.31 / 53.38 ± 5.08</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 14.18 ± 0.38</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.61 ± 0.65 / 9.48 ± 0.19</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">20.21 ± 1.63 / 37.93 ± 1.39</td> <!-- MMLU-nl -->
   <td class="nl reason">5.94 ± 1.54 / 28.98 ± 0.98</td> <!-- HellaSwag-nl -->
   <td>12.6.1</td> <!-- CoNLL-nl version -->
   <td>12.6.1</td> <!-- Dutch Social version -->
   <td>12.6.1</td> <!-- ScaLA-nl version -->
   <td>12.6.1</td> <!-- SQuAD-nl version -->
   <td>12.6.1</td> <!-- Wiki-Lingua-NL version -->
   <td>12.6.1</td> <!-- MMLU-nl version -->
   <td>12.6.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,035 ± 503 / 911 ± 300</td> <!-- Model inference speed -->
   <td class="rank">4.08</td> <!-- ScandEval rank -->
   <td class="nl ner">24.15 ± 5.73 / 26.49 ± 4.13</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.31 ± 1.56 / 20.06 ± 1.06</td> <!-- Dutch Social -->
   <td class="nl la">1.60 ± 1.71 / 41.51 ± 3.60</td> <!-- ScaLA-nl -->
   <td class="nl rc">37.08 ± 1.76 / 49.32 ± 0.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">59.43 ± 1.17 / 14.57 ± 0.83</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.04 ± 1.28 / 26.56 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">3.70 ± 1.54 / 26.98 ± 1.26</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>LumiOpen/Viking-13B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">14030</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">131</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4224</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">840 ± 79 / 400 ± 124</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="nl ner">36.74 ± 3.36 / 32.36 ± 1.39</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.57 ± 2.44 / 34.17 ± 2.59</td> <!-- Dutch Social -->
   <td class="nl la">3.01 ± 1.94 / 46.03 ± 4.19</td> <!-- ScaLA-nl -->
   <td class="nl rc">32.32 ± 1.55 / 40.73 ± 1.64</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.76 ± 1.36 / 10.67 ± 0.56</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.67 ± 1.15 / 24.89 ± 0.79</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.30 ± 1.01 / 23.52 ± 0.38</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B-Chat (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">False</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,740 ± 3,000 / 2,209 ± 721</td> <!-- Model inference speed -->
   <td class="rank">4.16</td> <!-- ScandEval rank -->
   <td class="nl ner">18.66 ± 4.43 / 17.56 ± 4.28</td> <!-- CoNLL-nl -->
   <td class="nl sent">8.59 ± 3.20 / 29.65 ± 5.10</td> <!-- Dutch Social -->
   <td class="nl la">0.34 ± 2.02 / 43.92 ± 3.15</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.74 ± 1.57 / 35.03 ± 2.14</td> <!-- SQuAD-nl -->
   <td class="nl summ">62.36 ± 0.81 / 11.72 ± 0.73</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">2.09 ± 1.13 / 25.90 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">1.44 ± 1.12 / 26.50 ± 0.68</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>11.0.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.5.0</td> <!-- SQuAD-nl version -->
   <td>12.5.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-1.8B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1837</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,666 ± 1,328 / 1,256 ± 408</td> <!-- Model inference speed -->
   <td class="rank">4.22</td> <!-- ScandEval rank -->
   <td class="nl ner">11.66 ± 6.46 / 15.15 ± 4.38</td> <!-- CoNLL-nl -->
   <td class="nl sent">5.20 ± 1.78 / 35.43 ± 2.14</td> <!-- Dutch Social -->
   <td class="nl la">2.89 ± 1.91 / 41.36 ± 4.63</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.60 ± 2.17 / 48.83 ± 1.05</td> <!-- SQuAD-nl -->
   <td class="nl summ">55.00 ± 1.73 / 11.21 ± 0.64</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">13.56 ± 0.64 / 34.17 ± 0.48</td> <!-- MMLU-nl -->
   <td class="nl reason">5.89 ± 0.82 / 29.17 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,403 ± 1,133 / 1,294 ± 423</td> <!-- Model inference speed -->
   <td class="rank">4.28</td> <!-- ScandEval rank -->
   <td class="nl ner">37.37 ± 2.22 / 30.45 ± 2.45</td> <!-- CoNLL-nl -->
   <td class="nl sent">9.55 ± 1.82 / 23.90 ± 1.53</td> <!-- Dutch Social -->
   <td class="nl la">0.05 ± 1.35 / 35.78 ± 2.30</td> <!-- ScaLA-nl -->
   <td class="nl rc">34.81 ± 1.54 / 46.37 ± 1.51</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.22 ± 0.39 / 8.61 ± 0.17</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">3.92 ± 1.04 / 27.22 ± 0.63</td> <!-- MMLU-nl -->
   <td class="nl reason">0.16 ± 0.55 / 25.29 ± 0.61</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>meta-llama/Llama-3.2-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1236</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">128</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">131200</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">7,577 ± 1,884 / 1,555 ± 492</td> <!-- Model inference speed -->
   <td class="rank">4.30</td> <!-- ScandEval rank -->
   <td class="nl ner">22.03 ± 4.43 / 19.22 ± 3.92</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.25 ± 2.95 / 26.57 ± 3.31</td> <!-- Dutch Social -->
   <td class="nl la">1.46 ± 1.83 / 42.29 ± 4.01</td> <!-- ScaLA-nl -->
   <td class="nl rc">41.76 ± 1.92 / 52.60 ± 1.99</td> <!-- SQuAD-nl -->
   <td class="nl summ">51.56 ± 1.45 / 10.34 ± 0.52</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">5.46 ± 1.05 / 28.09 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.58 ± 0.81 / 23.58 ± 0.50</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>Qwen/Qwen1.5-0.5B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">620</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">152</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32768</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,371 ± 2,924 / 2,122 ± 692</td> <!-- Model inference speed -->
   <td class="rank">4.31</td> <!-- ScandEval rank -->
   <td class="nl ner">28.30 ± 3.90 / 28.67 ± 3.15</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.54 ± 2.76 / 26.53 ± 3.74</td> <!-- Dutch Social -->
   <td class="nl la">-0.42 ± 2.41 / 37.60 ± 3.89</td> <!-- ScaLA-nl -->
   <td class="nl rc">20.81 ± 2.21 / 29.05 ± 2.31</td> <!-- SQuAD-nl -->
   <td class="nl summ">58.40 ± 2.03 / 10.34 ± 0.54</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">7.44 ± 0.51 / 29.86 ± 0.35</td> <!-- MMLU-nl -->
   <td class="nl reason">1.70 ± 1.42 / 26.04 ± 0.91</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Llama2-7B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7033</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">4,438 ± 1,128 / 1,028 ± 346</td> <!-- Model inference speed -->
   <td class="rank">4.36</td> <!-- ScandEval rank -->
   <td class="nl ner">22.50 ± 2.27 / 24.09 ± 2.40</td> <!-- CoNLL-nl -->
   <td class="nl sent">6.04 ± 1.51 / 18.08 ± 2.09</td> <!-- Dutch Social -->
   <td class="nl la">-0.61 ± 1.30 / 46.51 ± 2.55</td> <!-- ScaLA-nl -->
   <td class="nl rc">26.96 ± 1.55 / 35.73 ± 1.87</td> <!-- SQuAD-nl -->
   <td class="nl summ">56.55 ± 3.05 / 13.22 ± 1.01</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.27 ± 1.29 / 24.94 ± 0.91</td> <!-- MMLU-nl -->
   <td class="nl reason">1.47 ± 0.79 / 25.75 ± 0.39</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>state-spaces/mamba-2.8b-hf (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">2768</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">32896</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">2,722 ± 495 / 766 ± 250</td> <!-- Model inference speed -->
   <td class="rank">4.59</td> <!-- ScandEval rank -->
   <td class="nl ner">22.95 ± 1.99 / 23.05 ± 1.55</td> <!-- CoNLL-nl -->
   <td class="nl sent">2.40 ± 1.70 / 22.89 ± 4.81</td> <!-- Dutch Social -->
   <td class="nl la">3.12 ± 1.51 / 45.58 ± 4.56</td> <!-- ScaLA-nl -->
   <td class="nl rc">22.40 ± 1.73 / 32.09 ± 1.56</td> <!-- SQuAD-nl -->
   <td class="nl summ">50.36 ± 2.03 / 9.96 ± 0.95</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.48 ± 0.81 / 24.57 ± 0.67</td> <!-- MMLU-nl -->
   <td class="nl reason">1.28 ± 1.03 / 26.62 ± 0.80</td> <!-- HellaSwag-nl -->
   <td>13.0.0</td> <!-- CoNLL-nl version -->
   <td>13.0.0</td> <!-- Dutch Social version -->
   <td>13.0.0</td> <!-- ScaLA-nl version -->
   <td>13.0.0</td> <!-- SQuAD-nl version -->
   <td>13.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>13.0.0</td> <!-- MMLU-nl version -->
   <td>13.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-7B-Twin-2T (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">6888</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,484 ± 1,125 / 1,317 ± 425</td> <!-- Model inference speed -->
   <td class="rank">4.65</td> <!-- ScandEval rank -->
   <td class="nl ner">18.70 ± 5.76 / 19.58 ± 4.59</td> <!-- CoNLL-nl -->
   <td class="nl sent">3.70 ± 1.69 / 17.91 ± 1.48</td> <!-- Dutch Social -->
   <td class="nl la">2.19 ± 2.08 / 45.43 ± 3.44</td> <!-- ScaLA-nl -->
   <td class="nl rc">38.08 ± 1.07 / 48.44 ± 1.55</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.79 ± 0.51 / 7.59 ± 0.20</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.65 ± 1.39 / 25.05 ± 1.02</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.02 ± 0.92 / 24.75 ± 0.66</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.5.2</td> <!-- Dutch Social version -->
   <td>12.5.2</td> <!-- ScaLA-nl version -->
   <td>12.5.2</td> <!-- SQuAD-nl version -->
   <td>12.5.2</td> <!-- Wiki-Lingua-NL version -->
   <td>12.5.2</td> <!-- MMLU-nl version -->
   <td>12.5.2</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>allenai/OLMo-1B (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">1177</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">50</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">2176</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">8,536 ± 1,926 / 1,940 ± 619</td> <!-- Model inference speed -->
   <td class="rank">4.84</td> <!-- ScandEval rank -->
   <td class="nl ner">22.58 ± 5.05 / 26.82 ± 3.69</td> <!-- CoNLL-nl -->
   <td class="nl sent">4.92 ± 2.71 / 19.51 ± 4.22</td> <!-- Dutch Social -->
   <td class="nl la">-1.27 ± 1.85 / 41.38 ± 3.59</td> <!-- ScaLA-nl -->
   <td class="nl rc">6.64 ± 1.96 / 11.74 ± 1.62</td> <!-- SQuAD-nl -->
   <td class="nl summ">43.43 ± 0.37 / 7.83 ± 0.14</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.56 ± 1.27 / 24.38 ± 0.98</td> <!-- MMLU-nl -->
   <td class="nl reason">0.29 ± 1.06 / 25.10 ± 0.83</td> <!-- HellaSwag-nl -->
   <td>12.5.2</td> <!-- CoNLL-nl version -->
   <td>12.1.0</td> <!-- Dutch Social version -->
   <td>12.1.0</td> <!-- ScaLA-nl version -->
   <td>12.1.0</td> <!-- SQuAD-nl version -->
   <td>12.1.0</td> <!-- Wiki-Lingua-NL version -->
   <td>12.1.0</td> <!-- MMLU-nl version -->
   <td>12.1.0</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>RJuro/kanelsnegl-v0.1 (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7242</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">32</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">512</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">5,847 ± 1,029 / 1,640 ± 525</td> <!-- Model inference speed -->
   <td class="rank">5.00</td> <!-- ScandEval rank -->
   <td class="nl ner">0.00 ± 0.00 / 0.00 ± 0.00</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.95 ± 1.17 / 9.87 ± 0.86</td> <!-- Dutch Social -->
   <td class="nl la">0.00 ± 0.00 / 33.34 ± 0.31</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.00 ± 0.00 / 5.43 ± 0.58</td> <!-- SQuAD-nl -->
   <td class="nl summ">60.14 ± 0.15 / 10.07 ± 0.16</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">0.11 ± 0.64 / 24.32 ± 0.78</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.13 ± 0.82 / 23.60 ± 0.33</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>9.3.1</td> <!-- Dutch Social version -->
   <td>9.3.1</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>9.3.1</td> <!-- Wiki-Lingua-NL version -->
   <td>9.3.1</td> <!-- MMLU-nl version -->
   <td>9.3.1</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>NorwAI/NorwAI-Mistral-7B-pretrain (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">7537</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">68</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">4096</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">3,024 ± 496 / 909 ± 301</td> <!-- Model inference speed -->
   <td class="rank">5.27</td> <!-- ScandEval rank -->
   <td class="nl ner">3.80 ± 1.23 / 4.24 ± 1.19</td> <!-- CoNLL-nl -->
   <td class="nl sent">0.97 ± 1.50 / 13.00 ± 2.52</td> <!-- Dutch Social -->
   <td class="nl la">-0.37 ± 0.55 / 33.40 ± 0.35</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.40 ± 0.25 / 2.98 ± 0.44</td> <!-- SQuAD-nl -->
   <td class="nl summ">45.25 ± 4.22 / 6.15 ± 1.03</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">-0.98 ± 0.91 / 24.82 ± 0.88</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.05 ± 1.07 / 24.51 ± 0.88</td> <!-- HellaSwag-nl -->
   <td>12.10.4</td> <!-- CoNLL-nl version -->
   <td>12.10.4</td> <!-- Dutch Social version -->
   <td>12.10.4</td> <!-- ScaLA-nl version -->
   <td>12.10.4</td> <!-- SQuAD-nl version -->
   <td>12.10.4</td> <!-- Wiki-Lingua-NL version -->
   <td>12.10.4</td> <!-- MMLU-nl version -->
   <td>12.10.4</td> <!-- HellaSwag-nl version -->
   </tr>
  <tr class="not-merged-model">
   <td>ai-forever/mGPT (few-shot)</td> <!-- Model ID -->
   <td class="num_model_parameters">unknown</td> <!-- Number of trainable parameters -->
   <td class="vocabulary_size">100</td> <!-- Size of the model's vocabulary -->
   <td class="max_sequence_length">1024</td> <!-- Maximum sequence length of the model -->
   <td class="commercially_licensed">True</td> <!-- Whether the model is commercially licensed -->
   <td class="speed">11,734 ± 3,124 / 2,174 ± 720</td> <!-- Model inference speed -->
   <td class="rank">5.59</td> <!-- ScandEval rank -->
   <td class="nl ner">0.11 ± 0.21 / 0.27 ± 0.53</td> <!-- CoNLL-nl -->
   <td class="nl sent">-0.67 ± 1.33 / 8.96 ± 0.37</td> <!-- Dutch Social -->
   <td class="nl la">-0.97 ± 1.56 / 34.83 ± 1.94</td> <!-- ScaLA-nl -->
   <td class="nl rc">0.29 ± 0.21 / 1.56 ± 0.19</td> <!-- SQuAD-nl -->
   <td class="nl summ">30.20 ± 0.68 / 2.14 ± 0.04</td> <!-- Wiki-Lingua-NL -->
   <td class="nl know">1.45 ± 0.84 / 24.91 ± 0.60</td> <!-- MMLU-nl -->
   <td class="nl reason">-0.56 ± 0.80 / 23.53 ± 0.49</td> <!-- HellaSwag-nl -->
   <td>9.3.1</td> <!-- CoNLL-nl version -->
   <td>10.0.1</td> <!-- Dutch Social version -->
   <td>11.0.0</td> <!-- ScaLA-nl version -->
   <td>12.5.1</td> <!-- SQuAD-nl version -->
   <td>12.0.0</td> <!-- Wiki-Lingua-NL version -->
   <td>11.0.0</td> <!-- MMLU-nl version -->
   <td>11.0.0</td> <!-- HellaSwag-nl version -->
   </tr>
 </tbody>
</table>
</div>

<div class="end-note">
  <a href="https://scandeval.com/dutch-nlg-test.csv" target="_blank">Download as CSV</a>
  &nbsp;&nbsp;&bull;&nbsp;&nbsp;
  <a href="javascript:void(0);" id="embed-link" data-embed="<iframe title=&quot;Dutch NLG&quot; aria-label=&quot;Table&quot; id=&quot;datawrapper-chart-SIBct&quot; src=&quot;https://datawrapper.dwcdn.net/SIBct/1/&quot; scrolling=&quot;no&quot; frameborder=&quot;0&quot; style=&quot;width: 0; min-width: 100% !important; border: none;&quot; height=&quot;400&quot; data-external=&quot;1&quot;></iframe><script type=&quot;text/javascript&quot;>!function(){&quot;use strict&quot;;window.addEventListener(&quot;message&quot;,(function(a){if(void 0!==a.data[&quot;datawrapper-height&quot;]){var e=document.querySelectorAll(&quot;iframe&quot;);for(var t in a.data[&quot;datawrapper-height&quot;])for(var r=0;r<e.length;r++)if(e[r].contentWindow===a.source){var i=a.data[&quot;datawrapper-height&quot;][t]+&quot;px&quot;;e[r].style.height=i}}}))}();
</script>">Copy embed HTML</a>
</div>
