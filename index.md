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

The Round 1 of the challenge simulates the document processing procedure, normally conducted by analysts. In particular, given a document consisting of a number of sentences, a system is asked to:
- First, **extract and select informative and relevant sentences**, and ...
- Second, **classify the extracted sentences according to sectoral Information**.

In the following, we explain the dataset and task, followed by describing the run files format, and evaluation metrics. 

### Dataset

The dataset of this round is available [here](https://deep-cheers-challenge.s3.amazonaws.com/data_round_1.zip) and consists of the following files:

    data_round_1/
      documents_train_en.csv
      documents_val_en.csv
      documents_test_en.csv
      sentences_train_en.csv
      sentences_val_en.csv
      sentences_test_en.csv
      immap_sector_name_to_id.json
      Terms of Use.txt
      
The primary data for the challenge is available in the `sentences_<split>_en.csv` files. Each of these files contain the following columns: 

- `doc_id`: The identifier of the document, from which the sentences are extracted.
- `sentence_id`: Sentence identifier. The Combination of `doc_id` and `sentence_id` forms a unique id for each sentence.
- `sentence_text`: Text of the sentence.
- `is_relevant` (not available in `sentences_test_en.csv`): Determines whether the sentence is relevant (`1`) or non-relevant (`0`) according to the need of the analyst. 
- `sector_ids` (not available in `sentences_test_en.csv`): The list of sector ids. If the sentence is not assigned to any sector, the list is empty (`[]`). Note that a relevant sentence (`is_relevant=1`) might have an empty `sector_ids`, as no information about the sector of the sentence is provided. A non-relevant sentence (`is_relevant=0`) has always no information about `sector_ids=[]`.


In addition to sentences, the `documents_<split>_en.csv` files provide the full text of the original documents, from which the sentences are extracted. Participant are free to use these original documents as any sort of additional data. The document files have the following columns:

- `doc_id`: The unique identifier of the document.
- `doc_text`: The full text content of the document.
- `doc_url`: URL of the document.
- `project_name`: The name of the project. Current projects are IMMAP/DFS Syria, Bangladesh, Nigeria, Burkina Faso, RDC, and Colombia.
- `country_code`: The country related to the content of the document. SYR for Syria, BGD for Bangladesh, NGA for Nigeria, BFA Burkina Faso, COD for RDC, and COL for Colombia.

The corresponding name of each sector is available in `immap_sector_name_to_id.json`. All provided documents and sentences in this round are in English.

### Task

As mentioned before, this task consists of two consecutive steps:
- First, predicting whether a sentence is relevant (`is_relevant` target), and ...
- Second, for any sentence that is predicted as relevant, predicting one sector (`sector_id` target).

Please consider that in the provided data, the `sector_ids` column can provide more than one value. However, we explicitly limit the prediction of sectors to **one class**. In fact, the users are free to exploit one or multiple sector(s) of the sentences during training, while at inference time, only one sector should be provided. The exact format of the run file is explained in the following.  


### Run File Format
The run (output) file format is in CSV format and have the following columns: 
- `doc_id` and `sentence_id`: indicating together the identifier of each sentence
- `is_relevant`: the `0` or `1` prediction value for sentence relevance
- `sector_id`: the predicted sector label if the predicted `is_relevant` is `1`, and `-1` otherwise.

For example, if the value of `sector_ids` of some sentences could be between `1` to `7`, a possible run file can look like:

    doc_id, sentence_id, is_relevant, sector_id
    0, 0, 0, -1
    0, 1, 1,  1
    0, 2, 0, -1
    1, 0, 1,  4
    2, 0, 1,  2
    2, 1, 1,  7
    2, 2, 0, -1
    2, 3, 1,  3
    2, 4, 0, -1

The code for creating a random baseline for the validation set is provided in [create_random_baseline.py](https://github.com/the-deep/CHEERS-challenge/blob/main/Round_1/create_random_baseline.py). Considering that the data is available in the same path as this script, the following command generates the run file of this baseline:

    python create_random_baseline.py

### Evaluation Metrics
Run files are evaluated according to three scores: First, the `is_relevant` predictions are evaluated with Macro [F1 Score](https://en.wikipedia.org/wiki/F-score#Definition). 

Next, for the sentences with predicted `is_relevant=1`, their corresponding predicted sectors are evaluated using a version of Accuracy based on the Hamming Score - in a similar way as in [this paper](https://link.springer.com/chapter/10.1007/978-3-540-24775-3_5). According to this formulation, Accuracy is defined as:

$$Accuracy = \frac{1}{n}\sum_{i=1}^{N}{\frac{\lvert Y_i\cap \{z_i\} \rvert}{\lvert Y_i\cup \{z_i\} \rvert}}$$

where $$Y_i$$ is the set of labels in the ground truth data, and $$z_i$$ is the predicted class. Please consider that Accuracy in this formulation is only calculated for sentences with predicted `is_relevant=1`. Also, the sentences in the ground truth with `is_relevant=1` but without any sectoral information (`sector_ids=[]`) are ignored during calculating Accuracy. Finally, since only one sector can be provided in the run file, the overall Accuracy value will not be equal to one, as some sentences in the ground truth have multiple sectors. To elaborate it with an example, if a sentence has `sector_ids=[2, 4]` in ground truth, and the predicted `sector_id` in the run file is `2`, then the Accuracy of this sentence would be equal to `1/2`.

Finally, to be able to measure the overall performance of a system, we combine the F1 Score and Accuracy and introduce `HumImpact` – the *Humanitarian Impact* evaluation metric. `HumImpact` is defined as: 

$$HumImpact = 0.5*F1\_Score + 0.5*Accuracy$$

Please use [evaluation.py](https://github.com/the-deep/CHEERS-challenge/blob/main/Round_1/evaluation.py) script to evaluate the run file. The following command provides the evaluation results of the above-created random baseline:

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
