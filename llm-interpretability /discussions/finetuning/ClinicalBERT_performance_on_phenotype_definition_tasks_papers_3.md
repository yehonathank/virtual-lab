## User

This is the beginning of an individual meeting with Computational Linguist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic ClinicalBERT performance on phenotype definition tasks in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on ClinicalBERT performance on phenotype definition tasks to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on ClinicalBERT performance on phenotype definition tasks. Include both general queries about ClinicalBERT performance on phenotype definition tasks and queries that specifically relate ClinicalBERT performance on phenotype definition tasks to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Computational Linguist, please provide your response to the agenda.

## Computational Linguist

To address the agenda, I'll first outline a series of search queries that will help us gather relevant scientific papers on ClinicalBERT performance on phenotype definition tasks. These queries will focus on both general aspects and specific connections to LLM interpretability, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
queries = [
    "ClinicalBERT performance phenotype definition",
    "ClinicalBERT interpretability phenotype definition",
    "ClinicalBERT electronic phenotype definition clinical applications",
    "ClinicalBERT phenotype definition clinician trust",
    "ClinicalBERT LLM interpretability electronic phenotype"
]
```

Next, I will use these queries to search for relevant scientific papers. Once I have the results, I will provide a Python dictionary mapping PMCIDs to titles. Let's proceed with the search.

## Computational Linguist

Based on the search queries, here are the PMCIDs and titles of the papers that are relevant to ClinicalBERT performance on phenotype definition tasks and related topics:

```python
papers = {
    "10368879": "Generalizability of machine learning methods in detecting adverse drug events from clinical narratives in electronic medical records",
    "8800516": "Sepsis prediction, early detection, and identification using clinical text for machine learning: a systematic review",
    "11041460": "Developing an Inpatient Electronic Medical Record Phenotype for Hospital-Acquired Pressure Injuries: Case Study Using Natural Language Processing Models",
    "7665985": "Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts",
    "9979798": "How data science and AI-based technologies impact genomics",
    "11287876": "Transformer models in biomedicine",
    "10474977": "Cerebrovascular disease case identification in inpatient electronic medical record data using natural language processing",
    "11585305": "Artificial intelligence research in radiation oncology: a practical guide for the clinician on concepts and methods",
    "11494256": "Use of SNOMED CT in Large Language Models: Scoping Review",
    "11221943": "Leveraging GPT-4 for identifying cancer phenotypes in electronic health records: a performance comparison between GPT-4, GPT-3.5-turbo, Flan-T5, Llama-3-8B, and spaCy’s rule-based and machine learning-based methods",
    "10801236": "Enhancing phenotype recognition in clinical notes using large language models: PhenoBCBERT and PhenoGPT",
    "10659449": "Enhancing Phenotype Recognition in Clinical Notes Using Large Language Models: PhenoBCBERT and PhenoGPT"
}
```

These papers cover various aspects of ClinicalBERT's application in phenotype definition tasks, LLM interpretability, and clinical applications, providing a comprehensive foundation for understanding and developing an interpretability tool.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "ClinicalBERT performance phenotype definition":

[begin paper 1]

PMCID = 10368879

Title = Generalizability of machine learning methods in detecting adverse drug events from clinical narratives in electronic medical records

We assessed the generalizability of machine learning methods using natural language processing (NLP) techniques to detect adverse drug events (ADEs) from clinical narratives in electronic medical records (EMRs). We constructed a new corpus correlating drugs with adverse drug events using 1,394 clinical notes of 47 randomly selected patients who received immune checkpoint inhibitors (ICIs) from 2011 to 2018 at The Ohio State University James Cancer Hospital, annotating 189 drug-ADE relations in single sentences within the medical records. We also used data from Harvard’s publicly available 2018 National Clinical Challenge (n2c2), which includes 505 discharge summaries with annotations of 1,355 single-sentence drug-ADE relations. We applied classical machine learning (support vector machine (SVM)), deep learning (convolutional neural network (CNN) and bidirectional long short-term memory (BiLSTM)), and state-of-the-art transformer-based (bidirectional encoder representations from transformers (BERT) and ClinicalBERT) methods trained and tested in the two different corpora and compared performance among them to detect drug–ADE relationships. ClinicalBERT detected drug–ADE relationships better than the other methods when trained using our dataset and tested in n2c2 (ClinicalBERT F-score, 0.78; other methods, F-scores, 0.61–0.73) and when trained using the n2c2 dataset and tested in ours (ClinicalBERT F-score, 0.74; other methods, F-scores, 0.55–0.72). Comparison among several machine learning methods demonstrated the superior performance and, therefore, the greatest generalizability of findings of ClinicalBERT for the detection of drug–ADE relations from clinical narratives in electronic medical records. 

[end paper 1]

[begin paper 2]

PMCID = 8800516

Title = Sepsis prediction, early detection, and identification using clinical text for machine learning: a systematic review

To determine the effects of using unstructured clinical text in machine learning (ML) for prediction, early detection, and identification of sepsis.

PubMed, Scopus, ACM DL, dblp, and IEEE Xplore databases were searched. Articles utilizing clinical text for ML or natural language processing (NLP) to detect, identify, recognize, diagnose, or predict the onset, development, progress, or prognosis of systemic inflammatory response syndrome, sepsis, severe sepsis, or septic shock were included. Sepsis definition, dataset, types of data, ML models, NLP techniques, and evaluation metrics were extracted.

The clinical text used in models include narrative notes written by nurses, physicians, and specialists in varying situations. This is often combined with common structured data such as demographics, vital signs, laboratory data, and medications. Area under the receiver operating characteristic curve (AUC) comparison of ML methods showed that utilizing both text and structured data predicts sepsis earlier and more accurately than structured data alone. No meta-analysis was performed because of incomparable measurements among the 9 included studies.

Studies focused on sepsis identification or early detection before onset; no studies used patient histories beyond the current episode of care to predict sepsis. Sepsis definition affects reporting methods, outcomes, and results. Many methods rely on continuous vital sign measurements in intensive care, making them not easily transferable to general ward units.

Approaches were heterogeneous, but studies showed that utilizing both unstructured text and structured data in ML can improve identification and early detection of sepsis.

[end paper 2]

[begin paper 3]

PMCID = 11041460

Title = Developing an Inpatient Electronic Medical Record Phenotype for Hospital-Acquired Pressure Injuries: Case Study Using Natural Language Processing Models

Surveillance of hospital-acquired pressure injuries (HAPI) is often suboptimal when relying on administrative health data, as International Classification of Diseases (ICD) codes are known to have long delays and are undercoded. We leveraged natural language processing (NLP) applications on free-text notes, particularly the inpatient nursing notes, from electronic medical records (EMRs), to more accurately and timely identify HAPIs.

This study aimed to show that EMR-based phenotyping algorithms are more fitted to detect HAPIs than ICD-10-CA algorithms alone, while the clinical logs are recorded with higher accuracy via NLP using nursing notes.

Patients with HAPIs were identified from head-to-toe skin assessments in a local tertiary acute care hospital during a clinical trial that took place from 2015 to 2018 in Calgary, Alberta, Canada. Clinical notes documented during the trial were extracted from the EMR database after the linkage with the discharge abstract database. Different combinations of several types of clinical notes were processed by sequential forward selection during the model development. Text classification algorithms for HAPI detection were developed using random forest (RF), extreme gradient boosting (XGBoost), and deep learning models. The classification threshold was tuned to enable the model to achieve similar specificity to an ICD-based phenotyping study. Each model’s performance was assessed, and comparisons were made between the metrics, including sensitivity, positive predictive value, negative predictive value, and F1-score.

Data from 280 eligible patients were used in this study, among whom 97 patients had HAPIs during the trial. RF was the optimal performing model with a sensitivity of 0.464 (95% CI 0.365-0.563), specificity of 0.984 (95% CI 0.965-1.000), and F1-score of 0.612 (95% CI of 0.473-0.751). The machine learning (ML) model reached higher sensitivity without sacrificing much specificity compared to the previously reported performance of ICD-based algorithms.

The EMR-based NLP phenotyping algorithms demonstrated improved performance in HAPI case detection over ICD-10-CA codes alone. Daily generated nursing notes in EMRs are a valuable data resource for ML models to accurately detect adverse events. The study contributes to enhancing automated health care quality and safety surveillance.

[end paper 3]

[begin paper 4]

PMCID = 7665985

Title = Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts

Currently, a major limitation for natural language processing (NLP) analyses in clinical applications is that concepts are not effectively referenced in various forms across different texts. This paper introduces Multi-Ontology Refined Embeddings (MORE), a novel hybrid framework that incorporates domain knowledge from multiple ontologies into a distributional semantic model, learned from a corpus of clinical text.

We use the RadCore and MIMIC-III free-text datasets for the corpus-based component of MORE. For the ontology-based part, we use the Medical Subject Headings (MeSH) ontology and three state-of-the-art ontology-based similarity measures. In our approach, we propose a new learning objective, modified from the sigmoid cross-entropy objective function.

We used two established datasets of semantic similarities among biomedical concept pairs to evaluate the quality of the generated word embeddings. On the first dataset with 29 concept pairs, with similarity scores established by physicians and medical coders, MORE’s similarity scores have the highest combined correlation (0.633), which is 5.0% higher than that of the baseline model, and 12.4% higher than that of the best ontology-based similarity measure. On the second dataset with 449 concept pairs, MORE’s similarity scores have a correlation of 0.481, based on the average of four medical residents’ similarity ratings, and that outperforms the skip-gram model by 8.1%, and the best ontology measure by 6.9%. Furthermore, MORE outperforms three pre-trained transformer-based word embedding models (i.e., BERT, ClinicalBERT, and BioBERT) on both datasets.

MORE incorporates knowledge from several biomedical ontologies into an existing corpus-based distributional semantics model, improving both the accuracy of the learned word embeddings and the extensibility of the model to a broader range of biomedical concepts. MORE allows for more accurate clustering of concepts across a wide range of applications, such as analyzing patient health records to identify subjects with similar pathologies, or integrating heterogeneous clinical data to improve interoperability between hospitals.

[end paper 4]

[begin paper 5]

PMCID = 9979798

Title = How data science and AI-based technologies impact genomics

Advancements in high-throughput sequencing have yielded vast amounts of genomic data, which are studied using genome-wide association study (GWAS)/phenome-wide association study (PheWAS) methods to identify associations between the genotype and phenotype. The associated findings have contributed to pharmacogenomics and improved clinical decision support at the point of care in many healthcare systems. However, the accumulation of genomic data from sequencing and clinical data from electronic health records (EHRs) poses significant challenges for data scientists. Following the rise of artificial intelligence (AI) technology such as machine learning and deep learning, an increasing number of GWAS/PheWAS studies have successfully leveraged this technology to overcome the aforementioned challenges. In this review, we focus on the application of data science and AI technology in three areas, including risk prediction and identification of causal single-nucleotide polymorphisms, EHR-based phenotyping and CRISPR guide RNA design. Additionally, we highlight a few emerging AI technologies, such as transfer learning and multi-view learning, which will or have started to benefit genomic studies.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "ClinicalBERT interpretability phenotype definition":

[begin paper 1]

PMCID = 9979798

Title = How data science and AI-based technologies impact genomics

Advancements in high-throughput sequencing have yielded vast amounts of genomic data, which are studied using genome-wide association study (GWAS)/phenome-wide association study (PheWAS) methods to identify associations between the genotype and phenotype. The associated findings have contributed to pharmacogenomics and improved clinical decision support at the point of care in many healthcare systems. However, the accumulation of genomic data from sequencing and clinical data from electronic health records (EHRs) poses significant challenges for data scientists. Following the rise of artificial intelligence (AI) technology such as machine learning and deep learning, an increasing number of GWAS/PheWAS studies have successfully leveraged this technology to overcome the aforementioned challenges. In this review, we focus on the application of data science and AI technology in three areas, including risk prediction and identification of causal single-nucleotide polymorphisms, EHR-based phenotyping and CRISPR guide RNA design. Additionally, we highlight a few emerging AI technologies, such as transfer learning and multi-view learning, which will or have started to benefit genomic studies.

[end paper 1]

[begin paper 2]

PMCID = 11287876

Title = Transformer models in biomedicine

Deep neural networks (DNN) have fundamentally revolutionized the artificial intelligence (AI) field. The transformer model is a type of DNN that was originally used for the natural language processing tasks and has since gained more and more attention for processing various kinds of sequential data, including biological sequences and structured electronic health records. Along with this development, transformer-based models such as BioBERT, MedBERT, and MassGenie have been trained and deployed by researchers to answer various scientific questions originating in the biomedical domain. In this paper, we review the development and application of transformer models for analyzing various biomedical-related datasets such as biomedical textual data, protein sequences, medical structured-longitudinal data, and biomedical images as well as graphs. Also, we look at explainable AI strategies that help to comprehend the predictions of transformer-based models. Finally, we discuss the limitations and challenges of current models, and point out emerging novel research directions.

[end paper 2]

[begin paper 3]

PMCID = 10474977

Title = Cerebrovascular disease case identification in inpatient electronic medical record data using natural language processing

Abstracting cerebrovascular disease (CeVD) from inpatient electronic medical records (EMRs) through natural language processing (NLP) is pivotal for automated disease surveillance and improving patient outcomes. Existing methods rely on coders’ abstraction, which has time delays and under-coding issues. This study sought to develop an NLP-based method to detect CeVD using EMR clinical notes.

CeVD status was confirmed through a chart review on randomly selected hospitalized patients who were 18 years or older and discharged from 3 hospitals in Calgary, Alberta, Canada, between January 1 and June 30, 2015. These patients’ chart data were linked to administrative discharge abstract database (DAD) and Sunrise™ Clinical Manager (SCM) EMR database records by Personal Health Number (a unique lifetime identifier) and admission date. We trained multiple natural language processing (NLP) predictive models by combining two clinical concept extraction methods and two supervised machine learning (ML) methods: random forest and XGBoost. Using chart review as the reference standard, we compared the model performances with those of the commonly applied International Classification of Diseases (ICD-10-CA) codes, on the metrics of sensitivity, specificity, positive predictive value (PPV), and negative predictive value (NPV).

Of the study sample (n = 3036), the prevalence of CeVD was 11.8% (n = 360); the median patient age was 63; and females accounted for 50.3% (n = 1528) based on chart data. Among 49 extracted clinical documents from the EMR, four document types were identified as the most influential text sources for identifying CeVD disease (“nursing transfer report,” “discharge summary,” “nursing notes,” and “inpatient consultation.”). The best performing NLP model was XGBoost, combining the Unified Medical Language System concepts extracted by cTAKES (e.g., top-ranked concepts, “Cerebrovascular accident” and “Transient ischemic attack”), and the term frequency-inverse document frequency vectorizer. Compared with ICD codes, the model achieved higher validity overall, such as sensitivity (25.0% vs 70.0%), specificity (99.3% vs 99.1%), PPV (82.6 vs. 87.8%), and NPV (90.8% vs 97.1%).

The NLP algorithm developed in this study performed better than the ICD code algorithm in detecting CeVD. The NLP models could result in an automated EMR tool for identifying CeVD cases and be applied for future studies such as surveillance, and longitudinal studies.

The online version contains supplementary material available at 10.1186/s40708-023-00203-w.

[end paper 3]

[begin paper 4]

PMCID = 11585305

Title = Artificial intelligence research in radiation oncology: a practical guide for the clinician on concepts and methods

The use of artificial intelligence (AI) holds great promise for radiation oncology, with many applications being reported in the literature, including some of which are already in clinical use. These are mainly in areas where AI provides benefits in efficiency (such as automatic segmentation and treatment planning). Prediction models that directly impact patient decision-making are far less mature in terms of their application in clinical practice. Part of the limited clinical uptake of these models may be explained by the need for broader knowledge, among practising clinicians within the medical community, about the processes of AI development. This lack of understanding could lead to low commitment to AI research, widespread scepticism, and low levels of trust. This attitude towards AI may be further negatively impacted by the perception that deep learning is a “black box” with inherently low transparency. Thus, there is an unmet need to train current and future clinicians in the development and application of AI in medicine. Improving clinicians’ AI-related knowledge and skills is necessary to enhance multidisciplinary collaboration between data scientists and physicians, that is, involving a clinician in the loop during AI development. Increased knowledge may also positively affect the acceptance and trust of AI. This paper describes the necessary steps involved in AI research and development, and thus identifies the possibilities, limitations, challenges, and opportunities, as seen from the perspective of a practising radiation oncologist. It offers the clinician with limited knowledge and experience in AI valuable tools to evaluate research papers related to an AI model application.

[end paper 4]

[begin paper 5]

PMCID = 10654844

Title = An open natural language processing (NLP) framework for EHR-based clinical research: a case demonstration using the National COVID Cohort Collaborative (N3C)

Despite recent methodology advancements in clinical natural language processing (NLP), the adoption of clinical NLP models within the translational research community remains hindered by process heterogeneity and human factor variations. Concurrently, these factors also dramatically increase the difficulty in developing NLP models in multi-site settings, which is necessary for algorithm robustness and generalizability. Here, we reported on our experience developing an NLP solution for Coronavirus Disease 2019 (COVID-19) signs and symptom extraction in an open NLP framework from a subset of sites participating in the National COVID Cohort (N3C). We then empirically highlight the benefits of multi-site data for both symbolic and statistical methods, as well as highlight the need for federated annotation and evaluation to resolve several pitfalls encountered in the course of these efforts.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "ClinicalBERT electronic phenotype definition clinical applications":

[begin paper 1]

PMCID = 10368879

Title = Generalizability of machine learning methods in detecting adverse drug events from clinical narratives in electronic medical records

We assessed the generalizability of machine learning methods using natural language processing (NLP) techniques to detect adverse drug events (ADEs) from clinical narratives in electronic medical records (EMRs). We constructed a new corpus correlating drugs with adverse drug events using 1,394 clinical notes of 47 randomly selected patients who received immune checkpoint inhibitors (ICIs) from 2011 to 2018 at The Ohio State University James Cancer Hospital, annotating 189 drug-ADE relations in single sentences within the medical records. We also used data from Harvard’s publicly available 2018 National Clinical Challenge (n2c2), which includes 505 discharge summaries with annotations of 1,355 single-sentence drug-ADE relations. We applied classical machine learning (support vector machine (SVM)), deep learning (convolutional neural network (CNN) and bidirectional long short-term memory (BiLSTM)), and state-of-the-art transformer-based (bidirectional encoder representations from transformers (BERT) and ClinicalBERT) methods trained and tested in the two different corpora and compared performance among them to detect drug–ADE relationships. ClinicalBERT detected drug–ADE relationships better than the other methods when trained using our dataset and tested in n2c2 (ClinicalBERT F-score, 0.78; other methods, F-scores, 0.61–0.73) and when trained using the n2c2 dataset and tested in ours (ClinicalBERT F-score, 0.74; other methods, F-scores, 0.55–0.72). Comparison among several machine learning methods demonstrated the superior performance and, therefore, the greatest generalizability of findings of ClinicalBERT for the detection of drug–ADE relations from clinical narratives in electronic medical records. 

[end paper 1]

[begin paper 2]

PMCID = 9979798

Title = How data science and AI-based technologies impact genomics

Advancements in high-throughput sequencing have yielded vast amounts of genomic data, which are studied using genome-wide association study (GWAS)/phenome-wide association study (PheWAS) methods to identify associations between the genotype and phenotype. The associated findings have contributed to pharmacogenomics and improved clinical decision support at the point of care in many healthcare systems. However, the accumulation of genomic data from sequencing and clinical data from electronic health records (EHRs) poses significant challenges for data scientists. Following the rise of artificial intelligence (AI) technology such as machine learning and deep learning, an increasing number of GWAS/PheWAS studies have successfully leveraged this technology to overcome the aforementioned challenges. In this review, we focus on the application of data science and AI technology in three areas, including risk prediction and identification of causal single-nucleotide polymorphisms, EHR-based phenotyping and CRISPR guide RNA design. Additionally, we highlight a few emerging AI technologies, such as transfer learning and multi-view learning, which will or have started to benefit genomic studies.

[end paper 2]

[begin paper 3]

PMCID = 8800516

Title = Sepsis prediction, early detection, and identification using clinical text for machine learning: a systematic review

To determine the effects of using unstructured clinical text in machine learning (ML) for prediction, early detection, and identification of sepsis.

PubMed, Scopus, ACM DL, dblp, and IEEE Xplore databases were searched. Articles utilizing clinical text for ML or natural language processing (NLP) to detect, identify, recognize, diagnose, or predict the onset, development, progress, or prognosis of systemic inflammatory response syndrome, sepsis, severe sepsis, or septic shock were included. Sepsis definition, dataset, types of data, ML models, NLP techniques, and evaluation metrics were extracted.

The clinical text used in models include narrative notes written by nurses, physicians, and specialists in varying situations. This is often combined with common structured data such as demographics, vital signs, laboratory data, and medications. Area under the receiver operating characteristic curve (AUC) comparison of ML methods showed that utilizing both text and structured data predicts sepsis earlier and more accurately than structured data alone. No meta-analysis was performed because of incomparable measurements among the 9 included studies.

Studies focused on sepsis identification or early detection before onset; no studies used patient histories beyond the current episode of care to predict sepsis. Sepsis definition affects reporting methods, outcomes, and results. Many methods rely on continuous vital sign measurements in intensive care, making them not easily transferable to general ward units.

Approaches were heterogeneous, but studies showed that utilizing both unstructured text and structured data in ML can improve identification and early detection of sepsis.

[end paper 3]

[begin paper 4]

PMCID = 11041460

Title = Developing an Inpatient Electronic Medical Record Phenotype for Hospital-Acquired Pressure Injuries: Case Study Using Natural Language Processing Models

Surveillance of hospital-acquired pressure injuries (HAPI) is often suboptimal when relying on administrative health data, as International Classification of Diseases (ICD) codes are known to have long delays and are undercoded. We leveraged natural language processing (NLP) applications on free-text notes, particularly the inpatient nursing notes, from electronic medical records (EMRs), to more accurately and timely identify HAPIs.

This study aimed to show that EMR-based phenotyping algorithms are more fitted to detect HAPIs than ICD-10-CA algorithms alone, while the clinical logs are recorded with higher accuracy via NLP using nursing notes.

Patients with HAPIs were identified from head-to-toe skin assessments in a local tertiary acute care hospital during a clinical trial that took place from 2015 to 2018 in Calgary, Alberta, Canada. Clinical notes documented during the trial were extracted from the EMR database after the linkage with the discharge abstract database. Different combinations of several types of clinical notes were processed by sequential forward selection during the model development. Text classification algorithms for HAPI detection were developed using random forest (RF), extreme gradient boosting (XGBoost), and deep learning models. The classification threshold was tuned to enable the model to achieve similar specificity to an ICD-based phenotyping study. Each model’s performance was assessed, and comparisons were made between the metrics, including sensitivity, positive predictive value, negative predictive value, and F1-score.

Data from 280 eligible patients were used in this study, among whom 97 patients had HAPIs during the trial. RF was the optimal performing model with a sensitivity of 0.464 (95% CI 0.365-0.563), specificity of 0.984 (95% CI 0.965-1.000), and F1-score of 0.612 (95% CI of 0.473-0.751). The machine learning (ML) model reached higher sensitivity without sacrificing much specificity compared to the previously reported performance of ICD-based algorithms.

The EMR-based NLP phenotyping algorithms demonstrated improved performance in HAPI case detection over ICD-10-CA codes alone. Daily generated nursing notes in EMRs are a valuable data resource for ML models to accurately detect adverse events. The study contributes to enhancing automated health care quality and safety surveillance.

[end paper 4]

[begin paper 5]

PMCID = 7665985

Title = Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts

Currently, a major limitation for natural language processing (NLP) analyses in clinical applications is that concepts are not effectively referenced in various forms across different texts. This paper introduces Multi-Ontology Refined Embeddings (MORE), a novel hybrid framework that incorporates domain knowledge from multiple ontologies into a distributional semantic model, learned from a corpus of clinical text.

We use the RadCore and MIMIC-III free-text datasets for the corpus-based component of MORE. For the ontology-based part, we use the Medical Subject Headings (MeSH) ontology and three state-of-the-art ontology-based similarity measures. In our approach, we propose a new learning objective, modified from the sigmoid cross-entropy objective function.

We used two established datasets of semantic similarities among biomedical concept pairs to evaluate the quality of the generated word embeddings. On the first dataset with 29 concept pairs, with similarity scores established by physicians and medical coders, MORE’s similarity scores have the highest combined correlation (0.633), which is 5.0% higher than that of the baseline model, and 12.4% higher than that of the best ontology-based similarity measure. On the second dataset with 449 concept pairs, MORE’s similarity scores have a correlation of 0.481, based on the average of four medical residents’ similarity ratings, and that outperforms the skip-gram model by 8.1%, and the best ontology measure by 6.9%. Furthermore, MORE outperforms three pre-trained transformer-based word embedding models (i.e., BERT, ClinicalBERT, and BioBERT) on both datasets.

MORE incorporates knowledge from several biomedical ontologies into an existing corpus-based distributional semantics model, improving both the accuracy of the learned word embeddings and the extensibility of the model to a broader range of biomedical concepts. MORE allows for more accurate clustering of concepts across a wide range of applications, such as analyzing patient health records to identify subjects with similar pathologies, or integrating heterogeneous clinical data to improve interoperability between hospitals.

[end paper 5]



Here are the top 1 articles on PubMed Central for the query "ClinicalBERT phenotype definition clinician trust":

[begin paper 1]

PMCID = 11585305

Title = Artificial intelligence research in radiation oncology: a practical guide for the clinician on concepts and methods

The use of artificial intelligence (AI) holds great promise for radiation oncology, with many applications being reported in the literature, including some of which are already in clinical use. These are mainly in areas where AI provides benefits in efficiency (such as automatic segmentation and treatment planning). Prediction models that directly impact patient decision-making are far less mature in terms of their application in clinical practice. Part of the limited clinical uptake of these models may be explained by the need for broader knowledge, among practising clinicians within the medical community, about the processes of AI development. This lack of understanding could lead to low commitment to AI research, widespread scepticism, and low levels of trust. This attitude towards AI may be further negatively impacted by the perception that deep learning is a “black box” with inherently low transparency. Thus, there is an unmet need to train current and future clinicians in the development and application of AI in medicine. Improving clinicians’ AI-related knowledge and skills is necessary to enhance multidisciplinary collaboration between data scientists and physicians, that is, involving a clinician in the loop during AI development. Increased knowledge may also positively affect the acceptance and trust of AI. This paper describes the necessary steps involved in AI research and development, and thus identifies the possibilities, limitations, challenges, and opportunities, as seen from the perspective of a practising radiation oncologist. It offers the clinician with limited knowledge and experience in AI valuable tools to evaluate research papers related to an AI model application.

[end paper 1]



Here are the top 5 articles on PubMed Central for the query "ClinicalBERT LLM interpretability electronic phenotype":

[begin paper 1]

PMCID = 11494256

Title = Use of SNOMED CT in Large Language Models: Scoping Review

Large language models (LLMs) have substantially advanced natural language processing (NLP) capabilities but often struggle with knowledge-driven tasks in specialized domains such as biomedicine. Integrating biomedical knowledge sources such as SNOMED CT into LLMs may enhance their performance on biomedical tasks. However, the methodologies and effectiveness of incorporating SNOMED CT into LLMs have not been systematically reviewed.

This scoping review aims to examine how SNOMED CT is integrated into LLMs, focusing on (1) the types and components of LLMs being integrated with SNOMED CT, (2) which contents of SNOMED CT are being integrated, and (3) whether this integration improves LLM performance on NLP tasks.

Following the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) guidelines, we searched ACM Digital Library, ACL Anthology, IEEE Xplore, PubMed, and Embase for relevant studies published from 2018 to 2023. Studies were included if they incorporated SNOMED CT into LLM pipelines for natural language understanding or generation tasks. Data on LLM types, SNOMED CT integration methods, end tasks, and performance metrics were extracted and synthesized.

The review included 37 studies. Bidirectional Encoder Representations from Transformers and its biomedical variants were the most commonly used LLMs. Three main approaches for integrating SNOMED CT were identified: (1) incorporating SNOMED CT into LLM inputs (28/37, 76%), primarily using concept descriptions to expand training corpora; (2) integrating SNOMED CT into additional fusion modules (5/37, 14%); and (3) using SNOMED CT as an external knowledge retriever during inference (5/37, 14%). The most frequent end task was medical concept normalization (15/37, 41%), followed by entity extraction or typing and classification. While most studies (17/19, 89%) reported performance improvements after SNOMED CT integration, only a small fraction (19/37, 51%) provided direct comparisons. The reported gains varied widely across different metrics and tasks, ranging from 0.87% to 131.66%. However, some studies showed either no improvement or a decline in certain performance metrics.

This review demonstrates diverse approaches for integrating SNOMED CT into LLMs, with a focus on using concept descriptions to enhance biomedical language understanding and generation. While the results suggest potential benefits of SNOMED CT integration, the lack of standardized evaluation methods and comprehensive performance reporting hinders definitive conclusions about its effectiveness. Future research should prioritize consistent reporting of performance comparisons and explore more sophisticated methods for incorporating SNOMED CT’s relational structure into LLMs. In addition, the biomedical NLP community should develop standardized evaluation frameworks to better assess the impact of ontology integration on LLM performance.

[end paper 1]

[begin paper 2]

PMCID = 11221943

Title = Leveraging GPT-4 for identifying cancer phenotypes in electronic health records: a performance comparison between GPT-4, GPT-3.5-turbo, Flan-T5, Llama-3-8B, and spaCy’s rule-based and machine learning-based methods

Accurately identifying clinical phenotypes from Electronic Health Records (EHRs) provides additional insights into patients’ health, especially when such information is unavailable in structured data. This study evaluates the application of OpenAI’s Generative Pre-trained Transformer (GPT)-4 model to identify clinical phenotypes from EHR text in non-small cell lung cancer (NSCLC) patients. The goal was to identify disease stages, treatments and progression utilizing GPT-4, and compare its performance against GPT-3.5-turbo, Flan-T5-xl, Flan-T5-xxl, Llama-3-8B, and 2 rule-based and machine learning-based methods, namely, scispaCy and medspaCy.

Phenotypes such as initial cancer stage, initial treatment, evidence of cancer recurrence, and affected organs during recurrence were identified from 13 646 clinical notes for 63 NSCLC patients from Washington University in St. Louis, Missouri. The performance of the GPT-4 model is evaluated against GPT-3.5-turbo, Flan-T5-xxl, Flan-T5-xl, Llama-3-8B, medspaCy, and scispaCy by comparing precision, recall, and micro-F1 scores.

GPT-4 achieved higher F1 score, precision, and recall compared to Flan-T5-xl, Flan-T5-xxl, Llama-3-8B, medspaCy, and scispaCy’s models. GPT-3.5-turbo performed similarly to that of GPT-4. GPT, Flan-T5, and Llama models were not constrained by explicit rule requirements for contextual pattern recognition. spaCy models relied on predefined patterns, leading to their suboptimal performance.

GPT-4 improves clinical phenotype identification due to its robust pre-training and remarkable pattern recognition capability on the embedded tokens. It demonstrates data-driven effectiveness even with limited context in the input. While rule-based models remain useful for some tasks, GPT models offer improved contextual understanding of the text, and robust clinical phenotype extraction.

[end paper 2]

[begin paper 3]

PMCID = 10801236

Title = Enhancing phenotype recognition in clinical notes using large language models: PhenoBCBERT and PhenoGPT

To enhance phenotype recognition in clinical notes of genetic diseases, we developed two models—PhenoBCBERT and PhenoGPT—for expanding the vocabularies of Human Phenotype Ontology (HPO) terms. While HPO offers a standardized vocabulary for phenotypes, existing tools often fail to capture the full scope of phenotypes due to limitations from traditional heuristic or rule-based approaches. Our models leverage large language models to automate the detection of phenotype terms, including those not in the current HPO. We compare these models with PhenoTagger, another HPO recognition tool, and found that our models identify a wider range of phenotype concepts, including previously uncharacterized ones. Our models also show strong performance in case studies on biomedical literature. We evaluate the strengths and weaknesses of BERT- and GPT-based models in aspects such as architecture and accuracy. Overall, our models enhance automated phenotype detection from clinical texts, improving downstream analyses on human diseases.

This study uses LLMs to effectively detect abnormal phenotypes in clinical notes

It evaluates various parameters of open-source and closed-source models

We cover significant details on adapting general LLMs for domain-specific research

Large language models (LLMs) are types of artificial intelligence models that leverage massive training datasets to achieve broad capabilities to “understand” and generate natural language content, for example, in the form of text. LLMs are being actively developed by both commercial companies and academic researchers to power many popular AI tools. Given their broad capabilities, there is widespread interest in how these models can be adapted to more specific technical tasks. One such area of interest is the development of LLMs that can understand, process, and reveal new insights from electronic health record data in ways that might help improve healthcare services or guide treatment.

This study illuminates the potential of large language models (LLMs) in identifying key medical information, specifically clinical phenotypes, within the intricate notes of rare genetic disease patients. By comparing different LLM approaches and their efficacy in this precise task, the research underscores significant variations in their operational aspects. Crucially, the findings serve as a beacon for diverse fields, guiding the adaptation of advanced LLMs for specialized, real-world applications, thus bridging the gap between AI technology and domain-specific challenges.

[end paper 3]

[begin paper 4]

PMCID = 11287876

Title = Transformer models in biomedicine

Deep neural networks (DNN) have fundamentally revolutionized the artificial intelligence (AI) field. The transformer model is a type of DNN that was originally used for the natural language processing tasks and has since gained more and more attention for processing various kinds of sequential data, including biological sequences and structured electronic health records. Along with this development, transformer-based models such as BioBERT, MedBERT, and MassGenie have been trained and deployed by researchers to answer various scientific questions originating in the biomedical domain. In this paper, we review the development and application of transformer models for analyzing various biomedical-related datasets such as biomedical textual data, protein sequences, medical structured-longitudinal data, and biomedical images as well as graphs. Also, we look at explainable AI strategies that help to comprehend the predictions of transformer-based models. Finally, we discuss the limitations and challenges of current models, and point out emerging novel research directions.

[end paper 4]

[begin paper 5]

PMCID = 10659449

Title = Enhancing Phenotype Recognition in Clinical Notes Using Large Language Models: PhenoBCBERT and PhenoGPT

To enhance phenotype recognition in clinical notes of genetic diseases, we developed two models - PhenoBCBERT and PhenoGPT - for expanding the vocabularies of Human Phenotype Ontology (HPO) terms. While HPO offers a standardized vocabulary for phenotypes, existing tools often fail to capture the full scope of phenotypes, due to limitations from traditional heuristic or rule-based approaches. Our models leverage large language models (LLMs) to automate the detection of phenotype terms, including those not in the current HPO. We compared these models to PhenoTagger, another HPO recognition tool, and found that our models identify a wider range of phenotype concepts, including previously uncharacterized ones. Our models also showed strong performance in case studies on biomedical literature. We evaluated the strengths and weaknesses of BERT-based and GPT-based models in aspects such as architecture and accuracy. Overall, our models enhance automated phenotype detection from clinical texts, improving downstream analyses on human diseases.

[end paper 5]



