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

To address the agenda and provide a comprehensive response, I'll first outline a series of search queries to find relevant scientific papers on the interoperability of phenotyping tools with EHR standards. These queries will cover both general topics and specific aspects related to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

### Search Queries

```python
search_queries = [
    "Interoperability of phenotyping tools with EHR standards",
    "LLM interpretability in electronic phenotype definition",
    "Interoperability of phenotyping tools and clinical applications",
    "SNOMED CT integration in phenotype definitions",
    "Clinician trust in LLM-based phenotype tools"
]
```

### Next Steps

I will now use these queries to search for relevant scientific papers. This will help us identify the PMCIDs and titles of papers that are crucial for fine-tuning our understanding and contributing effectively to the development of the interpretability tool.

Let's proceed with retrieving the articles using these queries.

## Clinical Informatics Specialist

Here are the PMCIDs and titles of the papers that are relevant to the topic of interoperability of phenotyping tools with EHR standards, as well as their relation to LLM interpretability, phenotype definition, clinical applications, and clinician trust:

```python
papers = {
    "11472501": "State-of-the-Art Fast Healthcare Interoperability Resources (FHIR)–Based Data Model and Structure Implementations: Systematic Scoping Review",
    "9147872": "HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study",
    "9346559": "Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review",
    "10865191": "Electronic Health Record and Semantic Issues Using Fast Healthcare Interoperability Resources: Systematic Mapping Review",
    "6990976": "Developing a FHIR-based EHR phenotyping framework: A case study for identification of patients with obesity and multiple comorbidities from discharge summaries",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "11639975": "EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy",
    "10689487": "Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models",
    "8367187": "Ethical Development of Digital Phenotyping Tools for Mental Health Applications: Delphi Study",
    "10169302": "Logical definition-based identification of potential missing concepts in SNOMED CT",
    "11865875": "Digital Phenotyping of Rare Endocrine Diseases Across International Data Networks and the Effect of Granularity of Original Vocabulary",
    "10834163": "Artificial intelligence: revolutionizing cardiology with large language models",
    "10984041": "Inductive reasoning with large language models: a simulated randomized controlled trial for epilepsy",
    "11748787": "Artificial intelligence in rheumatology research: what is it good for?"
}
```

These papers cover a range of topics including FHIR-based data models, SNOMED CT integration, LLM interpretability, and the use of AI in clinical applications, which are all relevant to your research project.

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



Here are the top 5 articles on PubMed Central for the query "LLM interpretability in electronic phenotype definition":

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

PMCID = 11480249

Title = Confronting the data deluge: How artificial intelligence can be used in the study of plant stress

The advent of the genomics era enabled the generation of high-throughput data and computational methods that serve as powerful hypothesis-generating tools to understand the genomic and gene functional basis of plant stress resilience. The proliferation of experimental and analytical methods used in biology has resulted in a situation where plentiful data exists, but the volume and heterogeneity of this data has made analysis a significant challenge. Current advanced deep-learning models have displayed an unprecedented level of comprehension and problem-solving ability, and have been used to predict gene structure, function and expression based on DNA or protein sequence, and prominently also their use in high-throughput phenomics in agriculture. However, the application of deep-learning models to understand gene regulatory and signalling behaviour is still in its infancy. We discuss in this review the availability of data resources and bioinformatic tools, and several applications of these advanced ML/AI models in the context of plant stress response, and demonstrate the use of a publicly available LLM (ChatGPT) to derive a knowledge graph of various experimental and computational methods used in the study of plant stress. We hope this will stimulate further interest in collaboration between computer scientists, computational biologists and plant scientists to distil the deluge of genomic, transcriptomic, proteomic, metabolomic and phenomic data into meaningful knowledge that can be used for the benefit of humanity.

[end paper 2]

[begin paper 3]

PMCID = 11639975

Title = EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy

In recent years, large language models have shown great potential to enhance traditional medical image processing by incorporating multimodality information into decision-making. Conventional artificial intelligence systems solely rely on images to make predictions or decisions. However, information from medical reports can provide invaluable information for the system to curate its decision. Here we are presenting a multimodality language-vision model and framework for accurate segmentation of medical images.

Background/Objectives: Lung cancer is a devastating disease with the highest mortality rate among cancer types. Over 60% of non-small cell lung cancer (NSCLC) patients, accounting for 87% of lung cancer diagnoses, require radiation therapy. Rapid treatment initiation significantly increases the patient’s survival rate and reduces the mortality rate. Accurate tumor segmentation is a critical step in diagnosing and treating NSCLC. Manual segmentation is time- and labor-consuming and causes delays in treatment initiation. Although many lung nodule detection methods, including deep learning-based models, have been proposed. Most of these methods still have a long-standing problem of high false positives (FPs). Methods: Here, we developed an electronic health record (EHR)-guided lung tumor auto-segmentation called EXACT-Net (EHR-enhanced eXACtitude in Tumor segmentation), where the extracted information from EHRs using a pre-trained large language model (LLM) was used to remove the FPs and keep the TP nodules only. Results: The auto-segmentation model was trained on NSCLC patients’ computed tomography (CT), and the pre-trained LLM was used with the zero-shot learning approach. Our approach resulted in a 250% boost in successful nodule detection using the data from ten NSCLC patients treated in our institution. Conclusions: We demonstrated that combining vision-language information in EXACT-Net multi-modal AI framework greatly enhances the performance of vision only models, paving the road to multimodal AI framework for medical image processing.

[end paper 3]

[begin paper 4]

PMCID = 11545079

Title = The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning

Artificial intelligence, now one of the most promising frontiers of medicine, has a long and tumultuous history punctuated by successes and failures. One of its successes was its application to medical images. We reconstruct the timeline of the advancements in this field, from its origins in the 1940s before crossing medical images to early applications of machine learning to radiology, to the present era where artificial intelligence is revolutionizing radiology.

Artificial intelligence (AI), the wide spectrum of technologies aiming to give machines or computers the ability to perform human-like cognitive functions, began in the 1940s with the first abstract models of intelligent machines. Soon after, in the 1950s and 1960s, machine learning algorithms such as neural networks and decision trees ignited significant enthusiasm. More recent advancements include the refinement of learning algorithms, the development of convolutional neural networks to efficiently analyze images, and methods to synthesize new images. This renewed enthusiasm was also due to the increase in computational power with graphical processing units and the availability of large digital databases to be mined by neural networks. AI soon began to be applied in medicine, first through expert systems designed to support the clinician’s decision and later with neural networks for the detection, classification, or segmentation of malignant lesions in medical images. A recent prospective clinical trial demonstrated the non-inferiority of AI alone compared with a double reading by two radiologists on screening mammography. Natural language processing, recurrent neural networks, transformers, and generative models have both improved the capabilities of making an automated reading of medical images and moved AI to new domains, including the text analysis of electronic health records, image self-labeling, and self-reporting. The availability of open-source and free libraries, as well as powerful computing resources, has greatly facilitated the adoption of deep learning by researchers and clinicians. Key concerns surrounding AI in healthcare include the need for clinical trials to demonstrate efficacy, the perception of AI tools as ‘black boxes’ that require greater interpretability and explainability, and ethical issues related to ensuring fairness and trustworthiness in AI systems. Thanks to its versatility and impressive results, AI is one of the most promising resources for frontier research and applications in medicine, in particular for oncological applications.

[end paper 4]

[begin paper 5]

PMCID = 10689487

Title = Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models

Many areas of medicine would benefit from deeper, more accurate phenotyping, but there are limited approaches for phenotyping using clinical notes without substantial annotated data. Large language models (LLMs) have demonstrated immense potential to adapt to novel tasks with no additional training by specifying task-specific instructions. Here we report the performance of a publicly available LLM, Flan-T5, in phenotyping patients with postpartum hemorrhage (PPH) using discharge notes from electronic health records (n = 271,081). The language model achieves strong performance in extracting 24 granular concepts associated with PPH. Identifying these granular concepts accurately allows the development of interpretable, complex phenotypes and subtypes. The Flan-T5 model achieves high fidelity in phenotyping PPH (positive predictive value of 0.95), identifying 47% more patients with this complication compared to the current standard of using claims codes. This LLM pipeline can be used reliably for subtyping PPH and outperforms a claims-based approach on the three most common PPH subtypes associated with uterine atony, abnormal placentation, and obstetric trauma. The advantage of this approach to subtyping is its interpretability, as each concept contributing to the subtype determination can be evaluated. Moreover, as definitions may change over time due to new guidelines, using granular concepts to create complex phenotypes enables prompt and efficient updating of the algorithm. Using this language modelling approach enables rapid phenotyping without the need for any manually annotated training data across multiple clinical use cases.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Interoperability of phenotyping tools and clinical applications":

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

PMCID = 8367187

Title = Ethical Development of Digital Phenotyping Tools for Mental Health Applications: Delphi Study

Digital phenotyping (also known as personal sensing, intelligent sensing, or body computing) involves the collection of biometric and personal data in situ from digital devices, such as smartphones, wearables, or social media, to measure behavior or other health indicators. The collected data are analyzed to generate moment-by-moment quantification of a person’s mental state and potentially predict future mental states. Digital phenotyping projects incorporate data from multiple sources, such as electronic health records, biometric scans, or genetic testing. As digital phenotyping tools can be used to study and predict behavior, they are of increasing interest for a range of consumer, government, and health care applications. In clinical care, digital phenotyping is expected to improve mental health diagnoses and treatment. At the same time, mental health applications of digital phenotyping present significant areas of ethical concern, particularly in terms of privacy and data protection, consent, bias, and accountability.

This study aims to develop consensus statements regarding key areas of ethical guidance for mental health applications of digital phenotyping in the United States.

We used a modified Delphi technique to identify the emerging ethical challenges posed by digital phenotyping for mental health applications and to formulate guidance for addressing these challenges. Experts in digital phenotyping, data science, mental health, law, and ethics participated as panelists in the study. The panel arrived at consensus recommendations through an iterative process involving interviews and surveys. The panelists focused primarily on clinical applications for digital phenotyping for mental health but also included recommendations regarding transparency and data protection to address potential areas of misuse of digital phenotyping data outside of the health care domain.

The findings of this study showed strong agreement related to these ethical issues in the development of mental health applications of digital phenotyping: privacy, transparency, consent, accountability, and fairness. Consensus regarding the recommendation statements was strongest when the guidance was stated broadly enough to accommodate a range of potential applications. The privacy and data protection issues that the Delphi participants found particularly critical to address related to the perceived inadequacies of current regulations and frameworks for protecting sensitive personal information and the potential for sale and analysis of personal data outside of health systems.

The Delphi study found agreement on a number of ethical issues to prioritize in the development of digital phenotyping for mental health applications. The Delphi consensus statements identified general recommendations and principles regarding the ethical application of digital phenotyping to mental health. As digital phenotyping for mental health is implemented in clinical care, there remains a need for empirical research and consultation with relevant stakeholders to further understand and address relevant ethical issues.

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

PMCID = 9346559

Title = Fast Healthcare Interoperability Resources (FHIR) for Interoperability in Health Research: Systematic Review

The standard Fast Healthcare Interoperability Resources (FHIR) is widely used in health information technology. However, its use as a standard for health research is still less prevalent. To use existing data sources more efficiently for health research, data interoperability becomes increasingly important. FHIR provides solutions by offering resource domains such as “Public Health & Research” and “Evidence-Based Medicine” while using already established web technologies. Therefore, FHIR could help standardize data across different data sources and improve interoperability in health research.

The aim of our study was to provide a systematic review of existing literature and determine the current state of FHIR implementations in health research and possible future directions.

We searched the PubMed/MEDLINE, Embase, Web of Science, IEEE Xplore, and Cochrane Library databases for studies published from 2011 to 2022. Studies investigating the use of FHIR in health research were included. Articles published before 2011, abstracts, reviews, editorials, and expert opinions were excluded. We followed the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines and registered this study with PROSPERO (CRD42021235393). Data synthesis was done in tables and figures.

We identified a total of 998 studies, of which 49 studies were eligible for inclusion. Of the 49 studies, most (73%, n=36) covered the domain of clinical research, whereas the remaining studies focused on public health or epidemiology (6%, n=3) or did not specify their research domain (20%, n=10). Studies used FHIR for data capture (29%, n=14), standardization of data (41%, n=20), analysis (12%, n=6), recruitment (14%, n=7), and consent management (4%, n=2). Most (55%, 27/49) of the studies had a generic approach, and 55% (12/22) of the studies focusing on specific medical specialties (infectious disease, genomics, oncology, environmental health, imaging, and pulmonary hypertension) reported their solutions to be conferrable to other use cases. Most (63%, 31/49) of the studies reported using additional data models or terminologies: Systematized Nomenclature of Medicine Clinical Terms (29%, n=14), Logical Observation Identifiers Names and Codes (37%, n=18), International Classification of Diseases 10th Revision (18%, n=9), Observational Medical Outcomes Partnership common data model (12%, n=6), and others (43%, n=21). Only 4 (8%) studies used a FHIR resource from the domain “Public Health & Research.” Limitations using FHIR included the possible change in the content of FHIR resources, safety, legal matters, and the need for a FHIR server.

Our review found that FHIR can be implemented in health research, and the areas of application are broad and generalizable in most use cases. The implementation of international terminologies was common, and other standards such as the Observational Medical Outcomes Partnership common data model could be used as a complement to FHIR. Limitations such as the change of FHIR content, lack of FHIR implementation, safety, and legal matters need to be addressed in future releases to expand the use of FHIR and, therefore, interoperability in health research.

[end paper 4]

[begin paper 5]

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in phenotype definitions":

[begin paper 1]

PMCID = 10169302

Title = Logical definition-based identification of potential missing concepts in SNOMED CT

Biomedical ontologies are representations of biomedical knowledge that provide terms with precisely defined meanings. They play a vital role in facilitating biomedical research in a cross-disciplinary manner. Quality issues of biomedical ontologies will hinder their effective usage. One such quality issue is missing concepts. In this study, we introduce a logical definition-based approach to identify potential missing concepts in SNOMED CT. A unique contribution of our approach is that it is capable of obtaining both logical definitions and fully specified names for potential missing concepts.

The logical definitions of unrelated pairs of fully defined concepts in non-lattice subgraphs that indicate quality issues are intersected to generate the logical definitions of potential missing concepts. A text summarization model (called PEGASUS) is fine-tuned to predict the fully specified names of the potential missing concepts from their generated logical definitions. Furthermore, the identified potential missing concepts are validated using external resources including the Unified Medical Language System (UMLS), biomedical literature in PubMed, and a newer version of SNOMED CT.

From the March 2021 US Edition of SNOMED CT, we obtained a total of 30,313 unique logical definitions for potential missing concepts through the intersecting process. We fine-tuned a PEGASUS summarization model with 289,169 training instances and tested it on 36,146 instances. The model achieved 72.83 of ROUGE-1, 51.06 of ROUGE-2, and 71.76 of ROUGE-L on the test dataset. The model correctly predicted 11,549 out of 36,146 fully specified names in the test dataset. Applying the fine-tuned model on the 30,313 unique logical definitions, 23,031 total potential missing concepts were identified. Out of these, a total of 2,312 (10.04%) were automatically validated by either of the three resources.

The results showed that our logical definition-based approach for identification of potential missing concepts in SNOMED CT is encouraging. Nevertheless, there is still room for improving the performance of naming concepts based on logical definitions.

[end paper 1]

[begin paper 2]

PMCID = 11865875

Title = Digital Phenotyping of Rare Endocrine Diseases Across International Data Networks and the Effect of Granularity of Original Vocabulary

Rare diseases occur in <50 per 100000 people and require lifelong management. However, essential epidemiological data on such diseases are lacking, and a consecutive monitoring system across time and regions remains to be established. Standardized digital phenotypes are required to leverage an international data network for research on rare endocrine diseases. We developed digital phenotypes for rare endocrine diseases using the observational medical outcome partnership common data model.

Digital phenotypes of three rare endocrine diseases (medullary thyroid cancer, hypoparathyroidism, pheochromocytoma/paraganglioma) were validated across three databases that use different vocabularies: Severance Hospital’s electronic health record from South Korea; IQVIA’s United Kingdom (UK) database for general practitioners; and IQVIA’s United States (US) hospital database for general hospitals. We estimated the performance of different digital phenotyping methods based on International Classification of Diseases (ICD)-10 in the UK and the US or systematized nomenclature of medicine clinical terms (SNOMED CT) in Korea.

The positive predictive value of digital phenotyping was higher using SNOMED CT-based phenotyping than ICD-10-based phenotyping for all three diseases in Korea (e.g., pheochromocytoma/paraganglioma: ICD-10, 58%–62%; SNOMED CT, 89%). Estimated incidence rates by digital phenotyping were as follows: medullary thyroid cancer, 0.34–2.07 (Korea), 0.13–0.30 (US); hypoparathyroidism, 0.40–1.20 (Korea), 0.59–1.01 (US), 0.00–1.78 (UK); and pheochromocytoma/paraganglioma, 0.95–1.67 (Korea), 0.35–0.77 (US), 0.00–0.49 (UK).

Our findings demonstrate the feasibility of developing digital phenotyping of rare endocrine diseases and highlight the importance of implementing SNOMED CT in routine clinical practice to provide granularity for research.

[end paper 2]

[begin paper 3]

PMCID = 8714300

Title = A State-of-the Art Review of SNOMED CT Terminology Binding and Recommendations for Practice and Research

Background  Unambiguous sharing of data requires information models and terminology in combination, but there is a lack of knowledge as to how they should be combined, leading to impaired interoperability. 

Objectives  To facilitate creation of guidelines for SNOMED CT terminology binding we have performed a literature review to find existing recommendations and expose knowledge gaps. The primary audience is practitioners and researchers working with terminology binding. 

Methods  PubMed, Scopus, and Web of Science were searched for papers containing “terminology binding,” “subset,” “map,” “information model” or “implement” and the term “SNOMED.” 

Results  The search yielded 616 unique papers published from 2004 to 2020, from which 55 papers were selected and analyzed inductively. Topics described in the papers include problems related to input material, SNOMED CT, information models, and lack of appropriate tools as well as recommendations regarding competence. 

Conclusion  Recommendations are given for practitioners and researchers. Many of the stated problems can be solved by better co-operation between domain experts and informaticians and better knowledge of SNOMED CT. Settings where these competences either work together or where staff with knowledge of both act as brokers are well equipped for terminology binding. Tooling is not thoroughly researched and might be a possible way to facilitate terminology binding. 

[end paper 3]

[begin paper 4]

PMCID = 6289550

Title = Effect of vocabulary mapping for conditions on phenotype cohorts

To study the effect on patient cohorts of mapping condition (diagnosis) codes from source billing vocabularies to a clinical vocabulary.

Nine International Classification of Diseases, Ninth Revision, Clinical Modification (ICD9-CM) concept sets were extracted from eMERGE network phenotypes, translated to Systematized Nomenclature of Medicine - Clinical Terms concept sets, and applied to patient data that were mapped from source ICD9-CM and ICD10-CM codes to Systematized Nomenclature of Medicine - Clinical Terms codes using Observational Health Data Sciences and Informatics (OHDSI) Observational Medical Outcomes Partnership (OMOP) vocabulary mappings. The original ICD9-CM concept set and a concept set extended to ICD10-CM were used to create patient cohorts that served as gold standards.

Four phenotype concept sets were able to be translated to Systematized Nomenclature of Medicine - Clinical Terms without ambiguities and were able to perform perfectly with respect to the gold standards. The other 5 lost performance when 2 or more ICD9-CM or ICD10-CM codes mapped to the same Systematized Nomenclature of Medicine - Clinical Terms code. The patient cohorts had a total error (false positive and false negative) of up to 0.15% compared to querying ICD9-CM source data and up to 0.26% compared to querying ICD9-CM and ICD10-CM data. Knowledge engineering was required to produce that performance; simple automated methods to generate concept sets had errors up to 10% (one outlier at 250%).

The translation of data from source vocabularies to Systematized Nomenclature of Medicine - Clinical Terms (SNOMED CT) resulted in very small error rates that were an order of magnitude smaller than other error sources.

It appears possible to map diagnoses from disparate vocabularies to a single clinical vocabulary and carry out research using a single set of definitions, thus improving efficiency and transportability of research.

[end paper 4]

[begin paper 5]

PMCID = 6351992

Title = SNOMED CT Concept Hierarchies for Computable Clinical Phenotypes From Electronic Health Record Data: Comparison of Intensional Versus Extensional Value Sets

Defining clinical phenotypes from electronic health record (EHR)–derived data proves crucial for clinical decision support, population health endeavors, and translational research. EHR diagnoses now commonly draw from a finely grained clinical terminology—either native SNOMED CT or a vendor-supplied terminology mapped to SNOMED CT concepts as the standard for EHR interoperability. Accordingly, electronic clinical quality measures (eCQMs) increasingly define clinical phenotypes with SNOMED CT value sets. The work of creating and maintaining list-based value sets proves daunting, as does insuring that their contents accurately represent the clinically intended condition.

The goal of the research was to compare an intensional (concept hierarchy-based) versus extensional (list-based) value set approach to defining clinical phenotypes using SNOMED CT–encoded data from EHRs by evaluating value set conciseness, time to create, and completeness.

Starting from published Centers for Medicare and Medicaid Services (CMS) high-priority eCQMs, we selected 10 clinical conditions referenced by those eCQMs. For each, the published SNOMED CT list-based (extensional) value set was downloaded from the Value Set Authority Center (VSAC). Ten corresponding SNOMED CT hierarchy-based intensional value sets for the same conditions were identified within our EHR. From each hierarchy-based intensional value set, an exactly equivalent full extensional value set was derived enumerating all included descendant SNOMED CT concepts. Comparisons were then made between (1) VSAC-downloaded list-based (extensional) value sets, (2) corresponding hierarchy-based intensional value sets for the same conditions, and (3) derived list-based (extensional) value sets exactly equivalent to the hierarchy-based intensional value sets. Value set conciseness was assessed by the number of SNOMED CT concepts needed for definition. Time to construct the value sets for local use was measured. Value set completeness was assessed by comparing contents of the downloaded extensional versus intensional value sets. Two measures of content completeness were made: for individual SNOMED CT concepts and for the mapped diagnosis clinical terms available for selection within the EHR by clinicians.

The 10 hierarchy-based intensional value sets proved far simpler and faster to construct than exactly equivalent derived extensional value set lists, requiring a median 3 versus 78 concepts to define and 5 versus 37 minutes to build. The hierarchy-based intensional value sets also proved more complete: in comparison, the 10 downloaded 2018 extensional value sets contained a median of just 35% of the intensional value sets’ SNOMED CT concepts and 65% of mapped EHR clinical terms.

In the EHR era, defining conditions preferentially should employ SNOMED CT concept hierarchy-based (intensional) value sets rather than extensional lists. By doing so, clinical guideline and eCQM authors can more readily engage specialists in vetting condition subtypes to include and exclude, and streamline broad EHR implementation of condition-specific decision support promoting guideline adherence for patient benefit.

[end paper 5]



Here are the top 3 articles on PubMed Central for the query "Clinician trust in LLM-based phenotype tools":

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



