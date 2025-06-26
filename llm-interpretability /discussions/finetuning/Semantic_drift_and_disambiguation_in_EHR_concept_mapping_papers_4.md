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

To address the agenda and find relevant literature on Semantic drift and disambiguation in EHR concept mapping, particularly in the context of LLM interpretability and electronic phenotype definitions, I will create a series of search queries. These queries will be designed to capture both the general aspects of the topic and its specific applications in clinical settings. Here are the search queries in Python syntax:

```python
search_queries = [
    "Semantic drift in EHR concept mapping",
    "Disambiguation in electronic health records",
    "LLM interpretability in phenotype definition",
    "Semantic drift and LLM in clinical applications",
    "Building clinician trust in LLM-based EHR tools"
]
```

Next, I will use these queries to search for relevant scientific papers on PubMed Central. Let's proceed with retrieving the PMCIDs and titles of the papers.

## Clinical Informatics Specialist

Here is a Python dictionary mapping PMCIDs to titles for the papers retrieved from the search queries:

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
    "10508824": "Evaluation of large language models for discovery of gene set function",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "11480249": "Confronting the data deluge: How artificial intelligence can be used in the study of plant stress",
    "11639975": "EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy",
    "11545079": "The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning",
    "10160120": "The SciQA Scientific Question Answering Benchmark for Scholarly Knowledge",
    "10629494": "Language models and psychological sciences",
    "11929979": "Digital evolution: Novo Nordisk’s shift to ontology-based data management",
    "11441322": "Biomedical knowledge graph-optimized prompt generation for large language models",
    "11925797": "Computational tools and data integration to accelerate vaccine development: challenges, opportunities, and future directions",
    "11809463": "Applications of Large Language Models in the Field of Suicide Prevention: Scoping Review",
    "11986386": "Generative Large Language Model—Powered Conversational AI App for Personalized Risk Assessment: Case Study in COVID-19",
    "10834163": "Artificial intelligence: revolutionizing cardiology with large language models"
}
```

These articles cover various aspects of semantic drift, disambiguation, and the application of LLMs in electronic health records, which should be useful for your research project.

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



Here are the top 5 articles on PubMed Central for the query "LLM interpretability in phenotype definition":

[begin paper 1]

PMCID = 10508824

Title = Evaluation of large language models for discovery of gene set function

Gene set analysis is a mainstay of functional genomics, but it relies on manually curated databases of gene functions that are incomplete and unaware of biological context. Here we evaluate the ability of OpenAI’s GPT-4, a Large Language Model (LLM), to develop hypotheses about common gene functions from its embedded biomedical knowledge. We created a GPT-4 pipeline to label gene sets with names that summarize their consensus functions, substantiated by analysis text and citations. Benchmarking against named gene sets in the Gene Ontology, GPT-4 generated very similar names in 50% of cases, while in most remaining cases it recovered the name of a more general concept. In gene sets discovered in ‘omics data, GPT-4 names were more informative than gene set enrichment, with supporting statements and citations that largely verified in human review. The ability to rapidly synthesize common gene functions positions LLMs as valuable functional genomics assistants.

[end paper 1]

[begin paper 2]

PMCID = 11422740

Title = Prompt Engineering Paradigms for Medical Applications: Scoping Review

Prompt engineering, focusing on crafting effective prompts to large language models (LLMs), has garnered attention for its capabilities at harnessing the potential of LLMs. This is even more crucial in the medical domain due to its specialized terminology and language technicity. Clinical natural language processing applications must navigate complex language and ensure privacy compliance. Prompt engineering offers a novel approach by designing tailored prompts to guide models in exploiting clinically relevant information from complex medical texts. Despite its promise, the efficacy of prompt engineering in the medical domain remains to be fully explored.

The aim of the study is to review research efforts and technical approaches in prompt engineering for medical applications as well as provide an overview of opportunities and challenges for clinical practice.

Databases indexing the fields of medicine, computer science, and medical informatics were queried in order to identify relevant published papers. Since prompt engineering is an emerging field, preprint databases were also considered. Multiple data were extracted, such as the prompt paradigm, the involved LLMs, the languages of the study, the domain of the topic, the baselines, and several learning, design, and architecture strategies specific to prompt engineering. We include studies that apply prompt engineering–based methods to the medical domain, published between 2022 and 2024, and covering multiple prompt paradigms such as prompt learning (PL), prompt tuning (PT), and prompt design (PD).

We included 114 recent prompt engineering studies. Among the 3 prompt paradigms, we have observed that PD is the most prevalent (78 papers). In 12 papers, PD, PL, and PT terms were used interchangeably. While ChatGPT is the most commonly used LLM, we have identified 7 studies using this LLM on a sensitive clinical data set. Chain-of-thought, present in 17 studies, emerges as the most frequent PD technique. While PL and PT papers typically provide a baseline for evaluating prompt-based approaches, 61% (48/78) of the PD studies do not report any nonprompt-related baseline. Finally, we individually examine each of the key prompt engineering–specific information reported across papers and find that many studies neglect to explicitly mention them, posing a challenge for advancing prompt engineering research.

In addition to reporting on trends and the scientific landscape of prompt engineering, we provide reporting guidelines for future studies to help advance research in the medical field. We also disclose tables and figures summarizing medical prompt engineering papers available and hope that future contributions will leverage these existing works to better advance the field.

[end paper 2]

[begin paper 3]

PMCID = 11480249

Title = Confronting the data deluge: How artificial intelligence can be used in the study of plant stress

The advent of the genomics era enabled the generation of high-throughput data and computational methods that serve as powerful hypothesis-generating tools to understand the genomic and gene functional basis of plant stress resilience. The proliferation of experimental and analytical methods used in biology has resulted in a situation where plentiful data exists, but the volume and heterogeneity of this data has made analysis a significant challenge. Current advanced deep-learning models have displayed an unprecedented level of comprehension and problem-solving ability, and have been used to predict gene structure, function and expression based on DNA or protein sequence, and prominently also their use in high-throughput phenomics in agriculture. However, the application of deep-learning models to understand gene regulatory and signalling behaviour is still in its infancy. We discuss in this review the availability of data resources and bioinformatic tools, and several applications of these advanced ML/AI models in the context of plant stress response, and demonstrate the use of a publicly available LLM (ChatGPT) to derive a knowledge graph of various experimental and computational methods used in the study of plant stress. We hope this will stimulate further interest in collaboration between computer scientists, computational biologists and plant scientists to distil the deluge of genomic, transcriptomic, proteomic, metabolomic and phenomic data into meaningful knowledge that can be used for the benefit of humanity.

[end paper 3]

[begin paper 4]

PMCID = 11639975

Title = EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy

In recent years, large language models have shown great potential to enhance traditional medical image processing by incorporating multimodality information into decision-making. Conventional artificial intelligence systems solely rely on images to make predictions or decisions. However, information from medical reports can provide invaluable information for the system to curate its decision. Here we are presenting a multimodality language-vision model and framework for accurate segmentation of medical images.

Background/Objectives: Lung cancer is a devastating disease with the highest mortality rate among cancer types. Over 60% of non-small cell lung cancer (NSCLC) patients, accounting for 87% of lung cancer diagnoses, require radiation therapy. Rapid treatment initiation significantly increases the patient’s survival rate and reduces the mortality rate. Accurate tumor segmentation is a critical step in diagnosing and treating NSCLC. Manual segmentation is time- and labor-consuming and causes delays in treatment initiation. Although many lung nodule detection methods, including deep learning-based models, have been proposed. Most of these methods still have a long-standing problem of high false positives (FPs). Methods: Here, we developed an electronic health record (EHR)-guided lung tumor auto-segmentation called EXACT-Net (EHR-enhanced eXACtitude in Tumor segmentation), where the extracted information from EHRs using a pre-trained large language model (LLM) was used to remove the FPs and keep the TP nodules only. Results: The auto-segmentation model was trained on NSCLC patients’ computed tomography (CT), and the pre-trained LLM was used with the zero-shot learning approach. Our approach resulted in a 250% boost in successful nodule detection using the data from ten NSCLC patients treated in our institution. Conclusions: We demonstrated that combining vision-language information in EXACT-Net multi-modal AI framework greatly enhances the performance of vision only models, paving the road to multimodal AI framework for medical image processing.

[end paper 4]

[begin paper 5]

PMCID = 11545079

Title = The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning

Artificial intelligence, now one of the most promising frontiers of medicine, has a long and tumultuous history punctuated by successes and failures. One of its successes was its application to medical images. We reconstruct the timeline of the advancements in this field, from its origins in the 1940s before crossing medical images to early applications of machine learning to radiology, to the present era where artificial intelligence is revolutionizing radiology.

Artificial intelligence (AI), the wide spectrum of technologies aiming to give machines or computers the ability to perform human-like cognitive functions, began in the 1940s with the first abstract models of intelligent machines. Soon after, in the 1950s and 1960s, machine learning algorithms such as neural networks and decision trees ignited significant enthusiasm. More recent advancements include the refinement of learning algorithms, the development of convolutional neural networks to efficiently analyze images, and methods to synthesize new images. This renewed enthusiasm was also due to the increase in computational power with graphical processing units and the availability of large digital databases to be mined by neural networks. AI soon began to be applied in medicine, first through expert systems designed to support the clinician’s decision and later with neural networks for the detection, classification, or segmentation of malignant lesions in medical images. A recent prospective clinical trial demonstrated the non-inferiority of AI alone compared with a double reading by two radiologists on screening mammography. Natural language processing, recurrent neural networks, transformers, and generative models have both improved the capabilities of making an automated reading of medical images and moved AI to new domains, including the text analysis of electronic health records, image self-labeling, and self-reporting. The availability of open-source and free libraries, as well as powerful computing resources, has greatly facilitated the adoption of deep learning by researchers and clinicians. Key concerns surrounding AI in healthcare include the need for clinical trials to demonstrate efficacy, the perception of AI tools as ‘black boxes’ that require greater interpretability and explainability, and ethical issues related to ensuring fairness and trustworthiness in AI systems. Thanks to its versatility and impressive results, AI is one of the most promising resources for frontier research and applications in medicine, in particular for oncological applications.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Semantic drift and LLM in clinical applications":

[begin paper 1]

PMCID = 10160120

Title = The SciQA Scientific Question Answering Benchmark for Scholarly Knowledge

Knowledge graphs have gained increasing popularity in the last decade in science and technology. However, knowledge graphs are currently relatively simple to moderate semantic structures that are mainly a collection of factual statements. Question answering (QA) benchmarks and systems were so far mainly geared towards encyclopedic knowledge graphs such as DBpedia and Wikidata. We present SciQA a scientific QA benchmark for scholarly knowledge. The benchmark leverages the Open Research Knowledge Graph (ORKG) which includes almost 170,000 resources describing research contributions of almost 15,000 scholarly articles from 709 research fields. Following a bottom-up methodology, we first manually developed a set of 100 complex questions that can be answered using this knowledge graph. Furthermore, we devised eight question templates with which we automatically generated further 2465 questions, that can also be answered with the ORKG. The questions cover a range of research fields and question types and are translated into corresponding SPARQL queries over the ORKG. Based on two preliminary evaluations, we show that the resulting SciQA benchmark represents a challenging task for next-generation QA systems. This task is part of the open competitions at the 22nd International Semantic Web Conference 2023 as the Scholarly Question Answering over Linked Data (QALD) Challenge.

[end paper 1]

[begin paper 2]

PMCID = 10629494

Title = Language models and psychological sciences

Large language models (LLMs) are demonstrating impressive performance on many reasoning and problem-solving tasks from cognitive psychology. When tested, their accuracy is often on par with average neurotypical adults, challenging long-standing critiques of associative models. Here we analyse recent findings at the intersection of LLMs and cognitive science. Here we discuss how modern LLMs resurrect associationist principles, with abilities like long-distance associations enabling complex reasoning. While limitations remain in areas like causal cognition and planning, phenomena like emergence suggest room for growth. Providing examples and increasing the dimensions of the network are methods that further improve LLM abilities, mirroring facilitation effects in human cognition. Analysis of LLMs errors provides insight into human cognitive biases. Overall, we argue LLMs represent a promising development for cognitive modelling, enabling new explorations of the mechanisms underlying intelligence and reasoning from an associationist point of view. Carefully evaluating LLMs with the tools of cognitive psychology will further understand the building blocks of the human mind.

[end paper 2]

[begin paper 3]

PMCID = 11929979

Title = Digital evolution: Novo Nordisk’s shift to ontology-based data management

The amount of biomedical data is growing, and managing it is increasingly challenging. While Findable, Accessible, Interoperable and Reusable (FAIR) data principles provide guidance, their adoption has proven difficult, especially in larger enterprises like pharmaceutical companies. In this manuscript, we describe how we leverage an Ontology-Based Data Management (OBDM) strategy for digital transformation in Novo Nordisk Research & Early Development. Here, we include both our technical blueprint and our approach for organizational change management. We further discuss how such an OBDM ecosystem plays a pivotal role in the organization’s digital aspirations for data federation and discovery fuelled by artificial intelligence. Our aim for this paper is to share the lessons learned in order to foster dialogue with parties navigating similar waters while collectively advancing the efforts in the fields of data management, semantics and data driven drug discovery.

[end paper 3]

[begin paper 4]

PMCID = 11441322

Title = Biomedical knowledge graph-optimized prompt generation for large language models

Large language models (LLMs) are being adopted at an unprecedented rate, yet still face challenges in knowledge-intensive domains such as biomedicine. Solutions such as pretraining and domain-specific fine-tuning add substantial computational overhead, requiring further domain-expertise. Here, we introduce a token-optimized and robust Knowledge Graph-based Retrieval Augmented Generation (KG-RAG) framework by leveraging a massive biomedical KG (SPOKE) with LLMs such as Llama-2-13b, GPT-3.5-Turbo, and GPT-4, to generate meaningful biomedical text rooted in established knowledge.

Compared to the existing RAG technique for Knowledge Graphs, the proposed method utilizes minimal graph schema for context extraction and uses embedding methods for context pruning. This optimization in context extraction results in more than 50% reduction in token consumption without compromising the accuracy, making a cost-effective and robust RAG implementation on proprietary LLMs. KG-RAG consistently enhanced the performance of LLMs across diverse biomedical prompts by generating responses rooted in established knowledge, accompanied by accurate provenance and statistical evidence (if available) to substantiate the claims. Further benchmarking on human curated datasets, such as biomedical true/false and multiple-choice questions (MCQ), showed a remarkable 71% boost in the performance of the Llama-2 model on the challenging MCQ dataset, demonstrating the framework’s capacity to empower open-source models with fewer parameters for domain-specific questions. Furthermore, KG-RAG enhanced the performance of proprietary GPT models, such as GPT-3.5 and GPT-4. In summary, the proposed framework combines explicit and implicit knowledge of KG and LLM in a token optimized fashion, thus enhancing the adaptability of general-purpose LLMs to tackle domain-specific questions in a cost-effective fashion.

SPOKE KG can be accessed at https://spoke.rbvi.ucsf.edu/neighborhood.html. It can also be accessed using REST-API (https://spoke.rbvi.ucsf.edu/swagger/). KG-RAG code is made available at https://github.com/BaranziniLab/KG_RAG. Biomedical benchmark datasets used in this study are made available to the research community in the same GitHub repository.

[end paper 4]

[begin paper 5]

PMCID = 11925797

Title = Computational tools and data integration to accelerate vaccine development: challenges, opportunities, and future directions

The development of effective vaccines is crucial for combating current and emerging pathogens. Despite significant advances in the field of vaccine development there remain numerous challenges including the lack of standardized data reporting and curation practices, making it difficult to determine correlates of protection from experimental and clinical studies. Significant gaps in data and knowledge integration can hinder vaccine development which relies on a comprehensive understanding of the interplay between pathogens and the host immune system. In this review, we explore the current landscape of vaccine development, highlighting the computational challenges, limitations, and opportunities associated with integrating diverse data types for leveraging artificial intelligence (AI) and machine learning (ML) techniques in vaccine design. We discuss the role of natural language processing, semantic integration, and causal inference in extracting valuable insights from published literature and unstructured data sources, as well as the computational modeling of immune responses. Furthermore, we highlight specific challenges associated with uncertainty quantification in vaccine development and emphasize the importance of establishing standardized data formats and ontologies to facilitate the integration and analysis of heterogeneous data. Through data harmonization and integration, the development of safe and effective vaccines can be accelerated to improve public health outcomes. Looking to the future, we highlight the need for collaborative efforts among researchers, data scientists, and public health experts to realize the full potential of AI-assisted vaccine design and streamline the vaccine development process.

[end paper 5]



Here are the top 3 articles on PubMed Central for the query "Building clinician trust in LLM-based EHR tools":

[begin paper 1]

PMCID = 11809463

Title = Applications of Large Language Models in the Field of Suicide Prevention: Scoping Review

Prevention of suicide is a global health priority. Approximately 800,000 individuals die by suicide yearly, and for every suicide death, there are another 20 estimated suicide attempts. Large language models (LLMs) hold the potential to enhance scalable, accessible, and affordable digital services for suicide prevention and self-harm interventions. However, their use also raises clinical and ethical questions that require careful consideration.

This scoping review aims to identify emergent trends in LLM applications in the field of suicide prevention and self-harm research. In addition, it summarizes key clinical and ethical considerations relevant to this nascent area of research.

Searches were conducted in 4 databases (PsycINFO, Embase, PubMed, and IEEE Xplore) in February 2024. Eligible studies described the application of LLMs for suicide or self-harm prevention, detection, or management. English-language peer-reviewed articles and conference proceedings were included, without date restrictions. Narrative synthesis was used to synthesize study characteristics, objectives, models, data sources, proposed clinical applications, and ethical considerations. This review adhered to the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) standards.

Of the 533 studies identified, 36 (6.8%) met the inclusion criteria. An additional 7 studies were identified through citation chaining, resulting in 43 studies for review. The studies showed a bifurcation of publication fields, with varying publication norms between computer science and mental health. While most of the studies (33/43, 77%) focused on identifying suicide risk, newer applications leveraging generative functions (eg, support, education, and training) are emerging. Social media was the most common source of LLM training data. Bidirectional Encoder Representations from Transformers (BERT) was the predominant model used, although generative pretrained transformers (GPTs) featured prominently in generative applications. Clinical LLM applications were reported in 60% (26/43) of the studies, often for suicide risk detection or as clinical assistance tools. Ethical considerations were reported in 33% (14/43) of the studies, with privacy, confidentiality, and consent strongly represented.

This evolving research area, bridging computer science and mental health, demands a multidisciplinary approach. While open access models and datasets will likely shape the field of suicide prevention, documenting their limitations and potential biases is crucial. High-quality training data are essential for refining these models and mitigating unwanted biases. Policies that address ethical concerns—particularly those related to privacy and security when using social media data—are imperative. Limitations include high variability across disciplines in how LLMs and study methodology are reported. The emergence of generative artificial intelligence signals a shift in approach, particularly in applications related to care, support, and education, such as improved crisis care and gatekeeper training methods, clinician copilot models, and improved educational practices. Ongoing human oversight—through human-in-the-loop testing or expert external validation—is essential for responsible development and use.

OSF Registries osf.io/nckq7; https://osf.io/nckq7

[end paper 1]

[begin paper 2]

PMCID = 11986386

Title = Generative Large Language Model—Powered Conversational AI App for Personalized Risk Assessment: Case Study in COVID-19

Large language models (LLMs) have demonstrated powerful capabilities in natural language tasks and are increasingly being integrated into health care for tasks like disease risk assessment. Traditional machine learning methods rely on structured data and coding, limiting their flexibility in dynamic clinical environments. This study presents a novel approach to disease risk assessment using generative LLMs through conversational artificial intelligence (AI), eliminating the need for programming.

This study evaluates the use of pretrained generative LLMs, including LLaMA2-7b and Flan-T5-xl, for COVID-19 severity prediction with the goal of enabling a real-time, no-code, risk assessment solution through chatbot-based, question-answering interactions. To contextualize their performance, we compare LLMs with traditional machine learning classifiers, such as logistic regression, extreme gradient boosting (XGBoost), and random forest, which rely on tabular data.

We fine-tuned LLMs using few-shot natural language examples from a dataset of 393 pediatric patients, developing a mobile app that integrates these models to provide real-time, no-code, COVID-19 severity risk assessment through clinician-patient interaction. The LLMs were compared with traditional classifiers across different experimental settings, using the area under the curve (AUC) as the primary evaluation metric. Feature importance derived from LLM attention layers was also analyzed to enhance interpretability.

Generative LLMs demonstrated strong performance in low-data settings. In zero-shot scenarios, the T0-3b-T model achieved an AUC of 0.75, while other LLMs, such as T0pp(8bit)-T and Flan-T5-xl-T, reached 0.67 and 0.69, respectively. At 2-shot settings, logistic regression and random forest achieved an AUC of 0.57, while Flan-T5-xl-T and T0-3b-T obtained 0.69 and 0.65, respectively. By 32-shot settings, Flan-T5-xl-T reached 0.70, similar to logistic regression (0.69) and random forest (0.68), while XGBoost improved to 0.65. These results illustrate the differences in how generative LLMs and traditional models handle the increasing data availability. LLMs perform well in low-data scenarios, whereas traditional models rely more on structured tabular data and labeled training examples. Furthermore, the mobile app provides real-time, COVID-19 severity assessments and personalized insights through attention-based feature importance, adding value to the clinical interpretation of the results.

Generative LLMs provide a robust alternative to traditional classifiers, particularly in scenarios with limited labeled data. Their ability to handle unstructured inputs and deliver personalized, real-time assessments without coding makes them highly adaptable to clinical settings. This study underscores the potential of LLM-powered conversational artificial intelligence (AI) in health care and encourages further exploration of its use for real-time, disease risk assessment and decision-making support.

[end paper 2]

[begin paper 3]

PMCID = 10834163

Title = Artificial intelligence: revolutionizing cardiology with large language models

Overview of input sources (top) to train or fine-tune cardio large language models and different applications (bottom). ECG, electrocardiogram; Q&A, questions and answers.

Natural language processing techniques are having an increasing impact on clinical care from patient, clinician, administrator, and research perspective. Among others are automated generation of clinical notes and discharge letters, medical term coding for billing, medical chatbots both for patients and clinicians, data enrichment in the identification of disease symptoms or diagnosis, cohort selection for clinical trial, and auditing purposes. In the review, an overview of the history in natural language processing techniques developed with brief technical background is presented. Subsequently, the review will discuss implementation strategies of natural language processing tools, thereby specifically focusing on large language models, and conclude with future opportunities in the application of such techniques in the field of cardiology.

[end paper 3]



