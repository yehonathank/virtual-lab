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

To address the agenda, I'll start by crafting a series of search queries to find relevant scientific papers on ClinicalBERT performance on phenotype definition tasks. These queries will cover both general aspects and specific relationships to LLM interpretability, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
search_queries = [
    "ClinicalBERT performance on phenotype definition tasks",
    "ClinicalBERT and LLM interpretability in phenotype definitions",
    "ClinicalBERT phenotype definition tasks and clinical applications",
    "ClinicalBERT and clinician trust in phenotype definitions",
    "ClinicalBERT performance and SNOMED CT integration in phenotype definitions"
]
```

Next, I'll use these queries to search for relevant scientific papers. This will help us identify the PMCIDs and titles of the papers that are crucial for fine-tuning our understanding of ClinicalBERT's performance in this context. Let's proceed with the search using these queries.

## Computational Linguist

Based on the search queries, here are the PMCIDs and titles of the papers that are relevant to ClinicalBERT performance on phenotype definition tasks and related topics:

```python
papers = {
    "10368879": "Generalizability of machine learning methods in detecting adverse drug events from clinical narratives in electronic medical records",
    "11041460": "Developing an Inpatient Electronic Medical Record Phenotype for Hospital-Acquired Pressure Injuries: Case Study Using Natural Language Processing Models",
    "7665985": "Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts",
    "9979798": "How data science and AI-based technologies impact genomics",
    "11287876": "Transformer models in biomedicine",
    "11585305": "Artificial intelligence research in radiation oncology: a practical guide for the clinician on concepts and methods",
    "10579102": "Optimized glycemic control of type 2 diabetes with reinforcement learning: a proof-of-concept trial",
    "11586117": "Lightweight transformers for clinical natural language processing",
    "11336492": "Enhancing Clinical Relevance of Pretrained Language Models Through Integration of External Knowledge: Case Study on Cardiovascular Diagnosis From Electronic Health Records",
    "11536026": "BioKGrapher: Initial evaluation of automated knowledge graph construction from biomedical literature"
}
```

These papers will provide a comprehensive understanding of ClinicalBERT's performance in phenotype definition tasks, its integration with SNOMED CT, and its implications for clinical applications and clinician trust.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "ClinicalBERT performance on phenotype definition tasks":

[begin paper 1]

PMCID = 10368879

Title = Generalizability of machine learning methods in detecting adverse drug events from clinical narratives in electronic medical records

We assessed the generalizability of machine learning methods using natural language processing (NLP) techniques to detect adverse drug events (ADEs) from clinical narratives in electronic medical records (EMRs). We constructed a new corpus correlating drugs with adverse drug events using 1,394 clinical notes of 47 randomly selected patients who received immune checkpoint inhibitors (ICIs) from 2011 to 2018 at The Ohio State University James Cancer Hospital, annotating 189 drug-ADE relations in single sentences within the medical records. We also used data from Harvard’s publicly available 2018 National Clinical Challenge (n2c2), which includes 505 discharge summaries with annotations of 1,355 single-sentence drug-ADE relations. We applied classical machine learning (support vector machine (SVM)), deep learning (convolutional neural network (CNN) and bidirectional long short-term memory (BiLSTM)), and state-of-the-art transformer-based (bidirectional encoder representations from transformers (BERT) and ClinicalBERT) methods trained and tested in the two different corpora and compared performance among them to detect drug–ADE relationships. ClinicalBERT detected drug–ADE relationships better than the other methods when trained using our dataset and tested in n2c2 (ClinicalBERT F-score, 0.78; other methods, F-scores, 0.61–0.73) and when trained using the n2c2 dataset and tested in ours (ClinicalBERT F-score, 0.74; other methods, F-scores, 0.55–0.72). Comparison among several machine learning methods demonstrated the superior performance and, therefore, the greatest generalizability of findings of ClinicalBERT for the detection of drug–ADE relations from clinical narratives in electronic medical records. 

[end paper 1]

[begin paper 2]

PMCID = 11041460

Title = Developing an Inpatient Electronic Medical Record Phenotype for Hospital-Acquired Pressure Injuries: Case Study Using Natural Language Processing Models

Surveillance of hospital-acquired pressure injuries (HAPI) is often suboptimal when relying on administrative health data, as International Classification of Diseases (ICD) codes are known to have long delays and are undercoded. We leveraged natural language processing (NLP) applications on free-text notes, particularly the inpatient nursing notes, from electronic medical records (EMRs), to more accurately and timely identify HAPIs.

This study aimed to show that EMR-based phenotyping algorithms are more fitted to detect HAPIs than ICD-10-CA algorithms alone, while the clinical logs are recorded with higher accuracy via NLP using nursing notes.

Patients with HAPIs were identified from head-to-toe skin assessments in a local tertiary acute care hospital during a clinical trial that took place from 2015 to 2018 in Calgary, Alberta, Canada. Clinical notes documented during the trial were extracted from the EMR database after the linkage with the discharge abstract database. Different combinations of several types of clinical notes were processed by sequential forward selection during the model development. Text classification algorithms for HAPI detection were developed using random forest (RF), extreme gradient boosting (XGBoost), and deep learning models. The classification threshold was tuned to enable the model to achieve similar specificity to an ICD-based phenotyping study. Each model’s performance was assessed, and comparisons were made between the metrics, including sensitivity, positive predictive value, negative predictive value, and F1-score.

Data from 280 eligible patients were used in this study, among whom 97 patients had HAPIs during the trial. RF was the optimal performing model with a sensitivity of 0.464 (95% CI 0.365-0.563), specificity of 0.984 (95% CI 0.965-1.000), and F1-score of 0.612 (95% CI of 0.473-0.751). The machine learning (ML) model reached higher sensitivity without sacrificing much specificity compared to the previously reported performance of ICD-based algorithms.

The EMR-based NLP phenotyping algorithms demonstrated improved performance in HAPI case detection over ICD-10-CA codes alone. Daily generated nursing notes in EMRs are a valuable data resource for ML models to accurately detect adverse events. The study contributes to enhancing automated health care quality and safety surveillance.

[end paper 2]

[begin paper 3]

PMCID = 7665985

Title = Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts

Currently, a major limitation for natural language processing (NLP) analyses in clinical applications is that concepts are not effectively referenced in various forms across different texts. This paper introduces Multi-Ontology Refined Embeddings (MORE), a novel hybrid framework that incorporates domain knowledge from multiple ontologies into a distributional semantic model, learned from a corpus of clinical text.

We use the RadCore and MIMIC-III free-text datasets for the corpus-based component of MORE. For the ontology-based part, we use the Medical Subject Headings (MeSH) ontology and three state-of-the-art ontology-based similarity measures. In our approach, we propose a new learning objective, modified from the sigmoid cross-entropy objective function.

We used two established datasets of semantic similarities among biomedical concept pairs to evaluate the quality of the generated word embeddings. On the first dataset with 29 concept pairs, with similarity scores established by physicians and medical coders, MORE’s similarity scores have the highest combined correlation (0.633), which is 5.0% higher than that of the baseline model, and 12.4% higher than that of the best ontology-based similarity measure. On the second dataset with 449 concept pairs, MORE’s similarity scores have a correlation of 0.481, based on the average of four medical residents’ similarity ratings, and that outperforms the skip-gram model by 8.1%, and the best ontology measure by 6.9%. Furthermore, MORE outperforms three pre-trained transformer-based word embedding models (i.e., BERT, ClinicalBERT, and BioBERT) on both datasets.

MORE incorporates knowledge from several biomedical ontologies into an existing corpus-based distributional semantics model, improving both the accuracy of the learned word embeddings and the extensibility of the model to a broader range of biomedical concepts. MORE allows for more accurate clustering of concepts across a wide range of applications, such as analyzing patient health records to identify subjects with similar pathologies, or integrating heterogeneous clinical data to improve interoperability between hospitals.

[end paper 3]

[begin paper 4]

PMCID = 9979798

Title = How data science and AI-based technologies impact genomics

Advancements in high-throughput sequencing have yielded vast amounts of genomic data, which are studied using genome-wide association study (GWAS)/phenome-wide association study (PheWAS) methods to identify associations between the genotype and phenotype. The associated findings have contributed to pharmacogenomics and improved clinical decision support at the point of care in many healthcare systems. However, the accumulation of genomic data from sequencing and clinical data from electronic health records (EHRs) poses significant challenges for data scientists. Following the rise of artificial intelligence (AI) technology such as machine learning and deep learning, an increasing number of GWAS/PheWAS studies have successfully leveraged this technology to overcome the aforementioned challenges. In this review, we focus on the application of data science and AI technology in three areas, including risk prediction and identification of causal single-nucleotide polymorphisms, EHR-based phenotyping and CRISPR guide RNA design. Additionally, we highlight a few emerging AI technologies, such as transfer learning and multi-view learning, which will or have started to benefit genomic studies.

[end paper 4]

[begin paper 5]

PMCID = 11287876

Title = Transformer models in biomedicine

Deep neural networks (DNN) have fundamentally revolutionized the artificial intelligence (AI) field. The transformer model is a type of DNN that was originally used for the natural language processing tasks and has since gained more and more attention for processing various kinds of sequential data, including biological sequences and structured electronic health records. Along with this development, transformer-based models such as BioBERT, MedBERT, and MassGenie have been trained and deployed by researchers to answer various scientific questions originating in the biomedical domain. In this paper, we review the development and application of transformer models for analyzing various biomedical-related datasets such as biomedical textual data, protein sequences, medical structured-longitudinal data, and biomedical images as well as graphs. Also, we look at explainable AI strategies that help to comprehend the predictions of transformer-based models. Finally, we discuss the limitations and challenges of current models, and point out emerging novel research directions.

[end paper 5]



No articles found on PubMed Central for the query "ClinicalBERT and LLM interpretability in phenotype definitions".

Here are the top 5 articles on PubMed Central for the query "ClinicalBERT phenotype definition tasks and clinical applications":

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

PMCID = 7665985

Title = Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts

Currently, a major limitation for natural language processing (NLP) analyses in clinical applications is that concepts are not effectively referenced in various forms across different texts. This paper introduces Multi-Ontology Refined Embeddings (MORE), a novel hybrid framework that incorporates domain knowledge from multiple ontologies into a distributional semantic model, learned from a corpus of clinical text.

We use the RadCore and MIMIC-III free-text datasets for the corpus-based component of MORE. For the ontology-based part, we use the Medical Subject Headings (MeSH) ontology and three state-of-the-art ontology-based similarity measures. In our approach, we propose a new learning objective, modified from the sigmoid cross-entropy objective function.

We used two established datasets of semantic similarities among biomedical concept pairs to evaluate the quality of the generated word embeddings. On the first dataset with 29 concept pairs, with similarity scores established by physicians and medical coders, MORE’s similarity scores have the highest combined correlation (0.633), which is 5.0% higher than that of the baseline model, and 12.4% higher than that of the best ontology-based similarity measure. On the second dataset with 449 concept pairs, MORE’s similarity scores have a correlation of 0.481, based on the average of four medical residents’ similarity ratings, and that outperforms the skip-gram model by 8.1%, and the best ontology measure by 6.9%. Furthermore, MORE outperforms three pre-trained transformer-based word embedding models (i.e., BERT, ClinicalBERT, and BioBERT) on both datasets.

MORE incorporates knowledge from several biomedical ontologies into an existing corpus-based distributional semantics model, improving both the accuracy of the learned word embeddings and the extensibility of the model to a broader range of biomedical concepts. MORE allows for more accurate clustering of concepts across a wide range of applications, such as analyzing patient health records to identify subjects with similar pathologies, or integrating heterogeneous clinical data to improve interoperability between hospitals.

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

PMCID = 9893183

Title = Building a knowledge graph to enable precision medicine

Developing personalized diagnostic strategies and targeted treatments requires a deep understanding of disease biology and the ability to dissect the relationship between molecular and genetic factors and their phenotypic consequences. However, such knowledge is fragmented across publications, non-standardized repositories, and evolving ontologies describing various scales of biological organization between genotypes and clinical phenotypes. Here, we present PrimeKG, a multimodal knowledge graph for precision medicine analyses. PrimeKG integrates 20 high-quality resources to describe 17,080 diseases with 4,050,249 relationships representing ten major biological scales, including disease-associated protein perturbations, biological processes and pathways, anatomical and phenotypic scales, and the entire range of approved drugs with their therapeutic action, considerably expanding previous efforts in disease-rooted knowledge graphs. PrimeKG contains an abundance of ‘indications’, ‘contradictions’, and ‘off-label use’ drug-disease edges that lack in other knowledge graphs and can support AI analyses of how drugs affect disease-associated networks. We supplement PrimeKG’s graph structure with language descriptions of clinical guidelines to enable multimodal analyses and provide instructions for continual updates of PrimeKG as new data become available.

[end paper 5]



Here are the top 3 articles on PubMed Central for the query "ClinicalBERT and clinician trust in phenotype definitions":

[begin paper 1]

PMCID = 11585305

Title = Artificial intelligence research in radiation oncology: a practical guide for the clinician on concepts and methods

The use of artificial intelligence (AI) holds great promise for radiation oncology, with many applications being reported in the literature, including some of which are already in clinical use. These are mainly in areas where AI provides benefits in efficiency (such as automatic segmentation and treatment planning). Prediction models that directly impact patient decision-making are far less mature in terms of their application in clinical practice. Part of the limited clinical uptake of these models may be explained by the need for broader knowledge, among practising clinicians within the medical community, about the processes of AI development. This lack of understanding could lead to low commitment to AI research, widespread scepticism, and low levels of trust. This attitude towards AI may be further negatively impacted by the perception that deep learning is a “black box” with inherently low transparency. Thus, there is an unmet need to train current and future clinicians in the development and application of AI in medicine. Improving clinicians’ AI-related knowledge and skills is necessary to enhance multidisciplinary collaboration between data scientists and physicians, that is, involving a clinician in the loop during AI development. Increased knowledge may also positively affect the acceptance and trust of AI. This paper describes the necessary steps involved in AI research and development, and thus identifies the possibilities, limitations, challenges, and opportunities, as seen from the perspective of a practising radiation oncologist. It offers the clinician with limited knowledge and experience in AI valuable tools to evaluate research papers related to an AI model application.

[end paper 1]

[begin paper 2]

PMCID = 10579102

Title = Optimized glycemic control of type 2 diabetes with reinforcement learning: a proof-of-concept trial

The personalized titration and optimization of insulin regimens for treatment of type 2 diabetes (T2D) are resource-demanding healthcare tasks. Here we propose a model-based reinforcement learning (RL) framework (called RL-DITR), which learns the optimal insulin regimen by analyzing glycemic state rewards through patient model interactions. When evaluated during the development phase for managing hospitalized patients with T2D, RL-DITR achieved superior insulin titration optimization (mean absolute error (MAE) of 1.10 ± 0.03 U) compared to other deep learning models and standard clinical methods. We performed a stepwise clinical validation of the artificial intelligence system from simulation to deployment, demonstrating better performance in glycemic control in inpatients compared to junior and intermediate-level physicians through quantitative (MAE of 1.18 ± 0.09 U) and qualitative metrics from a blinded review. Additionally, we conducted a single-arm, patient-blinded, proof-of-concept feasibility trial in 16 patients with T2D. The primary outcome was difference in mean daily capillary blood glucose during the trial, which decreased from 11.1 (±3.6) to 8.6 (±2.4) mmol L−1 (P < 0.01), meeting the pre-specified endpoint. No episodes of severe hypoglycemia or hyperglycemia with ketosis occurred. These preliminary results warrant further investigation in larger, more diverse clinical studies. ClinicalTrials.gov registration: NCT05409391.

A reinforcement learning algorithm achieved superior insulin titration optimization versus other deep learning models and standard clinical methods in a prospective cohort and in a proof-of-concept feasibility trial.

[end paper 2]

[begin paper 3]

PMCID = 11586117

Title = Lightweight transformers for clinical natural language processing

Specialised pre-trained language models are becoming more frequent in Natural language Processing (NLP) since they can potentially outperform models trained on generic texts. BioBERT (Sanh et al., Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. arXiv preprint arXiv: 1910.01108, 2019) and BioClinicalBERT (Alsentzer et al., Publicly available clinical bert embeddings. In Proceedings of the 2nd Clinical Natural Language Processing Workshop, pp. 72–78, 2019) are two examples of such models that have shown promise in medical NLP tasks. Many of these models are overparametrised and resource-intensive, but thanks to techniques like knowledge distillation, it is possible to create smaller versions that perform almost as well as their larger counterparts. In this work, we specifically focus on development of compact language models for processing clinical texts (i.e. progress notes, discharge summaries, etc). We developed a number of efficient lightweight clinical transformers using knowledge distillation and continual learning, with the number of parameters ranging from  million to  million. These models performed comparably to larger models such as BioBERT and ClinicalBioBERT and significantly outperformed other compact models trained on general or biomedical data. Our extensive evaluation was done across several standard datasets and covered a wide range of clinical text-mining tasks, including natural language inference, relation extraction, named entity recognition and sequence classification. To our knowledge, this is the first comprehensive study specifically focused on creating efficient and compact transformers for clinical NLP tasks. The models and code used in this study can be found on our Huggingface profile at  and Github page at , respectively, promoting reproducibility of our results.

[end paper 3]



Here are the top 3 articles on PubMed Central for the query "ClinicalBERT performance and SNOMED CT integration in phenotype definitions":

[begin paper 1]

PMCID = 11336492

Title = Enhancing Clinical Relevance of Pretrained Language Models Through Integration of External Knowledge: Case Study on Cardiovascular Diagnosis From Electronic Health Records

Despite their growing use in health care, pretrained language models (PLMs) often lack clinical relevance due to insufficient domain expertise and poor interpretability. A key strategy to overcome these challenges is integrating external knowledge into PLMs, enhancing their adaptability and clinical usefulness. Current biomedical knowledge graphs like UMLS (Unified Medical Language System), SNOMED CT (Systematized Medical Nomenclature for Medicine–Clinical Terminology), and HPO (Human Phenotype Ontology), while comprehensive, fail to effectively connect general biomedical knowledge with physician insights. There is an equally important need for a model that integrates diverse knowledge in a way that is both unified and compartmentalized. This approach not only addresses the heterogeneous nature of domain knowledge but also recognizes the unique data and knowledge repositories of individual health care institutions, necessitating careful and respectful management of proprietary information.

This study aimed to enhance the clinical relevance and interpretability of PLMs by integrating external knowledge in a manner that respects the diversity and proprietary nature of health care data. We hypothesize that domain knowledge, when captured and distributed as stand-alone modules, can be effectively reintegrated into PLMs to significantly improve their adaptability and utility in clinical settings.

We demonstrate that through adapters, small and lightweight neural networks that enable the integration of extra information without full model fine-tuning, we can inject diverse sources of external domain knowledge into language models and improve the overall performance with an increased level of interpretability. As a practical application of this methodology, we introduce a novel task, structured as a case study, that endeavors to capture physician knowledge in assigning cardiovascular diagnoses from clinical narratives, where we extract diagnosis-comment pairs from electronic health records (EHRs) and cast the problem as text classification.

The study demonstrates that integrating domain knowledge into PLMs significantly improves their performance. While improvements with ClinicalBERT are more modest, likely due to its pretraining on clinical texts, BERT (bidirectional encoder representations from transformer) equipped with knowledge adapters surprisingly matches or exceeds ClinicalBERT in several metrics. This underscores the effectiveness of knowledge adapters and highlights their potential in settings with strict data privacy constraints. This approach also increases the level of interpretability of these models in a clinical context, which enhances our ability to precisely identify and apply the most relevant domain knowledge for specific tasks, thereby optimizing the model’s performance and tailoring it to meet specific clinical needs.

This research provides a basis for creating health knowledge graphs infused with physician knowledge, marking a significant step forward for PLMs in health care. Notably, the model balances integrating knowledge both comprehensively and selectively, addressing the heterogeneous nature of medical knowledge and the privacy needs of health care institutions.

[end paper 1]

[begin paper 2]

PMCID = 11536026

Title = BioKGrapher: Initial evaluation of automated knowledge graph construction from biomedical literature

Background The growth of biomedical literature presents challenges in extracting and structuring knowledge. Knowledge Graphs (KGs) offer a solution by representing relationships between biomedical entities. However, manual construction of KGs is labor-intensive and time-consuming, highlighting the need for automated methods. This work introduces BioKGrapher, a tool for automatic KG construction using large-scale publication data, with a focus on biomedical concepts related to specific medical conditions. BioKGrapher allows researchers to construct KGs from PubMed IDs.

Methods The BioKGrapher pipeline begins with Named Entity Recognition and Linking (NER+NEL) to extract and normalize biomedical concepts from PubMed, mapping them to the Unified Medical Language System (UMLS). Extracted concepts are weighted and re-ranked using Kullback-Leibler divergence and local frequency balancing. These concepts are then integrated into hierarchical KGs, with relationships formed using terminologies like SNOMED CT and NCIt. Downstream applications include multi-label document classification using Adapter-infused Transformer models.

Results BioKGrapher effectively aligns generated concepts with clinical practice guidelines from the German Guideline Program in Oncology (GGPO), achieving -Scores of up to 0.6. In multi-label classification, Adapter-infused models using a BioKGrapher cancer-specific KG improved micro -Scores by up to 0.89 percentage points over a non-specific KG and 2.16 points over base models across three BERT variants. The drug-disease extraction case study identified indications for Nivolumab and Rituximab.

Conclusion BioKGrapher is a tool for automatic KG construction, aligning with the GGPO and enhancing downstream task performance. It offers a scalable solution for managing biomedical knowledge, with potential applications in literature recommendation, decision support, and drug repurposing.

Automated knowledge graph construction from PubMed abstracts for conditions.

Achieves up to 0.6 -Score alignment of concepts with oncology clinical practice guidelines.

Improves cancer document classification using Adapter-infused Transformer models.

Automatically retrieve Drug-Disease associations for potential drug repurposing applications.

[end paper 2]

[begin paper 3]

PMCID = 11586117

Title = Lightweight transformers for clinical natural language processing

Specialised pre-trained language models are becoming more frequent in Natural language Processing (NLP) since they can potentially outperform models trained on generic texts. BioBERT (Sanh et al., Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. arXiv preprint arXiv: 1910.01108, 2019) and BioClinicalBERT (Alsentzer et al., Publicly available clinical bert embeddings. In Proceedings of the 2nd Clinical Natural Language Processing Workshop, pp. 72–78, 2019) are two examples of such models that have shown promise in medical NLP tasks. Many of these models are overparametrised and resource-intensive, but thanks to techniques like knowledge distillation, it is possible to create smaller versions that perform almost as well as their larger counterparts. In this work, we specifically focus on development of compact language models for processing clinical texts (i.e. progress notes, discharge summaries, etc). We developed a number of efficient lightweight clinical transformers using knowledge distillation and continual learning, with the number of parameters ranging from  million to  million. These models performed comparably to larger models such as BioBERT and ClinicalBioBERT and significantly outperformed other compact models trained on general or biomedical data. Our extensive evaluation was done across several standard datasets and covered a wide range of clinical text-mining tasks, including natural language inference, relation extraction, named entity recognition and sequence classification. To our knowledge, this is the first comprehensive study specifically focused on creating efficient and compact transformers for clinical NLP tasks. The models and code used in this study can be found on our Huggingface profile at  and Github page at , respectively, promoting reproducibility of our results.

[end paper 3]



