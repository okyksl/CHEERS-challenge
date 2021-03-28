# Welcome

TODO: 1-2 sentences about this page, the chllange, and organizer (DFS) . use the word natural language processing (NLP)

## Who is Data Friendly Space?
<img src="resources/dfs.png" alt="Deep Logo" width="150"/>

Data Friendly Space (DFS) is a non-profit organization based in the United States with a global presence. DFS’ guiding principle is to improve information management and analysis capacity, tools and processes in the humanitarian and development community to enable better informed and more targeted assistance.

DFS staff is composed of experts from the humanitarian information management and analysis field who specialize in real time secondary data review and build humanitarian applications that support fast extraction of information from large volumes of unstructured data.

DFS also focuses on creation of data centric web applications, websites and mobile applications to support humanitarian organizations. When building software, DFS focuses on the intersection between data automation processes powered by Artificial Intelligences and human knowledge and skills, in particular when one can help the other to execute analysis. More information on Data Friendly Space and its projects can be found [here](https://datafriendlyspace.org/).

### Product: DEEP Platform
<img src="resources/thedeep.png" alt="Deep Logo" width="150"/>

DFS is the technical host of the Data Entry and Exploration Platform (DEEP, [thedeep.io](https://www.thedeep.io/)), a tool used by humanitarians all over the world to monitor and assess crises. Over the past 4 years, humanitarian information analysts have been using the DEEP to facilitate collaborative, and joint analysis of unstructured data. The aim of the platform is to provide insights from years of historical and in-crisis humanitarian text data. The platform allows users to upload documents and classify text snippets according to predefined humanitarian target labels, grouped into and referred to as analytical frameworks. Tagging this data leads to the structuring of large volumes of information that enables effective analysis of the humanitarian conditions of the populations of interest and empowers humanitarians to identify information gaps and to provide sound recommendations in terms of needs assessment strategies and response plans. DEEP supports global operations of a range of international humanitarian organizations and the United Nations.

More information on the DEEP and how it is being used can be found here:
*	[DEEP Website](https://www.thedeep.io/)
*	[DEEP YouTube channel](https://www.youtube.com/channel/UCO3naDryeQIFny6BsEJwCaA)
*	[IFRC tutorial for conducting Needs Assessments with DEEP](https://deephelp.zendesk.com/hc/en-us/articles/360041904812-4-DEEP-Using-the-DEEP-Platform-)

As an example project, In 2020 DFS partnered with IMMAP, an international not-for-profit organization that provides information management services to humanitarian and development partners, in the COVID-19 Situational Analysis Project. The aim of the project is to provide the wider humanitarian community with timely and comprehensive information on the spread of the COVID-19 pandemic accross 6 countires: Syria, Bangladesh, Nigeria, the Democratic Republic of the Congo, Burkina-Faso and Colombia. More information on the project can be found [here](https://immap.org/news/covid-19-situational-analysis-project-in-six-countries/).

### How NLP can help in humanitarian crises?

The day-to-day workload of DEEP is mainly based on manual tagging of the experts, especialized in the humanitarian domain. The experts have extensive domain knowledge to understand how to use the analytical framework with its different taxonomies in order to assign the right labels to the right text snippets. Below, you can see the interface of the DFS/IMMAP analytical framework, where the experts are asked to assign approperiate classes to a selected snippet of text.

<center><img src="resources/analytical_framework.png" alt="Analytical Framework" width="400"/></center>

This process of selecting informative text excerpts from documents, and assigning approperiate tags is highly laborious and time consuming, while time is a decicive factor during humanitarian crises. The innovation of the DEEP relies upon leveraging recent advances in NLP to automate this process to assist experts to do what they are best at. 


[comment]: In this challenge, participants will focus on the analysis of text snippets that have been tagged inside the Sectoral Information matrix of the DFS/IMMAP analytical framework.


[comment]: Over the years, the DEEP has generated a dataset of over 180,000 sets of annotated snippets from approximately 85,000 documents that come from recognized humanitarian domains. These large volumes of quality training data put DFS in a unique position for the creation of high-performance NLP models that can serve the humanitarian community at large. 

[comment]: While DEEP comes with a generic analytical framework, each organization may also create its own custom framework based on the specific needs of its domain: UNHCR, the UN refugee agency, might focus on protection issues of refugee populations in a given crisis while OCHA, the humanitairan coordination agency of the UN, might focus on more general and cross-sectoral issues. In fact, while there is a large conceptual overlap for humanitarian organizations, various domains define slightly different analytical frameworks to describe their specific concepts. These differences between the analytical frameworks in different domains can still contain various degrees of conceptual (semantic) linkages. For instance when it comes to the analysis of sectoral information, different organisations tend to classify information according to labels that represent the humanitarian sectors of intervention: Food Security, Livelihoods, Health, Nutrition, WASH (Water, Sanitation and Hygiene), Protection, Shelter, Education, Agriculture, Logistics and Cross for snippets that belong to multiple sectors.


# CHEAT Challenge

## Round 1: Extraction and Classification of Humanitarian Data

Participants are asked to build build the following:
  1. A **sentence extraction model** that predicts whether a sentence in a given document is **relevant** and belongs in the Secotral Information matrix or not
  2. A **classifier** that will predict the sector of a sentence that belongs in the Secotral Information matric

TBD: more details ... what is expected from the participants

### Dataset

TDB: about the dataset, size, format, train data, validation, and test

[comment]: The dataset provided contains 3,301 documents in English, 1,301 in French and 689 in Spanish, each respectively with 249,992, 144,793, 129,077 labeled sentences, for a total of 5,291 documents and 523,862 labeled sentences.

TBD details about how to obtain data


### Output and Evaluation

#### Run File Format

TBD

#### Evaluation Metrics

TBD

TBD after explaning the metrics, the instruction about the evaluation script 

### Results on Leaderboard

coming soon...!

# Terms and Conditions

The provided datasets are intended for non-commercial research purposes to promote advancement in the field of natural language processing, information retrieval and related areas in the humanitarian sector, and are made available free of charge without extending any license or other intellectual property rights. In particular:

* Any parts of the datasets cannot be publicly shared or hosted (with exception for aggregated findings and visualizations);
* The datasets can only be used for non-commercial research purposes; Upon violation of any of these terms, your rights to use the dataset will end automatically. The datasets are provided “as is” without warranty. The side granting access to the datasets is not liable for any damages related to use of the dataset.

### Contact

If you have any questions regarding technical aspects of the dataset, or how to obtain it, please contact us:
* Jean-Baptiste Bove (Innovation Lead): [email](mailto:jean@datafriendlyspace.org)
* Abdullah Al Nahas (R&D): [email](mailto:abdullah@datafriendlyspace.org)
* Navid Rekab-Saz (Academic Advisor): [webpage](http://navid-rekabsaz.com/)

[comment]: ![image](https://user-images.githubusercontent.com/71701125/112473998-53198600-8d6f-11eb-908c-060ae568226c.png)


[comment]: > NOTE: [Markdown documentation](https://www.markdownguide.org/basic-syntax/)
