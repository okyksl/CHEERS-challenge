{% include math.html %}

# Welcome

The aim of the CHEERS challenge is to exploit the latest advances in Natural Language Processing (NLP) to assist responders and analysts in humanitarian crises for analyzing and harvesting valuable information from data. The challenge is hosted by Data Friendly Space (DFS), a non-profit organization, and is also supported by the academic researchers at the Johannes Kepler University Linz. We encourages anyone who is interested in advancing the applications of NLP and Deep/Machine Learning in the humanitarian sector to take part in this challenge, as the benefits would be immediately seen in helping to increase the quality of the humanitarian community’s data analysis. As such, humanitarian analysts would be able to spend time doing what the human mind does best: subjective analysis of information.

<h2>Table of contents</h2>
<ul>
    <a href="#section-background"><li style="font-size:large;font-weight:bold">Context and Background</li></a>
    <ul>
        <a href="#section-background-dfs"><li style="font-size:large;font-weight:bold">Who is Data Friendly Space?</li></a>
        <a href="#section-background-deep"><li style="font-size:large;font-weight:bold">Product: DEEP Platform</li></a>
        <a href="#section-background-nlp"><li style="font-size:large;font-weight:bold">How can NLP help in humanitarian crises?</li></a>
    </ul>
    <a href="#section-cheers"><li style="font-size:large;font-weight:bold">CHEERS Challenge</li></a>
    <ul>
        <a href="#section-cheers-round1"><li style="font-size:large;font-weight:bold">Round 1: Extraction and Classification of Humanitarian Data</li></a>
    </ul>
    <a href="#section-terms"><li style="font-size:large;font-weight:bold">Terms and Conditions</li></a>
    <a href="#section-contact"><li style="font-size:large;font-weight:bold">Contact Us</li></a>
</ul>

# <a name="section-background"></a>Context and Background

## <a name="section-background-dfs"></a>Who is Data Friendly Space?
<img src="resources/dfs.png" alt="Deep Logo" width="150"/>

Data Friendly Space (DFS) is a non-profit organization based in the United States with a global presence. DFS’ guiding principle is to improve information management and analysis capacity, tools and processes in the humanitarian and development community to enable better informed and more targeted assistance. DFS staff is composed of experts from the humanitarian information management and analysis field who specialize in real time secondary data review and build humanitarian applications that support fast extraction of information from large volumes of unstructured data.

DFS also focuses on creation of data centric web applications, websites and mobile applications to support humanitarian organizations. When building software, DFS focuses on the intersection between data automation processes powered by Artificial Intelligences and human knowledge and skills, in particular when one can help the other to execute analysis. More information on Data Friendly Space and its projects can be found [here](https://datafriendlyspace.org/).

## <a name="section-background-deep"></a>Product: DEEP Platform
<img src="resources/thedeep.png" alt="Deep Logo" width="150"/>

DFS is the technical host of the Data Entry and Exploration Platform (DEEP, [thedeep.io](https://www.thedeep.io/)), a tool used by humanitarians all over the world to monitor and assess crises. The DEEP project provides effective solutions to analyze and harvest data from secondary sources such as news articles, social media, and reports that are used by responders and analysts in humanitarian crises. During crises, rapidly identifying important information from the constantly-increasing data is crucial to understand the needs of affected populations and to improve evidence-based decision making. The DEEP has been used by many organizations in multiple crisis contexts, such as:
* The [monitoring of the impact of cyclone Idai and Kenneht in Mozambique, Malawi and Zimbabwe](https://media.ifrc.org/wp-content/uploads/sites/5/2019/07/201907-MOZ-MovementHandOut.pdf) by the Red Cross and Red Crescent Movement
* The [UNHCR Coordination Platform](https://r4v.info/en/situations/platform) for Refugees and Migrants from Venezuela
* The ACAPS secondary data review of the Rohingya influx in Bangladesh
* The [IMMAP/DFS Situation Analysis of the impacts of COVID in Syria](https://reliefweb.int/report/syrian-arab-republic/syria-immapdfs-covid-19-situation-analysis-january-2021)


The aim of the DEEP platform is to provide insights from years of historical and in-crisis humanitarian text data. The platform allows users to upload documents and classify text snippets according to predefined humanitarian target labels, grouped into and referred to as analytical frameworks. Tagging this data leads to the structuring of large volumes of information that enables effective analysis of the humanitarian conditions of the populations of interest and empowers humanitarians to identify information gaps and to provide sound recommendations in terms of needs assessment strategies and response plans. DEEP supports global operations of a range of international humanitarian organizations and the United Nations.

More information on the DEEP and how it is being used can be found here:
*	[DEEP Website](https://www.thedeep.io/)
*	[DEEP YouTube channel](https://www.youtube.com/channel/UCO3naDryeQIFny6BsEJwCaA)
*	[IFRC tutorial for conducting Needs Assessments with DEEP](https://deephelp.zendesk.com/hc/en-us/articles/360041904812-4-DEEP-Using-the-DEEP-Platform-)


## <a name="section-background-nlp"></a>How can NLP help in humanitarian crises?

The day-to-day workload of analysts and experts with DEEP concerns manual tagging of secondary data resources. These experts have extensive domain knowledge to understand how to use the analytical framework with its different taxonomies in order to assign the right labels to the right text snippets. Below, you can see the interface of the DFS/IMMAP analytical framework, where the experts are asked to assign appropriate classes to a text snippet.

<center><img src="resources/analytical_framework.png" alt="Analytical Framework" width="400"/></center>

This process of selecting informative text excerpts from documents, and assigning correct tags is highly laborious and time consuming, while time is the decisive factor during humanitarian crises. The innovation of the DEEP relies upon leveraging recent advances in NLP to automate this process. 


# <a name="section-cheers"></a> CHEERS Challenge

## <a name="section-cheers-round1"></a> Round 1: Extraction and Classification of Humanitarian Data

In this round, we simulate the document processing procedure of analysts. In particular, given a document consisting of a number of sentences, a system is asked to:
- First, **extract informative and relevant sentences**, and ...
- Second, **classify the extracted sentences** according to the Sectoral Information.

In the following, we first explain the dataset and task, and then describe the run file format and evaluation metrics. 

### Dataset

The dataset of this round is available [here](https://deep-cheers-challenge.s3.amazonaws.com/data_round_1.zip). The dataset consists of the following files:

    data_round_1/
      documents_train_en.csv
      documents_val_en.csv
      documents_test_en.csv
      sentences_train_en.csv
      sentences_val_en.csv
      sentences_test_en.csv
      immap_sector_name_to_id.json
      Terms of Use.txt
      
The primary data for the challenge is available in the `sentences_<split>_en.csv` files, containing the information of sentences of the document. Each of these files contain the following columns: 

- `doc_id`: The identifier of the document, from which the sentence is extracted.
- `sentence_id`: The identifier of the sentence. Combined with the corresponding `doc_id`, `sentence_id` and `doc_id` form a unique id for each sentence.
- `sentence_text`: Text of the sentence.
- `is_relevant`: Determines whether the sentence is relevant (1) or not (0) to the information need of the analyst.
- `sector_ids`: A list of sector ids, to which this sentence belongs to. If the sentence is not assigned to any sector, the list is empty. Note that a sentence maybe relevant (`is_relevant=1`) but have an empty `sector_ids` list. However a non-relevant sentence (`is_relevant=0`) always has an empty `sector_ids` list.


As mentioned above, each sentence is classified by data analysts as relevant or irrelevant (`0` or `1` in the `is_relevant` column). If a sentence is marked as relevant (i.e. `is_relevant` column is `1`) the `sector_ids` column *may* contain a list of sector ids that this sentence belongs to. Otherwise, the `sector_ids` column is an empty list. The label columns (`is_relevant` and `sector_ids`) are provided only for the train and validation splits of the data. The corresponding name of each sector is available in `immap_sector_name_to_id.json`.

In addition, in the `documents_<split>_en.csv` files, we provide the text of the original documents, from which the sentences are extracted. Participant are free to use these original documents for any type of training they want. The document files have the following columns:

- `project_name`: We have six projects in this dataset. They are: IMMAP/DFS Syria, Bangladesh, Nigeria, Burkina Faso, RDC, and Colombia.
- `country_code`: SYR for Syria, BGD for Bangladesh, NGA for Nigeria, BFA Burkina Faso, COD for RDC, and COL for Colombia.
- `doc_id`: A unique identifier for each document.
- `doc_text`: The textual content documents.
- `doc_url`: A url of source documents.

All documents and sentences in this round are in English.

### Task

As mentioned before, this task consists of two consecutive steps:
- First, predicting whether a sentence is relevant, namely the `is_relevant` value, and ...
- Then, for any sentence *predicted as relevant* (i.e. predicted `is_relevant=1`), output *one* `sector_id` value.

Please consider that in the provided data `sector_ids` can be more than one (a multi-class multi-label setting). However, in this round, we explicitly limit the prediction of sectors to one class (a multi-class single-label setting). In fact, the users are free to exploit the one or multiple sector(s) of a sentence for training, but at inference time, only one sector should be provided.   


### Run File Format
The run (output) file format must be in the CSV format and have the following columns: `doc_id` and `sentence_id` of each sentence in the validation/test set; `0` or `1` prediction value for the `is_relevant` column; `sector_id` column is one predicted sector label if the predicted `is_relevant` is `1`, and otherwise `sector_id` is set to `-1`. For example, if the value of `sector_ids` of some sentence is `[1, 7]`, a possible run file could look like this:

    doc_id, sentence_id, is_relevant, sector_id
    0, 0, 0, -1
    0, 1, 1,  1
    0, 2, 0, -1
    1, 0, 1,  4
    2, 0, 1,  2
    2, 1, 1,  7
    2, 2, 1, -1
    2, 3, 1,  3
    2, 4, 0, -1

Please look at [create_random_baseline.py](https://github.com/the-deep/CHEERS-challenge/blob/main/Round_1/create_random_baseline.py) for creating a random baseline for the validation set. If the data is available in the same root path as this script, the following command generated a random baseline run:

    python create_random_baseline.py

### Evaluation Metrics
Run files are evaluated on two scores. First, the `is_relevant` predictions are evaluation with Macro [F1 Score](https://en.wikipedia.org/wiki/F-score#Definition). Then, the sectoral variable of the sentences with predicted `is_relevant=1` is evaluated using Accuracy based on Hamming Score as used in [this paper](https://link.springer.com/chapter/10.1007/978-3-540-24775-3_5). According to this formulation, accuracy is defined as:

$$Accuracy = \frac{1}{n}\sum_{i=1}^{N}{\frac{\lvert Y_i\cap \{z_i\} \rvert}{\lvert Y_i\cup \{z_i\} \rvert}}$$

where $$Y_i$$ is the set of classes in the ground truth data, $$z_i$$ is the predicted class. Please consider that Accuracy in this formulation is only calculated for sentences with predicted `is_relevant=1`. Also, the sentences in the ground truth with `is_relevant=1` but without any sectoral information `sector_ids=[]` are ignored during evaluation. Finally, since only one sector can be provided in the run file, even if the sectors of all sentences are correctly classified, the Accuracy value will not be equal to one, as some sentences have multiple sectors. For example, if a sentence has `sector_ids=[2, 4]` in ground truth, and the predicted `sector_id` in the run file is `2`, then the Accuracy of this sentence would be equal to `1/2`.


Finally, to be able to measure the overall performance of a system, we combine the F1 Score and Accuracy and introduce `HumImpact` – the *Humanitarian Impact* evaluation metric. `HumImpact` is calculated as: 

$$HumImpact = 0.5*F1\_Score + 0.5*Accuracy$$

To execute the evaluation for a run file, please use [evaluation.py](https://github.com/the-deep/CHEERS-challenge/blob/main/Round_1/evaluation.py) script. As an example, the above created random baseline can be evaluated by executing:

    python evaluation.py --ground-truth-path data_round_1/sentences_en_val.csv --runfile-path runs/en_val_baseline_random.csv

which outputs:

    Macro-averaged F1 score for is_relevant variable is: 49.92
    Accuracy for sector_ids variable is: 44.57
    HumImpact Score is: 47.24
    {'relevance_f1_score_macro': 0.4992029079372476, 'sectorids_accuracy': 0.4456756756756766, 'HumImpact': 0.4724392918064621}

### Results on Leaderboard
coming soon...!

# <a name="section-terms"></a> Terms and Conditions

The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas in the humanitarian sector, and are made available free of charge without extending any license or other intellectual property rights. In particular:

* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes; Upon violation of any of these terms, your rights to use the dataset will end automatically. The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.

# <a name="section-contact"></a> Contact Us

If you have any questions regarding technical aspects of the dataset, or how to obtain it, please contact us:
* Jean-Baptiste Bove (Innovation Lead): [email](mailto:jean@datafriendlyspace.org)
* Abdullah Al Nahas (R&D): [email](mailto:abdullah@datafriendlyspace.org)
* Navid Rekab-Saz (Academic Advisor): [webpage](http://navid-rekabsaz.com/)

[comment]: ![image](https://user-images.githubusercontent.com/71701125/112473998-53198600-8d6f-11eb-908c-060ae568226c.png)
