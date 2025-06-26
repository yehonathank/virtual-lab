## User

This is the beginning of an individual meeting with Clinical Informatics Specialist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic SNOMED CT integration in phenotyping pipelines in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on SNOMED CT integration in phenotyping pipelines to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on SNOMED CT integration in phenotyping pipelines. Include both general queries about SNOMED CT integration in phenotyping pipelines and queries that specifically relate SNOMED CT integration in phenotyping pipelines to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Clinical Informatics Specialist, please provide your response to the agenda.

## Clinical Informatics Specialist

Here are the search queries in Python syntax:

```python
queries = [
    "SNOMED CT integration in phenotyping pipelines",
    "SNOMED CT integration in phenotyping pipelines and LLM interpretability",
    "SNOMED CT integration and phenotype definition",
    "SNOMED CT integration in clinical applications",
    "SNOMED CT integration and clinician trust"
]
```

Based on these queries, here is a dictionary mapping PMCID to the title of the papers that are relevant for fine-tuning on SNOMED CT integration in phenotyping pipelines:

```python
papers = {
    "9757572": "Mapping of UK Biobank clinical codes: Challenges and possible solutions",
    "11179014": "Redefining Health Care Data Interoperability: Empirical Exploration of Large Language Models in Information Exchange",
    "11087727": "Phenotype execution and modeling architecture to support disease surveillance and real-world evidence studies: English sentinel network evaluation",
    "6527418": "Semantic integration of clinical laboratory tests from electronic health records for deep phenotyping and biomarker discovery",
    "10693655": "Natural Language Processing with Machine Learning Methods to Analyze Unstructured Patient-Reported Outcomes Derived from Electronic Health Records: A Systematic Review",
    "11786076": "Methods for identifying health status from routinely collected health data: An overview",
    "9147872": "HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study",
    "10169302": "Logical definition-based identification of potential missing concepts in SNOMED CT",
    "11865875": "Digital Phenotyping of Rare Endocrine Diseases Across International Data Networks and the Effect of Granularity of Original Vocabulary",
    "6289550": "Effect of vocabulary mapping for conditions on phenotype cohorts",
    "11494256": "Use of SNOMED CT in Large Language Models: Scoping Review",
    "7921567": "Strategies for Adopting and Implementing SNOMED CT in Korea",
    "6115234": "Recent Developments in Clinical Terminologies — SNOMED CT, LOINC, and RxNorm",
    "11445620": "PCEtoFHIR: Decomposition of Postcoordinated SNOMED CT Expressions for Storage as HL7 FHIR Resources",
    "11269391": "Early evaluation of a natural language processing tool to improve access to educational resources for surgical patients",
    "10407648": "Ten Topics to Get Started in Medical Informatics Research",
    "10193205": "Understanding Views Around the Creation of a Consented, Donated Databank of Clinical Free Text to Develop and Train Natural Language Processing Models for Research: Focus Group Interviews With Stakeholders",
    "11643188": "Unified Clinical Vocabulary Embeddings for Advancing Precision Medicine"
}
```

These papers cover a range of topics related to SNOMED CT integration, LLM interpretability, phenotype definition, clinical applications, and clinician trust, providing a comprehensive foundation for your research project.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in phenotyping pipelines":

[begin paper 1]

PMCID = 9757572

Title = Mapping of UK Biobank clinical codes: Challenges and possible solutions

The UK Biobank provides a rich collection of longitudinal clinical data coming from different healthcare providers and sources in England, Wales, and Scotland. Although extremely valuable and available to a wide research community, the heterogeneous dataset contains inconsistent medical terminology that is either aligned to several ontologies within the same category or unprocessed. To make these data useful to a research community, data cleaning, curation, and standardization are needed. Significant efforts to perform data reformatting, mapping to any selected ontologies (such as SNOMED-CT) and harmonization are required from any data user to integrate UK Biobank hospital inpatient and self-reported data, data from various registers with primary care (GP) data. The integrated clinical data would provide a more comprehensive picture of one’s medical history.

We evaluated several approaches to map GP clinical Read codes to International Classification of Diseases (ICD) and Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT) terminologies. The results were compared, mapping inconsistencies were flagged, a quality category was assigned to each mapping to evaluate overall mapping quality.

We propose a curation and data integration pipeline for harmonizing diagnosis. We also report challenges identified in mapping Read codes from UK Biobank GP tables to ICD and SNOMED CT.

Some of the challenges–the lack of precise one-to-one mapping between ontologies or the need for additional ontology to fully map terms–are general reflecting trade-offs to be made at different steps. Other challenges are due to automatic mapping and can be overcome by leveraging existing mappings, supplemented with automated and manual curation.

[end paper 1]

[begin paper 2]

PMCID = 11179014

Title = Redefining Health Care Data Interoperability: Empirical Exploration of Large Language Models in Information Exchange

Efficient data exchange and health care interoperability are impeded by medical records often being in nonstandardized or unstructured natural language format. Advanced language models, such as large language models (LLMs), may help overcome current challenges in information exchange.

This study aims to evaluate the capability of LLMs in transforming and transferring health care data to support interoperability.

Using data from the Medical Information Mart for Intensive Care III and UK Biobank, the study conducted 3 experiments. Experiment 1 assessed the accuracy of transforming structured laboratory results into unstructured format. Experiment 2 explored the conversion of diagnostic codes between the coding frameworks of the ICD-9-CM (International Classification of Diseases, Ninth Revision, Clinical Modification), and Systematized Nomenclature of Medicine Clinical Terms (SNOMED-CT) using a traditional mapping table and a text-based approach facilitated by the LLM ChatGPT. Experiment 3 focused on extracting targeted information from unstructured records that included comprehensive clinical information (discharge notes).

The text-based approach showed a high conversion accuracy in transforming laboratory results (experiment 1) and an enhanced consistency in diagnostic code conversion, particularly for frequently used diagnostic names, compared with the traditional mapping approach (experiment 2). In experiment 3, the LLM showed a positive predictive value of 87.2% in extracting generic drug names.

This study highlighted the potential role of LLMs in significantly improving health care data interoperability, demonstrated by their high accuracy and efficiency in data transformation and exchange. The LLMs hold vast potential for enhancing medical data exchange without complex standardization for medical terms and data structure.

[end paper 2]

[begin paper 3]

PMCID = 11087727

Title = Phenotype execution and modeling architecture to support disease surveillance and real-world evidence studies: English sentinel network evaluation

To evaluate Phenotype Execution and Modelling Architecture (PhEMA), to express sharable phenotypes using Clinical Quality Language (CQL) and intensional Systematised Nomenclature of Medicine (SNOMED) Clinical Terms (CT) Fast Healthcare Interoperability Resources (FHIR) valuesets, for exemplar chronic disease, sociodemographic risk factor, and surveillance phenotypes.

We curated 3 phenotypes: Type 2 diabetes mellitus (T2DM), excessive alcohol use, and incident influenza-like illness (ILI) using CQL to define clinical and administrative logic. We defined our phenotypes with valuesets, using SNOMED’s hierarchy and expression constraint language, and CQL, combining valuesets and adding temporal elements where needed. We compared the count of cases found using PhEMA with our existing approach using convenience datasets. We assessed our new approach against published desiderata for phenotypes.

The T2DM phenotype could be defined as 2 intensionally defined SNOMED valuesets and a CQL script. It increased the prevalence from 7.2% to 7.3%. Excess alcohol phenotype was defined by valuesets that added qualitative clinical terms to the quantitative conceptual definitions we currently use; this change increased prevalence by 58%, from 1.2% to 1.9%. We created an ILI valueset with SNOMED concepts, adding a temporal element using CQL to differentiate new episodes. This increased the weekly incidence in our convenience sample (weeks 26-38) from 0.95 cases to 1.11 cases per 100 000 people.

Phenotypes for surveillance and research can be described fully and comprehensibly using CQL and intensional FHIR valuesets. Our use case phenotypes identified a greater number of cases, whilst anticipated from excessive alcohol this was not for our other variable. This may have been due to our use of SNOMED CT hierarchy. Our new process fulfilled a greater number of phenotype desiderata than the one that we had used previously, mostly in the modeling domain. More work is needed to implement that sharing and warehousing domains.

[end paper 3]

[begin paper 4]

PMCID = 6527418

Title = Semantic integration of clinical laboratory tests from electronic health records for deep phenotyping and biomarker discovery

Electronic Health Record (EHR) systems typically define laboratory test results using the Laboratory Observation Identifier Names and Codes (LOINC) and can transmit them using Fast Healthcare Interoperability Resource (FHIR) standards. LOINC has not yet been semantically integrated with computational resources for phenotype analysis. Here, we provide a method for mapping LOINC-encoded laboratory test results transmitted in FHIR standards to Human Phenotype Ontology (HPO) terms. We annotated the medical implications of 2923 commonly used laboratory tests with HPO terms. Using these annotations, our software assesses laboratory test results and converts each result into an HPO term. We validated our approach with EHR data from 15,681 patients with respiratory complaints and identified known biomarkers for asthma. Finally, we provide a freely available SMART on FHIR application that can be used within EHR systems. Our approach allows readily available laboratory tests in EHR to be reused for deep phenotyping and exploits the hierarchical structure of HPO to integrate distinct tests that have comparable medical interpretations for association studies.

[end paper 4]

[begin paper 5]

PMCID = 10693655

Title = Natural Language Processing with Machine Learning Methods to Analyze Unstructured Patient-Reported Outcomes Derived from Electronic Health Records: A Systematic Review

Natural language processing (NLP) combined with machine learning (ML) techniques are increasingly used to process unstructured/free-text patient-reported outcome (PRO) data available in electronic health records (EHRs). This systematic review summarizes the literature reporting NLP/ML systems/toolkits for analyzing PROs in clinical narratives of EHRs and discusses the future directions for the application of this modality in clinical care.

We searched PubMed, Scopus, and Web of Science for studies written in English between 1/1/2000 and 12/31/2020. Seventy-nine studies meeting the eligibility criteria were included. We abstracted and summarized information related to the study purpose, patient population, type/source/amount of unstructured PRO data, linguistic features, and NLP systems/toolkits for processing unstructured PROs in EHRs.

Most of the studies used NLP/ML techniques to extract PROs from clinical narratives (n=74) and mapped the extracted PROs into specific PRO domains for phenotyping or clustering purposes (n=26). Some studies used NLP/ML to process PROs for predicting disease progression or onset of adverse events (n=22) or developing/validating NLP/ML pipelines for analyzing unstructured PROs (n=19). Studies used different linguistic features, including lexical, syntactic, semantic, and contextual features, to process unstructured PROs. Among the 26 NLP systems/toolkits we identified, 14 used rule-based NLP, 8 used hybrid NLP, and 4 used ML algorithms embedded in NLP.

This study supports the potential utility of different NLP/ML techniques in processing unstructured PROs available in EHRs for clinical care. Though using annotation rules for NLP/ML to analyze unstructured PROs is dominant, deploying novel neural ML-based methods is warranted.

[end paper 5]



Here are the top 1 articles on PubMed Central for the query "SNOMED CT integration in phenotyping pipelines and LLM interpretability":

[begin paper 1]

PMCID = 11786076

Title = Methods for identifying health status from routinely collected health data: An overview

Routinely collected health data (RCD) are currently accelerating publications that evaluate the effectiveness and safety of medicines and medical devices. One of the fundamental steps in using these data is developing algorithms to identify health status that can be used for observational studies. However, the process and methodologies for identifying health status from RCD remain insufficiently understood. While most current methods rely on International Classification of Diseases (ICD) codes, they may not be universally applicable. Although machine learning methods hold promise for more accurately identifying the health status, they remain underutilized in RCD studies. To address these significant methodological gaps, we outline key steps and methodological considerations for identifying health statuses in observational studies using RCD. This review has the potential to boost the credibility of findings from observational studies that use RCD.

[end paper 1]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration and phenotype definition":

[begin paper 1]

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 1]

[begin paper 2]

PMCID = 10169302

Title = Logical definition-based identification of potential missing concepts in SNOMED CT

Biomedical ontologies are representations of biomedical knowledge that provide terms with precisely defined meanings. They play a vital role in facilitating biomedical research in a cross-disciplinary manner. Quality issues of biomedical ontologies will hinder their effective usage. One such quality issue is missing concepts. In this study, we introduce a logical definition-based approach to identify potential missing concepts in SNOMED CT. A unique contribution of our approach is that it is capable of obtaining both logical definitions and fully specified names for potential missing concepts.

The logical definitions of unrelated pairs of fully defined concepts in non-lattice subgraphs that indicate quality issues are intersected to generate the logical definitions of potential missing concepts. A text summarization model (called PEGASUS) is fine-tuned to predict the fully specified names of the potential missing concepts from their generated logical definitions. Furthermore, the identified potential missing concepts are validated using external resources including the Unified Medical Language System (UMLS), biomedical literature in PubMed, and a newer version of SNOMED CT.

From the March 2021 US Edition of SNOMED CT, we obtained a total of 30,313 unique logical definitions for potential missing concepts through the intersecting process. We fine-tuned a PEGASUS summarization model with 289,169 training instances and tested it on 36,146 instances. The model achieved 72.83 of ROUGE-1, 51.06 of ROUGE-2, and 71.76 of ROUGE-L on the test dataset. The model correctly predicted 11,549 out of 36,146 fully specified names in the test dataset. Applying the fine-tuned model on the 30,313 unique logical definitions, 23,031 total potential missing concepts were identified. Out of these, a total of 2,312 (10.04%) were automatically validated by either of the three resources.

The results showed that our logical definition-based approach for identification of potential missing concepts in SNOMED CT is encouraging. Nevertheless, there is still room for improving the performance of naming concepts based on logical definitions.

[end paper 2]

[begin paper 3]

PMCID = 11865875

Title = Digital Phenotyping of Rare Endocrine Diseases Across International Data Networks and the Effect of Granularity of Original Vocabulary

Rare diseases occur in <50 per 100000 people and require lifelong management. However, essential epidemiological data on such diseases are lacking, and a consecutive monitoring system across time and regions remains to be established. Standardized digital phenotypes are required to leverage an international data network for research on rare endocrine diseases. We developed digital phenotypes for rare endocrine diseases using the observational medical outcome partnership common data model.

Digital phenotypes of three rare endocrine diseases (medullary thyroid cancer, hypoparathyroidism, pheochromocytoma/paraganglioma) were validated across three databases that use different vocabularies: Severance Hospital’s electronic health record from South Korea; IQVIA’s United Kingdom (UK) database for general practitioners; and IQVIA’s United States (US) hospital database for general hospitals. We estimated the performance of different digital phenotyping methods based on International Classification of Diseases (ICD)-10 in the UK and the US or systematized nomenclature of medicine clinical terms (SNOMED CT) in Korea.

The positive predictive value of digital phenotyping was higher using SNOMED CT-based phenotyping than ICD-10-based phenotyping for all three diseases in Korea (e.g., pheochromocytoma/paraganglioma: ICD-10, 58%–62%; SNOMED CT, 89%). Estimated incidence rates by digital phenotyping were as follows: medullary thyroid cancer, 0.34–2.07 (Korea), 0.13–0.30 (US); hypoparathyroidism, 0.40–1.20 (Korea), 0.59–1.01 (US), 0.00–1.78 (UK); and pheochromocytoma/paraganglioma, 0.95–1.67 (Korea), 0.35–0.77 (US), 0.00–0.49 (UK).

Our findings demonstrate the feasibility of developing digital phenotyping of rare endocrine diseases and highlight the importance of implementing SNOMED CT in routine clinical practice to provide granularity for research.

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

PMCID = 10403057

Title = A health terminological system for inherited retinal diseases: Content coverage evaluation and a proposed classification

To present a classification of inherited retinal diseases (IRDs) and evaluate its content coverage in comparison with common standard terminology systems.

In this comparative cross-sectional study, a panel of subject matter experts annotated a list of IRDs based on a comprehensive review of the literature. Then, they leveraged clinical terminologies from various reference sets including Unified Medical Language System (UMLS), Online Mendelian Inheritance in Man (OMIM), International Classification of Diseases (ICD-11), Systematized Nomenclature of Medicine (SNOMED-CT) and Orphanet Rare Disease Ontology (ORDO).

Initially, we generated a hierarchical classification of 62 IRD diagnosis concepts in six categories. Subsequently, the classification was extended to 164 IRD diagnoses after adding concepts from various standard terminologies. Finally, 158 concepts were selected to be classified into six categories and genetic subtypes of 412 cases were added to the related concepts. UMLS has the greatest content coverage of 90.51% followed respectively by SNOMED-CT (83.54%), ORDO (81.01%), OMIM (60.76%), and ICD-11 (60.13%). There were 53 IRD concepts (33.54%) that were covered by all five investigated systems. However, 2.53% of the IRD concepts in our classification were not covered by any of the standard terminologies.

This comprehensive classification system was established to organize IRD diseases based on phenotypic and genotypic specifications. It could potentially be used for IRD clinical documentation purposes and could also be considered a preliminary step forward to developing a more robust standard ontology for IRDs or updating available standard terminologies. In comparison, the greatest content coverage of our proposed classification was related to the UMLS Metathesaurus.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in clinical applications":

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

PMCID = 9147872

Title = HL7 FHIR with SNOMED-CT to Achieve Semantic and Structural Interoperability in Personal Health Data: A Proof-of-Concept Study

Heterogeneity is a problem in storing and exchanging data in a digital health information system (HIS) following semantic and structural integrity. The existing literature shows different methods to overcome this problem. Fast healthcare interoperable resources (FHIR) as a structural standard may explain other information models, (e.g., personal, physiological, and behavioral data from heterogeneous sources, such as activity sensors, questionnaires, and interviews) with semantic vocabularies, (e.g., Systematized Nomenclature of Medicine—Clinical Terms (SNOMED-CT)) to connect personal health data to an electronic health record (EHR). We design and develop an intuitive health coaching (eCoach) smartphone application to prove the concept. We combine HL7 FHIR and SNOMED-CT vocabularies to exchange personal health data in JavaScript object notion (JSON). This study explores and analyzes our attempt to design and implement a structurally and logically compatible tethered personal health record (PHR) that allows bidirectional communication with an EHR. Our eCoach prototype implements most PHR-S FM functions as an interoperability quality standard. Its end-to-end (E2E) data are protected with a TSD (Services for Sensitive Data) security mechanism. We achieve 0% data loss and 0% unreliable performances during data transfer between PHR and EHR. Furthermore, this experimental study shows the effectiveness of FHIR modular resources toward flexible management of data components in the PHR (eCoach) prototype.

[end paper 2]

[begin paper 3]

PMCID = 7921567

Title = Strategies for Adopting and Implementing SNOMED CT in Korea

The objective of this study was to introduce the Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT), to describe use cases of SNOMED CT with the barriers and facilitators, and finally, to propose strategies for adopting and implementing SNOMED CT in Korea as a member of SNOMED International.

We reviewed a collection of SNOMED CT documents, such as introductory materials, practical guides, technical specifications, and reference materials provided by SNOMED International and the literature on SNOMED CT published by researchers to identify use cases of SNOMED CT with barriers and facilitators. We also surveyed the attendees of SNOMED CT education and training series offered by the Korea Human Resource Development Institute for Health and Welfare to identify perceived barriers to adopting SNOMED CT in Korea.

We identified the barriers and facilitators to adopt SNOMED CT experienced by international terminology experts and prospective Korean users. They were related to governance and infrastructure, support services for use, education and training programs, use cases, and vendor capability to implement SNOMED CT. Based on these findings, we identified strategies for adopting and implementing SNOMED CT in Korea. They included the establishment of SNOMED CT management infrastructure, the development of SNOMED CT education and training programs for various user groups, the provision of support services for SNOMED CT use, and the development of SNOMED CT use cases.

These strategies for the adoption and implementation of SNOMED CT need to be executed step by step.

[end paper 3]

[begin paper 4]

PMCID = 6115234

Title = Recent Developments in Clinical Terminologies — SNOMED CT, LOINC, and RxNorm

 Objective:  To discuss recent developments in clinical terminologies. SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms) is the world's largest clinical terminology, developed by an international consortium. LOINC (Logical Observation Identifiers, Names, and Codes) is an international terminology widely used for clinical and laboratory observations. RxNorm is the standard drug terminology in the U.S. 

 Methods and results:  We present a brief review of the history, current state, and future development of SNOMED CT, LOINC and RxNorm. We also analyze their similarities and differences, and outline areas for greater interoperability among them. 

 Conclusions:  With different starting points, representation formalisms, funding sources, and evolutionary paths, SNOMED CT, LOINC, and RxNorm have evolved over the past few decades into three major clinical terminologies supporting key use cases in clinical practice. Despite their differences, partnerships have been created among their development teams to facilitate interoperability and minimize duplication of effort. 

[end paper 4]

[begin paper 5]

PMCID = 11445620

Title = PCEtoFHIR: Decomposition of Postcoordinated SNOMED CT Expressions for Storage as HL7 FHIR Resources

To ensure interoperability, both structural and semantic standards must be followed. For exchanging medical data between information systems, the structural standard FHIR (Fast Healthcare Interoperability Resources) has recently gained popularity. Regarding semantic interoperability, the reference terminology SNOMED Clinical Terms (SNOMED CT), as a semantic standard, allows for postcoordination, offering advantages over many other vocabularies. These postcoordinated expressions (PCEs) make SNOMED CT an expressive and flexible interlingua, allowing for precise coding of medical facts. However, this comes at the cost of increased complexity, as well as challenges in storage and processing. Additionally, the boundary between semantic (terminology) and structural (information model) standards becomes blurred, leading to what is known as the TermInfo problem. Although often viewed critically, the TermInfo overlap can also be explored for its potential benefits, such as enabling flexible transformation of parts of PCEs.

In this paper, an alternative solution for storing PCEs is presented, which involves combining them with the FHIR data model. Ultimately, all components of a PCE should be expressible solely through precoordinated concepts that are linked to the appropriate elements of the information model.

The approach involves storing PCEs decomposed into their components in alignment with FHIR resources. By utilizing the Web Ontology Language (OWL) to generate an OWL ClassExpression, and combining it with an external reasoner and semantic similarity measures, a precoordinated SNOMED CT concept that most accurately describes the PCE is identified as a Superconcept. In addition, the nonmatching attribute relationships between the Superconcept and the PCE are identified as the “Delta.” Once SNOMED CT attributes are manually mapped to FHIR elements, FHIRPath expressions can be defined for both the Superconcept and the Delta, allowing the identified precoordinated codes to be stored within FHIR resources.

A web application called PCEtoFHIR was developed to implement this approach. In a validation process with 600 randomly selected precoordinated concepts, the formal correctness of the generated OWL ClassExpressions was verified. Additionally, 33 PCEs were used for two separate validation tests. Based on these validations, it was demonstrated that a previously proposed semantic similarity calculation is suitable for determining the Superconcept. Additionally, the 33 PCEs were used to confirm the correct functioning of the entire approach. Furthermore, the FHIR StructureMaps were reviewed and deemed meaningful by FHIR experts.

PCEtoFHIR offers services to decompose PCEs for storage within FHIR resources. When creating structure mappings for specific subdomains of SNOMED CT concepts (eg, allergies) to desired FHIR profiles, the use of SNOMED CT Expression Templates has proven highly effective. Domain experts can create templates with appropriate mappings, which can then be easily reused in a constrained manner by end users.

[end paper 5]



Here are the top 4 articles on PubMed Central for the query "SNOMED CT integration and clinician trust":

[begin paper 1]

PMCID = 11269391

Title = Early evaluation of a natural language processing tool to improve access to educational resources for surgical patients

Accessible patient information sources are vital in educating patients about the benefits and risks of spinal surgery, which is crucial for obtaining informed consent. We aim to assess the effectiveness of a natural language processing (NLP) pipeline in recognizing surgical procedures from clinic letters and linking this with educational resources.

Retrospective examination of letters from patients seeking surgery for degenerative spinal disease at a single neurosurgical center. We utilized MedCAT, a named entity recognition and linking NLP, integrated into the electronic health record (EHR), which extracts concepts and links them to systematized nomenclature of medicine-clinical terms (SNOMED-CT). Investigators reviewed clinic letters, identifying words or phrases that described or identified operations and recording the SNOMED-CT terms as ground truth. This was compared to SNOMED-CT terms identified by the model, untrained on our dataset. A pipeline linking clinic letters to patient-specific educational resources was established, and precision, recall, and F1 scores were calculated.

Across 199 letters the model identified 582 surgical procedures, and the overall pipeline after adding rules a total of 784 procedures (precision = 0.94, recall = 0.86, F1 = 0.91). Across 187 letters with identified SNOMED-CT terms the integrated pipeline linking education resources directly to the EHR was successful in 157 (78%) patients (precision = 0.99, recall = 0.87, F1 = 0.92).

NLP accurately identifies surgical procedures in pre-operative clinic letters within an untrained subspecialty. Performance varies among letter authors and depends on the language used by clinicians. The identified procedures can be linked to patient education resources, potentially improving patients’ understanding of surgical procedures.

The online version contains supplementary material available at 10.1007/s00586-024-08315-5.

[end paper 1]

[begin paper 2]

PMCID = 10407648

Title = Ten Topics to Get Started in Medical Informatics Research

The vast and heterogeneous data being constantly generated in clinics can provide great wealth for patients and research alike. The quickly evolving field of medical informatics research has contributed numerous concepts, algorithms, and standards to facilitate this development. However, these difficult relationships, complex terminologies, and multiple implementations can present obstacles for people who want to get active in the field. With a particular focus on medical informatics research conducted in Germany, we present in our Viewpoint a set of 10 important topics to improve the overall interdisciplinary communication between different stakeholders (eg, physicians, computational experts, experimentalists, students, patient representatives). This may lower the barriers to entry and offer a starting point for collaborations at different levels. The suggested topics are briefly introduced, then general best practice guidance is given, and further resources for in-depth reading or hands-on tutorials are recommended. In addition, the topics are set to cover current aspects and open research gaps of the medical informatics domain, including data regulations and concepts; data harmonization and processing; and data evaluation, visualization, and dissemination. In addition, we give an example on how these topics can be integrated in a medical informatics curriculum for higher education. By recognizing these topics, readers will be able to (1) set clinical and research data into the context of medical informatics, understanding what is possible to achieve with data or how data should be handled in terms of data privacy and storage; (2) distinguish current interoperability standards and obtain first insights into the processes leading to effective data transfer and analysis; and (3) value the use of newly developed technical approaches to utilize the full potential of clinical data.

[end paper 2]

[begin paper 3]

PMCID = 10193205

Title = Understanding Views Around the Creation of a Consented, Donated Databank of Clinical Free Text to Develop and Train Natural Language Processing Models for Research: Focus Group Interviews With Stakeholders

Information stored within electronic health records is often recorded as unstructured text. Special computerized natural language processing (NLP) tools are needed to process this text; however, complex governance arrangements make such data in the National Health Service hard to access, and therefore, it is difficult to use for research in improving NLP methods. The creation of a donated databank of clinical free text could provide an important opportunity for researchers to develop NLP methods and tools and may circumvent delays in accessing the data needed to train the models. However, to date, there has been little or no engagement with stakeholders on the acceptability and design considerations of establishing a free-text databank for this purpose.

This study aimed to ascertain stakeholder views around the creation of a consented, donated databank of clinical free text to help create, train, and evaluate NLP for clinical research and to inform the potential next steps for adopting a partner-led approach to establish a national, funded databank of free text for use by the research community.

Web-based in-depth focus group interviews were conducted with 4 stakeholder groups (patients and members of the public, clinicians, information governance leads and research ethics members, and NLP researchers).

All stakeholder groups were strongly in favor of the databank and saw great value in creating an environment where NLP tools can be tested and trained to improve their accuracy. Participants highlighted a range of complex issues for consideration as the databank is developed, including communicating the intended purpose, the approach to access and safeguarding the data, who should have access, and how to fund the databank. Participants recommended that a small-scale, gradual approach be adopted to start to gather donations and encouraged further engagement with stakeholders to develop a road map and set of standards for the databank.

These findings provide a clear mandate to begin developing the databank and a framework for stakeholder expectations, which we would aim to meet with the databank delivery.

[end paper 3]

[begin paper 4]

PMCID = 11643188

Title = Unified Clinical Vocabulary Embeddings for Advancing Precision Medicine

Integrating clinical knowledge into AI remains challenging despite numerous medical guidelines and vocabularies. Medical codes, central to healthcare systems, often reflect operational patterns shaped by geographic factors, national policies, insurance frameworks, and physician practices rather than the precise representation of clinical knowledge. This disconnect hampers AI in representing clinical relationships, raising concerns about bias, transparency, and generalizability. Here, we developed a resource of 67,124 clinical vocabulary embeddings derived from a clinical knowledge graph tailored to electronic health record vocabularies, spanning over 1.3 million edges. Using graph transformer neural networks, we generated clinical vocabulary embeddings that provide a new representation of clinical knowledge by unifying seven medical vocabularies. These embeddings were validated through a phenotype risk score analysis involving 4.57 million patients from Clalit Healthcare Services, effectively stratifying individuals based on survival outcomes. Inter-institutional panels of clinicians evaluated the embeddings for alignment with clinical knowledge across 90 diseases and 3,000 clinical codes, confirming their robustness and transferability. This resource addresses gaps in integrating clinical vocabularies into AI models and training datasets, paving the way for knowledge-grounded population and patient-level models.

[end paper 4]



