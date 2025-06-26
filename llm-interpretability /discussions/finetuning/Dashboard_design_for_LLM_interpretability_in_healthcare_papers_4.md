## User

This is the beginning of an individual meeting with Data Visualization Expert to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Dashboard design for LLM interpretability in healthcare in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Dashboard design for LLM interpretability in healthcare to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Dashboard design for LLM interpretability in healthcare. Include both general queries about Dashboard design for LLM interpretability in healthcare and queries that specifically relate Dashboard design for LLM interpretability in healthcare to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Data Visualization Expert, please provide your response to the agenda.

## Data Visualization Expert

Here are the PMCIDs and titles of the papers that are relevant to the topic of Dashboard design for LLM interpretability in healthcare, along with their specific contexts:

```python
{
    "11413421": "Prompt engineering on leveraging large language models in generating response to InBasket messages",
    "11762383": "Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules",
    "11511449": "AI Applications in Adult Stroke Recovery and Rehabilitation: A Scoping Review Using AI",
    "4959395": "The Mining Minds digital health and wellness framework",
    "11502405": "Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature",
    "10649223": "Deep Learning for Genomics: From Early Neural Nets to Modern Large Language Models",
    "11638732": "Real-world evidence in the cloud: Tutorial on developing an end-to-end data and analytics pipeline using Amazon Web Services resources",
    "11494256": "Use of SNOMED CT in Large Language Models: Scoping Review",
    "11925797": "Computational tools and data integration to accelerate vaccine development: challenges, opportunities, and future directions",
    "10793431": "Fine-tuning Large Language Models for Rare Disease Concept Normalization",
    "10601652": "A review of the explainability and safety of conversational agents for mental health to identify avenues for improvement",
    "11891111": "NSSC: a neuro-symbolic AI system for enhancing accuracy of named entity recognition and linking from oncologic clinical notes"
}
```

These papers cover a range of topics related to LLM interpretability, clinical applications, phenotype definitions, and the integration of SNOMED CT, providing a comprehensive foundation for understanding dashboard design in healthcare.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Dashboard design for LLM interpretability in healthcare":

[begin paper 1]

PMCID = 11413421

Title = Prompt engineering on leveraging large language models in generating response to InBasket messages

Large Language Models (LLMs) have been proposed as a solution to address high volumes of Patient Medical Advice Requests (PMARs). This study addresses whether LLMs can generate high quality draft responses to PMARs that satisfies both patients and clinicians with prompt engineering.

We designed a novel human-involved iterative processes to train and validate prompts to LLM in creating appropriate responses to PMARs. GPT-4 was used to generate response to the messages. We updated the prompts, and evaluated both clinician and patient acceptance of LLM-generated draft responses at each iteration, and tested the optimized prompt on independent validation data sets. The optimized prompt was implemented in the electronic health record production environment and tested by 69 primary care clinicians.

After 3 iterations of prompt engineering, physician acceptance of draft suitability increased from 62% to 84% (P <.001) in the validation dataset (N = 200), and 74% of drafts in the test dataset were rated as “helpful.” Patients also noted significantly increased favorability of message tone (78%) and overall quality (80%) for the optimized prompt compared to the original prompt in the training dataset, patients were unable to differentiate human and LLM-generated draft PMAR responses for 76% of the messages, in contrast to the earlier preference for human-generated responses. Majority (72%) of clinicians believed it can reduce cognitive load in dealing with InBasket messages.

Informed by clinician and patient feedback synergistically, tuning in LLM prompt alone can be effective in creating clinically relevant and useful draft responses to PMARs.

[end paper 1]

[begin paper 2]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 2]

[begin paper 3]

PMCID = 11511449

Title = AI Applications in Adult Stroke Recovery and Rehabilitation: A Scoping Review Using AI

Stroke is a leading cause of long-term disability worldwide. With the advancements in sensor technologies and data availability, artificial intelligence (AI) holds the promise of improving the amount, quality and efficiency of care and enhancing the precision of stroke rehabilitation. We aimed to identify and characterize the existing research on AI applications in stroke recovery and rehabilitation of adults, including categories of application and progression of technologies over time. Data were collected from peer-reviewed articles across various electronic databases up to January 2024. Insights were extracted using AI-enhanced multi-method, data-driven techniques, including clustering of themes and topics. This scoping review summarizes outcomes from 704 studies. Four common themes (impairment, assisted intervention, prediction and imaging, and neuroscience) were identified, in which time-linked patterns emerged. The impairment theme revealed a focus on motor function, gait and mobility, while the assisted intervention theme included applications of robotic and brain–computer interface (BCI) techniques. AI applications progressed over time, starting from conceptualization and then expanding to a broader range of techniques in supervised learning, artificial neural networks (ANN), natural language processing (NLP) and more. Applications focused on upper limb rehabilitation were reviewed in more detail, with machine learning (ML), deep learning techniques and sensors such as inertial measurement units (IMU) used for upper limb and functional movement analysis. AI applications have potential to facilitate tailored therapeutic delivery, thereby contributing to the optimization of rehabilitation outcomes and promoting sustained recovery from rehabilitation to real-world settings.

[end paper 3]

[begin paper 4]

PMCID = 4959395

Title = The Mining Minds digital health and wellness framework

The provision of health and wellness care is undergoing an enormous transformation. A key element of this revolution consists in prioritizing prevention and proactivity based on the analysis of people’s conducts and the empowerment of individuals in their self-management. Digital technologies are unquestionably destined to be the main engine of this change, with an increasing number of domain-specific applications and devices commercialized every year; however, there is an apparent lack of frameworks capable of orchestrating and intelligently leveraging, all the data, information and knowledge generated through these systems.

This work presents Mining Minds, a novel framework that builds on the core ideas of the digital health and wellness paradigms to enable the provision of personalized support. Mining Minds embraces some of the most prominent digital technologies, ranging from Big Data and Cloud Computing to Wearables and Internet of Things, as well as modern concepts and methods, such as context-awareness, knowledge bases or analytics, to holistically and continuously investigate on people’s lifestyles and provide a variety of smart coaching and support services.

This paper comprehensively describes the efficient and rational combination and interoperation of these technologies and methods through Mining Minds, while meeting the essential requirements posed by a framework for personalized health and wellness support. Moreover, this work presents a realization of the key architectural components of Mining Minds, as well as various exemplary user applications and expert tools to illustrate some of the potential services supported by the proposed framework.

Mining Minds constitutes an innovative holistic means to inspect human behavior and provide personalized health and wellness support. The principles behind this framework uncover new research ideas and may serve as a reference for similar initiatives.

[end paper 4]

[begin paper 5]

PMCID = 11502405

Title = Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature

This study explores the implementation and evaluation of OwlMentor, an AI-powered learning environment designed to assist university students in comprehending scientific texts. OwlMentor was developed participatorily and then integrated into a course, with development and evaluation taking place over two semesters. It offers features like document-based chats, automatic question generation, and quiz creation.

We used the Technology Acceptance Model to assess system acceptance, examined learning outcomes, and explored the influence of general self-efficacy on system acceptance and OwlMentor use.

The results indicated complex relationships between perceived ease of use, perceived usefulness, and actual use, suggesting the need for more dynamic models of system acceptance. Although no direct correlation between OwlMentor use and learning gains was found, descriptive results indicated higher gains among users compared to non-users. Additionally, general self-efficacy was strongly related to perceived usefulness, intention to use, and actual use of the system.

These findings highlight the importance of aligning AI tools with students’ needs and existing learning strategies to maximize their educational benefits.

[end paper 5]



Here are the top 1 articles on PubMed Central for the query "Dashboard design for LLM interpretability and phenotype definition":

[begin paper 1]

PMCID = 10649223

Title = Deep Learning for Genomics: From Early Neural Nets to Modern Large Language Models

The data explosion driven by advancements in genomic research, such as high-throughput sequencing techniques, is constantly challenging conventional methods used in genomics. In parallel with the urgent demand for robust algorithms, deep learning has succeeded in various fields such as vision, speech, and text processing. Yet genomics entails unique challenges to deep learning, since we expect a superhuman intelligence that explores beyond our knowledge to interpret the genome from deep learning. A powerful deep learning model should rely on the insightful utilization of task-specific knowledge. In this paper, we briefly discuss the strengths of different deep learning models from a genomic perspective so as to fit each particular task with proper deep learning-based architecture, and we remark on practical considerations of developing deep learning architectures for genomics. We also provide a concise review of deep learning applications in various aspects of genomic research and point out current challenges and potential research directions for future genomics applications. We believe the collaborative use of ever-growing diverse data and the fast iteration of deep learning models will continue to contribute to the future of genomics.

[end paper 1]



Here are the top 4 articles on PubMed Central for the query "Dashboard design for LLM interpretability in clinical applications":

[begin paper 1]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 1]

[begin paper 2]

PMCID = 11413421

Title = Prompt engineering on leveraging large language models in generating response to InBasket messages

Large Language Models (LLMs) have been proposed as a solution to address high volumes of Patient Medical Advice Requests (PMARs). This study addresses whether LLMs can generate high quality draft responses to PMARs that satisfies both patients and clinicians with prompt engineering.

We designed a novel human-involved iterative processes to train and validate prompts to LLM in creating appropriate responses to PMARs. GPT-4 was used to generate response to the messages. We updated the prompts, and evaluated both clinician and patient acceptance of LLM-generated draft responses at each iteration, and tested the optimized prompt on independent validation data sets. The optimized prompt was implemented in the electronic health record production environment and tested by 69 primary care clinicians.

After 3 iterations of prompt engineering, physician acceptance of draft suitability increased from 62% to 84% (P <.001) in the validation dataset (N = 200), and 74% of drafts in the test dataset were rated as “helpful.” Patients also noted significantly increased favorability of message tone (78%) and overall quality (80%) for the optimized prompt compared to the original prompt in the training dataset, patients were unable to differentiate human and LLM-generated draft PMAR responses for 76% of the messages, in contrast to the earlier preference for human-generated responses. Majority (72%) of clinicians believed it can reduce cognitive load in dealing with InBasket messages.

Informed by clinician and patient feedback synergistically, tuning in LLM prompt alone can be effective in creating clinically relevant and useful draft responses to PMARs.

[end paper 2]

[begin paper 3]

PMCID = 11511449

Title = AI Applications in Adult Stroke Recovery and Rehabilitation: A Scoping Review Using AI

Stroke is a leading cause of long-term disability worldwide. With the advancements in sensor technologies and data availability, artificial intelligence (AI) holds the promise of improving the amount, quality and efficiency of care and enhancing the precision of stroke rehabilitation. We aimed to identify and characterize the existing research on AI applications in stroke recovery and rehabilitation of adults, including categories of application and progression of technologies over time. Data were collected from peer-reviewed articles across various electronic databases up to January 2024. Insights were extracted using AI-enhanced multi-method, data-driven techniques, including clustering of themes and topics. This scoping review summarizes outcomes from 704 studies. Four common themes (impairment, assisted intervention, prediction and imaging, and neuroscience) were identified, in which time-linked patterns emerged. The impairment theme revealed a focus on motor function, gait and mobility, while the assisted intervention theme included applications of robotic and brain–computer interface (BCI) techniques. AI applications progressed over time, starting from conceptualization and then expanding to a broader range of techniques in supervised learning, artificial neural networks (ANN), natural language processing (NLP) and more. Applications focused on upper limb rehabilitation were reviewed in more detail, with machine learning (ML), deep learning techniques and sensors such as inertial measurement units (IMU) used for upper limb and functional movement analysis. AI applications have potential to facilitate tailored therapeutic delivery, thereby contributing to the optimization of rehabilitation outcomes and promoting sustained recovery from rehabilitation to real-world settings.

[end paper 3]

[begin paper 4]

PMCID = 11638732

Title = Real‐world evidence in the cloud: Tutorial on developing an end‐to‐end data and analytics pipeline using Amazon Web Services resources

In the rapidly evolving landscape of healthcare and drug development, the ability to efficiently collect, process, and analyze large volumes of real‐world data (RWD) is critical for advancing drug development. This article provides a blueprint for establishing an end‐to‐end data and analytics pipeline in a cloud‐based environment. The pipeline presented here includes four major components, including data ingestion, transformation, visualization, and analytics, each supported by a suite of Amazon Web Services (AWS) tools. The pipeline is exemplified through the CURE ID platform, a collaborative tool designed to capture and analyze real‐world, off‐label treatment administrations. By using services such as AWS Lambda, Amazon Relational Database Service (RDS), Amazon QuickSight, and Amazon SageMaker, the pipeline facilitates the ingestion of diverse data sources, the transformation of raw data into structured formats, the creation of interactive dashboards for data visualization, and the application of advanced machine learning models for data analytics. The described architecture not only supports the needs of the CURE ID platform, but also offers a scalable and adaptable framework that can be applied across various domains to enhance data‐driven decision making beyond drug repurposing.

[end paper 4]



Here are the top 2 articles on PubMed Central for the query "Dashboard design for LLM interpretability and clinician trust":

[begin paper 1]

PMCID = 11413421

Title = Prompt engineering on leveraging large language models in generating response to InBasket messages

Large Language Models (LLMs) have been proposed as a solution to address high volumes of Patient Medical Advice Requests (PMARs). This study addresses whether LLMs can generate high quality draft responses to PMARs that satisfies both patients and clinicians with prompt engineering.

We designed a novel human-involved iterative processes to train and validate prompts to LLM in creating appropriate responses to PMARs. GPT-4 was used to generate response to the messages. We updated the prompts, and evaluated both clinician and patient acceptance of LLM-generated draft responses at each iteration, and tested the optimized prompt on independent validation data sets. The optimized prompt was implemented in the electronic health record production environment and tested by 69 primary care clinicians.

After 3 iterations of prompt engineering, physician acceptance of draft suitability increased from 62% to 84% (P <.001) in the validation dataset (N = 200), and 74% of drafts in the test dataset were rated as “helpful.” Patients also noted significantly increased favorability of message tone (78%) and overall quality (80%) for the optimized prompt compared to the original prompt in the training dataset, patients were unable to differentiate human and LLM-generated draft PMAR responses for 76% of the messages, in contrast to the earlier preference for human-generated responses. Majority (72%) of clinicians believed it can reduce cognitive load in dealing with InBasket messages.

Informed by clinician and patient feedback synergistically, tuning in LLM prompt alone can be effective in creating clinically relevant and useful draft responses to PMARs.

[end paper 1]

[begin paper 2]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 2]



Here are the top 5 articles on PubMed Central for the query "LLM interpretability and SNOMED CT integration":

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

PMCID = 11925797

Title = Computational tools and data integration to accelerate vaccine development: challenges, opportunities, and future directions

The development of effective vaccines is crucial for combating current and emerging pathogens. Despite significant advances in the field of vaccine development there remain numerous challenges including the lack of standardized data reporting and curation practices, making it difficult to determine correlates of protection from experimental and clinical studies. Significant gaps in data and knowledge integration can hinder vaccine development which relies on a comprehensive understanding of the interplay between pathogens and the host immune system. In this review, we explore the current landscape of vaccine development, highlighting the computational challenges, limitations, and opportunities associated with integrating diverse data types for leveraging artificial intelligence (AI) and machine learning (ML) techniques in vaccine design. We discuss the role of natural language processing, semantic integration, and causal inference in extracting valuable insights from published literature and unstructured data sources, as well as the computational modeling of immune responses. Furthermore, we highlight specific challenges associated with uncertainty quantification in vaccine development and emphasize the importance of establishing standardized data formats and ontologies to facilitate the integration and analysis of heterogeneous data. Through data harmonization and integration, the development of safe and effective vaccines can be accelerated to improve public health outcomes. Looking to the future, we highlight the need for collaborative efforts among researchers, data scientists, and public health experts to realize the full potential of AI-assisted vaccine design and streamline the vaccine development process.

[end paper 2]

[begin paper 3]

PMCID = 10793431

Title = Fine-tuning Large Language Models for Rare Disease Concept Normalization

We aim to develop a novel method for rare disease concept normalization by fine-tuning Llama 2, an open-source large language model (LLM), using a domain-specific corpus sourced from the Human Phenotype Ontology (HPO).

We developed an in-house template-based script to generate two corpora for fine-tuning. The first (NAME) contains standardized HPO names, sourced from the HPO vocabularies, along with their corresponding identifiers. The second (NAME+SYN) includes HPO names and half of the concept’s synonyms as well as identifiers. Subsequently, we fine-tuned Llama2 (Llama2-7B) for each sentence set and conducted an evaluation using a range of sentence prompts and various phenotype terms.

When the phenotype terms for normalization were included in the fine-tuning corpora, both models demonstrated nearly perfect performance, averaging over 99% accuracy. In comparison, ChatGPT-3.5 has only ~20% accuracy in identifying HPO IDs for phenotype terms. When single-character typos were introduced in the phenotype terms, the accuracy of NAME and NAME+SYN is 10.2% and 36.1%, respectively, but increases to 61.8% (NAME+SYN) with additional typo-specific fine-tuning. For terms sourced from HPO vocabularies as unseen synonyms, the NAME model achieved 11.2% accuracy, while the NAME+SYN model achieved 92.7% accuracy.

Our fine-tuned models demonstrate ability to normalize phenotype terms unseen in the fine-tuning corpus, including misspellings, synonyms, terms from other ontologies, and laymen’s terms. Our approach provides a solution for the use of LLM to identify named medical entities from the clinical narratives, while successfully normalizing them to standard concepts in a controlled vocabulary.

[end paper 3]

[begin paper 4]

PMCID = 10601652

Title = A review of the explainability and safety of conversational agents for mental health to identify avenues for improvement

Virtual Mental Health Assistants (VMHAs) continuously evolve to support the overloaded global healthcare system, which receives approximately 60 million primary care visits and 6 million emergency room visits annually. These systems, developed by clinical psychologists, psychiatrists, and AI researchers, are designed to aid in Cognitive Behavioral Therapy (CBT). The main focus of VMHAs is to provide relevant information to mental health professionals (MHPs) and engage in meaningful conversations to support individuals with mental health conditions. However, certain gaps prevent VMHAs from fully delivering on their promise during active communications. One of the gaps is their inability to explain their decisions to patients and MHPs, making conversations less trustworthy. Additionally, VMHAs can be vulnerable in providing unsafe responses to patient queries, further undermining their reliability. In this review, we assess the current state of VMHAs on the grounds of user-level explainability and safety, a set of desired properties for the broader adoption of VMHAs. This includes the examination of ChatGPT, a conversation agent developed on AI-driven models: GPT3.5 and GPT-4, that has been proposed for use in providing mental health services. By harnessing the collaborative and impactful contributions of AI, natural language processing, and the mental health professionals (MHPs) community, the review identifies opportunities for technological progress in VMHAs to ensure their capabilities include explainable and safe behaviors. It also emphasizes the importance of measures to guarantee that these advancements align with the promise of fostering trustworthy conversations.

[end paper 4]

[begin paper 5]

PMCID = 11891111

Title = NSSC: a neuro-symbolic AI system for enhancing accuracy of named entity recognition and linking from oncologic clinical notes

Accurate recognition and linking of oncologic entities in clinical notes is essential for extracting insights across cancer research, patient care, clinical decision-making, and treatment optimization. We present the Neuro-Symbolic System for Cancer (NSSC), a hybrid AI framework that integrates neurosymbolic methods with named entity recognition (NER) and entity linking (EL) to transform unstructured clinical notes into structured terms using medical vocabularies, with the Unified Medical Language System (UMLS) as a case study. NSSC was evaluated on a dataset of clinical notes from breast cancer patients, demonstrating significant improvements in the accuracy of both entity recognition and linking compared to state-of-the-art models. Specifically, NSSC achieved a 33% improvement over BioFalcon and a 58% improvement over scispaCy. By combining large language models (LLMs) with symbolic reasoning, NSSC improves the recognition and interoperability of oncologic entities, enabling seamless integration with existing biomedical knowledge. This approach marks a significant advancement in extracting meaningful information from clinical narratives, offering promising applications in cancer research and personalized patient care.

[end paper 5]



