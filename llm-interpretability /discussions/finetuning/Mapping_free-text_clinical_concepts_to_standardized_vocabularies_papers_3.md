## User

This is the beginning of an individual meeting with Clinical Informatics Specialist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Mapping free-text clinical concepts to standardized vocabularies in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Mapping free-text clinical concepts to standardized vocabularies to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Mapping free-text clinical concepts to standardized vocabularies. Include both general queries about Mapping free-text clinical concepts to standardized vocabularies and queries that specifically relate Mapping free-text clinical concepts to standardized vocabularies to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Clinical Informatics Specialist, please provide your response to the agenda.

## Clinical Informatics Specialist

To address the agenda and gather relevant literature on mapping free-text clinical concepts to standardized vocabularies, especially in the context of LLM interpretability and electronic phenotype definitions, I will craft a series of search queries. These queries will focus on various aspects such as general mapping, LLM interpretability, phenotype definition, clinical applications, and clinician trust. Here are the search queries in Python syntax:

```python
search_queries = [
    "Mapping free-text clinical concepts to standardized vocabularies",
    "LLM interpretability in mapping clinical concepts to standardized vocabularies",
    "Electronic phenotype definition using standardized vocabularies",
    "Clinical applications of mapping free-text to standardized vocabularies",
    "Building clinician trust through standardized vocabularies in LLMs"
]
```

Next, I will use these queries to search for relevant scientific papers on PubMed Central. Let's proceed with retrieving the PMCIDs and titles of the papers.

## Clinical Informatics Specialist

Here are the PMCIDs and titles of the papers from the search queries, which will help in fine-tuning on the topic of mapping free-text clinical concepts to standardized vocabularies:

```python
papers = {
    "10452256": "Mapping the Oncological Basis Dataset to the Standardized Vocabularies of a Common Data Model: A Feasibility Study",
    "10196319": "Ontologizing health systems data at scale: making translational discovery a reality",
    "11739813": "A review of large language models and autonomous agents in chemistry",
    "10793431": "Fine-tuning Large Language Models for Rare Disease Concept Normalization",
    "10873827": "OHDSI Standardized Vocabularies—a large-scale centralized reference ontology for international data harmonization",
    "11643188": "Unified Clinical Vocabulary Embeddings for Advancing Precision Medicine",
    "11307071": "IMPatienT: An Integrated Web Application to Digitize, Process and Explore Multimodal PATIENt daTa",
    "8565035": "Standardizing registry data to the OMOP Common Data Model: experience from three pulmonary hypertension databases"
}
```

These papers cover various aspects of mapping free-text clinical concepts to standardized vocabularies, including their application in LLM interpretability, phenotype definition, and building clinician trust. They will serve as a valuable resource for developing a transparent, clinically grounded, and visually intuitive interpretability tool.

## User

Tool Output:

Here are the top 2 articles on PubMed Central for the query "Mapping free-text clinical concepts to standardized vocabularies":

[begin paper 1]

PMCID = 10452256

Title = Mapping the Oncological Basis Dataset to the Standardized Vocabularies of a Common Data Model: A Feasibility Study

Resident physicians and medical institutions in Germany are required to report diagnostics, treatments, progression, and follow-up information for tumor patients to the respective state cancer registries. The information is transmitted electronically according to a defined data scheme (oncological basis dataset [oBDS]). In this study, we first mapped oBDS elements to the standardized vocabularies, a metadata repository of the observational medical outcomes partnership (OMOP) common data model (CDM). The mapping of the oBDS to the standardized vocabularies promotes the semantic interoperability of oncological data in Germany and provides the opportunity to participate in network studies of observational health data sciences and informatics under the usage of federated analysis.

In their joint effort against cancer, all involved parties within the German healthcare system are obligated to report diagnostics, treatments, progression, and follow-up information for tumor patients to the respective cancer registries. Given the federal structure of Germany, the oncological basis dataset (oBDS) operates as the legally required national standard for oncological reporting. Unfortunately, the usage of various documentation software solutions leads to semantic and technical heterogeneity of the data, complicating the establishment of research networks and collective data analysis. Within this feasibility study, we evaluated the transferability of all oBDS characteristics to the standardized vocabularies, a metadata repository of the observational medical outcomes partnership (OMOP) common data model (CDM). A total of 17,844 oBDS expressions were mapped automatically or manually to standardized concepts of the OMOP CDM. In a second step, we converted real patient data retrieved from the Hamburg Cancer Registry to the new terminologies. Given our pipeline, we transformed 1773.373 cancer-related data elements to the OMOP CDM. The mapping of the oBDS to the standardized vocabularies of the OMOP CDM promotes the semantic interoperability of oncological data in Germany. Moreover, it allows the participation in network studies of the observational health data sciences and informatics under the usage of federated analysis beyond the level of individual countries.

[end paper 1]

[begin paper 2]

PMCID = 10196319

Title = Ontologizing health systems data at scale: making translational discovery a reality

Common data models solve many challenges of standardizing electronic health record (EHR) data but are unable to semantically integrate all of the resources needed for deep phenotyping. Open Biological and Biomedical Ontology (OBO) Foundry ontologies provide computable representations of biological knowledge and enable the integration of heterogeneous data. However, mapping EHR data to OBO ontologies requires significant manual curation and domain expertise. We introduce OMOP2OBO, an algorithm for mapping Observational Medical Outcomes Partnership (OMOP) vocabularies to OBO ontologies. Using OMOP2OBO, we produced mappings for 92,367 conditions, 8611 drug ingredients, and 10,673 measurement results, which covered 68–99% of concepts used in clinical practice when examined across 24 hospitals. When used to phenotype rare disease patients, the mappings helped systematically identify undiagnosed patients who might benefit from genetic testing. By aligning OMOP vocabularies to OBO ontologies our algorithm presents new opportunities to advance EHR-based deep phenotyping.

[end paper 2]



Here are the top 2 articles on PubMed Central for the query "LLM interpretability in mapping clinical concepts to standardized vocabularies":

[begin paper 1]

PMCID = 11739813

Title = A review of large language models and autonomous agents in chemistry

Large language models (LLMs) have emerged as powerful tools in chemistry, significantly impacting molecule design, property prediction, and synthesis optimization. This review highlights LLM capabilities in these domains and their potential to accelerate scientific discovery through automation. We also review LLM-based autonomous agents: LLMs with a broader set of tools to interact with their surrounding environment. These agents perform diverse tasks such as paper scraping, interfacing with automated laboratories, and synthesis planning. As agents are an emerging topic, we extend the scope of our review of agents beyond chemistry and discuss across any scientific domains. This review covers the recent history, current capabilities, and design of LLMs and autonomous agents, addressing specific challenges, opportunities, and future directions in chemistry. Key challenges include data quality and integration, model interpretability, and the need for standard benchmarks, while future directions point towards more sophisticated multi-modal agents and enhanced collaboration between agents and experimental methods. Due to the quick pace of this field, a repository has been built to keep track of the latest studies: .

This review examines the roles of large language models (LLMs) and autonomous agents in chemistry, exploring advancements in molecule design, property prediction, and synthesis automation.

[end paper 1]

[begin paper 2]

PMCID = 10793431

Title = Fine-tuning Large Language Models for Rare Disease Concept Normalization

We aim to develop a novel method for rare disease concept normalization by fine-tuning Llama 2, an open-source large language model (LLM), using a domain-specific corpus sourced from the Human Phenotype Ontology (HPO).

We developed an in-house template-based script to generate two corpora for fine-tuning. The first (NAME) contains standardized HPO names, sourced from the HPO vocabularies, along with their corresponding identifiers. The second (NAME+SYN) includes HPO names and half of the concept’s synonyms as well as identifiers. Subsequently, we fine-tuned Llama2 (Llama2-7B) for each sentence set and conducted an evaluation using a range of sentence prompts and various phenotype terms.

When the phenotype terms for normalization were included in the fine-tuning corpora, both models demonstrated nearly perfect performance, averaging over 99% accuracy. In comparison, ChatGPT-3.5 has only ~20% accuracy in identifying HPO IDs for phenotype terms. When single-character typos were introduced in the phenotype terms, the accuracy of NAME and NAME+SYN is 10.2% and 36.1%, respectively, but increases to 61.8% (NAME+SYN) with additional typo-specific fine-tuning. For terms sourced from HPO vocabularies as unseen synonyms, the NAME model achieved 11.2% accuracy, while the NAME+SYN model achieved 92.7% accuracy.

Our fine-tuned models demonstrate ability to normalize phenotype terms unseen in the fine-tuning corpus, including misspellings, synonyms, terms from other ontologies, and laymen’s terms. Our approach provides a solution for the use of LLM to identify named medical entities from the clinical narratives, while successfully normalizing them to standard concepts in a controlled vocabulary.

[end paper 2]



Here are the top 2 articles on PubMed Central for the query "Electronic phenotype definition using standardized vocabularies":

[begin paper 1]

PMCID = 10873827

Title = OHDSI Standardized Vocabularies—a large-scale centralized reference ontology for international data harmonization

The Observational Health Data Sciences and Informatics (OHDSI) is the largest distributed data network in the world encompassing more than 331 data sources with 2.1 billion patient records across 34 countries. It enables large-scale observational research through standardizing the data into a common data model (CDM) (Observational Medical Outcomes Partnership [OMOP] CDM) and requires a comprehensive, efficient, and reliable ontology system to support data harmonization.

We created the OHDSI Standardized Vocabularies—a common reference ontology mandatory to all data sites in the network. It comprises imported and de novo-generated ontologies containing concepts and relationships between them, and the praxis of converting the source data to the OMOP CDM based on these. It enables harmonization through assigned domains according to clinical categories, comprehensive coverage of entities within each domain, support for commonly used international coding schemes, and standardization of semantically equivalent concepts.

The OHDSI Standardized Vocabularies comprise over 10 million concepts from 136 vocabularies. They are used by hundreds of groups and several large data networks. More than 8600 users have performed 50 000 downloads of the system. This open-source resource has proven to address an impediment of large-scale observational research—the dependence on the context of source data representation. With that, it has enabled efficient phenotyping, covariate construction, patient-level prediction, population-level estimation, and standard reporting.

OHDSI has made available a comprehensive, open vocabulary system that is unmatched in its ability to support global observational research. We encourage researchers to exploit it and contribute their use cases to this dynamic resource.

[end paper 1]

[begin paper 2]

PMCID = 11643188

Title = Unified Clinical Vocabulary Embeddings for Advancing Precision Medicine

Integrating clinical knowledge into AI remains challenging despite numerous medical guidelines and vocabularies. Medical codes, central to healthcare systems, often reflect operational patterns shaped by geographic factors, national policies, insurance frameworks, and physician practices rather than the precise representation of clinical knowledge. This disconnect hampers AI in representing clinical relationships, raising concerns about bias, transparency, and generalizability. Here, we developed a resource of 67,124 clinical vocabulary embeddings derived from a clinical knowledge graph tailored to electronic health record vocabularies, spanning over 1.3 million edges. Using graph transformer neural networks, we generated clinical vocabulary embeddings that provide a new representation of clinical knowledge by unifying seven medical vocabularies. These embeddings were validated through a phenotype risk score analysis involving 4.57 million patients from Clalit Healthcare Services, effectively stratifying individuals based on survival outcomes. Inter-institutional panels of clinicians evaluated the embeddings for alignment with clinical knowledge across 90 diseases and 3,000 clinical codes, confirming their robustness and transferability. This resource addresses gaps in integrating clinical vocabularies into AI models and training datasets, paving the way for knowledge-grounded population and patient-level models.

[end paper 2]



Here are the top 2 articles on PubMed Central for the query "Clinical applications of mapping free-text to standardized vocabularies":

[begin paper 1]

PMCID = 11307071

Title = IMPatienT: An Integrated Web Application to Digitize, Process and Explore Multimodal PATIENt daTa

Medical acts, such as imaging, lead to the production of various medical text reports that describe the relevant findings. This induces multimodality in patient data by combining image data with free-text and consequently, multimodal data have become central to drive research and improve diagnoses. However, the exploitation of patient data is problematic as the ecosystem of analysis tools is fragmented according to the type of data (images, text, genetics), the task (processing, exploration) and domain of interest (clinical phenotype, histology). To address the challenges, we developed IMPatienT (Integrated digital Multimodal PATIENt daTa), a simple, flexible and open-source web application to digitize, process and explore multimodal patient data. IMPatienT has a modular architecture allowing to: (i) create a standard vocabulary for a domain, (ii) digitize and process free-text data, (iii) annotate images and perform image segmentation, (iv) generate a visualization dashboard and provide diagnosis decision support. To demonstrate the advantages of IMPatienT, we present a use case on a corpus of 40 simulated muscle biopsy reports of congenital myopathy patients. As IMPatienT provides users with the ability to design their own vocabulary, it can be adapted to any research domain and can be used as a patient registry for exploratory data analysis. A demo instance of the application is available at https://impatient.lbgi.fr/.

[end paper 1]

[begin paper 2]

PMCID = 8565035

Title = Standardizing registry data to the OMOP Common Data Model: experience from three pulmonary hypertension databases

The Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM) can be used to transform observational health data to a common format. CDM transformation allows for analysis across disparate databases for the generation of new, real-word evidence, which is especially important in rare disease where data are limited. Pulmonary hypertension (PH) is a progressive, life-threatening disease, with rare subgroups such as pulmonary arterial hypertension (PAH), for which generating real-world evidence is challenging. Our objective is to document the process and outcomes of transforming registry data in PH to the OMOP CDM, and highlight challenges and our potential solutions.

Three observational studies were transformed from the Clinical Data Interchange Standards Consortium study data tabulation model (SDTM) to OMOP CDM format. OPUS was a prospective, multi-centre registry (2014–2020) and OrPHeUS was a retrospective, multi-centre chart review (2013–2017); both enrolled patients newly treated with macitentan in the US. EXPOSURE is a prospective, multi-centre cohort study (2017–ongoing) of patients newly treated with selexipag or any PAH-specific therapy in Europe and Canada. OMOP CDM version 5.3.1 with recent OMOP CDM vocabulary was used. Imputation rules were defined and applied for missing dates to avoid exclusion of data. Custom target concepts were introduced when existing concepts did not provide sufficient granularity.

Of the 6622 patients in the three registry studies, records were mapped for 6457. Custom target concepts were introduced for PAH subgroups (by combining SNOMED concepts or creating custom concepts) and World Health Organization functional class. Per the OMOP CDM convention, records about the absence of an event, or the lack of information, were not mapped. Excluding these non-event records, 4% (OPUS), 2% (OrPHeUS) and 1% (EXPOSURE) of records were not mapped.

SDTM data from three registries were transformed to the OMOP CDM with limited exclusion of data and deviation from the SDTM database content. Future researchers can apply our strategy and methods in different disease areas, with tailoring as necessary. Mapping registry data to the OMOP CDM facilitates more efficient collaborations between researchers and establishment of federated data networks, which is an unmet need in rare diseases.

The online version contains supplementary material available at 10.1186/s12874-021-01434-3.

[end paper 2]



Here are the top 1 articles on PubMed Central for the query "Building clinician trust through standardized vocabularies in LLMs":

[begin paper 1]

PMCID = 11643188

Title = Unified Clinical Vocabulary Embeddings for Advancing Precision Medicine

Integrating clinical knowledge into AI remains challenging despite numerous medical guidelines and vocabularies. Medical codes, central to healthcare systems, often reflect operational patterns shaped by geographic factors, national policies, insurance frameworks, and physician practices rather than the precise representation of clinical knowledge. This disconnect hampers AI in representing clinical relationships, raising concerns about bias, transparency, and generalizability. Here, we developed a resource of 67,124 clinical vocabulary embeddings derived from a clinical knowledge graph tailored to electronic health record vocabularies, spanning over 1.3 million edges. Using graph transformer neural networks, we generated clinical vocabulary embeddings that provide a new representation of clinical knowledge by unifying seven medical vocabularies. These embeddings were validated through a phenotype risk score analysis involving 4.57 million patients from Clalit Healthcare Services, effectively stratifying individuals based on survival outcomes. Inter-institutional panels of clinicians evaluated the embeddings for alignment with clinical knowledge across 90 diseases and 3,000 clinical codes, confirming their robustness and transferability. This resource addresses gaps in integrating clinical vocabularies into AI models and training datasets, paving the way for knowledge-grounded population and patient-level models.

[end paper 1]



