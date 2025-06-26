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

Here are the PMCIDs and titles of the papers that are relevant to the topic of Dashboard design for LLM interpretability in healthcare:

```python
{
    "11413421": "Prompt engineering on leveraging large language models in generating response to InBasket messages",
    "11762383": "Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules",
    "11511449": "AI Applications in Adult Stroke Recovery and Rehabilitation: A Scoping Review Using AI",
    "4959395": "The Mining Minds digital health and wellness framework",
    "11502405": "Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature",
    "11638732": "Real-world evidence in the cloud: Tutorial on developing an end-to-end data and analytics pipeline using Amazon Web Services resources",
    "10649223": "Deep Learning for Genomics: From Early Neural Nets to Modern Large Language Models"
}
```

These papers cover various aspects of LLM interpretability, clinical applications, and the integration of AI in healthcare, which are crucial for developing a transparent and clinically grounded interpretability tool.

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



Here are the top 5 articles on PubMed Central for the query "Dashboard design for LLM interpretability in healthcare and LLM interpretability":

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

PMCID = 11502405

Title = Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature

This study explores the implementation and evaluation of OwlMentor, an AI-powered learning environment designed to assist university students in comprehending scientific texts. OwlMentor was developed participatorily and then integrated into a course, with development and evaluation taking place over two semesters. It offers features like document-based chats, automatic question generation, and quiz creation.

We used the Technology Acceptance Model to assess system acceptance, examined learning outcomes, and explored the influence of general self-efficacy on system acceptance and OwlMentor use.

The results indicated complex relationships between perceived ease of use, perceived usefulness, and actual use, suggesting the need for more dynamic models of system acceptance. Although no direct correlation between OwlMentor use and learning gains was found, descriptive results indicated higher gains among users compared to non-users. Additionally, general self-efficacy was strongly related to perceived usefulness, intention to use, and actual use of the system.

These findings highlight the importance of aligning AI tools with students’ needs and existing learning strategies to maximize their educational benefits.

[end paper 4]

[begin paper 5]

PMCID = 11638732

Title = Real‐world evidence in the cloud: Tutorial on developing an end‐to‐end data and analytics pipeline using Amazon Web Services resources

In the rapidly evolving landscape of healthcare and drug development, the ability to efficiently collect, process, and analyze large volumes of real‐world data (RWD) is critical for advancing drug development. This article provides a blueprint for establishing an end‐to‐end data and analytics pipeline in a cloud‐based environment. The pipeline presented here includes four major components, including data ingestion, transformation, visualization, and analytics, each supported by a suite of Amazon Web Services (AWS) tools. The pipeline is exemplified through the CURE ID platform, a collaborative tool designed to capture and analyze real‐world, off‐label treatment administrations. By using services such as AWS Lambda, Amazon Relational Database Service (RDS), Amazon QuickSight, and Amazon SageMaker, the pipeline facilitates the ingestion of diverse data sources, the transformation of raw data into structured formats, the creation of interactive dashboards for data visualization, and the application of advanced machine learning models for data analytics. The described architecture not only supports the needs of the CURE ID platform, but also offers a scalable and adaptable framework that can be applied across various domains to enhance data‐driven decision making beyond drug repurposing.

[end paper 5]



Here are the top 1 articles on PubMed Central for the query "Dashboard design for LLM interpretability in healthcare and phenotype definition":

[begin paper 1]

PMCID = 10649223

Title = Deep Learning for Genomics: From Early Neural Nets to Modern Large Language Models

The data explosion driven by advancements in genomic research, such as high-throughput sequencing techniques, is constantly challenging conventional methods used in genomics. In parallel with the urgent demand for robust algorithms, deep learning has succeeded in various fields such as vision, speech, and text processing. Yet genomics entails unique challenges to deep learning, since we expect a superhuman intelligence that explores beyond our knowledge to interpret the genome from deep learning. A powerful deep learning model should rely on the insightful utilization of task-specific knowledge. In this paper, we briefly discuss the strengths of different deep learning models from a genomic perspective so as to fit each particular task with proper deep learning-based architecture, and we remark on practical considerations of developing deep learning architectures for genomics. We also provide a concise review of deep learning applications in various aspects of genomic research and point out current challenges and potential research directions for future genomics applications. We believe the collaborative use of ever-growing diverse data and the fast iteration of deep learning models will continue to contribute to the future of genomics.

[end paper 1]



Here are the top 4 articles on PubMed Central for the query "Dashboard design for LLM interpretability in healthcare and clinical applications":

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

PMCID = 4959395

Title = The Mining Minds digital health and wellness framework

The provision of health and wellness care is undergoing an enormous transformation. A key element of this revolution consists in prioritizing prevention and proactivity based on the analysis of people’s conducts and the empowerment of individuals in their self-management. Digital technologies are unquestionably destined to be the main engine of this change, with an increasing number of domain-specific applications and devices commercialized every year; however, there is an apparent lack of frameworks capable of orchestrating and intelligently leveraging, all the data, information and knowledge generated through these systems.

This work presents Mining Minds, a novel framework that builds on the core ideas of the digital health and wellness paradigms to enable the provision of personalized support. Mining Minds embraces some of the most prominent digital technologies, ranging from Big Data and Cloud Computing to Wearables and Internet of Things, as well as modern concepts and methods, such as context-awareness, knowledge bases or analytics, to holistically and continuously investigate on people’s lifestyles and provide a variety of smart coaching and support services.

This paper comprehensively describes the efficient and rational combination and interoperation of these technologies and methods through Mining Minds, while meeting the essential requirements posed by a framework for personalized health and wellness support. Moreover, this work presents a realization of the key architectural components of Mining Minds, as well as various exemplary user applications and expert tools to illustrate some of the potential services supported by the proposed framework.

Mining Minds constitutes an innovative holistic means to inspect human behavior and provide personalized health and wellness support. The principles behind this framework uncover new research ideas and may serve as a reference for similar initiatives.

[end paper 4]



Here are the top 2 articles on PubMed Central for the query "Dashboard design for LLM interpretability in healthcare and clinician trust":

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



