## User

This is the beginning of an individual meeting with Clinical Informatics Specialist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Interoperability of phenotyping tools with EHR standards in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Interoperability of phenotyping tools with EHR standards to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Interoperability of phenotyping tools with EHR standards. Include both general queries about Interoperability of phenotyping tools with EHR standards and queries that specifically relate Interoperability of phenotyping tools with EHR standards to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Clinical Informatics Specialist, please provide your response to the agenda.

## Clinical Informatics Specialist

To address the agenda and effectively contribute to the development of an LLM-based interpretability tool for electronic phenotype definitions, I will begin by crafting a series of search queries to find relevant scientific papers. These queries will focus on the interoperability of phenotyping tools with EHR standards, as well as their relation to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
search_queries = [
    "Interoperability of phenotyping tools with EHR standards",
    "LLM interpretability in electronic phenotype definitions",
    "Interoperability and phenotype definition in clinical applications",
    "Building clinician trust in LLM-based phenotyping tools",
    "SNOMED CT integration in phenotype tools for EHR interoperability"
]
```

Next, I will use these queries to search for relevant scientific papers. I will retrieve the PMCIDs and titles of the papers to fine-tune myself on. Let's proceed with the search using these queries.

## Clinical Informatics Specialist

Based on the search queries, here are the PMCIDs and titles of the papers that are relevant to the interoperability of phenotyping tools with EHR standards, LLM interpretability, phenotype definition, clinical applications, and clinician trust:

```python
papers = {
    "11472501": "State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)–Based Data Model and Structure Implementations: Systematic Scoping Review",
    "9147872": "HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study",
    "9346559": "Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review",
    "10865191": "Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review",
    "6990976": "Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "10689487": "Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models",
    "11545079": "The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning",
    "3302143": "Proximal correlates of metabolic phenotypes during ‘at-risk' and ‘case' stages of the metabolic disease continuum",
    "11460004": "A hybrid framework with large language models for rare disease phenotyping",
    "11193731": "A study on interoperability between two Personal Health Train infrastructures in leukodystrophy data analysis",
    "5036847": "The digital revolution in phenotyping",
    "11809463": "Applications of Large Language Models in the Field of Suicide Prevention: Scoping Review",
    "10834163": "Artificial intelligence: revolutionizing cardiology with large language models",
    "10984041": "Inductive reasoning with large language models: a simulated randomized controlled trial for epilepsy",
    "11748787": "Artificial intelligence in rheumatology research: what is it good for?",
    "11984408": "Artificial intelligence in chronic kidney disease management: a scoping review",
    "8714300": "A State-of-the Art Review of SNOMED CT Terminology Binding and Recommendations for Practice and Research",
    "6351992": "SNOMED CT Concept Hierarchies for Computable Clinical Phenotypes From Electronic Health Record Data: Comparison of Intensional Versus Extensional Value Sets",
    "10403057": "A health terminological system for inherited retinal diseases: Content coverage evaluation and a proposed classification",
    "4748471": "Interoperability between phenotypes in research and healthcare terminologies—Investigating partial mappings between HPO and SNOMED CT"
}
```

These papers will provide a comprehensive understanding of the current landscape and challenges in the interoperability of phenotyping tools with EHR standards, and how LLMs can be integrated into this context to enhance interpretability and clinician trust.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Interoperability of phenotyping tools with EHR standards":

[begin paper 1]

PMCID = 11472501

Title = State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)–Based Data Model and Structure Implementations: Systematic Scoping Review

Data models are crucial for clinical research as they enable researchers to fully use the vast amount of clinical data stored in medical systems. Standardized data and well-defined relationships between data points are necessary to guarantee semantic interoperability. Using the Fast Healthcare Interoperability Resources (FHIR) standard for clinical data representation would be a practical methodology to enhance and accelerate interoperability and data availability for research.

This research aims to provide a comprehensive overview of the state-of-the-art and current landscape in FHIR-based data models and structures. In addition, we intend to identify and discuss the tools, resources, limitations, and other critical aspects mentioned in the selected research papers.

To ensure the extraction of reliable results, we followed the instructions of the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) checklist. We analyzed the indexed articles in PubMed, Scopus, Web of Science, IEEE Xplore, the ACM Digital Library, and Google Scholar. After identifying, extracting, and assessing the quality and relevance of the articles, we synthesized the extracted data to identify common patterns, themes, and variations in the use of FHIR-based data models and structures across different studies.

On the basis of the reviewed articles, we could identify 2 main themes: dynamic (pipeline-based) and static data models. The articles were also categorized into health care use cases, including chronic diseases, COVID-19 and infectious diseases, cancer research, acute or intensive care, random and general medical notes, and other conditions. Furthermore, we summarized the important or common tools and approaches of the selected papers. These items included FHIR-based tools and frameworks, machine learning approaches, and data storage and security. The most common resource was “Observation” followed by “Condition” and “Patient.” The limitations and challenges of developing data models were categorized based on the issues of data integration, interoperability, standardization, performance, and scalability or generalizability.

FHIR serves as a highly promising interoperability standard for developing real-world health care apps. The implementation of FHIR modeling for electronic health record data facilitates the integration, transmission, and analysis of data while also advancing translational research and phenotyping. Generally, FHIR-based exports of local data repositories improve data interoperability for systems and data warehouses across different settings. However, ongoing efforts to address existing limitations and challenges are essential for the successful implementation and integration of FHIR data models.

[end paper 1]

[begin paper 2]

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 2]

[begin paper 3]

PMCID = 9346559

Title = Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review

The standard Fast Healthcare Interoperability Resources (FHIR) is widely used in health information technology. However, its use as a standard for health research is still less prevalent. To use existing data sources more efficiently for health research, data interoperability becomes increasingly important. FHIR provides solutions by offering resource domains such as “Public Health & Research” and “Evidence-Based Medicine” while using already established web technologies. Therefore, FHIR could help standardize data across different data sources and improve interoperability in health research.

The aim of our study was to provide a systematic review of existing literature and determine the current state of FHIR implementations in health research and possible future directions.

We searched the PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore, and Cochrane Library databases for studies published from 2011 to 2022. Studies investigating the use of FHIR in health research were included. Articles published before 2011, abstracts, reviews, editorials, and expert opinions were excluded. We followed the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines and registered this study with PROSPERO (CRD42021235393). Data synthesis was done in tables and figures.

We identified a total of 998 studies, of which 49 studies were eligible for inclusion. Of the 49 studies, most (73%, n=36) covered the domain of clinical research, whereas the remaining studies focused on public health or epidemiology (6%, n=3) or did not specify their research domain (20%, n=10). Studies used FHIR for data capture (29%, n=14), standardization of data (41%, n=20), analysis (12%, n=6), recruitment (14%, n=7), and consent management (4%, n=2). Most (55%, 27/49) of the studies had a generic approach, and 55% (12/22) of the studies focusing on specific medical specialties (infectious disease, genomics, oncology, environmental health, imaging, and pulmonary hypertension) reported their solutions to be conferrable to other use cases. Most (63%, 31/49) of the studies reported using additional data models or terminologies: Systematized Nomenclature of Medicine Clinical Terms (29%, n=14), Logical Observation Identifiers Names and Codes (37%, n=18), International Classification of Diseases 10th Revision (18%, n=9), Observational Medical Outcomes Partnership common data model (12%, n=6), and others (43%, n=21). Only 4 (8%) studies used a FHIR resource from the domain “Public Health & Research.” Limitations using FHIR included the possible change in the content of FHIR resources, safety, legal matters, and the need for a FHIR server.

Our review found that FHIR can be implemented in health research, and the areas of application are broad and generalizable in most use cases. The implementation of international terminologies was common, and other standards such as the Observational Medical Outcomes Partnership common data model could be used as a complement to FHIR. Limitations such as the change of FHIR content, lack of FHIR implementation, safety, and legal matters need to be addressed in future releases to expand the use of FHIR and, therefore, interoperability in health research.

[end paper 3]

[begin paper 4]

PMCID = 10865191

Title = Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review

The increasing use of electronic health records and the Internet of Things has led to interoperability issues at different levels (structural and semantic). Standards are important not only for successfully exchanging data but also for appropriately interpreting them (semantic interoperability). Thus, to facilitate the semantic interoperability of data exchanged in health care, considerable resources have been deployed to improve the quality of shared clinical data by structuring and mapping them to the Fast Healthcare Interoperability Resources (FHIR) standard.

The aims of this study are 2-fold: to inventory the studies on FHIR semantic interoperability resources and terminologies and to identify and classify the approaches and contributions proposed in these studies.

A systematic mapping review (SMR) was conducted using 10 electronic databases as sources of information for inventory and review studies published during 2012 to 2022 on the development and improvement of semantic interoperability using the FHIR standard.

A total of 70 FHIR studies were selected and analyzed to identify FHIR resource types and terminologies from a semantic perspective. The proposed semantic approaches were classified into 6 categories, namely mapping (31/126, 24.6%), terminology services (18/126, 14.3%), resource description framework or web ontology language–based proposals (24/126, 19%), annotation proposals (18/126, 14.3%), machine learning (ML) and natural language processing (NLP) proposals (20/126, 15.9%), and ontology-based proposals (15/126, 11.9%). From 2012 to 2022, there has been continued research in 6 categories of approaches as well as in new and emerging annotations and ML and NLP proposals. This SMR also classifies the contributions of the selected studies into 5 categories: framework or architecture proposals, model proposals, technique proposals, comparison services, and tool proposals. The most frequent type of contribution is the proposal of a framework or architecture to enable semantic interoperability.

This SMR provides a classification of the different solutions proposed to address semantic interoperability using FHIR at different levels: collecting, extracting and annotating data, modeling electronic health record data from legacy systems, and applying transformation and mapping to FHIR models and terminologies. The use of ML and NLP for unstructured data is promising and has been applied to specific use case scenarios. In addition, terminology services are needed to accelerate their use and adoption; furthermore, techniques and tools to automate annotation and ontology comparison should help reduce human interaction.

[end paper 4]

[begin paper 5]

PMCID = 6990976

Title = Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries

Standards-based clinical data normalization has become a key component of effective data integration and accurate phenotyping for secondary use of electronic healthcare records (EHR) data. HL7 Fast Healthcare Interoperability Resources (FHIR) is an emerging clinical data standard for exchanging electronic healthcare data and has been used in modeling and integrating both structured and unstructured EHR data for a variety of clinical research applications. The overall objective of this study is to develop and evaluate a FHIR-based EHR phenotyping framework for identification of patients with obesity and its multiple comorbidities from semi-structured discharge summaries leveraging a FHIR-based clinical data normalization pipeline (known as NLP2FHIR).

We implemented a multi-class and multi-label classification system based on the i2b2 Obesity Challenge task to evaluate the FHIR-based EHR phenotyping framework. Two core parts of the framework are: (a) the conversion of discharge summaries into corresponding FHIR resources – Composition, Condition, MedicationStatement, Procedure and FamilyMemberHistory using the NLP2FHIR pipeline, and (b) the implementation of four machine learning algorithms (logistic regression, support vector machine, decision tree, and random forest) to train classifiers to predict disease state of obesity and 15 comorbidities using features extracted from standard FHIR resources and terminology expansions. We used the macro- and micro-averaged precision (P), recall (R), and F1 score (F1) measures to evaluate the classifier performance. We validated the framework using a second obesity dataset extracted from the MIMIC-III database.

Using the NLP2FHIR pipeline, 1237 clinical discharge summaries from the 2008 i2b2 obesity challenge dataset were represented as the instances of the FHIR Composition resource consisting of 5677 records with 16 unique section types. After the NLP processing and FHIR modeling, a set of 244,438 FHIR clinical resource instances were generated. As the results of the four machine learning classifiers, the random forest algorithm performed the best with F1-micro(0.9466)/F1-macro(0.7887) and F1-micro(0.9536)/F1-macro(0.6524) for intuitive classification (reflecting medical professionals’ judgments) and textual classification (reflecting the judgments based on explicitly reported information of diseases), respectively. The MIMIC-III obesity dataset was successfully integrated for prediction with minimal configuration of the NLP2FHIR pipeline and machine learning models.

The study demonstrated that the FHIR-based EHR phenotyping approach could effectively identify the state of obesity and multiple comorbidities using semi-structured discharge summaries. Our FHIR-based phenotyping approach is a first concrete step towards improving the data aspect of phenotyping portability across EHR systems and enhancing interpretability of the machine learning-based phenotyping algorithms.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "LLM interpretability in electronic phenotype definitions":

[begin paper 1]

PMCID = 11422740

Title = Prompt Engineering Paradigms for Medical Applications: Scoping Review

Prompt engineering, focusing on crafting effective prompts to large language models (LLMs), has garnered attention for its capabilities at harnessing the potential of LLMs. This is even more crucial in the medical domain due to its specialized terminology and language technicity. Clinical natural language processing applications must navigate complex language and ensure privacy compliance. Prompt engineering offers a novel approach by designing tailored prompts to guide models in exploiting clinically relevant information from complex medical texts. Despite its promise, the efficacy of prompt engineering in the medical domain remains to be fully explored.

The aim of the study is to review research efforts and technical approaches in prompt engineering for medical applications as well as provide an overview of opportunities and challenges for clinical practice.

Databases indexing the fields of medicine, computer science, and medical informatics were queried in order to identify relevant published papers. Since prompt engineering is an emerging field, preprint databases were also considered. Multiple data were extracted, such as the prompt paradigm, the involved LLMs, the languages of the study, the domain of the topic, the baselines, and several learning, design, and architecture strategies specific to prompt engineering. We include studies that apply prompt engineering–based methods to the medical domain, published between 2022 and 2024, and covering multiple prompt paradigms such as prompt learning (PL), prompt tuning (PT), and prompt design (PD).

We included 114 recent prompt engineering studies. Among the 3 prompt paradigms, we have observed that PD is the most prevalent (78 papers). In 12 papers, PD, PL, and PT terms were used interchangeably. While ChatGPT is the most commonly used LLM, we have identified 7 studies using this LLM on a sensitive clinical data set. Chain-of-thought, present in 17 studies, emerges as the most frequent PD technique. While PL and PT papers typically provide a baseline for evaluating prompt-based approaches, 61% (48/78) of the PD studies do not report any nonprompt-related baseline. Finally, we individually examine each of the key prompt engineering–specific information reported across papers and find that many studies neglect to explicitly mention them, posing a challenge for advancing prompt engineering research.

In addition to reporting on trends and the scientific landscape of prompt engineering, we provide reporting guidelines for future studies to help advance research in the medical field. We also disclose tables and figures summarizing medical prompt engineering papers available and hope that future contributions will leverage these existing works to better advance the field.

[end paper 1]

[begin paper 2]

PMCID = 10689487

Title = Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models

Many areas of medicine would benefit from deeper, more accurate phenotyping, but there are limited approaches for phenotyping using clinical notes without substantial annotated data. Large language models (LLMs) have demonstrated immense potential to adapt to novel tasks with no additional training by specifying task-specific instructions. Here we report the performance of a publicly available LLM, Flan-T5, in phenotyping patients with postpartum hemorrhage (PPH) using discharge notes from electronic health records (n = 271,081). The language model achieves strong performance in extracting 24 granular concepts associated with PPH. Identifying these granular concepts accurately allows the development of interpretable, complex phenotypes and subtypes. The Flan-T5 model achieves high fidelity in phenotyping PPH (positive predictive value of 0.95), identifying 47% more patients with this complication compared to the current standard of using claims codes. This LLM pipeline can be used reliably for subtyping PPH and outperforms a claims-based approach on the three most common PPH subtypes associated with uterine atony, abnormal placentation, and obstetric trauma. The advantage of this approach to subtyping is its interpretability, as each concept contributing to the subtype determination can be evaluated. Moreover, as definitions may change over time due to new guidelines, using granular concepts to create complex phenotypes enables prompt and efficient updating of the algorithm. Using this language modelling approach enables rapid phenotyping without the need for any manually annotated training data across multiple clinical use cases.

[end paper 2]

[begin paper 3]

PMCID = 11545079

Title = The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning

Artificial intelligence, now one of the most promising frontiers of medicine, has a long and tumultuous history punctuated by successes and failures. One of its successes was its application to medical images. We reconstruct the timeline of the advancements in this field, from its origins in the 1940s before crossing medical images to early applications of machine learning to radiology, to the present era where artificial intelligence is revolutionizing radiology.

Artificial intelligence (AI), the wide spectrum of technologies aiming to give machines or computers the ability to perform human-like cognitive functions, began in the 1940s with the first abstract models of intelligent machines. Soon after, in the 1950s and 1960s, machine learning algorithms such as neural networks and decision trees ignited significant enthusiasm. More recent advancements include the refinement of learning algorithms, the development of convolutional neural networks to efficiently analyze images, and methods to synthesize new images. This renewed enthusiasm was also due to the increase in computational power with graphical processing units and the availability of large digital databases to be mined by neural networks. AI soon began to be applied in medicine, first through expert systems designed to support the clinician’s decision and later with neural networks for the detection, classification, or segmentation of malignant lesions in medical images. A recent prospective clinical trial demonstrated the non-inferiority of AI alone compared with a double reading by two radiologists on screening mammography. Natural language processing, recurrent neural networks, transformers, and generative models have both improved the capabilities of making an automated reading of medical images and moved AI to new domains, including the text analysis of electronic health records, image self-labeling, and self-reporting. The availability of open-source and free libraries, as well as powerful computing resources, has greatly facilitated the adoption of deep learning by researchers and clinicians. Key concerns surrounding AI in healthcare include the need for clinical trials to demonstrate efficacy, the perception of AI tools as ‘black boxes’ that require greater interpretability and explainability, and ethical issues related to ensuring fairness and trustworthiness in AI systems. Thanks to its versatility and impressive results, AI is one of the most promising resources for frontier research and applications in medicine, in particular for oncological applications.

[end paper 3]

[begin paper 4]

PMCID = 3302143

Title = Proximal correlates of metabolic phenotypes during ‘at-risk' and ‘case' stages of the metabolic disease continuum

To examine the social and behavioural correlates of metabolic phenotypes during ‘at-risk' and ‘case' stages of the metabolic disease continuum.

Cross-sectional study of a random population sample.

A total of 718 community-dwelling adults (57% female), aged 18–92 years from a regional South Australian city.

Total body fat and lean mass and abdominal fat mass were assessed by dual energy x-ray absorptiometry. Fasting venous blood was collected in the morning for assessment of glycated haemoglobin, plasma glucose, serum triglycerides, cholesterol lipoproteins and insulin. Seated blood pressure (BP) was measured. Physical activity and smoking, alcohol and diet (96-item food frequency), sleep duration and frequency of sleep disordered breathing (SDB) symptoms, and family history of cardiometabolic disease, education, lifetime occupation and household income were assessed by questionnaire. Current medications were determined by clinical inventory.

36.5% were pharmacologically managed for a metabolic risk factor or had known diabetes (‘cases'), otherwise were classified as the ‘at-risk' population. In both ‘at-risk' and ‘cases', four major metabolic phenotypes were identified using principal components analysis that explained over 77% of the metabolic variance between people: fat mass/insulinemia (FMI); BP; lipidaemia/lean mass (LLM) and glycaemia (GLY). The BP phenotype was uncorrelated with other phenotypes in ‘cases', whereas all phenotypes were inter-correlated in the ‘at-risk'. Over and above other socioeconomic and behavioural factors, medications were the dominant correlates of all phenotypes in ‘cases' and SDB symptom frequency was most strongly associated with FMI, LLM and GLY phenotypes in the ‘at-risk'.

Previous research has shown FMI, LLM and GLY phenotypes to be most strongly predictive of diabetes development. Reducing SDB symptom frequency and optimising the duration of sleep may be important concomitant interventions to standard diabetes risk reduction interventions. Prospective studies are required to examine this hypothesis.

[end paper 4]

[begin paper 5]

PMCID = 11460004

Title = A hybrid framework with large language models for rare disease phenotyping

Rare diseases pose significant challenges in diagnosis and treatment due to their low prevalence and heterogeneous clinical presentations. Unstructured clinical notes contain valuable information for identifying rare diseases, but manual curation is time-consuming and prone to subjectivity. This study aims to develop a hybrid approach combining dictionary-based natural language processing (NLP) tools with large language models (LLMs) to improve rare disease identification from unstructured clinical reports.

We propose a novel hybrid framework that integrates the Orphanet Rare Disease Ontology (ORDO) and the Unified Medical Language System (UMLS) to create a comprehensive rare disease vocabulary. SemEHR, a dictionary-based NLP tool, is employed to extract rare disease mentions from clinical notes. To refine the results and improve accuracy, we leverage various LLMs, including LLaMA3, Phi3-mini, and domain-specific models like OpenBioLLM and BioMistral. Different prompting strategies, such as zero-shot, few-shot, and knowledge-augmented generation, are explored to optimize the LLMs’ performance.

The proposed hybrid approach demonstrates superior performance compared to traditional NLP systems and standalone LLMs. LLaMA3 and Phi3-mini achieve the highest F1 scores in rare disease identification. Few-shot prompting with 1-3 examples yields the best results, while knowledge-augmented generation shows limited improvement. Notably, the approach uncovers a significant number of potential rare disease cases not documented in structured diagnostic records, highlighting its ability to identify previously unrecognized patients.

The hybrid approach combining dictionary-based NLP tools with LLMs shows great promise for improving rare disease identification from unstructured clinical reports. By leveraging the strengths of both techniques, the method demonstrates superior performance and the potential to uncover hidden rare disease cases. Further research is needed to address limitations related to ontology mapping and overlapping case identification, and to integrate the approach into clinical practice for early diagnosis and improved patient outcomes.

The online version contains supplementary material available at 10.1186/s12911-024-02698-7.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Interoperability and phenotype definition in clinical applications":

[begin paper 1]

PMCID = 11193731

Title = A study on interoperability between two Personal Health Train infrastructures in leukodystrophy data analysis

The development of platforms for distributed analytics has been driven by a growing need to comply with various governance-related or legal constraints. Among these platforms, the so-called Personal Health Train (PHT) is one representative that has emerged over the recent years. However, in projects that require data from sites featuring different PHT infrastructures, institutions are facing challenges emerging from the combination of multiple PHT ecosystems, including data governance, regulatory compliance, or the modification of existing workflows. In these scenarios, the interoperability of the platforms is preferable. In this work, we introduce a conceptual framework for the technical interoperability of the PHT covering five essential requirements: Data integration, unified station identifiers, mutual metadata, aligned security protocols, and business logic. We evaluated our concept in a feasibility study that involves two distinct PHT infrastructures: PHT-meDIC and PADME. We analyzed data on leukodystrophy from patients in the University Hospitals of Tübingen and Leipzig, and patients with differential diagnoses at the University Hospital Aachen. The results of our study demonstrate the technical interoperability between these two PHT infrastructures, allowing researchers to perform analyses across the participating institutions. Our method is more space-efficient compared to the multi-homing strategy, and it shows only a minimal time overhead.

[end paper 1]

[begin paper 2]

PMCID = 9346559

Title = Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review

The standard Fast Healthcare Interoperability Resources (FHIR) is widely used in health information technology. However, its use as a standard for health research is still less prevalent. To use existing data sources more efficiently for health research, data interoperability becomes increasingly important. FHIR provides solutions by offering resource domains such as “Public Health & Research” and “Evidence-Based Medicine” while using already established web technologies. Therefore, FHIR could help standardize data across different data sources and improve interoperability in health research.

The aim of our study was to provide a systematic review of existing literature and determine the current state of FHIR implementations in health research and possible future directions.

We searched the PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore, and Cochrane Library databases for studies published from 2011 to 2022. Studies investigating the use of FHIR in health research were included. Articles published before 2011, abstracts, reviews, editorials, and expert opinions were excluded. We followed the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines and registered this study with PROSPERO (CRD42021235393). Data synthesis was done in tables and figures.

We identified a total of 998 studies, of which 49 studies were eligible for inclusion. Of the 49 studies, most (73%, n=36) covered the domain of clinical research, whereas the remaining studies focused on public health or epidemiology (6%, n=3) or did not specify their research domain (20%, n=10). Studies used FHIR for data capture (29%, n=14), standardization of data (41%, n=20), analysis (12%, n=6), recruitment (14%, n=7), and consent management (4%, n=2). Most (55%, 27/49) of the studies had a generic approach, and 55% (12/22) of the studies focusing on specific medical specialties (infectious disease, genomics, oncology, environmental health, imaging, and pulmonary hypertension) reported their solutions to be conferrable to other use cases. Most (63%, 31/49) of the studies reported using additional data models or terminologies: Systematized Nomenclature of Medicine Clinical Terms (29%, n=14), Logical Observation Identifiers Names and Codes (37%, n=18), International Classification of Diseases 10th Revision (18%, n=9), Observational Medical Outcomes Partnership common data model (12%, n=6), and others (43%, n=21). Only 4 (8%) studies used a FHIR resource from the domain “Public Health & Research.” Limitations using FHIR included the possible change in the content of FHIR resources, safety, legal matters, and the need for a FHIR server.

Our review found that FHIR can be implemented in health research, and the areas of application are broad and generalizable in most use cases. The implementation of international terminologies was common, and other standards such as the Observational Medical Outcomes Partnership common data model could be used as a complement to FHIR. Limitations such as the change of FHIR content, lack of FHIR implementation, safety, and legal matters need to be addressed in future releases to expand the use of FHIR and, therefore, interoperability in health research.

[end paper 2]

[begin paper 3]

PMCID = 10865191

Title = Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review

The increasing use of electronic health records and the Internet of Things has led to interoperability issues at different levels (structural and semantic). Standards are important not only for successfully exchanging data but also for appropriately interpreting them (semantic interoperability). Thus, to facilitate the semantic interoperability of data exchanged in health care, considerable resources have been deployed to improve the quality of shared clinical data by structuring and mapping them to the Fast Healthcare Interoperability Resources (FHIR) standard.

The aims of this study are 2-fold: to inventory the studies on FHIR semantic interoperability resources and terminologies and to identify and classify the approaches and contributions proposed in these studies.

A systematic mapping review (SMR) was conducted using 10 electronic databases as sources of information for inventory and review studies published during 2012 to 2022 on the development and improvement of semantic interoperability using the FHIR standard.

A total of 70 FHIR studies were selected and analyzed to identify FHIR resource types and terminologies from a semantic perspective. The proposed semantic approaches were classified into 6 categories, namely mapping (31/126, 24.6%), terminology services (18/126, 14.3%), resource description framework or web ontology language–based proposals (24/126, 19%), annotation proposals (18/126, 14.3%), machine learning (ML) and natural language processing (NLP) proposals (20/126, 15.9%), and ontology-based proposals (15/126, 11.9%). From 2012 to 2022, there has been continued research in 6 categories of approaches as well as in new and emerging annotations and ML and NLP proposals. This SMR also classifies the contributions of the selected studies into 5 categories: framework or architecture proposals, model proposals, technique proposals, comparison services, and tool proposals. The most frequent type of contribution is the proposal of a framework or architecture to enable semantic interoperability.

This SMR provides a classification of the different solutions proposed to address semantic interoperability using FHIR at different levels: collecting, extracting and annotating data, modeling electronic health record data from legacy systems, and applying transformation and mapping to FHIR models and terminologies. The use of ML and NLP for unstructured data is promising and has been applied to specific use case scenarios. In addition, terminology services are needed to accelerate their use and adoption; furthermore, techniques and tools to automate annotation and ontology comparison should help reduce human interaction.

[end paper 3]

[begin paper 4]

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 4]

[begin paper 5]

PMCID = 5036847

Title = The digital revolution in phenotyping

Phenotypes have gained increased notoriety in the clinical and biological domain owing to their application in numerous areas such as the discovery of disease genes and drug targets, phylogenetics and pharmacogenomics. Phenotypes, defined as observable characteristics of organisms, can be seen as one of the bridges that lead to a translation of experimental findings into clinical applications and thereby support ‘bench to bedside’ efforts. However, to build this translational bridge, a common and universal understanding of phenotypes is required that goes beyond domain-specific definitions. To achieve this ambitious goal, a digital revolution is ongoing that enables the encoding of data in computer-readable formats and the data storage in specialized repositories, ready for integration, enabling translational research. While phenome research is an ongoing endeavor, the true potential hidden in the currently available data still needs to be unlocked, offering exciting opportunities for the forthcoming years. Here, we provide insights into the state-of-the-art in digital phenotyping, by means of representing, acquiring and analyzing phenotype data. In addition, we provide visions of this field for future research work that could enable better applications of phenotype data.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Building clinician trust in LLM-based phenotyping tools":

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

PMCID = 10834163

Title = Artificial intelligence: revolutionizing cardiology with large language models

Overview of input sources (top) to train or fine-tune cardio large language models and different applications (bottom). ECG, electrocardiogram; Q&A, questions and answers.

Natural language processing techniques are having an increasing impact on clinical care from patient, clinician, administrator, and research perspective. Among others are automated generation of clinical notes and discharge letters, medical term coding for billing, medical chatbots both for patients and clinicians, data enrichment in the identification of disease symptoms or diagnosis, cohort selection for clinical trial, and auditing purposes. In the review, an overview of the history in natural language processing techniques developed with brief technical background is presented. Subsequently, the review will discuss implementation strategies of natural language processing tools, thereby specifically focusing on large language models, and conclude with future opportunities in the application of such techniques in the field of cardiology.

[end paper 2]

[begin paper 3]

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

[end paper 3]

[begin paper 4]

PMCID = 11748787

Title = Artificial intelligence in rheumatology research: what is it good for?

Artificial intelligence (AI) is transforming rheumatology research, with a myriad of studies aiming to improve diagnosis, prognosis and treatment prediction, while also showing potential capability to optimise the research workflow, improve drug discovery and clinical trials. Machine learning, a key element of discriminative AI, has demonstrated the ability of accurately classifying rheumatic diseases and predicting therapeutic outcomes by using diverse data types, including structured databases, imaging and text. In parallel, generative AI, driven by large language models, is becoming a powerful tool for optimising the research workflow by supporting with content generation, literature review automation and clinical decision support. This review explores the current applications and future potential of both discriminative and generative AI in rheumatology. It also highlights the challenges posed by these technologies, such as ethical concerns and the need for rigorous validation and regulatory oversight. The integration of AI in rheumatology promises substantial advancements but requires a balanced approach to optimise benefits and minimise potential possible downsides.

[end paper 4]

[begin paper 5]

PMCID = 11984408

Title = Artificial intelligence in chronic kidney disease management: a scoping review

Rationale: Chronic kidney disease (CKD) is a major public health problem worldwide associated with cardiovascular disease, renal failure, and mortality. To effectively address this growing burden, innovative solutions to management are urgently required. We conducted a scoping review to identify key use cases in which artificial intelligence (AI) could be leveraged for improving management of CKD. Additionally, we examined the challenges faced by AI in CKD management, proposed potential solutions to overcome these barriers.

Methods: We reviewed 41 articles published between 2014-2024 which examined various AI techniques including machine learning (ML) and deep learning (DL), unsupervised clustering, digital twin, natural language processing (NLP) and large language models (LLMs) in CKD management. We focused on four areas: early detection, risk stratification and prediction, treatment recommendations and patient care and communication.

Results: We identified 41 articles published between 2014-2024 that assessed image-based DL models for early detection (n = 6), ML models for risk stratification and prediction (n = 14) and treatment recommendations (n = 4), and NLP and LLMs for patient care and communication (n = 17). Key challenges in integrating AI models into healthcare include technical issues such as data quality and access, model accuracy, and interpretability, alongside adoption barriers like workflow integration, user training, and regulatory approval.

Conclusions: There is tremendous potential of integrating AI into clinical care of CKD patients to enable early detection, prediction, and improved patient outcomes. Collaboration among healthcare providers, researchers, regulators, and industries is crucial to developing robust protocols that ensure compliance with legal standards, while minimizing risks and maintaining patient safety.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in phenotype tools for EHR interoperability":

[begin paper 1]

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 1]

[begin paper 2]

PMCID = 8714300

Title = A State-of-the Art Review of SNOMED CT Terminology Binding and Recommendations for Practice and Research

Background  Unambiguous sharing of data requires information models and terminology in combination, but there is a lack of knowledge as to how they should be combined, leading to impaired interoperability. 

Objectives  To facilitate creation of guidelines for SNOMED CT terminology binding we have performed a literature review to find existing recommendations and expose knowledge gaps. The primary audience is practitioners and researchers working with terminology binding. 

Methods  PubMed, Scopus, and Web of Science were searched for papers containing “terminology binding,” “subset,” “map,” “information model” or “implement” and the term “SNOMED.” 

Results  The search yielded 616 unique papers published from 2004 to 2020, from which 55 papers were selected and analyzed inductively. Topics described in the papers include problems related to input material, SNOMED CT, information models, and lack of appropriate tools as well as recommendations regarding competence. 

Conclusion  Recommendations are given for practitioners and researchers. Many of the stated problems can be solved by better co-operation between domain experts and informaticians and better knowledge of SNOMED CT. Settings where these competences either work together or where staff with knowledge of both act as brokers are well equipped for terminology binding. Tooling is not thoroughly researched and might be a possible way to facilitate terminology binding. 

[end paper 2]

[begin paper 3]

PMCID = 6351992

Title = SNOMED CT Concept Hierarchies for Computable Clinical Phenotypes From Electronic Health Record Data: Comparison of Intensional Versus Extensional Value Sets

Defining clinical phenotypes from electronic health record (EHR)–derived data proves crucial for clinical decision support, population health endeavors, and translational research. EHR diagnoses now commonly draw from a finely grained clinical terminology—either native SNOMED CT or a vendor-supplied terminology mapped to SNOMED CT concepts as the standard for EHR interoperability. Accordingly, electronic clinical quality measures (eCQMs) increasingly define clinical phenotypes with SNOMED CT value sets. The work of creating and maintaining list-based value sets proves daunting, as does insuring that their contents accurately represent the clinically intended condition.

The goal of the research was to compare an intensional (concept hierarchy-based) versus extensional (list-based) value set approach to defining clinical phenotypes using SNOMED CT–encoded data from EHRs by evaluating value set conciseness, time to create, and completeness.

Starting from published Centers for Medicare and Medicaid Services (CMS) high-priority eCQMs, we selected 10 clinical conditions referenced by those eCQMs. For each, the published SNOMED CT list-based (extensional) value set was downloaded from the Value Set Authority Center (VSAC). Ten corresponding SNOMED CT hierarchy-based intensional value sets for the same conditions were identified within our EHR. From each hierarchy-based intensional value set, an exactly equivalent full extensional value set was derived enumerating all included descendant SNOMED CT concepts. Comparisons were then made between (1) VSAC-downloaded list-based (extensional) value sets, (2) corresponding hierarchy-based intensional value sets for the same conditions, and (3) derived list-based (extensional) value sets exactly equivalent to the hierarchy-based intensional value sets. Value set conciseness was assessed by the number of SNOMED CT concepts needed for definition. Time to construct the value sets for local use was measured. Value set completeness was assessed by comparing contents of the downloaded extensional versus intensional value sets. Two measures of content completeness were made: for individual SNOMED CT concepts and for the mapped diagnosis clinical terms available for selection within the EHR by clinicians.

The 10 hierarchy-based intensional value sets proved far simpler and faster to construct than exactly equivalent derived extensional value set lists, requiring a median 3 versus 78 concepts to define and 5 versus 37 minutes to build. The hierarchy-based intensional value sets also proved more complete: in comparison, the 10 downloaded 2018 extensional value sets contained a median of just 35% of the intensional value sets’ SNOMED CT concepts and 65% of mapped EHR clinical terms.

In the EHR era, defining conditions preferentially should employ SNOMED CT concept hierarchy-based (intensional) value sets rather than extensional lists. By doing so, clinical guideline and eCQM authors can more readily engage specialists in vetting condition subtypes to include and exclude, and streamline broad EHR implementation of condition-specific decision support promoting guideline adherence for patient benefit.

[end paper 3]

[begin paper 4]

PMCID = 10403057

Title = A health terminological system for inherited retinal diseases: Content coverage evaluation and a proposed classification

To present a classification of inherited retinal diseases (IRDs) and evaluate its content coverage in comparison with common standard terminology systems.

In this comparative cross-sectional study, a panel of subject matter experts annotated a list of IRDs based on a comprehensive review of the literature. Then, they leveraged clinical terminologies from various reference sets including Unified Medical Language System (UMLS), Online Mendelian Inheritance in Man (OMIM), International Classification of Diseases (ICD-11), Systematized Nomenclature of Medicine (SNOMED-CT) and Orphanet Rare Disease Ontology (ORDO).

Initially, we generated a hierarchical classification of 62 IRD diagnosis concepts in six categories. Subsequently, the classification was extended to 164 IRD diagnoses after adding concepts from various standard terminologies. Finally, 158 concepts were selected to be classified into six categories and genetic subtypes of 412 cases were added to the related concepts. UMLS has the greatest content coverage of 90.51% followed respectively by SNOMED-CT (83.54%), ORDO (81.01%), OMIM (60.76%), and ICD-11 (60.13%). There were 53 IRD concepts (33.54%) that were covered by all five investigated systems. However, 2.53% of the IRD concepts in our classification were not covered by any of the standard terminologies.

This comprehensive classification system was established to organize IRD diseases based on phenotypic and genotypic specifications. It could potentially be used for IRD clinical documentation purposes and could also be considered a preliminary step forward to developing a more robust standard ontology for IRDs or updating available standard terminologies. In comparison, the greatest content coverage of our proposed classification was related to the UMLS Metathesaurus.

[end paper 4]

[begin paper 5]

PMCID = 4748471

Title = Interoperability between phenotypes in research and healthcare terminologies—Investigating partial mappings between HPO and SNOMED CT

Identifying partial mappings between two terminologies is of special importance when one terminology is finer-grained than the other, as is the case for the Human Phenotype Ontology (HPO), mainly used for research purposes, and SNOMED CT, mainly used in healthcare.

To investigate and contrast lexical and logical approaches to deriving partial mappings between HPO and SNOMED CT.

1) Lexical approach—We identify modifiers in HPO terms and attempt to map demodified terms to SNOMED CT through UMLS; 2) Logical approach—We leverage subsumption relations in HPO to infer partial mappings to SNOMED CT; 3) Comparison—We analyze the specific contribution of each approach and evaluate the quality of the partial mappings through manual review.

There are 7358 HPO concepts with no complete mapping to SNOMED CT. We identified partial mappings lexically for 33 % of them and logically for 82 %. We identified partial mappings both lexically and logically for 27 %. The clinical relevance of the partial mappings (for a cohort selection use case) is 49 % for lexical mappings and 67 % for logical mappings.

Through complete and partial mappings, 92 % of the 10,454 HPO concepts can be mapped to SNOMED CT (30 % complete and 62 % partial). Equivalence mappings between HPO and SNOMED CT allow for interoperability between data described using these two systems. However, due to differences in focus and granularity, equivalence is only possible for 30 % of HPO classes. In the remaining cases, partial mappings provide a next-best approach for traversing between the two systems. Both lexical and logical mapping techniques produce mappings that cannot be generated by the other technique, suggesting that the two techniques are complementary to each other. Finally, this work demonstrates interesting properties (both lexical and logical) of HPO and SNOMED CT and illustrates some limitations of mapping through UMLS.

[end paper 5]



