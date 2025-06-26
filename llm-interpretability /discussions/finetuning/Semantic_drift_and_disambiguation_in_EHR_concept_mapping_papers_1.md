## User

This is the beginning of an individual meeting with Clinical Informatics Specialist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Semantic drift and disambiguation in EHR concept mapping in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Semantic drift and disambiguation in EHR concept mapping to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Semantic drift and disambiguation in EHR concept mapping. Include both general queries about Semantic drift and disambiguation in EHR concept mapping and queries that specifically relate Semantic drift and disambiguation in EHR concept mapping to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Clinical Informatics Specialist, please provide your response to the agenda.

## Clinical Informatics Specialist

To address the agenda, we need to perform a series of searches to gather relevant literature on Semantic drift and disambiguation in EHR concept mapping, particularly in the context of LLM interpretability and electronic phenotype definitions. Here are the search queries I propose:

```python
search_queries = [
    "Semantic drift in EHR concept mapping",
    "Disambiguation in electronic health records",
    "Semantic drift and LLM interpretability in phenotype definitions",
    "EHR concept mapping and clinical applications",
    "Building clinician trust in LLM-based phenotype tools"
]
```

Next, I will use these queries to search for relevant scientific papers. Let's proceed with retrieving the PMCIDs and titles of the papers that match these queries.

## Clinical Informatics Specialist

Here are the PMCIDs and titles of the papers that are relevant to the queries on Semantic drift and disambiguation in EHR concept mapping, particularly in the context of LLM interpretability and electronic phenotype definitions:

```python
papers = {
    "10224668": "Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications",
    "11074891": "Generating Synthetic Electronic Health Record Data Using Generative Adversarial Networks: Tutorial",
    "8234679": "Using NLP in openEHR archetypes retrieval to promote interoperability: a feasibility study in China",
    "6990976": "Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries",
    "11638972": "Transformers and large language models in healthcare: A review",
    "11467596": "Processing of Short-Form Content in Clinical Narratives: Systematic Scoping Review",
    "8449626": "Automated detection of substance use information from electronic health records for a pediatric population",
    "11339513": "Disambiguation of acronyms in clinical narratives with large language models",
    "11751965": "Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation",
    "10538589": "Artificial Intelligence–Enabled Software Prototype to Inform Opioid Pharmacovigilance From Electronic Health Records: Development and Usability Study",
    "11076269": "A mini-review on perturbation modelling across single-cell omic modalities",
    "10873158": "Learning across diverse biomedical data modalities and cohorts: Challenges and opportunities for innovation",
    "11798655": "Interventions to Mitigate EHR and Documentation Burden in Health Professions Trainees: A Scoping Review",
    "11561445": "Question Answering for Electronic Health Records: Scoping Review of Datasets and Models",
    "11259764": "Electronic Health Record–Oriented Knowledge Graph System for Collaborative Clinical Decision Support Using Multicenter Fragmented Medical Data: Design and Application Study",
    "11153589": "Deployment and validation of the CLL treatment infection model adjoined to an EHR system",
    "10834163": "Artificial intelligence: revolutionizing cardiology with large language models",
    "10984041": "Inductive reasoning with large language models: a simulated randomized controlled trial for epilepsy",
    "11748787": "Artificial intelligence in rheumatology research: what is it good for?"
}
```

These papers cover various aspects of semantic drift, disambiguation, LLM interpretability, and their applications in electronic health records and clinical settings. They will provide a comprehensive foundation for understanding the challenges and opportunities in this research area.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Semantic drift in EHR concept mapping":

[begin paper 1]

PMCID = 10224668

Title = Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications

The recent availability of electronic health records (EHRs) have provided enormous opportunities to develop artificial intelligence (AI) algorithms. However, patient privacy has become a major concern that limits data sharing across hospital settings and subsequently hinders the advances in AI. Synthetic data, which benefits from the development and proliferation of generative models, has served as a promising substitute for real patient EHR data. However, the current generative models are limited as they only generate single type of clinical data for a synthetic patient, i.e., either continuous-valued or discrete-valued. To mimic the nature of clinical decision-making which encompasses various data types/sources, in this study, we propose a generative adversarial network (GAN) entitled EHR-M-GAN that simultaneously synthesizes mixed-type timeseries EHR data. EHR-M-GAN is capable of capturing the multidimensional, heterogeneous, and correlated temporal dynamics in patient trajectories. We have validated EHR-M-GAN on three publicly-available intensive care unit databases with records from a total of 141,488 unique patients, and performed privacy risk evaluation of the proposed model. EHR-M-GAN has demonstrated its superiority over state-of-the-art benchmarks for synthesizing clinical timeseries with high fidelity, while addressing the limitations regarding data types and dimensionality in the current generative models. Notably, prediction models for outcomes of intensive care performed significantly better when training data was augmented with the addition of EHR-M-GAN-generated timeseries. EHR-M-GAN may have use in developing AI algorithms in resource-limited settings, lowering the barrier for data acquisition while preserving patient privacy.

[end paper 1]

[begin paper 2]

PMCID = 11074891

Title = Generating Synthetic Electronic Health Record Data Using Generative Adversarial Networks: Tutorial

Synthetic electronic health record (EHR) data generation has been increasingly recognized as an important solution to expand the accessibility and maximize the value of private health data on a large scale. Recent advances in machine learning have facilitated more accurate modeling for complex and high-dimensional data, thereby greatly enhancing the data quality of synthetic EHR data. Among various approaches, generative adversarial networks (GANs) have become the main technical path in the literature due to their ability to capture the statistical characteristics of real data. However, there is a scarcity of detailed guidance within the domain regarding the development procedures of synthetic EHR data. The objective of this tutorial is to present a transparent and reproducible process for generating structured synthetic EHR data using a publicly accessible EHR data set as an example. We cover the topics of GAN architecture, EHR data types and representation, data preprocessing, GAN training, synthetic data generation and postprocessing, and data quality evaluation. We conclude this tutorial by discussing multiple important issues and future opportunities in this domain. The source code of the entire process has been made publicly available.

[end paper 2]

[begin paper 3]

PMCID = 8234679

Title = Using NLP in openEHR archetypes retrieval to promote interoperability: a feasibility study in China

With the development and application of medical information system, semantic interoperability is essential for accurate and advanced health-related computing and electronic health record (EHR) information sharing. The openEHR approach can improve semantic interoperability. One key improvement of openEHR is that it allows for the use of existing archetypes. The crucial problem is how to improve the precision and resolve ambiguity in the archetype retrieval.

Based on the query expansion technology and Word2Vec model in Nature Language Processing (NLP), we propose to find synonyms as substitutes for original search terms in archetype retrieval. Test sets in different medical professional level are used to verify the feasibility.

Applying the approach to each original search term (n = 120) in test sets, a total of 69,348 substitutes were constructed. Precision at 5 (P@5) was improved by 0.767, on average. For the best result, the P@5 was up to 0.975.

We introduce a novel approach that using NLP technology and corpus to find synonyms as substitutes for original search terms. Compared to simply mapping the element contained in openEHR to an external dictionary, this approach could greatly improve precision and resolve ambiguity in retrieval tasks. This is helpful to promote the application of openEHR and advance EHR information sharing.

[end paper 3]

[begin paper 4]

PMCID = 6990976

Title = Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries

Standards-based clinical data normalization has become a key component of effective data integration and accurate phenotyping for secondary use of electronic healthcare records (EHR) data. HL7 Fast Healthcare Interoperability Resources (FHIR) is an emerging clinical data standard for exchanging electronic healthcare data and has been used in modeling and integrating both structured and unstructured EHR data for a variety of clinical research applications. The overall objective of this study is to develop and evaluate a FHIR-based EHR phenotyping framework for identification of patients with obesity and its multiple comorbidities from semi-structured discharge summaries leveraging a FHIR-based clinical data normalization pipeline (known as NLP2FHIR).

We implemented a multi-class and multi-label classification system based on the i2b2 Obesity Challenge task to evaluate the FHIR-based EHR phenotyping framework. Two core parts of the framework are: (a) the conversion of discharge summaries into corresponding FHIR resources – Composition, Condition, MedicationStatement, Procedure and FamilyMemberHistory using the NLP2FHIR pipeline, and (b) the implementation of four machine learning algorithms (logistic regression, support vector machine, decision tree, and random forest) to train classifiers to predict disease state of obesity and 15 comorbidities using features extracted from standard FHIR resources and terminology expansions. We used the macro- and micro-averaged precision (P), recall (R), and F1 score (F1) measures to evaluate the classifier performance. We validated the framework using a second obesity dataset extracted from the MIMIC-III database.

Using the NLP2FHIR pipeline, 1237 clinical discharge summaries from the 2008 i2b2 obesity challenge dataset were represented as the instances of the FHIR Composition resource consisting of 5677 records with 16 unique section types. After the NLP processing and FHIR modeling, a set of 244,438 FHIR clinical resource instances were generated. As the results of the four machine learning classifiers, the random forest algorithm performed the best with F1-micro(0.9466)/F1-macro(0.7887) and F1-micro(0.9536)/F1-macro(0.6524) for intuitive classification (reflecting medical professionals’ judgments) and textual classification (reflecting the judgments based on explicitly reported information of diseases), respectively. The MIMIC-III obesity dataset was successfully integrated for prediction with minimal configuration of the NLP2FHIR pipeline and machine learning models.

The study demonstrated that the FHIR-based EHR phenotyping approach could effectively identify the state of obesity and multiple comorbidities using semi-structured discharge summaries. Our FHIR-based phenotyping approach is a first concrete step towards improving the data aspect of phenotyping portability across EHR systems and enhancing interpretability of the machine learning-based phenotyping algorithms.

[end paper 4]

[begin paper 5]

PMCID = 11638972

Title = Transformers and large language models in healthcare: A review

With Artificial Intelligence (AI) increasingly permeating various aspects of society, including healthcare, the adoption of the Transformers neural network architecture is rapidly changing many applications. Transformer is a type of deep learning architecture initially developed to solve general-purpose Natural Language Processing (NLP) tasks and has subsequently been adapted in many fields, including healthcare. In this survey paper, we provide an overview of how this architecture has been adopted to analyze various forms of healthcare data, including clinical NLP, medical imaging, structured Electronic Health Records (EHR), social media, bio-physiological signals, biomolecular sequences. Furthermore, which have also include the articles that used the transformer architecture for generating surgical instructions and predicting adverse outcomes after surgeries under the umbrella of critical care. Under diverse settings, these models have been used for clinical diagnosis, report generation, data reconstruction, and drug/protein synthesis. Finally, we also discuss the benefits and limitations of using transformers in healthcare and examine issues such as computational cost, model interpretability, fairness, alignment with human values, ethical implications, and environmental impact.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Disambiguation in electronic health records":

[begin paper 1]

PMCID = 11467596

Title = Processing of Short-Form Content in Clinical Narratives: Systematic Scoping Review

Clinical narratives are essential components of electronic health records. The adoption of electronic health records has increased documentation time for hospital staff, leading to the use of abbreviations and acronyms more frequently. This brevity can potentially hinder comprehension for both professionals and patients.

This review aims to provide an overview of the types of short forms found in clinical narratives, as well as the natural language processing (NLP) techniques used for their identification, expansion, and disambiguation.

In the databases Web of Science, Embase, MEDLINE, EBMR (Evidence-Based Medicine Reviews), and ACL Anthology, publications that met the inclusion criteria were searched according to PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines for a systematic scoping review. Original, peer-reviewed publications focusing on short-form processing in human clinical narratives were included, covering the period from January 2018 to February 2023. Short-form types were extracted, and multidimensional research methodologies were assigned to each target objective (identification, expansion, and disambiguation). NLP study recommendations and study characteristics were systematically assigned occurrence rates for evaluation.

Out of a total of 6639 records, only 19 articles were included in the final analysis. Rule-based approaches were predominantly used for identifying short forms, while string similarity and vector representations were applied for expansion. Embeddings and deep learning approaches were used for disambiguation.

The scope and types of what constitutes a clinical short form were often not explicitly defined by the authors. This lack of definition poses challenges for reproducibility and for determining whether specific methodologies are suitable for different types of short forms. Analysis of a subset of NLP recommendations for assessing quality and reproducibility revealed only partial adherence to these recommendations. Single-character abbreviations were underrepresented in studies on clinical narrative processing, as were investigations in languages other than English. Future research should focus on these 2 areas, and each paper should include descriptions of the types of content analyzed.

[end paper 1]

[begin paper 2]

PMCID = 8449626

Title = Automated detection of substance use information from electronic health records for a pediatric population

Substance use screening in adolescence is unstandardized and often documented in clinical notes, rather than in structured electronic health records (EHRs). The objective of this study was to integrate logic rules with state-of-the-art natural language processing (NLP) and machine learning technologies to detect substance use information from both structured and unstructured EHR data.

Pediatric patients (10-20 years of age) with any encounter between July 1, 2012, and October 31, 2017, were included (n = 3890 patients; 19 478 encounters). EHR data were extracted at each encounter, manually reviewed for substance use (alcohol, tobacco, marijuana, opiate, any use), and coded as lifetime use, current use, or family use. Logic rules mapped structured EHR indicators to screening results. A knowledge-based NLP system and a deep learning model detected substance use information from unstructured clinical narratives. System performance was evaluated using positive predictive value, sensitivity, negative predictive value, specificity, and area under the receiver-operating characteristic curve (AUC).

The dataset included 17 235 structured indicators and 27 141 clinical narratives. Manual review of clinical narratives captured 94.0% of positive screening results, while structured EHR data captured 22.0%. Logic rules detected screening results from structured data with 1.0 and 0.99 for sensitivity and specificity, respectively. The knowledge-based system detected substance use information from clinical narratives with 0.86, 0.79, and 0.88 for AUC, sensitivity, and specificity, respectively. The deep learning model further improved detection capacity, achieving 0.88, 0.81, and 0.85 for AUC, sensitivity, and specificity, respectively. Finally, integrating predictions from structured and unstructured data achieved high detection capacity across all cases (0.96, 0.85, and 0.87 for AUC, sensitivity, and specificity, respectively).

It is feasible to detect substance use screening and results among pediatric patients using logic rules, NLP, and machine learning technologies.

[end paper 2]

[begin paper 3]

PMCID = 11339513

Title = Disambiguation of acronyms in clinical narratives with large language models

To assess the performance of large language models (LLMs) for zero-shot disambiguation of acronyms in clinical narratives.

Clinical narratives in English, German, and Portuguese were applied for testing the performance of four LLMs: GPT-3.5, GPT-4, Llama-2-7b-chat, and Llama-2-70b-chat. For English, the anonymized Clinical Abbreviation Sense Inventory (CASI, University of Minnesota) was used. For German and Portuguese, at least 500 text spans were processed. The output of LLM models, prompted with contextual information, was analyzed to compare their acronym disambiguation capability, grouped by document-level metadata, the source language, and the LLM.

On CASI, GPT-3.5 achieved 0.91 in accuracy. GPT-4 outperformed GPT-3.5 across all datasets, reaching 0.98 in accuracy for CASI, 0.86 and 0.65 for two German datasets, and 0.88 for Portuguese. Llama models only reached 0.73 for CASI and failed severely for German and Portuguese. Across LLMs, performance decreased from English to German and Portuguese processing languages. There was no evidence that additional document-level metadata had a significant effect.

For English clinical narratives, acronym resolution by GPT-4 can be recommended to improve readability of clinical text by patients and professionals. For German and Portuguese, better models are needed. Llama models, which are particularly interesting for processing sensitive content on premise, cannot yet be recommended for acronym resolution.

[end paper 3]

[begin paper 4]

PMCID = 11751965

Title = Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation

We aimed to evaluate the performance of multiple large language models (LLMs) in data extraction from unstructured and semi-structured electronic health records.

50 synthetic medical notes in English, containing a structured and an unstructured part, were drafted and evaluated by domain experts, and subsequently used for LLM-prompting. 18 LLMs were evaluated against a baseline transformer-based model. Performance assessment comprised four entity extraction and five binary classification tasks with a total of 450 predictions for each LLM. LLM-response consistency assessment was performed over three same-prompt iterations.

Claude 3.0 Opus, Claude 3.0 Sonnet, Claude 2.0, GPT 4, Claude 2.1, Gemini Advanced, PaLM 2 chat-bison and Llama 3-70b exhibited an excellent overall accuracy >0.98 (0.995, 0.988, 0.988, 0.988, 0.986, 0.982, 0.982, and 0.982, respectively), significantly higher than the baseline RoBERTa model (0.742). Claude 2.0, Claude 2.1, Claude 3.0 Opus, PaLM 2 chat-bison, GPT 4, Claude 3.0 Sonnet and Llama 3-70b showed a marginally higher and Gemini Advanced a marginally lower multiple-run consistency than the baseline model RoBERTa (Krippendorff’s alpha value 1, 0.998, 0.996, 0.996, 0.992, 0.991, 0.989, 0.988, and 0.985, respectively).

Claude 3.0 Opus, Claude 3.0 Sonnet, Claude 2.0, GPT 4, Claude 2.1, Gemini Advanced, PaLM 2 chat bison and Llama 3-70b performed the best, exhibiting outstanding performance in both entity extraction and binary classification, with highly consistent responses over multiple same-prompt iterations. Their use could leverage data for research and unburden healthcare professionals. Real-data analyses are warranted to confirm their performance in a real-world setting.

Claude 3.0 Opus, Claude 3.0 Sonnet, Claude 2.0, GPT 4, Claude 2.1, Gemini Advanced, PaLM 2 chat-bison and Llama 3-70b seem to be able to reliably extract data from unstructured and semi-structured electronic health records. Further analyses using real data are warranted to confirm their performance in a real-world setting.

[end paper 4]

[begin paper 5]

PMCID = 10538589

Title = Artificial Intelligence–Enabled Software Prototype to Inform Opioid Pharmacovigilance From Electronic Health Records: Development and Usability Study

The use of patient health and treatment information captured in structured and unstructured formats in computerized electronic health record (EHR) repositories could potentially augment the detection of safety signals for drug products regulated by the US Food and Drug Administration (FDA). Natural language processing and other artificial intelligence (AI) techniques provide novel methodologies that could be leveraged to extract clinically useful information from EHR resources.

Our aim is to develop a novel AI-enabled software prototype to identify adverse drug event (ADE) safety signals from free-text discharge summaries in EHRs to enhance opioid drug safety and research activities at the FDA.

We developed a prototype for web-based software that leverages keyword and trigger-phrase searching with rule-based algorithms and deep learning to extract candidate ADEs for specific opioid drugs from discharge summaries in the Medical Information Mart for Intensive Care III (MIMIC III) database. The prototype uses MedSpacy components to identify relevant sections of discharge summaries and a pretrained natural language processing (NLP) model, Spark NLP for Healthcare, for named entity recognition. Fifteen FDA staff members provided feedback on the prototype’s features and functionalities.

Using the prototype, we were able to identify known, labeled, opioid-related adverse drug reactions from text in EHRs. The AI-enabled model achieved accuracy, recall, precision, and F1-scores of 0.66, 0.69, 0.64, and 0.67, respectively. FDA participants assessed the prototype as highly desirable in user satisfaction, visualizations, and in the potential to support drug safety signal detection for opioid drugs from EHR data while saving time and manual effort. Actionable design recommendations included (1) enlarging the tabs and visualizations; (2) enabling more flexibility and customizations to fit end users’ individual needs; (3) providing additional instructional resources; (4) adding multiple graph export functionality; and (5) adding project summaries.

The novel prototype uses innovative AI-based techniques to automate searching for, extracting, and analyzing clinically useful information captured in unstructured text in EHRs. It increases efficiency in harnessing real-world data for opioid drug safety and increases the usability of the data to support regulatory review while decreasing the manual research burden.

[end paper 5]



Here are the top 2 articles on PubMed Central for the query "Semantic drift and LLM interpretability in phenotype definitions":

[begin paper 1]

PMCID = 11076269

Title = A mini-review on perturbation modelling across single-cell omic modalities

Recent advances in single-cell omics technology have transformed the landscape of cellular and molecular research, enriching the scope and intricacy of cellular characterisation. Perturbation modelling seeks to comprehensively grasp the effects of external influences like disease onset or molecular knock-outs or external stimulants on cellular physiology, specifically on transcription factors, signal transducers, biological pathways, and dynamic cell states. Machine and deep learning tools transform complex perturbational phenomena in algorithmically tractable tasks to formulate predictions based on various types of single-cell datasets. However, the recent surge in tools and datasets makes it challenging for experimental biologists and computational scientists to keep track of the recent advances in this rapidly expanding filed of single-cell modelling. Here, we recapitulate the main objectives of perturbation modelling and summarise novel single-cell perturbation technologies based on genetic manipulation like CRISPR or compounds, spanning across omic modalities. We then concisely review a burgeoning group of computational methods extending from classical statistical inference methodologies to various machine and deep learning architectures like shallow models or autoencoders, to biologically informed approaches based on gene regulatory networks, and to combinatorial efforts reminiscent of ensemble learning. We also discuss the rising trend of large foundational models in single-cell perturbation modelling inspired by large language models. Lastly, we critically assess the challenges that underline single-cell perturbation modelling while pointing towards relevant future perspectives like perturbation atlases, multi-omics and spatial datasets, causal machine learning for interpretability, multi-task learning for performance and explainability as well as prospects for solving interoperability and benchmarking pitfalls.

[end paper 1]

[begin paper 2]

PMCID = 10873158

Title = Learning across diverse biomedical data modalities and cohorts: Challenges and opportunities for innovation

In healthcare, machine learning (ML) shows significant potential to augment patient care, improve population health, and streamline healthcare workflows. Realizing its full potential is, however, often hampered by concerns about data privacy, diversity in data sources, and suboptimal utilization of different data modalities. This review studies the utility of cross-cohort cross-category (C4) integration in such contexts: the process of combining information from diverse datasets distributed across distinct, secure sites. We argue that C4 approaches could pave the way for ML models that are both holistic and widely applicable. This paper provides a comprehensive overview of C4 in health care, including its present stage, potential opportunities, and associated challenges.

Machine learning and artificial intelligence offer immense potential to improve health care in the future, but a variety of real-world issues present hurdles to adoption. Data must be handled carefully to protect patient privacy. Data collected from different sources can vary in quality and completeness. Data from different assay methods (i.e., multimodal data) can be hard to combine and integrate. Here, we review and discuss methods, models, and workflows that are well suited to handling these kinds of challenges, which we argue will ensure that the promise of machine learning for health care is fully realized.

Machine learning has great potential to revolutionize health care. Yet, it is hindered by privacy concerns, varied data sources, and limited use of different types of data. Cross-cohort cross-category learning (C4) aims to overcome these obstacles by merging varied datasets. C4 involves multiple secure locations, each contributing different data types, to build comprehensive machine learning models. These models utilize data from every site, offering a broader understanding. This review explores the applications and challenges of C4 in health care.

[end paper 2]



Here are the top 5 articles on PubMed Central for the query "EHR concept mapping and clinical applications":

[begin paper 1]

PMCID = 11798655

Title = Interventions to Mitigate EHR and Documentation Burden in Health Professions Trainees: A Scoping Review

Background  Health professions trainees (trainees) are unique as they learn a chosen field while working within electronic health records (EHRs). Efforts to mitigate EHR burden have been described for the experienced health professional (HP), but less is understood for trainees. EHR or documentation burden ( EHR burden ) affects trainees, although not all trainees use EHRs, and use may differ for experienced HPs. 

Objectives  This study aimed to develop a model of how interventions to mitigate EHR burden fit within the trainee EHR workflow: the Trainee EHR Burden Model . (We: 1) Examined trainee experiences of interventions aimed at mitigating EHR burden (scoping review) and (2) Adapted an existing workflow model by mapping included studies (concept clarification). 

Methods  We conducted a four-database scoping review applying Preferred Reporting Items for Systematic Reviews and Meta-Analysis Extensions for Scoping Review (PRISMA-ScR) guidance, examining scholarly, peer-reviewed studies that measured trainee experience of interventions to mitigate EHR burden. We conducted a concept clarification categorizing, then mapping studies to workflow model elements. We adapted the model to intervenable points for trainee EHR burden. 

Results  We identified 11 studies examining interventions to mitigate EHR burden that measured trainee experience. Interventions included curriculum, training, and coaching on the existing EHR for both simulated or live tasks; evaluating scribes' impact; adding devices or technology tailored to rounds; and team communication or data presentation at end-of-shift handoffs. Interventions had varying effects on EHR burden, most commonly measured through surveys, and less commonly, direct observation. Most studies had limited sample sizes and focused on inpatient settings and physician trainees. 

Conclusion  Few studies measured trainee perspectives of interventions aiming to mitigate EHR burden. Many studies applied quasi-experimental designs and focused on inpatient settings. The Trainee EHR Burden Model , adapted from an existing workflow model, offers a starting place to situate points of intervention in trainee workflow. Further research is needed to design new interventions targeting stages of HP trainee workflow, in a range of clinical settings. 

[end paper 1]

[begin paper 2]

PMCID = 11561445

Title = Question Answering for Electronic Health Records: Scoping Review of Datasets and Models

Question answering (QA) systems for patient-related data can assist both clinicians and patients. They can, for example, assist clinicians in decision-making and enable patients to have a better understanding of their medical history. Substantial amounts of patient data are stored in electronic health records (EHRs), making EHR QA an important research area. Because of the differences in data format and modality, this differs greatly from other medical QA tasks that use medical websites or scientific papers to retrieve answers, making it critical to research EHR QA.

This study aims to provide a methodological review of existing works on QA for EHRs. The objectives of this study were to identify the existing EHR QA datasets and analyze them, study the state-of-the-art methodologies used in this task, compare the different evaluation metrics used by these state-of-the-art models, and finally elicit the various challenges and the ongoing issues in EHR QA.

We searched for articles from January 1, 2005, to September 30, 2023, in 4 digital sources, including Google Scholar, ACL Anthology, ACM Digital Library, and PubMed, to collect relevant publications on EHR QA. Our systematic screening process followed PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines. A total of 4111 papers were identified for our study, and after screening based on our inclusion criteria, we obtained 47 papers for further study. The selected studies were then classified into 2 non–mutually exclusive categories depending on their scope: “EHR QA datasets” and “EHR QA models.”

A systematic screening process obtained 47 papers on EHR QA for final review. Out of the 47 papers, 53% (n=25) were about EHR QA datasets, and 79% (n=37) papers were about EHR QA models. It was observed that QA on EHRs is relatively new and unexplored. Most of the works are fairly recent. In addition, it was observed that emrQA is by far the most popular EHR QA dataset, both in terms of citations and usage in other papers. We have classified the EHR QA datasets based on their modality, and we have inferred that Medical Information Mart for Intensive Care (MIMIC-III) and the National Natural Language Processing Clinical Challenges datasets (ie, n2c2 datasets) are the most popular EHR databases and corpuses used in EHR QA. Furthermore, we identified the different models used in EHR QA along with the evaluation metrics used for these models.

EHR QA research faces multiple challenges, such as the limited availability of clinical annotations, concept normalization in EHR QA, and challenges faced in generating realistic EHR QA datasets. There are still many gaps in research that motivate further work. This study will assist future researchers in focusing on areas of EHR QA that have possible future research directions.

[end paper 2]

[begin paper 3]

PMCID = 11259764

Title = Electronic Health Record–Oriented Knowledge Graph System for Collaborative Clinical Decision Support Using Multicenter Fragmented Medical Data: Design and Application Study

The medical knowledge graph provides explainable decision support, helping clinicians with prompt diagnosis and treatment suggestions. However, in real-world clinical practice, patients visit different hospitals seeking various medical services, resulting in fragmented patient data across hospitals. With data security issues, data fragmentation limits the application of knowledge graphs because single-hospital data cannot provide complete evidence for generating precise decision support and comprehensive explanations. It is important to study new methods for knowledge graph systems to integrate into multicenter, information-sensitive medical environments, using fragmented patient records for decision support while maintaining data privacy and security.

This study aims to propose an electronic health record (EHR)–oriented knowledge graph system for collaborative reasoning with multicenter fragmented patient medical data, all the while preserving data privacy.

The study introduced an EHR knowledge graph framework and a novel collaborative reasoning process for utilizing multicenter fragmented information. The system was deployed in each hospital and used a unified semantic structure and Observational Medical Outcomes Partnership (OMOP) vocabulary to standardize the local EHR data set. The system transforms local EHR data into semantic formats and performs semantic reasoning to generate intermediate reasoning findings. The generated intermediate findings used hypernym concepts to isolate original medical data. The intermediate findings and hash-encrypted patient identities were synchronized through a blockchain network. The multicenter intermediate findings were collaborated for final reasoning and clinical decision support without gathering original EHR data.

The system underwent evaluation through an application study involving the utilization of multicenter fragmented EHR data to alert non-nephrology clinicians about overlooked patients with chronic kidney disease (CKD). The study covered 1185 patients in nonnephrology departments from 3 hospitals. The patients visited at least two of the hospitals. Of these, 124 patients were identified as meeting CKD diagnosis criteria through collaborative reasoning using multicenter EHR data, whereas the data from individual hospitals alone could not facilitate the identification of CKD in these patients. The assessment by clinicians indicated that 78/91 (86%) patients were CKD positive.

The proposed system was able to effectively utilize multicenter fragmented EHR data for clinical application. The application study showed the clinical benefits of the system with prompt and comprehensive decision support.

[end paper 3]

[begin paper 4]

PMCID = 10224668

Title = Generating synthetic mixed-type longitudinal electronic health records for artificial intelligent applications

The recent availability of electronic health records (EHRs) have provided enormous opportunities to develop artificial intelligence (AI) algorithms. However, patient privacy has become a major concern that limits data sharing across hospital settings and subsequently hinders the advances in AI. Synthetic data, which benefits from the development and proliferation of generative models, has served as a promising substitute for real patient EHR data. However, the current generative models are limited as they only generate single type of clinical data for a synthetic patient, i.e., either continuous-valued or discrete-valued. To mimic the nature of clinical decision-making which encompasses various data types/sources, in this study, we propose a generative adversarial network (GAN) entitled EHR-M-GAN that simultaneously synthesizes mixed-type timeseries EHR data. EHR-M-GAN is capable of capturing the multidimensional, heterogeneous, and correlated temporal dynamics in patient trajectories. We have validated EHR-M-GAN on three publicly-available intensive care unit databases with records from a total of 141,488 unique patients, and performed privacy risk evaluation of the proposed model. EHR-M-GAN has demonstrated its superiority over state-of-the-art benchmarks for synthesizing clinical timeseries with high fidelity, while addressing the limitations regarding data types and dimensionality in the current generative models. Notably, prediction models for outcomes of intensive care performed significantly better when training data was augmented with the addition of EHR-M-GAN-generated timeseries. EHR-M-GAN may have use in developing AI algorithms in resource-limited settings, lowering the barrier for data acquisition while preserving patient privacy.

[end paper 4]

[begin paper 5]

PMCID = 11153589

Title = Deployment and validation of the CLL treatment infection model adjoined to an EHR system

Research algorithms are seldom externally validated or integrated into clinical practice, leaving unknown challenges in deployment. In such efforts, one needs to address challenges related to data harmonization, the performance of an algorithm in unforeseen missingness, automation and monitoring of predictions, and legal frameworks. We here describe the deployment of a high-dimensional data-driven decision support model into an EHR and derive practical guidelines informed by this deployment that includes the necessary processes, stakeholders and design requirements for a successful deployment. For this, we describe our deployment of the chronic lymphocytic leukemia (CLL) treatment infection model (CLL-TIM) as a stand-alone platform adjoined to an EPIC-based Danish Electronic Health Record (EHR), with the presentation of personalized predictions in a clinical context. CLL-TIM is an 84-variable data-driven prognostic model utilizing 7-year medical patient records and predicts the 2-year risk composite outcome of infection and/or treatment post-CLL diagnosis. As an independent validation cohort for this deployment, we used a retrospective population-based cohort of patients diagnosed with CLL from 2018 onwards (n = 1480). Unexpectedly high levels of missingness for key CLL-TIM variables were exhibited upon deployment. High dimensionality, with the handling of missingness, and predictive confidence were critical design elements that enabled trustworthy predictions and thus serves as a priority for prognostic models seeking deployment in new EHRs. Our setup for deployment, including automation and monitoring into EHR that meets Medical Device Regulations, may be used as step-by-step guidelines for others aiming at designing and deploying research algorithms into clinical practice.

[end paper 5]



Here are the top 3 articles on PubMed Central for the query "Building clinician trust in LLM-based phenotype tools":

[begin paper 1]

PMCID = 10834163

Title = Artificial intelligence: revolutionizing cardiology with large language models

Overview of input sources (top) to train or fine-tune cardio large language models and different applications (bottom). ECG, electrocardiogram; Q&A, questions and answers.

Natural language processing techniques are having an increasing impact on clinical care from patient, clinician, administrator, and research perspective. Among others are automated generation of clinical notes and discharge letters, medical term coding for billing, medical chatbots both for patients and clinicians, data enrichment in the identification of disease symptoms or diagnosis, cohort selection for clinical trial, and auditing purposes. In the review, an overview of the history in natural language processing techniques developed with brief technical background is presented. Subsequently, the review will discuss implementation strategies of natural language processing tools, thereby specifically focusing on large language models, and conclude with future opportunities in the application of such techniques in the field of cardiology.

[end paper 1]

[begin paper 2]

PMCID = 10984041

Title = Inductive reasoning with large language models: a simulated randomized controlled trial for epilepsy

The analysis of electronic medical records at scale to learn from clinical experience is currently very challenging. The integration of artificial intelligence (AI), specifically foundational large language models (LLMs), into an analysis pipeline may overcome some of the current limitations of modest input sizes, inaccuracies, biases, and incomplete knowledge bases.

To explore the effectiveness of using an LLM for generating realistic clinical data and other LLMs for summarizing and synthesizing information in a model system, simulating a randomized clinical trial (RCT) in epilepsy to demonstrate the potential of inductive reasoning via medical chart review.

An LLM-generated simulated RCT based on a RCT for treatment with an antiseizure medication, cenobamate, including a placebo arm and a full-strength drug arm, evaluated by an LLM-based pipeline versus a human reader.

Simulation based on realistic seizure diaries, treatment effects, reported symptoms and clinical notes generated by LLMs with multiple different neurologist writing styles.

Simulated cohort of 240 patients, divided 1:1 into placebo and drug arms.

Utilization of LLMs for the generation of clinical notes and for the synthesis of data from these notes, aiming to evaluate the efficacy and safety of cenobamate in seizure control either with a human evaluator or AI-pipeline.

The AI and human analysis focused on identifying the number of seizures, symptom reports, and treatment efficacy, with statistical analysis comparing the 50%-responder rate and median percentage change between the placebo and drug arms, as well as side effect rates in each arm.

AI closely mirrored human analysis, demonstrating the drug’s efficacy with marginal differences (<3%) in identifying both drug efficacy and reported symptoms.

This study showcases the potential of LLMs accurately simulate and analyze clinical trials. Significantly, it highlights the ability of LLMs to reconstruct essential trial elements, identify treatment effects, and recognize reported symptoms, within a realistic clinical framework. The findings underscore the relevance of LLMs in future clinical research, offering a scalable, efficient alternative to traditional data mining methods without the need for specialized medical language training.

[end paper 2]

[begin paper 3]

PMCID = 11748787

Title = Artificial intelligence in rheumatology research: what is it good for?

Artificial intelligence (AI) is transforming rheumatology research, with a myriad of studies aiming to improve diagnosis, prognosis and treatment prediction, while also showing potential capability to optimise the research workflow, improve drug discovery and clinical trials. Machine learning, a key element of discriminative AI, has demonstrated the ability of accurately classifying rheumatic diseases and predicting therapeutic outcomes by using diverse data types, including structured databases, imaging and text. In parallel, generative AI, driven by large language models, is becoming a powerful tool for optimising the research workflow by supporting with content generation, literature review automation and clinical decision support. This review explores the current applications and future potential of both discriminative and generative AI in rheumatology. It also highlights the challenges posed by these technologies, such as ethical concerns and the need for rigorous validation and regulatory oversight. The integration of AI in rheumatology promises substantial advancements but requires a balanced approach to optimise benefits and minimise potential possible downsides.

[end paper 3]



