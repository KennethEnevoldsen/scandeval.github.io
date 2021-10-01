---
layout: leaderboard
title: Pretrained Benchmark
---

<div class="table-wrapper centered">
<table id="pretrained-leaderboard" class="sortable fixed centered small-font">
 <thead>
   <tr>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="HuggingFace Hub Model ID">Model ID</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model size, in megabytes">Size</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Model inference speed, in samples per second">Speed</span></th>
     <th id="score-col"><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="ScandEval score - Mean of the language scores">Score</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Danish score - Macro-average across tasks">DA</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Norwegian score - Macro-average across tasks">NO</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Swedish score - Macro-average across tasks">SV</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Icelandic score - Macro-average across tasks">IS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total Faroese score - Macro-average across tasks">FO</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total NER tagging score - Macro-average across languages">NER</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total POS tagging score - Macro-average across languages">POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total dependency parsing score - Macro-average across languages">DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Total classification score - Macro-average across languages">CLF</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish NER tagging - Micro-F1 / Micro-F1 without MISC tags">DaNE</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish POS tagging - Accuracy">DDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish dependency parsing - LAS / UAS">DDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">AngryTweets</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">TwitterSent</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">Europarl</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish sentiment classification - Macro-F1">LCC</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Danish hate speech classification - Macro-F1">DKHate</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NB</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk NER tagging - Micro-F1 / Micro-F1 without MISC tags">NorNE-NN</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål POS tagging - Accuracy">NDT-NB-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk POS tagging - Accuracy">NDT-NN-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Bokmål dependency parsing - LAS / UAS">NDT-NB-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian Nynorsk dependency parsing - LAS / UAS">NDT-NN-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian sentiment classification - Macro-F1">NoReC</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Norwegian dialect classification - Macro-F1">NorDial</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish NER tagging - Micro-F1 / Micro-F1 without MISC tags">SUC3</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish POS tagging - Accuracy">SDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish dependency parsing - LAS / UAS">SDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish correct grammar classification - Macro-F1">DaLaJ</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Swedish immigration sentiment classification - Macro-F1">ABSAbank-Imm</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic NER tagging - Micro-F1">WikiANN-IS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic POS tagging - Accuracy">IDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic dependency parsing - LAS / UAS">IDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Icelandic sentiment classification - Macro-F1">NoReC-IS</span></th>

     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese NER tagging - Micro-F1">WikiANN-FO</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese POS tagging - Accuracy">FDT-POS</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese dependency parsing - LAS / UAS">FDT-DEP</span></th>
     <th><span data-toggle="tooltip" data-placement="bottom" data-container="body" title="Faroese sentiment classification - Macro-F1">NoReC-FO</span></th>
  </tr>
 </thead>
 <tbody>
   <tr>
    <td>Maltehb/danish-bert-botxo</td> <!-- Model ID -->
    <td class="size">424</td> <!-- Model size -->
    <td class="speed">4.11 ± 0.12</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">74.29 ± 0.34 / 77.94 ± 0.41</td> <!-- DaNE -->
    <td class="da pos">97.72 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">61.03 ± 0.53</td> <!-- AngryTweets -->
    <td class="da clf">61.61 ± 0.48</td> <!-- TwitterSent -->
    <td class="da clf">64.02 ± 0.64</td> <!-- Europarl -->
    <td class="da clf">59.19 ± 0.80</td> <!-- LCC -->
    <td class="da clf">70.56 ± 0.57</td> <!-- DKHate -->
    <td class="no ner">77.27 ± 0.22 / 79.72 ± 0.15</td> <!-- NorNE-NB -->
    <td class="no ner">75.54 ± 0.27 / 78.42 ± 0.28</td> <!-- NorNE-NN -->
    <td class="no pos">97.32 ± 0.04</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.47 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">79.99 ± 0.36 / 82.25 ± 0.35</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">57.47 ± 2.35</td> <!-- NoReC -->
    <td class="no clf">68.74 ± 1.16</td> <!-- NorDial -->
    <td class="sv ner">71.37 ± 0.15 / 74.52 ± 0.17</td> <!-- SUC3 -->
    <td class="sv pos">91.57 ± 0.05</td> <!-- SDT-POS -->
    <td class="sv dep">44.38 ± 0.21 / 48.61 ± 0.19</td> <!-- SDT-DEP -->
    <td class="sv clf">33.14 ± 0.12</td> <!-- DaLaJ -->
    <td class="sv clf">30.75 ± 0.51</td> <!-- ABSAbank-Imm -->
    <td class="is ner">70.68 ± 0.21</td> <!-- WikiANN-IS -->
    <td class="is pos">90.79 ± 0.12</td> <!-- IDT-POS -->
    <td class="is dep">77.13 ± 0.31 / 80.53 ± 0.27</td> <!-- IDT-DEP -->
    <td class="is clf">36.81 ± 1.31</td> <!-- NoReC-IS -->
    <td class="fo ner">76.60 ± 0.28</td> <!-- WikiANN-FO -->
    <td class="fo pos">82.71 ± 0.09</td> <!-- FDT-POS -->
    <td class="fo dep">29.60 ± 0.29 / 33.56 ± 0.29</td> <!-- FDT-DEP -->
    <td class="fo clf">30.50 ± 0.55</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Maltehb/-l-ctra-danish-electra-small-cased</td> <!-- Model ID -->
    <td class="size">55</td> <!-- Model size -->
    <td class="speed">25.56 ± 2.39</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">75.62 ± 0.55 / 78.12 ± 0.59</td> <!-- DaNE -->
    <td class="da pos">98.04 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep">61.14 ± 0.36 / 63.24 ± 0.36</td> <!-- DDT-DEP -->
    <td class="da clf">62.15 ± 0.38</td> <!-- AngryTweets -->
    <td class="da clf">43.73 ± 0.35</td> <!-- TwitterSent -->
    <td class="da clf">59.35 ± 1.89</td> <!-- Europarl -->
    <td class="da clf">58.34 ± 1.57</td> <!-- LCC -->
    <td class="da clf">76.90 ± 0.91</td> <!-- DKHate -->
    <td class="no ner">79.51 ± 0.19 / 81.41 ± 0.19</td> <!-- NorNE-NB -->
    <td class="no ner">77.21 ± 0.27 / 80.87 ± 0.27</td> <!-- NorNE-NN -->
    <td class="no pos">98.11 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.42 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">58.23 ± 0.92</td> <!-- NoReC -->
    <td class="no clf">66.66 ± 0.38</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">42.60 ± 0.39</td> <!-- DaLaJ -->
    <td class="sv clf">48.78 ± 0.47</td> <!-- ABSAbank-Imm -->
    <td class="is ner">83.67 ± 0.16</td> <!-- WikiANN-IS -->
    <td class="is pos">98.32 ± 0.05^</td> <!-- IDT-POS -->
    <td class="is dep">74.64 ± 0.37 / 78.04 ± 0.36</td> <!-- IDT-DEP -->
    <td class="is clf">37.83 ± 0.21</td> <!-- NoReC-IS -->
    <td class="fo ner">85.99 ± 0.19</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.01 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">41.32 ± 0.64 / 44.23 ± 0.66</td> <!-- FDT-DEP -->
    <td class="fo clf">37.39 ± 0.23</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>flax-community/roberta-base-danish</td> <!-- Model ID -->
    <td class="size">476</td> <!-- Model size -->
    <td class="speed">2.75 ± 0.08</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">79.19 ± 0.54 / 81.66 ± 0.46</td> <!-- DaNE -->
    <td class="da pos">98.00 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">48.21 ± 2.96</td> <!-- AngryTweets -->
    <td class="da clf">58.71 ± 2.43</td> <!-- TwitterSent -->
    <td class="da clf">22.01 ± 0.25</td> <!-- Europarl -->
    <td class="da clf">29.55 ± 2.12</td> <!-- LCC -->
    <td class="da clf">56.94 ± 1.06</td> <!-- DKHate -->
    <td class="no ner">85.14 ± 0.16 / 86.76 ± 0.20</td> <!-- NorNE-NB -->
    <td class="no ner">80.39 ± 0.47 / 84.13 ± 0.53</td> <!-- NorNE-NN -->
    <td class="no pos">98.19 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.40 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">57.19 ± 0.74</td> <!-- NoReC -->
    <td class="no clf">65.78 ± 0.52</td> <!-- NorDial -->
    <td class="sv ner">81.22 ± 0.09 / 85.10 ± 0.09</td> <!-- SUC3 -->
    <td class="sv pos">97.57 ± 0.03</td> <!-- SDT-POS -->
    <td class="sv dep">59.49 ± 0.62 / 62.83 ± 0.63</td> <!-- SDT-DEP -->
    <td class="sv clf">41.48 ± 1.66</td> <!-- DaLaJ -->
    <td class="sv clf">26.97 ± 1.21</td> <!-- ABSAbank-Imm -->
    <td class="is ner">82.91 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">98.54 ± 0.10</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">39.58 ± 1.41</td> <!-- NoReC-IS -->
    <td class="fo ner">83.11 ± 0.27</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.66 ± 0.12</td> <!-- FDT-POS -->
    <td class="fo dep">29.59 ± 0.29 / 32.39 ± 0.31</td> <!-- FDT-DEP -->
    <td class="fo clf">34.91 ± 0.81</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>flax-community/roberta-base-scandinavian</td> <!-- Model ID -->
    <td class="size">476</td> <!-- Model size -->
    <td class="speed">2.57 ± 0.08</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.94 ± 0.35 / 84.90 ± 0.30</td> <!-- DaNE -->
    <td class="da pos">97.93 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">39.68 ± 1.28</td> <!-- AngryTweets -->
    <td class="da clf">34.03 ± 1.67</td> <!-- TwitterSent -->
    <td class="da clf">23.78 ± 1.83</td> <!-- Europarl -->
    <td class="da clf">23.62 ± 0.25</td> <!-- LCC -->
    <td class="da clf">46.94 ± 0.05</td> <!-- DKHate -->
    <td class="no ner">86.52 ± 0.17 / 87.97 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">85.29 ± 0.25 / 88.47 ± 0.24</td> <!-- NorNE-NN -->
    <td class="no pos">98.52 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.29 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">53.70 ± 0.69</td> <!-- NoReC -->
    <td class="no clf">66.83 ± 0.42</td> <!-- NorDial -->
    <td class="sv ner">82.71 ± 0.06 / 86.28 ± 0.06</td> <!-- SUC3 -->
    <td class="sv pos">98.31 ± 0.03</td> <!-- SDT-POS -->
    <td class="sv dep">61.95 ± 0.50 / 64.64 ± 0.52</td> <!-- SDT-DEP -->
    <td class="sv clf">43.17 ± 1.45</td> <!-- DaLaJ -->
    <td class="sv clf">27.05 ± 1.37</td> <!-- ABSAbank-Imm -->
    <td class="is ner">82.18 ± 0.36</td> <!-- WikiANN-IS -->
    <td class="is pos">98.83 ± 0.03</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">26.02 ± 0.48</td> <!-- NoReC-IS -->
    <td class="fo ner">82.50 ± 0.41</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.20 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">30.09 ± 0.28 / 33.93 ± 0.30</td> <!-- FDT-DEP -->
    <td class="fo clf">27.85 ± 1.05</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Maltehb/-l-ctra-danish-electra-small-uncased</td> <!-- Model ID -->
    <td class="size">55</td> <!-- Model size -->
    <td class="speed">25.54 ± 1.53</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">76.63 ± 0.41 / 79.09 ± 0.46</td> <!-- DaNE -->
    <td class="da pos">98.03 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">62.81 ± 0.35</td> <!-- AngryTweets -->
    <td class="da clf">47.08 ± 0.47</td> <!-- TwitterSent -->
    <td class="da clf">57.42 ± 1.60</td> <!-- Europarl -->
    <td class="da clf">51.74 ± 1.21</td> <!-- LCC -->
    <td class="da clf">82.33 ± 0.69</td> <!-- DKHate -->
    <td class="no ner">75.27 ± 0.19 / 77.71 ± 0.19</td> <!-- NorNE-NB -->
    <td class="no ner">70.40 ± 0.29 / 73.88 ± 0.30</td> <!-- NorNE-NN -->
    <td class="no pos">97.15 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.66 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">80.10 ± 0.24 / 82.54 ± 0.23</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">51.88 ± 1.28</td> <!-- NoReC -->
    <td class="no clf">64.96 ± 0.38</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">49.63 ± 1.14</td> <!-- DaLaJ -->
    <td class="sv clf">38.84 ± 1.86</td> <!-- ABSAbank-Imm -->
    <td class="is ner">79.04 ± 0.35</td> <!-- WikiANN-IS -->
    <td class="is pos">98.22 ± 0.04</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">37.48 ± 0.17</td> <!-- NoReC-IS -->
    <td class="fo ner">84.09 ± 0.18</td> <!-- WikiANN-FO -->
    <td class="fo pos">94.40 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">42.53 ± 0.43 / 45.26 ± 0.44</td> <!-- FDT-DEP -->
    <td class="fo clf">38.70 ± 0.23</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>alexanderfalk/danbert-small-cased</td> <!-- Model ID -->
    <td class="size">321</td> <!-- Model size -->
    <td class="speed">8.73 ± 0.26</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">57.20 ± 0.50 / 59.12 ± 0.55</td> <!-- DaNE -->
    <td class="da pos">95.48 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">56.48 ± 0.38</td> <!-- AngryTweets -->
    <td class="da clf">43.77 ± 0.68</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 1.56</td> <!-- Europarl -->
    <td class="da clf">45.58 ± 0.89</td> <!-- LCC -->
    <td class="da clf">70.53 ± 0.85</td> <!-- DKHate -->
    <td class="no ner">63.79 ± 0.29 / 66.42 ± 0.28</td> <!-- NorNE-NB -->
    <td class="no ner">59.64 ± 0.32 / 62.66 ± 0.26</td> <!-- NorNE-NN -->
    <td class="no pos">95.17 ± 0.04</td> <!-- NDT-NB-POS -->
    <td class="no pos">94.05 ± 0.04</td> <!-- NDT-NN-POS -->
    <td class="no dep">64.59 ± 0.09 / 68.21 ± 0.09</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">50.21 ± 0.49</td> <!-- NoReC -->
    <td class="no clf">64.26 ± 0.42</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">47.24 ± 0.27</td> <!-- DaLaJ -->
    <td class="sv clf">44.43 ± 0.35</td> <!-- ABSAbank-Imm -->
    <td class="is ner">73.63 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">97.75 ± 0.05</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">38.42 ± 0.20</td> <!-- NoReC-IS -->
    <td class="fo ner">76.28 ± 0.18</td> <!-- WikiANN-FO -->
    <td class="fo pos">91.28 ± 0.10</td> <!-- FDT-POS -->
    <td class="fo dep">27.94 ± 0.27 / 30.67 ± 0.27</td> <!-- FDT-DEP -->
    <td class="fo clf">40.22 ± 0.31</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-da-cased</td> <!-- Model ID -->
    <td class="size">396</td> <!-- Model size -->
    <td class="speed">4.26 ± 0.12</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">82.86 ± 0.50 / 85.01 ± 0.57</td> <!-- DaNE -->
    <td class="da pos">97.32 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep">59.99 ± 0.47 / 62.54 ± 0.47</td> <!-- DDT-DEP -->
    <td class="da clf">56.75 ± 0.36</td> <!-- AngryTweets -->
    <td class="da clf">48.40 ± 0.54</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 2.14</td> <!-- Europarl -->
    <td class="da clf">54.11 ± 0.96</td> <!-- LCC -->
    <td class="da clf">64.71 ± 0.83</td> <!-- DKHate -->
    <td class="no ner">86.82 ± 0.16 / 88.18 ± 0.15</td> <!-- NorNE-NB -->
    <td class="no ner">85.65 ± 0.15 / 88.92 ± 0.13</td> <!-- NorNE-NN -->
    <td class="no pos">98.16 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.88 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">60.48 ± 0.60</td> <!-- NoReC -->
    <td class="no clf">74.18 ± 1.56</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">48.26 ± 0.41</td> <!-- DaLaJ -->
    <td class="sv clf">49.53 ± 0.43</td> <!-- ABSAbank-Imm -->
    <td class="is ner">88.86 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">99.12 ± 0.03</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">43.96 ± 0.29</td> <!-- NoReC-IS -->
    <td class="fo ner">89.91 ± 0.14</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.19 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">46.68 ± 0.39 / 48.90 ± 0.40</td> <!-- FDT-DEP -->
    <td class="fo clf">47.80 ± 0.52</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>sarnikowski/electra-small-generator-da-256-cased</td> <!-- Model ID -->
    <td class="size">17</td> <!-- Model size -->
    <td class="speed">90.79 ± 11.32</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">47.72 ± 0.32 / 50.14 ± 0.41</td> <!-- DaNE -->
    <td class="da pos">87.85 ± 0.07</td> <!-- DDT-POS -->
    <td class="da dep">17.92 ± 0.19 / 21.70 ± 0.20</td> <!-- DDT-DEP -->
    <td class="da clf">43.15 ± 1.09</td> <!-- AngryTweets -->
    <td class="da clf">42.64 ± 0.75</td> <!-- TwitterSent -->
    <td class="da clf">37.05 ± 1.27</td> <!-- Europarl -->
    <td class="da clf">33.55 ± 0.90</td> <!-- LCC -->
    <td class="da clf">66.98 ± 0.77</td> <!-- DKHate -->
    <td class="no ner">52.70 ± 0.33 / 55.43 ± 0.32</td> <!-- NorNE-NB -->
    <td class="no ner">42.38 ± 0.38 / 45.76 ± 0.39</td> <!-- NorNE-NN -->
    <td class="no pos">87.30 ± 0.06</td> <!-- NDT-NB-POS -->
    <td class="no pos">83.08 ± 0.05</td> <!-- NDT-NN-POS -->
    <td class="no dep">31.79 ± 0.14 / 36.66 ± 0.14</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">44.60 ± 0.50</td> <!-- NoReC -->
    <td class="no clf">44.31 ± 1.80</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">73.87 ± 0.08</td> <!-- SDT-POS -->
    <td class="sv dep">14.96 ± 0.08 / 20.08 ± 0.08</td> <!-- SDT-DEP -->
    <td class="sv clf">39.77 ± 0.30</td> <!-- DaLaJ -->
    <td class="sv clf">25.49 ± 0.25</td> <!-- ABSAbank-Imm -->
    <td class="is ner">54.52 ± 0.20</td> <!-- WikiANN-IS -->
    <td class="is pos">63.95 ± 0.28</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">43.14 ± 0.39</td> <!-- NoReC-IS -->
    <td class="fo ner">63.54 ± 0.21</td> <!-- WikiANN-FO -->
    <td class="fo pos">68.74 ± 0.11</td> <!-- FDT-POS -->
    <td class="fo dep">15.90 ± 0.18 / 20.74 ± 0.21</td> <!-- FDT-DEP -->
    <td class="fo clf">37.42 ± 0.19</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-da-cased</td> <!-- Model ID -->
    <td class="size">234</td> <!-- Model size -->
    <td class="speed">8.36 ± 0.43</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">80.79 ± 0.33 / 82.67 ± 0.33</td> <!-- DaNE -->
    <td class="da pos">96.79 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">53.73 ± 0.40</td> <!-- AngryTweets -->
    <td class="da clf">45.03 ± 0.38</td> <!-- TwitterSent -->
    <td class="da clf">51.71 ± 0.87</td> <!-- Europarl -->
    <td class="da clf">44.15 ± 1.25</td> <!-- LCC -->
    <td class="da clf">64.63 ± 0.60</td> <!-- DKHate -->
    <td class="no ner">81.33 ± 0.18 / 83.18 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">83.71 ± 0.22 / 87.39 ± 0.17</td> <!-- NorNE-NN -->
    <td class="no pos">97.73 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.42 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">58.39 ± 0.38</td> <!-- NoReC -->
    <td class="no clf">74.04 ± 1.29</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">48.33 ± 0.28</td> <!-- DaLaJ -->
    <td class="sv clf">47.82 ± 0.57</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.77 ± 0.17</td> <!-- WikiANN-IS -->
    <td class="is pos">98.92 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">43.54 ± 0.41</td> <!-- NoReC-IS -->
    <td class="fo ner">88.92 ± 0.15</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.99 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">41.06 ± 0.34 / 43.38 ± 0.35</td> <!-- FDT-DEP -->
    <td class="fo clf">40.88 ± 0.23</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>KB/bert-base-swedish-cased</td> <!-- Model ID -->
    <td class="size">478</td> <!-- Model size -->
    <td class="speed">4.13 ± 0.14</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.30 ± 0.40 / 83.19 ± 0.39</td> <!-- DaNE -->
    <td class="da pos">96.94 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep">61.53 ± 0.31 / 64.51 ± 0.31</td> <!-- DDT-DEP -->
    <td class="da clf">59.44 ± 0.40</td> <!-- AngryTweets -->
    <td class="da clf">55.48 ± 0.41</td> <!-- TwitterSent -->
    <td class="da clf">22.63 ± 1.90</td> <!-- Europarl -->
    <td class="da clf">45.73 ± 1.02</td> <!-- LCC -->
    <td class="da clf">70.24 ± 0.88</td> <!-- DKHate -->
    <td class="no ner">84.97 ± 0.32 / 86.25 ± 0.29</td> <!-- NorNE-NB -->
    <td class="no ner">83.86 ± 0.35 / 87.78 ± 0.31</td> <!-- NorNE-NN -->
    <td class="no pos">97.90 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.53 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">65.43 ± 0.34</td> <!-- NoReC -->
    <td class="no clf">68.86 ± 1.26</td> <!-- NorDial -->
    <td class="sv ner">88.47 ± 0.06 / 91.41 ± 0.05</td> <!-- SUC3 -->
    <td class="sv pos">98.72 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">76.34 ± 0.14 / 78.13 ± 0.14</td> <!-- SDT-DEP -->
    <td class="sv clf">62.80 ± 0.38</td> <!-- DaLaJ -->
    <td class="sv clf">59.50 ± 0.32</td> <!-- ABSAbank-Imm -->
    <td class="is ner">84.91 ± 0.16</td> <!-- WikiANN-IS -->
    <td class="is pos">97.28 ± 0.04</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">48.28 ± 0.29</td> <!-- NoReC-IS -->
    <td class="fo ner">88.52 ± 0.12</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.59 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">46.04 ± 0.34 / 49.51 ± 0.36</td> <!-- FDT-DEP -->
    <td class="fo clf">49.71 ± 0.22</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>flax-community/nordic-roberta-wiki</td> <!-- Model ID -->
    <td class="size">476</td> <!-- Model size -->
    <td class="speed">4.09 ± 0.13</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">77.32 ± 0.28 / 81.12 ± 0.32</td> <!-- DaNE -->
    <td class="da pos">97.38 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">56.19 ± 0.27</td> <!-- AngryTweets -->
    <td class="da clf">39.52 ± 0.75</td> <!-- TwitterSent -->
    <td class="da clf">24.70 ± 1.70</td> <!-- Europarl -->
    <td class="da clf">47.33 ± 0.83</td> <!-- LCC -->
    <td class="da clf">68.87 ± 0.78</td> <!-- DKHate -->
    <td class="no ner">85.09 ± 0.25 / 86.81 ± 0.24</td> <!-- NorNE-NB -->
    <td class="no ner">83.69 ± 0.29 / 87.47 ± 0.24</td> <!-- NorNE-NN -->
    <td class="no pos">98.26 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.67 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">60.02 ± 0.63</td> <!-- NoReC -->
    <td class="no clf">63.72 ± 0.49</td> <!-- NorDial -->
    <td class="sv ner">85.10 ± 0.06 / 88.27 ± 0.06</td> <!-- SUC3 -->
    <td class="sv pos">98.09 ± 0.0</td> <!-- SDT-POS -->
    <td class="sv dep">63.74 ± 0.12 / 66.19 ± 0.12</td> <!-- SDT-DEP -->
    <td class="sv clf">50.54 ± 0.36</td> <!-- DaLaJ -->
    <td class="sv clf">45.54 ± 0.30</td> <!-- ABSAbank-Imm -->
    <td class="is ner">85.92 ± 0.10</td> <!-- WikiANN-IS -->
    <td class="is pos">98.52 ± 0.04</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">48.21 ± 0.34</td> <!-- NoReC-IS -->
    <td class="fo ner">86.55 ± 0.12</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.92 ± 0.05</td> <!-- FDT-POS -->
    <td class="fo dep">37.16 ± 0.39 / 39.87 ± 0.40</td> <!-- FDT-DEP -->
    <td class="fo clf">49.37 ± 0.28</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>flax-community/swe-roberta-wiki-oscar</td> <!-- Model ID -->
    <td class="size">476</td> <!-- Model size -->
    <td class="speed">3.80 ± 0.12</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">78.74 ± 0.36 / 81.28 ± 0.34</td> <!-- DaNE -->
    <td class="da pos">96.41 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">56.60 ± 0.53</td> <!-- AngryTweets -->
    <td class="da clf">50.75 ± 0.69</td> <!-- TwitterSent -->
    <td class="da clf">22.63 ± 1.55</td> <!-- Europarl -->
    <td class="da clf">40.51 ± 1.24</td> <!-- LCC -->
    <td class="da clf">62.45 ± 0.87</td> <!-- DKHate -->
    <td class="no ner">82.54 ± 0.23 / 83.76 ± 0.24</td> <!-- NorNE-NB -->
    <td class="no ner">83.16 ± 0.22 / 85.93 ± 0.19</td> <!-- NorNE-NN -->
    <td class="no pos">97.64 ± 0.13</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.94 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">84.26 ± 0.08 / 86.57 ± 0.08</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">61.14 ± 0.36</td> <!-- NoReC -->
    <td class="no clf">62.76 ± 0.59</td> <!-- NorDial -->
    <td class="sv ner">87.07 ± 0.24 / 89.73 ± 0.18</td> <!-- SUC3 -->
    <td class="sv pos">98.31 ± 0.03</td> <!-- SDT-POS -->
    <td class="sv dep">71.32 ± 0.10 / 73.19 ± 0.11</td> <!-- SDT-DEP -->
    <td class="sv clf">54.33 ± 1.37</td> <!-- DaLaJ -->
    <td class="sv clf">48.84 ± 0.61</td> <!-- ABSAbank-Imm -->
    <td class="is ner">81.77 ± 0.17</td> <!-- WikiANN-IS -->
    <td class="is pos">98.08 ± 0.08</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">48.92 ± 0.51</td> <!-- NoReC-IS -->
    <td class="fo ner">80.24 ± 0.84</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.24 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">40.85 ± 0.50 / 43.49 ± 0.51</td> <!-- FDT-DEP -->
    <td class="fo clf">37.40 ± 1.46</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>KB/albert-base-swedish-cased-alpha</td> <!-- Model ID -->
    <td class="size">54</td> <!-- Model size -->
    <td class="speed">4.46 ± 0.17</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">69.88 ± 0.41 / 71.89 ± 0.45</td> <!-- DaNE -->
    <td class="da pos">94.50 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">47.97 ± 0.36</td> <!-- AngryTweets -->
    <td class="da clf">43.37 ± 0.35</td> <!-- TwitterSent -->
    <td class="da clf">22.58 ± 1.23</td> <!-- Europarl -->
    <td class="da clf">29.37 ± 1.07</td> <!-- LCC -->
    <td class="da clf">47.60 ± 0.43</td> <!-- DKHate -->
    <td class="no ner">75.07 ± 0.24 / 76.97 ± 0.26</td> <!-- NorNE-NB -->
    <td class="no ner">77.02 ± 0.35 / 80.70 ± 0.39</td> <!-- NorNE-NN -->
    <td class="no pos">96.49 ± 0.04</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.03 ± 0.05</td> <!-- NDT-NN-POS -->
    <td class="no dep">77.26 ± 0.14 / 80.40 ± 0.15</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">50.35 ± 1.59</td> <!-- NoReC -->
    <td class="no clf">62.84 ± 0.54</td> <!-- NorDial -->
    <td class="sv ner">77.63 ± 0.09 / 81.36 ± 0.10</td> <!-- SUC3 -->
    <td class="sv pos">94.12 ± 0.04</td> <!-- SDT-POS -->
    <td class="sv dep">56.42 ± 0.13 / 59.37 ± 0.14</td> <!-- SDT-DEP -->
    <td class="sv clf">44.57 ± 0.52</td> <!-- DaLaJ -->
    <td class="sv clf">30.21 ± 1.73</td> <!-- ABSAbank-Imm -->
    <td class="is ner">77.50 ± 0.32</td> <!-- WikiANN-IS -->
    <td class="is pos">95.91 ± 0.32</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">28.16 ± 0.58</td> <!-- NoReC-IS -->
    <td class="fo ner">82.25 ± 0.14</td> <!-- WikiANN-FO -->
    <td class="fo pos">89.95 ± 0.11</td> <!-- FDT-POS -->
    <td class="fo dep">29.67 ± 0.43 / 32.64 ± 0.45</td> <!-- FDT-DEP -->
    <td class="fo clf">37.61 ± 0.75</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>ltgoslo/norbert</td> <!-- Model ID -->
    <td class="size">427</td> <!-- Model size -->
    <td class="speed">4.15 ± 0.13</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">79.05 ± 0.43 / 80.88 ± 0.39</td> <!-- DaNE -->
    <td class="da pos">97.39 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">60.78 ± 0.20</td> <!-- AngryTweets -->
    <td class="da clf">23.18 ± 0.22</td> <!-- TwitterSent -->
    <td class="da clf">22.63 ± 0.72</td> <!-- Europarl -->
    <td class="da clf">56.12 ± 0.96</td> <!-- LCC -->
    <td class="da clf">46.94 ± 0.05</td> <!-- DKHate -->
    <td class="no ner">90.21 ± 0.15 / 91.12 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">87.48 ± 0.23 / 90.80 ± 0.19</td> <!-- NorNE-NN -->
    <td class="no pos">98.51 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.45 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">30.68 ± 0.62</td> <!-- NoReC -->
    <td class="no clf">67.17 ± 0.36</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">48.91 ± 1.08</td> <!-- DaLaJ -->
    <td class="sv clf">42.96 ± 0.42</td> <!-- ABSAbank-Imm -->
    <td class="is ner">83.41 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">92.06 ± 0.06</td> <!-- IDT-POS -->
    <td class="is dep">31.77 ± 0.88 / 36.26 ± 0.81</td> <!-- IDT-DEP -->
    <td class="is clf">22.44 ± 0.10</td> <!-- NoReC-IS -->
    <td class="fo ner">85.90 ± 0.17</td> <!-- WikiANN-FO -->
    <td class="fo pos">94.31 ± 0.09</td> <!-- FDT-POS -->
    <td class="fo dep">22.38 ± 0.56 / 25.15 ± 0.57</td> <!-- FDT-DEP -->
    <td class="fo clf">24.82 ± 0.46</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>NbAiLab/nb-bert-base</td> <!-- Model ID -->
    <td class="size">681</td> <!-- Model size -->
    <td class="speed">4.26 ± 0.15</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">83.81 ± 0.34 / 85.14 ± 0.37</td> <!-- DaNE -->
    <td class="da pos">98.28 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">64.83 ± 0.48</td> <!-- AngryTweets -->
    <td class="da clf">52.42 ± 0.75</td> <!-- TwitterSent -->
    <td class="da clf">65.54 ± 0.75</td> <!-- Europarl -->
    <td class="da clf">58.10 ± 1.12</td> <!-- LCC -->
    <td class="da clf">75.53 ± 0.96</td> <!-- DKHate -->
    <td class="no ner">91.98 ± 0.17 / 92.95 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">90.93 ± 0.12 / 94.06 ± 0.11</td> <!-- NorNE-NN -->
    <td class="no pos">98.80 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.83 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">75.60 ± 0.42</td> <!-- NoReC -->
    <td class="no clf">69.39 ± 0.38</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">98.53 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">73.91 ± 0.12 / 75.99 ± 0.13</td> <!-- SDT-DEP -->
    <td class="sv clf">57.56 ± 0.50</td> <!-- DaLaJ -->
    <td class="sv clf">51.83 ± 0.64</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.52 ± 0.11</td> <!-- WikiANN-IS -->
    <td class="is pos">99.18 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">53.21 ± 0.26</td> <!-- NoReC-IS -->
    <td class="fo ner">90.43 ± 0.14</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.23 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">53.73 ± 0.40 / 56.38 ± 0.40</td> <!-- FDT-DEP -->
    <td class="fo clf">44.95 ± 0.80</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>NbAiLab/nb-bert-large</td> <!-- Model ID -->
    <td class="size">1330</td> <!-- Model size -->
    <td class="speed">0.60 ± 0.01</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">82.66 ± 0.44 / 85.02 ± 0.38</td> <!-- DaNE -->
    <td class="da pos">98.55 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep">66.05 ± 0.13 / 68.59 ± 0.13</td> <!-- DDT-DEP -->
    <td class="da clf">67.08 ± 0.36</td> <!-- AngryTweets -->
    <td class="da clf">59.52 ± 0.48</td> <!-- TwitterSent -->
    <td class="da clf">70.30 ± 0.86</td> <!-- Europarl -->
    <td class="da clf">59.21 ± 2.63</td> <!-- LCC -->
    <td class="da clf">78.65 ± 0.86</td> <!-- DKHate -->
    <td class="no ner">90.45 ± 0.14 / 92.46 ± 0.15</td> <!-- NorNE-NB -->
    <td class="no ner">88.01 ± 0.19 / 91.90 ± 0.16</td> <!-- NorNE-NN -->
    <td class="no pos">98.56 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.48 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">75.68 ± 0.33</td> <!-- NoReC -->
    <td class="no clf">67.30 ± 0.41</td> <!-- NorDial -->
    <td class="sv ner">85.54 ± 0.08 / 88.55 ± 0.12</td> <!-- SUC3 -->
    <td class="sv pos">98.66 ± 0.03</td> <!-- SDT-POS -->
    <td class="sv dep">72.14 ± 0.91 / 73.90 ± 0.90</td> <!-- SDT-DEP -->
    <td class="sv clf">54.93 ± 0.93</td> <!-- DaLaJ -->
    <td class="sv clf">46.03 ± 0.63</td> <!-- ABSAbank-Imm -->
    <td class="is ner">85.98 ± 0.14</td> <!-- WikiANN-IS -->
    <td class="is pos">98.36 ± 0.03</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">30.10 ± 1.71</td> <!-- NoReC-IS -->
    <td class="fo ner">89.80 ± 0.16</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.19 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">46.91 ± 0.85 / 49.19 ± 0.87</td> <!-- FDT-DEP -->
    <td class="fo clf">48.38 ± 2.50</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-no-cased</td> <!-- Model ID -->
    <td class="size">397</td> <!-- Model size -->
    <td class="speed">4.14 ± 0.16</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">82.22 ± 0.26 / 85.55 ± 0.29</td> <!-- DaNE -->
    <td class="da pos">97.22 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">56.49 ± 0.40</td> <!-- AngryTweets -->
    <td class="da clf">49.94 ± 0.58</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 2.10</td> <!-- Europarl -->
    <td class="da clf">53.54 ± 0.92</td> <!-- LCC -->
    <td class="da clf">69.05 ± 0.72</td> <!-- DKHate -->
    <td class="no ner">87.83 ± 0.13 / 89.09 ± 0.14</td> <!-- NorNE-NB -->
    <td class="no ner">86.57 ± 0.25 / 89.18 ± 0.19</td> <!-- NorNE-NN -->
    <td class="no pos">98.21 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.99 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">61.88 ± 0.28</td> <!-- NoReC -->
    <td class="no clf">69.43 ± 0.97</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">47.80 ± 0.39</td> <!-- DaLaJ -->
    <td class="sv clf">47.25 ± 0.60</td> <!-- ABSAbank-Imm -->
    <td class="is ner">88.99 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">99.11 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">51.78 ± 0.31</td> <!-- NoReC-IS -->
    <td class="fo ner">89.23 ± 0.16</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.28 ± 0.05</td> <!-- FDT-POS -->
    <td class="fo dep">43.74 ± 0.41 / 45.88 ± 0.40</td> <!-- FDT-DEP -->
    <td class="fo clf">46.55 ± 0.37</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-no-cased</td> <!-- Model ID -->
    <td class="size">235</td> <!-- Model size -->
    <td class="speed">8.49 ± 0.36</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">79.62 ± 0.34 / 81.75 ± 0.34</td> <!-- DaNE -->
    <td class="da pos">96.70 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep">55.48 ± 0.25 / 58.52 ± 0.24</td> <!-- DDT-DEP -->
    <td class="da clf">52.35 ± 0.29</td> <!-- AngryTweets -->
    <td class="da clf">44.14 ± 0.67</td> <!-- TwitterSent -->
    <td class="da clf">23.67 ± 1.66</td> <!-- Europarl -->
    <td class="da clf">37.13 ± 0.49</td> <!-- LCC -->
    <td class="da clf">58.93 ± 0.81</td> <!-- DKHate -->
    <td class="no ner">81.83 ± 0.21 / 83.96 ± 0.20</td> <!-- NorNE-NB -->
    <td class="no ner">85.75 ± 0.26 / 89.06 ± 0.21</td> <!-- NorNE-NN -->
    <td class="no pos">97.72 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.45 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">78.25 ± 0.11 / 80.92 ± 0.10</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">55.38 ± 0.48</td> <!-- NoReC -->
    <td class="no clf">69.34 ± 0.85</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">46.44 ± 0.25</td> <!-- DaLaJ -->
    <td class="sv clf">45.09 ± 0.50</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.08 ± 0.11</td> <!-- WikiANN-IS -->
    <td class="is pos">98.95 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">48.36 ± 0.28</td> <!-- NoReC-IS -->
    <td class="fo ner">89.82 ± 0.15</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.03 ± 0.03</td> <!-- FDT-POS -->
    <td class="fo dep">42.58 ± 0.30 / 45.13 ± 0.30</td> <!-- FDT-DEP -->
    <td class="fo clf">40.91 ± 0.97</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>ViktorAlm/electra-base-norwegian-uncased-discriminator</td> <!-- Model ID -->
    <td class="size">416</td> <!-- Model size -->
    <td class="speed">4.27 ± 0.15</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">61.70 ± 0.40 / 59.20 ± 0.44</td> <!-- DaNE -->
    <td class="da pos">94.73 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep">58.10 ± 0.25 / 61.70 ± 0.24</td> <!-- DDT-DEP -->
    <td class="da clf">59.22 ± 0.26</td> <!-- AngryTweets -->
    <td class="da clf">44.50 ± 0.89</td> <!-- TwitterSent -->
    <td class="da clf">59.79 ± 0.74</td> <!-- Europarl -->
    <td class="da clf">60.94 ± 1.19</td> <!-- LCC -->
    <td class="da clf">69.12 ± 1.00</td> <!-- DKHate -->
    <td class="no ner">69.53 ± 0.24 / 70.65 ± 0.24</td> <!-- NorNE-NB -->
    <td class="no ner">69.34 ± 0.38 / 71.08 ± 0.41</td> <!-- NorNE-NN -->
    <td class="no pos">96.70 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.00 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep">83.71 ± 0.08 / 86.09 ± 0.07</td> <!-- NDT-NB-DEP -->
    <td class="no dep">80.25 ± 0.22 / 83.17 ± 0.21</td> <!-- NDT-NN-DEP -->
    <td class="no clf">73.00 ± 0.24</td> <!-- NoReC -->
    <td class="no clf">64.82 ± 0.47</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">47.67 ± 1.13</td> <!-- DaLaJ -->
    <td class="sv clf">48.93 ± 0.60</td> <!-- ABSAbank-Imm -->
    <td class="is ner">66.68 ± 0.27</td> <!-- WikiANN-IS -->
    <td class="is pos">93.90 ± 0.06</td> <!-- IDT-POS -->
    <td class="is dep">77.98 ± 0.61 / 81.32 ± 0.49</td> <!-- IDT-DEP -->
    <td class="is clf">41.08 ± 1.03</td> <!-- NoReC-IS -->
    <td class="fo ner">69.74 ± 0.42</td> <!-- WikiANN-FO -->
    <td class="fo pos">87.11 ± 0.10</td> <!-- FDT-POS -->
    <td class="fo dep">38.55 ± 0.34 / 42.45 ± 0.36</td> <!-- FDT-DEP -->
    <td class="fo clf">41.46 ± 0.49</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>sarnikowski/electra-small-discriminator-da-256-cased</td> <!-- Model ID -->
    <td class="size">51</td> <!-- Model size -->
    <td class="speed">25.94 ± 3.47</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">74.84 ± 0.55 / 77.51 ± 0.53</td> <!-- DaNE -->
    <td class="da pos">97.76 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">42.98 ± 0.53</td> <!-- AngryTweets -->
    <td class="da clf">41.60 ± 0.36</td> <!-- TwitterSent -->
    <td class="da clf">49.08 ± 0.53</td> <!-- Europarl -->
    <td class="da clf">57.99 ± 1.02</td> <!-- LCC -->
    <td class="da clf">65.16 ± 0.92</td> <!-- DKHate -->
    <td class="no ner">78.90 ± 0.22 / 80.72 ± 0.21</td> <!-- NorNE-NB -->
    <td class="no ner">76.09 ± 0.28 / 79.38 ± 0.26</td> <!-- NorNE-NN -->
    <td class="no pos">97.77 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.18 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">45.04 ± 0.15</td> <!-- NoReC -->
    <td class="no clf">69.09 ± 0.86</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">90.89 ± 0.06</td> <!-- SDT-POS -->
    <td class="sv dep">43.75 ± 0.38 / 48.39 ± 0.40</td> <!-- SDT-DEP -->
    <td class="sv clf">39.00 ± 0.25</td> <!-- DaLaJ -->
    <td class="sv clf">30.21 ± 1.18</td> <!-- ABSAbank-Imm -->
    <td class="is ner">70.97 ± 0.18</td> <!-- WikiANN-IS -->
    <td class="is pos">90.78 ± 0.11</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">38.78 ± 0.36</td> <!-- NoReC-IS -->
    <td class="fo ner">78.36 ± 0.15</td> <!-- WikiANN-FO -->
    <td class="fo pos">83.93 ± 0.09</td> <!-- FDT-POS -->
    <td class="fo dep">31.23 ± 0.31 / 35.34 ± 0.33</td> <!-- FDT-DEP -->
    <td class="fo clf">37.20 ± 0.41</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>setu4993/LaBSE</td> <!-- Model ID -->
    <td class="size">1750</td> <!-- Model size -->
    <td class="speed">4.42 ± 0.11</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">82.51 ± 0.33 / 83.49 ± 0.34</td> <!-- DaNE -->
    <td class="da pos">97.97 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">64.30 ± 0.29</td> <!-- AngryTweets -->
    <td class="da clf">66.10 ± 0.50</td> <!-- TwitterSent -->
    <td class="da clf">73.70 ± 0.46</td> <!-- Europarl -->
    <td class="da clf">67.24 ± 1.07</td> <!-- LCC -->
    <td class="da clf">63.45 ± 0.58</td> <!-- DKHate -->
    <td class="no ner">89.51 ± 0.12 / 90.50 ± 0.13</td> <!-- NorNE-NB -->
    <td class="no ner">89.34 ± 0.17 / 91.96 ± 0.17</td> <!-- NorNE-NN -->
    <td class="no pos">98.56 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.13 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">69.49 ± 0.33</td> <!-- NoReC -->
    <td class="no clf">67.50 ± 0.61</td> <!-- NorDial -->
    <td class="sv ner">85.33 ± 0.06 / 88.36 ± 0.06</td> <!-- SUC3 -->
    <td class="sv pos">98.50 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">71.91 ± 0.13 / 74.13 ± 0.13</td> <!-- SDT-DEP -->
    <td class="sv clf">51.08 ± 0.48</td> <!-- DaLaJ -->
    <td class="sv clf">55.04 ± 0.39</td> <!-- ABSAbank-Imm -->
    <td class="is ner">90.31 ± 0.16</td> <!-- WikiANN-IS -->
    <td class="is pos">99.33 ± 0.07</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">57.00 ± 0.28</td> <!-- NoReC-IS -->
    <td class="fo ner">90.06 ± 0.29</td> <!-- WikiANN-FO -->
    <td class="fo pos">98.27 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">51.99 ± 0.42 / 54.14 ± 0.43</td> <!-- FDT-DEP -->
    <td class="fo clf">60.54 ± 0.29</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>mideind/IceBERT</td> <!-- Model ID -->
    <td class="size">475</td> <!-- Model size -->
    <td class="speed">3.65 ± 0.11</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">68.54 ± 0.47 / 71.60 ± 0.43</td> <!-- DaNE -->
    <td class="da pos">95.00 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep">79.43 ± 0.16 / 82.84 ± 0.13</td> <!-- DDT-DEP -->
    <td class="da clf">51.79 ± 0.27</td> <!-- AngryTweets -->
    <td class="da clf">38.61 ± 0.67</td> <!-- TwitterSent -->
    <td class="da clf">21.96 ± 0.16</td> <!-- Europarl -->
    <td class="da clf">40.56 ± 0.83</td> <!-- LCC -->
    <td class="da clf">46.94 ± 0.05</td> <!-- DKHate -->
    <td class="no ner">77.65 ± 0.29 / 79.23 ± 0.28</td> <!-- NorNE-NB -->
    <td class="no ner">76.71 ± 0.26 / 80.14 ± 0.31</td> <!-- NorNE-NN -->
    <td class="no pos">97.07 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.72 ± 0.04</td> <!-- NDT-NN-POS -->
    <td class="no dep">79.92 ± 0.10 / 83.27 ± 0.08</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">46.51 ± 0.50</td> <!-- NoReC -->
    <td class="no clf">64.31 ± 0.62</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">33.17 ± 0.12</td> <!-- DaLaJ -->
    <td class="sv clf">47.84 ± 0.39</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.94 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">99.46 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">53.98 ± 0.31</td> <!-- NoReC-IS -->
    <td class="fo ner">86.78 ± 0.17</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.47 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">46.20 ± 0.35 / 48.65 ± 0.35</td> <!-- FDT-DEP -->
    <td class="fo clf">46.37 ± 1.36</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>neurocode/IsRoBERTa</td> <!-- Model ID -->
    <td class="size">319</td> <!-- Model size -->
    <td class="speed">7.77 ± 0.33</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">59.80 ± 0.38 / 61.70 ± 0.43</td> <!-- DaNE -->
    <td class="da pos">93.17 ± 0.11</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">52.93 ± 0.32</td> <!-- AngryTweets -->
    <td class="da clf">30.17 ± 0.51</td> <!-- TwitterSent -->
    <td class="da clf">21.96 ± 0.16</td> <!-- Europarl -->
    <td class="da clf">35.67 ± 0.97</td> <!-- LCC -->
    <td class="da clf">67.93 ± 0.82</td> <!-- DKHate -->
    <td class="no ner">71.63 ± 0.27 / 73.30 ± 0.26</td> <!-- NorNE-NB -->
    <td class="no ner">70.76 ± 0.26 / 73.74 ± 0.29</td> <!-- NorNE-NN -->
    <td class="no pos">96.16 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">95.89 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep">67.45 ± 0.25 / 71.42 ± 0.24</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">48.47 ± 0.26</td> <!-- NoReC -->
    <td class="no clf">62.56 ± 0.49</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">33.17 ± 0.12</td> <!-- DaLaJ -->
    <td class="sv clf">42.12 ± 0.41</td> <!-- ABSAbank-Imm -->
    <td class="is ner">83.41 ± 0.16</td> <!-- WikiANN-IS -->
    <td class="is pos">99.27 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep">84.35 ± 0.23 / 85.39 ± 0.22</td> <!-- IDT-DEP -->
    <td class="is clf">50.53 ± 0.19</td> <!-- NoReC-IS -->
    <td class="fo ner">82.16 ± 0.18</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.76 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">33.22 ± 0.27 / 35.32 ± 0.27</td> <!-- FDT-DEP -->
    <td class="fo clf">50.45 ± 0.15</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>xlm-roberta-base</td> <!-- Model ID -->
    <td class="size">1040</td> <!-- Model size -->
    <td class="speed">4.10 ± 0.12</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">84.31 ± 0.32 / 85.60 ± 0.34</td> <!-- DaNE -->
    <td class="da pos">98.32 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">63.89 ± 0.75</td> <!-- AngryTweets -->
    <td class="da clf">55.46 ± 0.49</td> <!-- TwitterSent -->
    <td class="da clf">69.92 ± 0.76</td> <!-- Europarl -->
    <td class="da clf">53.02 ± 4.75</td> <!-- LCC -->
    <td class="da clf">77.92 ± 0.92</td> <!-- DKHate -->
    <td class="no ner">90.22 ± 0.14 / 90.99 ± 0.13</td> <!-- NorNE-NB -->
    <td class="no ner">88.56 ± 0.27 / 91.38 ± 0.25</td> <!-- NorNE-NN -->
    <td class="no pos">98.63 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.30 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">71.62 ± 0.24</td> <!-- NoReC -->
    <td class="no clf">68.31 ± 0.57</td> <!-- NorDial -->
    <td class="sv ner">87.30 ± 0.07 / 90.04 ± 0.07</td> <!-- SUC3 -->
    <td class="sv pos">98.67 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">77.56 ± 0.30 / 79.50 ± 0.30</td> <!-- SDT-DEP -->
    <td class="sv clf">47.01 ± 0.91</td> <!-- DaLaJ -->
    <td class="sv clf">48.81 ± 0.72</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.33 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">99.32 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">49.33 ± 0.80</td> <!-- NoReC-IS -->
    <td class="fo ner">90.07 ± 0.36</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.98 ± 0.03</td> <!-- FDT-POS -->
    <td class="fo dep">53.71 ± 0.57 / 55.96 ± 0.56</td> <!-- FDT-DEP -->
    <td class="fo clf">47.78 ± 2.19</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>xlm-roberta-large</td> <!-- Model ID -->
    <td class="size">2090</td> <!-- Model size -->
    <td class="speed">1.13 ± 0.03</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">85.98 ± 0.41 / 87.49 ± 0.35</td> <!-- DaNE -->
    <td class="da pos">98.49 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">69.19 ± 0.91</td> <!-- AngryTweets -->
    <td class="da clf">67.07 ± 0.44</td> <!-- TwitterSent -->
    <td class="da clf">50.66 ± 4.65</td> <!-- Europarl -->
    <td class="da clf">42.12 ± 4.45</td> <!-- LCC -->
    <td class="da clf">77.92 ± 0.92</td> <!-- DKHate -->
    <td class="no ner">91.88 ± 0.15 / 92.30 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">90.63 ± 0.16 / 93.25 ± 0.11</td> <!-- NorNE-NN -->
    <td class="no pos">98.78 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.55 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">63.44 ± 3.51</td> <!-- NoReC -->
    <td class="no clf">68.29 ± 0.66</td> <!-- NorDial -->
    <td class="sv ner">88.07 ± 0.11 / 90.63 ± 0.11</td> <!-- SUC3 -->
    <td class="sv pos">98.95 ± 0.01</td> <!-- SDT-POS -->
    <td class="sv dep">74.41 ± 0.84 / 76.01 ± 0.86</td> <!-- SDT-DEP -->
    <td class="sv clf">34.03 ± 0.26</td> <!-- DaLaJ -->
    <td class="sv clf">54.05 ± 0.87</td> <!-- ABSAbank-Imm -->
    <td class="is ner">90.64 ± 0.16</td> <!-- WikiANN-IS -->
    <td class="is pos">99.45 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">56.63 ± 0.27</td> <!-- NoReC-IS -->
    <td class="fo ner">91.09 ± 0.11</td> <!-- WikiANN-FO -->
    <td class="fo pos">98.26 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">47.89 ± 0.94 / 49.53 ± 0.93</td> <!-- FDT-DEP -->
    <td class="fo clf">35.81 ± 2.55</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>bert-base-multilingual-cased</td> <!-- Model ID -->
    <td class="size">681</td> <!-- Model size -->
    <td class="speed">4.11 ± 0.11</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.71 ± 0.26 / 83.91 ± 0.29</td> <!-- DaNE -->
    <td class="da pos">97.38 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">58.61 ± 0.56</td> <!-- AngryTweets -->
    <td class="da clf">50.63 ± 0.69</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 2.03</td> <!-- Europarl -->
    <td class="da clf">56.44 ± 0.89</td> <!-- LCC -->
    <td class="da clf">69.46 ± 0.72</td> <!-- DKHate -->
    <td class="no ner">86.93 ± 0.19 / 88.22 ± 0.18</td> <!-- NorNE-NB -->
    <td class="no ner">88.07 ± 0.18 / 90.82 ± 0.17</td> <!-- NorNE-NN -->
    <td class="no pos">98.25 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.03 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep">84.30 ± 0.05 / 86.33 ± 0.05</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">62.48 ± 0.27</td> <!-- NoReC -->
    <td class="no clf">67.65 ± 0.96</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">98.01 ± 0.03</td> <!-- SDT-POS -->
    <td class="sv dep">67.09 ± 0.49 / 69.57 ± 0.48</td> <!-- SDT-DEP -->
    <td class="sv clf">48.27 ± 0.79</td> <!-- DaLaJ -->
    <td class="sv clf">47.01 ± 0.49</td> <!-- ABSAbank-Imm -->
    <td class="is ner">90.04 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">99.27 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">52.67 ± 0.65</td> <!-- NoReC-IS -->
    <td class="fo ner">90.39 ± 0.22</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.67 ± 0.05</td> <!-- FDT-POS -->
    <td class="fo dep">46.37 ± 0.44 / 48.64 ± 0.43</td> <!-- FDT-DEP -->
    <td class="fo clf">45.07 ± 0.36</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>distilbert-base-multilingual-cased</td> <!-- Model ID -->
    <td class="size">517</td> <!-- Model size -->
    <td class="speed">8.29 ± 0.28</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.24 ± 0.35 / 83.51 ± 0.34</td> <!-- DaNE -->
    <td class="da pos">96.87 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">55.27 ± 0.33</td> <!-- AngryTweets -->
    <td class="da clf">35.77 ± 1.24</td> <!-- TwitterSent -->
    <td class="da clf">38.20 ± 1.21</td> <!-- Europarl -->
    <td class="da clf">55.61 ± 1.03</td> <!-- LCC -->
    <td class="da clf">72.95 ± 1.09</td> <!-- DKHate -->
    <td class="no ner">82.57 ± 0.16 / 84.47 ± 0.15</td> <!-- NorNE-NB -->
    <td class="no ner">83.23 ± 0.29 / 86.74 ± 0.21</td> <!-- NorNE-NN -->
    <td class="no pos">97.81 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.52 ± 0.04</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">54.25 ± 0.55</td> <!-- NoReC -->
    <td class="no clf">67.53 ± 0.54</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">97.25 ± 0.04</td> <!-- SDT-POS -->
    <td class="sv dep">60.97 ± 0.25 / 64.07 ± 0.26</td> <!-- SDT-DEP -->
    <td class="sv clf">47.59 ± 0.47</td> <!-- DaLaJ -->
    <td class="sv clf">46.56 ± 0.50</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.94 ± 0.10</td> <!-- WikiANN-IS -->
    <td class="is pos">99.13 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">48.69 ± 1.06</td> <!-- NoReC-IS -->
    <td class="fo ner">88.91 ± 0.17</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.73 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">41.22 ± 0.37 / 43.60 ± 0.38</td> <!-- FDT-DEP -->
    <td class="fo clf">41.14 ± 0.60</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>cardiffnlp/twitter-xlm-roberta-base</td> <!-- Model ID -->
    <td class="size">1040</td> <!-- Model size -->
    <td class="speed">3.91 ± 0.12</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">79.15 ± 0.29 / 81.48 ± 0.31</td> <!-- DaNE -->
    <td class="da pos">97.97 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep">67.58 ± 0.29 / 69.89 ± 0.29</td> <!-- DDT-DEP -->
    <td class="da clf">65.39 ± 0.29</td> <!-- AngryTweets -->
    <td class="da clf">55.03 ± 0.53</td> <!-- TwitterSent -->
    <td class="da clf">67.67 ± 0.93</td> <!-- Europarl -->
    <td class="da clf">67.69 ± 1.18</td> <!-- LCC -->
    <td class="da clf">71.80 ± 0.71</td> <!-- DKHate -->
    <td class="no ner">88.57 ± 0.15 / 89.71 ± 0.14</td> <!-- NorNE-NB -->
    <td class="no ner">86.11 ± 0.25 / 89.73 ± 0.15</td> <!-- NorNE-NN -->
    <td class="no pos">98.43 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.11 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">67.20 ± 0.32</td> <!-- NoReC -->
    <td class="no clf">66.24 ± 0.47</td> <!-- NorDial -->
    <td class="sv ner">85.34 ± 0.07 / 88.74 ± 0.07</td> <!-- SUC3 -->
    <td class="sv pos">98.53 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">72.91 ± 0.20 / 74.93 ± 0.20</td> <!-- SDT-DEP -->
    <td class="sv clf">46.19 ± 1.17</td> <!-- DaLaJ -->
    <td class="sv clf">34.64 ± 0.74</td> <!-- ABSAbank-Imm -->
    <td class="is ner">88.55 ± 0.14</td> <!-- WikiANN-IS -->
    <td class="is pos">99.38 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">49.10 ± 0.24</td> <!-- NoReC-IS -->
    <td class="fo ner">88.70 ± 0.17</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.43 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">51.23 ± 0.41 / 53.62 ± 0.41</td> <!-- FDT-DEP -->
    <td class="fo clf">46.43 ± 0.83</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-en-da-cased</td> <!-- Model ID -->
    <td class="size">424</td> <!-- Model size -->
    <td class="speed">4.16 ± 0.14</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">83.73 ± 0.29 / 86.41 ± 0.25</td> <!-- DaNE -->
    <td class="da pos">97.36 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep">61.89 ± 0.20 / 64.39 ± 0.20</td> <!-- DDT-DEP -->
    <td class="da clf">56.73 ± 0.45</td> <!-- AngryTweets -->
    <td class="da clf">51.16 ± 0.42</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 2.12</td> <!-- Europarl -->
    <td class="da clf">54.04 ± 0.88</td> <!-- LCC -->
    <td class="da clf">63.65 ± 1.29</td> <!-- DKHate -->
    <td class="no ner">86.19 ± 0.15 / 87.76 ± 0.13</td> <!-- NorNE-NB -->
    <td class="no ner">86.74 ± 0.20 / 89.79 ± 0.17</td> <!-- NorNE-NN -->
    <td class="no pos">98.15 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.05 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">62.44 ± 0.26</td> <!-- NoReC -->
    <td class="no clf">72.99 ± 1.46</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">46.87 ± 0.43</td> <!-- DaLaJ -->
    <td class="sv clf">47.93 ± 0.42</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.19 ± 0.14</td> <!-- WikiANN-IS -->
    <td class="is pos">99.21 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">49.54 ± 0.28</td> <!-- NoReC-IS -->
    <td class="fo ner">90.45 ± 0.11</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.30 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">46.95 ± 0.47 / 49.25 ± 0.48</td> <!-- FDT-DEP -->
    <td class="fo clf">41.70 ± 0.39</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-25lang-cased</td> <!-- Model ID -->
    <td class="size">578</td> <!-- Model size -->
    <td class="speed">4.21 ± 0.13</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.87 ± 0.36 / 84.11 ± 0.40</td> <!-- DaNE -->
    <td class="da pos">97.46 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">57.43 ± 0.60</td> <!-- AngryTweets -->
    <td class="da clf">49.73 ± 0.73</td> <!-- TwitterSent -->
    <td class="da clf">54.04 ± 0.88</td> <!-- Europarl -->
    <td class="da clf">49.78 ± 0.82</td> <!-- LCC -->
    <td class="da clf">67.19 ± 0.85</td> <!-- DKHate -->
    <td class="no ner">88.02 ± 0.12 / 89.15 ± 0.12</td> <!-- NorNE-NB -->
    <td class="no ner">86.32 ± 0.28 / 89.03 ± 0.24</td> <!-- NorNE-NN -->
    <td class="no pos">98.24 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.03 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep">80.35 ± 0.21 / 82.82 ± 0.20</td> <!-- NDT-NN-DEP -->
    <td class="no clf">62.97 ± 0.29</td> <!-- NoReC -->
    <td class="no clf">70.33 ± 1.59</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">45.02 ± 0.50</td> <!-- DaLaJ -->
    <td class="sv clf">47.82 ± 0.46</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.55 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">99.22 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">44.78 ± 1.11</td> <!-- NoReC-IS -->
    <td class="fo ner">90.50 ± 0.14</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.47 ± 0.03</td> <!-- FDT-POS -->
    <td class="fo dep">47.52 ± 0.33 / 49.57 ± 0.34</td> <!-- FDT-DEP -->
    <td class="fo clf">43.65 ± 0.20</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
    <td class="size">451</td> <!-- Model size -->
    <td class="speed">4.13 ± 0.17</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">80.89 ± 0.42 / 83.33 ± 0.35</td> <!-- DaNE -->
    <td class="da pos">97.21 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">57.96 ± 0.54</td> <!-- AngryTweets -->
    <td class="da clf">49.34 ± 0.49</td> <!-- TwitterSent -->
    <td class="da clf">22.73 ± 1.88</td> <!-- Europarl -->
    <td class="da clf">53.72 ± 1.05</td> <!-- LCC -->
    <td class="da clf">65.85 ± 0.87</td> <!-- DKHate -->
    <td class="no ner">86.80 ± 0.27 / 88.42 ± 0.20</td> <!-- NorNE-NB -->
    <td class="no ner">86.17 ± 0.12 / 89.40 ± 0.15</td> <!-- NorNE-NN -->
    <td class="no pos">98.21 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.05 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">64.61 ± 0.37</td> <!-- NoReC -->
    <td class="no clf">74.97 ± 1.34</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">46.55 ± 0.36</td> <!-- DaLaJ -->
    <td class="sv clf">45.34 ± 0.47</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.12 ± 0.11</td> <!-- WikiANN-IS -->
    <td class="is pos">99.20 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">40.66 ± 0.70</td> <!-- NoReC-IS -->
    <td class="fo ner">90.35 ± 0.16</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.83 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">47.75 ± 0.38 / 49.79 ± 0.38</td> <!-- FDT-DEP -->
    <td class="fo clf">46.52 ± 0.45</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-25lang-cased</td> <!-- Model ID -->
    <td class="size">415</td> <!-- Model size -->
    <td class="speed">8.22 ± 0.42</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">81.23 ± 0.36 / 83.28 ± 0.35</td> <!-- DaNE -->
    <td class="da pos">96.68 ± 0.07</td> <!-- DDT-POS -->
    <td class="da dep">55.91 ± 0.31 / 58.84 ± 0.31</td> <!-- DDT-DEP -->
    <td class="da clf">52.90 ± 0.31</td> <!-- AngryTweets -->
    <td class="da clf">45.72 ± 0.57</td> <!-- TwitterSent -->
    <td class="da clf">56.26 ± 0.85</td> <!-- Europarl -->
    <td class="da clf">45.45 ± 0.89</td> <!-- LCC -->
    <td class="da clf">67.78 ± 1.37</td> <!-- DKHate -->
    <td class="no ner">83.89 ± 0.25 / 85.67 ± 0.27</td> <!-- NorNE-NB -->
    <td class="no ner">84.81 ± 0.23 / 88.09 ± 0.19</td> <!-- NorNE-NN -->
    <td class="no pos">97.81 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.54 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">55.33 ± 0.51</td> <!-- NoReC -->
    <td class="no clf">73.66 ± 1.40</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">47.74 ± 0.31</td> <!-- DaLaJ -->
    <td class="sv clf">49.64 ± 0.38</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.76 ± 0.12</td> <!-- WikiANN-IS -->
    <td class="is pos">99.09 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">49.50 ± 0.29</td> <!-- NoReC-IS -->
    <td class="fo ner">89.16 ± 0.13</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.99 ± 0.05</td> <!-- FDT-POS -->
    <td class="fo dep">40.24 ± 0.40 / 42.63 ± 0.42</td> <!-- FDT-DEP -->
    <td class="fo clf">30.02 ± 0.24</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-en-fr-de-no-da-cased</td> <!-- Model ID -->
    <td class="size">288</td> <!-- Model size -->
    <td class="speed">8.40 ± 0.34</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">79.12 ± 0.49 / 81.49 ± 0.51</td> <!-- DaNE -->
    <td class="da pos">96.83 ± 0.03</td> <!-- DDT-POS -->
    <td class="da dep">54.67 ± 0.30 / 57.54 ± 0.31</td> <!-- DDT-DEP -->
    <td class="da clf">55.90 ± 0.36</td> <!-- AngryTweets -->
    <td class="da clf">46.09 ± 0.71</td> <!-- TwitterSent -->
    <td class="da clf">36.83 ± 1.10</td> <!-- Europarl -->
    <td class="da clf">38.31 ± 1.28</td> <!-- LCC -->
    <td class="da clf">67.79 ± 0.94</td> <!-- DKHate -->
    <td class="no ner">81.87 ± 0.23 / 83.94 ± 0.23</td> <!-- NorNE-NB -->
    <td class="no ner">83.06 ± 0.25 / 86.77 ± 0.21</td> <!-- NorNE-NN -->
    <td class="no pos">97.79 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.57 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">55.86 ± 0.59</td> <!-- NoReC -->
    <td class="no clf">67.32 ± 0.38</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">48.10 ± 0.38</td> <!-- DaLaJ -->
    <td class="sv clf">48.25 ± 0.57</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.66 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">99.00 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">36.33 ± 0.89</td> <!-- NoReC-IS -->
    <td class="fo ner">89.67 ± 0.12</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.73 ± 0.06</td> <!-- FDT-POS -->
    <td class="fo dep">43.24 ± 0.32 / 45.72 ± 0.32</td> <!-- FDT-DEP -->
    <td class="fo clf">47.48 ± 0.79</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/bert-base-en-no-cased</td> <!-- Model ID -->
    <td class="size">425</td> <!-- Model size -->
    <td class="speed">4.11 ± 0.14</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">82.55 ± 0.45 / 85.83 ± 0.36</td> <!-- DaNE -->
    <td class="da pos">97.25 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep">59.86 ± 0.30 / 62.61 ± 0.29</td> <!-- DDT-DEP -->
    <td class="da clf">58.47 ± 0.40</td> <!-- AngryTweets -->
    <td class="da clf">50.03 ± 0.56</td> <!-- TwitterSent -->
    <td class="da clf">22.53 ± 2.05</td> <!-- Europarl -->
    <td class="da clf">50.65 ± 0.76</td> <!-- LCC -->
    <td class="da clf">67.40 ± 0.99</td> <!-- DKHate -->
    <td class="no ner">87.90 ± 0.16 / 89.17 ± 0.16</td> <!-- NorNE-NB -->
    <td class="no ner">88.18 ± 0.23 / 91.19 ± 0.19</td> <!-- NorNE-NN -->
    <td class="no pos">98.28 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">98.01 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">63.64 ± 0.29</td> <!-- NoReC -->
    <td class="no clf">67.17 ± 1.15</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">46.25 ± 0.79</td> <!-- DaLaJ -->
    <td class="sv clf">49.62 ± 0.38</td> <!-- ABSAbank-Imm -->
    <td class="is ner">89.36 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">99.06 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">40.16 ± 0.62</td> <!-- NoReC-IS -->
    <td class="fo ner">89.05 ± 0.23</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.39 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">48.27 ± 0.53 / 50.55 ± 0.54</td> <!-- FDT-DEP -->
    <td class="fo clf">47.04 ± 0.34</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-en-no-cased</td> <!-- Model ID -->
    <td class="size">263</td> <!-- Model size -->
    <td class="speed">8.25 ± 0.33</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">77.16 ± 0.54 / 79.64 ± 0.54</td> <!-- DaNE -->
    <td class="da pos">96.71 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">53.93 ± 0.47</td> <!-- AngryTweets -->
    <td class="da clf">45.71 ± 1.17</td> <!-- TwitterSent -->
    <td class="da clf">35.70 ± 1.30</td> <!-- Europarl -->
    <td class="da clf">38.24 ± 2.38</td> <!-- LCC -->
    <td class="da clf">71.04 ± 0.56</td> <!-- DKHate -->
    <td class="no ner">82.05 ± 0.21 / 84.09 ± 0.21</td> <!-- NorNE-NB -->
    <td class="no ner">84.19 ± 0.28 / 87.81 ± 0.23</td> <!-- NorNE-NN -->
    <td class="no pos">97.83 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.56 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">57.58 ± 0.60</td> <!-- NoReC -->
    <td class="no clf">67.21 ± 0.54</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">47.25 ± 0.38</td> <!-- DaLaJ -->
    <td class="sv clf">47.72 ± 0.37</td> <!-- ABSAbank-Imm -->
    <td class="is ner">87.15 ± 0.11</td> <!-- WikiANN-IS -->
    <td class="is pos">98.90 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">40.85 ± 0.31</td> <!-- NoReC-IS -->
    <td class="fo ner">89.10 ± 0.16</td> <!-- WikiANN-FO -->
    <td class="fo pos">96.95 ± 0.04</td> <!-- FDT-POS -->
    <td class="fo dep">40.88 ± 0.43 / 43.26 ± 0.43</td> <!-- FDT-DEP -->
    <td class="fo clf">44.39 ± 0.59</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>Geotrend/distilbert-base-en-da-cased</td> <!-- Model ID -->
    <td class="size">262</td> <!-- Model size -->
    <td class="speed">8.35 ± 0.39</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">80.18 ± 0.40 / 82.02 ± 0.42</td> <!-- DaNE -->
    <td class="da pos">96.72 ± 0.05</td> <!-- DDT-POS -->
    <td class="da dep">55.99 ± 0.27 / 58.92 ± 0.28</td> <!-- DDT-DEP -->
    <td class="da clf">55.24 ± 0.48</td> <!-- AngryTweets -->
    <td class="da clf">42.49 ± 0.53</td> <!-- TwitterSent -->
    <td class="da clf">41.29 ± 1.31</td> <!-- Europarl -->
    <td class="da clf">39.43 ± 1.62</td> <!-- LCC -->
    <td class="da clf">67.34 ± 0.91</td> <!-- DKHate -->
    <td class="no ner">80.46 ± 0.31 / 82.47 ± 0.26</td> <!-- NorNE-NB -->
    <td class="no ner">83.60 ± 0.27 / 86.67 ± 0.23</td> <!-- NorNE-NN -->
    <td class="no pos">97.73 ± 0.02</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.54 ± 0.03</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">56.33 ± 0.40</td> <!-- NoReC -->
    <td class="no clf">74.07 ± 1.01</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos"></td> <!-- SDT-POS -->
    <td class="sv dep"></td> <!-- SDT-DEP -->
    <td class="sv clf">34.30 ± 0.68</td> <!-- DaLaJ -->
    <td class="sv clf">46.37 ± 0.44</td> <!-- ABSAbank-Imm -->
    <td class="is ner">86.94 ± 0.12</td> <!-- WikiANN-IS -->
    <td class="is pos">99.08 ± 0.02</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">46.88 ± 0.15</td> <!-- NoReC-IS -->
    <td class="fo ner">89.90 ± 0.13</td> <!-- WikiANN-FO -->
    <td class="fo pos">97.01 ± 0.05</td> <!-- FDT-POS -->
    <td class="fo dep">42.44 ± 0.36 / 44.96 ± 0.37</td> <!-- FDT-DEP -->
    <td class="fo clf">41.63 ± 0.46</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>sarnikowski/convbert-medium-small-da-cased</td> <!-- Model ID -->
    <td class="size">94</td> <!-- Model size -->
    <td class="speed">11.52 ± 0.43</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">78.89 ± 0.59 / 81.62 ± 0.56</td> <!-- DaNE -->
    <td class="da pos">97.85 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep">57.47 ± 0.49 / 60.10 ± 0.49</td> <!-- DDT-DEP -->
    <td class="da clf">62.05 ± 0.32</td> <!-- AngryTweets -->
    <td class="da clf">51.83 ± 0.36</td> <!-- TwitterSent -->
    <td class="da clf">55.58 ± 1.70</td> <!-- Europarl -->
    <td class="da clf">63.00 ± 0.88</td> <!-- LCC -->
    <td class="da clf">70.98 ± 0.71</td> <!-- DKHate -->
    <td class="no ner">82.56 ± 0.21 / 84.46 ± 0.19</td> <!-- NorNE-NB -->
    <td class="no ner">76.86 ± 0.25 / 80.40 ± 0.27</td> <!-- NorNE-NN -->
    <td class="no pos">97.81 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.45 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">61.32 ± 0.30</td> <!-- NoReC -->
    <td class="no clf">64.94 ± 0.54</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">91.44 ± 0.05</td> <!-- SDT-POS -->
    <td class="sv dep">43.46 ± 0.10 / 47.95 ± 0.11</td> <!-- SDT-DEP -->
    <td class="sv clf">40.69 ± 0.53</td> <!-- DaLaJ -->
    <td class="sv clf">44.44 ± 0.54</td> <!-- ABSAbank-Imm -->
    <td class="is ner">68.10 ± 0.15</td> <!-- WikiANN-IS -->
    <td class="is pos">91.15 ± 0.10</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">43.75 ± 1.14</td> <!-- NoReC-IS -->
    <td class="fo ner">79.08 ± 0.15</td> <!-- WikiANN-FO -->
    <td class="fo pos">84.06 ± 0.10</td> <!-- FDT-POS -->
    <td class="fo dep">31.00 ± 0.34 / 35.01 ± 0.35</td> <!-- FDT-DEP -->
    <td class="fo clf">40.56 ± 0.82</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>sarnikowski/convbert-small-da-cased</td> <!-- Model ID -->
    <td class="size">50</td> <!-- Model size -->
    <td class="speed">18.62 ± 1.20</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">75.17 ± 0.44 / 77.59 ± 0.53</td> <!-- DaNE -->
    <td class="da pos">97.63 ± 0.02</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">60.72 ± 0.28</td> <!-- AngryTweets -->
    <td class="da clf">45.40 ± 0.35</td> <!-- TwitterSent -->
    <td class="da clf">42.15 ± 2.21</td> <!-- Europarl -->
    <td class="da clf">54.51 ± 0.69</td> <!-- LCC -->
    <td class="da clf">72.36 ± 0.61</td> <!-- DKHate -->
    <td class="no ner">79.48 ± 0.23 / 81.52 ± 0.22</td> <!-- NorNE-NB -->
    <td class="no ner">75.73 ± 0.34 / 79.22 ± 0.31</td> <!-- NorNE-NN -->
    <td class="no pos">97.54 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">97.15 ± 0.02</td> <!-- NDT-NN-POS -->
    <td class="no dep">72.15 ± 0.53 / 75.04 ± 0.51</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">46.62 ± 0.19</td> <!-- NoReC -->
    <td class="no clf">64.23 ± 0.54</td> <!-- NorDial -->
    <td class="sv ner"></td> <!-- SUC3 -->
    <td class="sv pos">90.55 ± 0.05</td> <!-- SDT-POS -->
    <td class="sv dep">42.09 ± 0.13 / 46.88 ± 0.12</td> <!-- SDT-DEP -->
    <td class="sv clf">40.00 ± 0.59</td> <!-- DaLaJ -->
    <td class="sv clf">43.73 ± 0.84</td> <!-- ABSAbank-Imm -->
    <td class="is ner">69.03 ± 0.19</td> <!-- WikiANN-IS -->
    <td class="is pos">90.69 ± 0.11</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">41.29 ± 1.01</td> <!-- NoReC-IS -->
    <td class="fo ner">78.15 ± 0.28</td> <!-- WikiANN-FO -->
    <td class="fo pos">84.54 ± 0.10</td> <!-- FDT-POS -->
    <td class="fo dep">27.97 ± 0.33 / 31.87 ± 0.37</td> <!-- FDT-DEP -->
    <td class="fo clf">35.59 ± 0.26</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>birgermoell/roberta-swedish-scandi</td> <!-- Model ID -->
    <td class="size">476</td> <!-- Model size -->
    <td class="speed">4.12 ± 0.13</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">73.92 ± 0.44 / 76.76 ± 0.40</td> <!-- DaNE -->
    <td class="da pos">96.54 ± 0.04</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">52.72 ± 0.32</td> <!-- AngryTweets -->
    <td class="da clf">49.10 ± 1.59</td> <!-- TwitterSent -->
    <td class="da clf">22.01 ± 0.19</td> <!-- Europarl -->
    <td class="da clf">45.33 ± 1.32</td> <!-- LCC -->
    <td class="da clf">65.66 ± 0.90</td> <!-- DKHate -->
    <td class="no ner">78.65 ± 0.20 / 79.96 ± 0.23</td> <!-- NorNE-NB -->
    <td class="no ner">77.93 ± 0.28 / 81.75 ± 0.27</td> <!-- NorNE-NN -->
    <td class="no pos">97.88 ± 0.03</td> <!-- NDT-NB-POS -->
    <td class="no pos">96.99 ± 0.04</td> <!-- NDT-NN-POS -->
    <td class="no dep"></td> <!-- NDT-NB-DEP -->
    <td class="no dep">79.13 ± 0.09 / 82.42 ± 0.08</td> <!-- NDT-NN-DEP -->
    <td class="no clf">45.58 ± 0.91</td> <!-- NoReC -->
    <td class="no clf">68.27 ± 1.00</td> <!-- NorDial -->
    <td class="sv ner">85.15 ± 0.05 / 88.35 ± 0.04</td> <!-- SUC3 -->
    <td class="sv pos">98.26 ± 0.02</td> <!-- SDT-POS -->
    <td class="sv dep">68.61 ± 0.18 / 71.47 ± 0.16</td> <!-- SDT-DEP -->
    <td class="sv clf">49.41 ± 0.27</td> <!-- DaLaJ -->
    <td class="sv clf">49.26 ± 0.22</td> <!-- ABSAbank-Imm -->
    <td class="is ner">82.53 ± 0.18</td> <!-- WikiANN-IS -->
    <td class="is pos">98.40 ± 0.05</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">47.56 ± 0.25</td> <!-- NoReC-IS -->
    <td class="fo ner">85.38 ± 0.19</td> <!-- WikiANN-FO -->
    <td class="fo pos">95.28 ± 0.08</td> <!-- FDT-POS -->
    <td class="fo dep">32.99 ± 0.34 / 36.30 ± 0.35</td> <!-- FDT-DEP -->
    <td class="fo clf">39.25 ± 0.16</td> <!-- NoReC-FO -->
   </tr>
   <tr>
    <td>random-roberta</td> <!-- Model ID -->
    <td class="size">478</td> <!-- Model size -->
    <td class="speed">3.83 ± 0.13</td> <!-- Inference speed -->
    <td class="score"></td> <!-- ScandEval score -->
    <td class="da-score"></td> <!-- Danish score -->
    <td class="no-score"></td> <!-- Norwegian score -->
    <td class="sv-score"></td> <!-- Swedish score -->
    <td class="is-score"></td> <!-- Icelandic score -->
    <td class="fo-score"></td> <!-- Faroese score -->
    <td class="ner-score"></td> <!-- Mean NER score -->
    <td class="pos-score"></td> <!-- Mean POS score -->
    <td class="dep-score"></td> <!-- Mean dependency parsing score -->
    <td class="clf-score"></td> <!-- Mean classification score -->
    <td class="da ner">32.65 ± 0.30 / 30.70 ± 0.33</td> <!-- DaNE -->
    <td class="da pos">81.92 ± 0.09</td> <!-- DDT-POS -->
    <td class="da dep"></td> <!-- DDT-DEP -->
    <td class="da clf">38.77 ± 0.18</td> <!-- AngryTweets -->
    <td class="da clf">22.93 ± 0.16</td> <!-- TwitterSent -->
    <td class="da clf">21.96 ± 0.16</td> <!-- Europarl -->
    <td class="da clf">23.80 ± 0.25</td> <!-- LCC -->
    <td class="da clf">46.94 ± 0.05</td> <!-- DKHate -->
    <td class="no ner">48.36 ± 0.20 / 52.13 ± 0.18</td> <!-- NorNE-NB -->
    <td class="no ner">42.55 ± 0.26 / 45.53 ± 0.24</td> <!-- NorNE-NN -->
    <td class="no pos">93.31 ± 0.05</td> <!-- NDT-NB-POS -->
    <td class="no pos">91.64 ± 0.10</td> <!-- NDT-NN-POS -->
    <td class="no dep">59.44 ± 0.10 / 64.07 ± 0.10</td> <!-- NDT-NB-DEP -->
    <td class="no dep"></td> <!-- NDT-NN-DEP -->
    <td class="no clf">39.07 ± 0.49</td> <!-- NoReC -->
    <td class="no clf">52.94 ± 2.74</td> <!-- NorDial -->
    <td class="sv ner">56.13 ± 0.84 / 59.51 ± 0.94</td> <!-- SUC3 -->
    <td class="sv pos">81.88 ± 0.06</td> <!-- SDT-POS -->
    <td class="sv dep">23.21 ± 0.17 / 28.43 ± 0.17</td> <!-- SDT-DEP -->
    <td class="sv clf">33.17 ± 0.12</td> <!-- DaLaJ -->
    <td class="sv clf">29.03 ± 0.69</td> <!-- ABSAbank-Imm -->
    <td class="is ner">63.44 ± 0.13</td> <!-- WikiANN-IS -->
    <td class="is pos">95.71 ± 0.07</td> <!-- IDT-POS -->
    <td class="is dep"></td> <!-- IDT-DEP -->
    <td class="is clf">38.68 ± 0.35</td> <!-- NoReC-IS -->
    <td class="fo ner">70.74 ± 0.31</td> <!-- WikiANN-FO -->
    <td class="fo pos">85.33 ± 0.09</td> <!-- FDT-POS -->
    <td class="fo dep">18.58 ± 0.19 / 22.14 ± 0.20</td> <!-- FDT-DEP -->
    <td class="fo clf">38.67 ± 0.21</td> <!-- NoReC-FO -->
   </tr>
 </tbody>
</table>
</div>