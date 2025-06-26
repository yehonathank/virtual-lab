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

To address the agenda, I'll first outline a series of search queries to find relevant scientific papers on Dashboard design for LLM interpretability in healthcare. These queries will cover general aspects as well as specific connections to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

### Search Queries

```python
search_queries = [
    "Dashboard design for LLM interpretability in healthcare",
    "LLM interpretability and dashboard design in electronic phenotype definition",
    "Clinical applications of LLM interpretability dashboards",
    "Building clinician trust through dashboard design for LLMs",
    "Integrating SNOMED CT in LLM interpretability dashboards for healthcare"
]
```

### Next Steps

I will use these queries to search for relevant scientific papers. Once I have the results, I will provide a list of PMCIDs and titles of the papers that are most relevant to fine-tuning my understanding of the topic.

Let's proceed with searching for these articles.

## Data Visualization Expert

Based on the search queries, here are the PMCIDs and titles of the papers that are relevant to fine-tuning my understanding of dashboard design for LLM interpretability in healthcare:

```python
papers = {
    "11413421": "Prompt engineering on leveraging large language models in generating response to InBasket messages",
    "11762383": "Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules",
    "11605263": "Economics and Equity of Large Language Models: Health Care Perspective",
    "11638732": "Real-world evidence in the cloud: Tutorial on developing an end-to-end data and analytics pipeline using Amazon Web Services resources",
    "11542778": "Bias in medical AI: Implications for clinical decision-making",
    "11650087": "Digital Information Ecosystems in Modern Care Coordination and Patient Care Pathways and the Challenges and Opportunities for AI Solutions"
}
```

These papers cover various aspects of LLM interpretability, clinical applications, and the integration of AI in healthcare, which are crucial for developing a transparent, clinically grounded, and visually intuitive interpretability tool.

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



No articles found on PubMed Central for the query "LLM interpretability and dashboard design in electronic phenotype definition".

Here are the top 5 articles on PubMed Central for the query "Clinical applications of LLM interpretability dashboards":

[begin paper 1]

PMCID = 11605263

Title = Economics and Equity of Large Language Models: Health Care Perspective

Large language models (LLMs) continue to exhibit noteworthy capabilities across a spectrum of areas, including emerging proficiencies across the health care continuum. Successful LLM implementation and adoption depend on digital readiness, modern infrastructure, a trained workforce, privacy, and an ethical regulatory landscape. These factors can vary significantly across health care ecosystems, dictating the choice of a particular LLM implementation pathway. This perspective discusses 3 LLM implementation pathways—training from scratch pathway (TSP), fine-tuned pathway (FTP), and out-of-the-box pathway (OBP)—as potential onboarding points for health systems while facilitating equitable adoption. The choice of a particular pathway is governed by needs as well as affordability. Therefore, the risks, benefits, and economics of these pathways across 4 major cloud service providers (Amazon, Microsoft, Google, and Oracle) are presented. While cost comparisons, such as on-demand and spot pricing across the cloud service providers for the 3 pathways, are presented for completeness, the usefulness of managed services and cloud enterprise tools is elucidated. Managed services can complement the traditional workforce and expertise, while enterprise tools, such as federated learning, can overcome sample size challenges when implementing LLMs using health care data. Of the 3 pathways, TSP is expected to be the most resource-intensive regarding infrastructure and workforce while providing maximum customization, enhanced transparency, and performance. Because TSP trains the LLM using enterprise health care data, it is expected to harness the digital signatures of the population served by the health care system with the potential to impact outcomes. The use of pretrained models in FTP is a limitation. It may impact its performance because the training data used in the pretrained model may have hidden bias and may not necessarily be health care–related. However, FTP provides a balance between customization, cost, and performance. While OBP can be rapidly deployed, it provides minimal customization and transparency without guaranteeing long-term availability. OBP may also present challenges in interfacing seamlessly with downstream applications in health care settings with variations in pricing and use over time. Lack of customization in OBP can significantly limit its ability to impact outcomes. Finally, potential applications of LLMs in health care, including conversational artificial intelligence, chatbots, summarization, and machine translation, are highlighted. While the 3 implementation pathways discussed in this perspective have the potential to facilitate equitable adoption and democratization of LLMs, transitions between them may be necessary as the needs of health systems evolve. Understanding the economics and trade-offs of these onboarding pathways can guide their strategic adoption and demonstrate value while impacting health care outcomes favorably.

[end paper 1]

[begin paper 2]

PMCID = 11638732

Title = Real‐world evidence in the cloud: Tutorial on developing an end‐to‐end data and analytics pipeline using Amazon Web Services resources

In the rapidly evolving landscape of healthcare and drug development, the ability to efficiently collect, process, and analyze large volumes of real‐world data (RWD) is critical for advancing drug development. This article provides a blueprint for establishing an end‐to‐end data and analytics pipeline in a cloud‐based environment. The pipeline presented here includes four major components, including data ingestion, transformation, visualization, and analytics, each supported by a suite of Amazon Web Services (AWS) tools. The pipeline is exemplified through the CURE ID platform, a collaborative tool designed to capture and analyze real‐world, off‐label treatment administrations. By using services such as AWS Lambda, Amazon Relational Database Service (RDS), Amazon QuickSight, and Amazon SageMaker, the pipeline facilitates the ingestion of diverse data sources, the transformation of raw data into structured formats, the creation of interactive dashboards for data visualization, and the application of advanced machine learning models for data analytics. The described architecture not only supports the needs of the CURE ID platform, but also offers a scalable and adaptable framework that can be applied across various domains to enhance data‐driven decision making beyond drug repurposing.

[end paper 2]

[begin paper 3]

PMCID = 11542778

Title = Bias in medical AI: Implications for clinical decision-making

Biases in medical artificial intelligence (AI) arise and compound throughout the AI lifecycle. These biases can have significant clinical consequences, especially in applications that involve clinical decision-making. Left unaddressed, biased medical AI can lead to substandard clinical decisions and the perpetuation and exacerbation of longstanding healthcare disparities. We discuss potential biases that can arise at different stages in the AI development pipeline and how they can affect AI algorithms and clinical decision-making. Bias can occur in data features and labels, model development and evaluation, deployment, and publication. Insufficient sample sizes for certain patient groups can result in suboptimal performance, algorithm underestimation, and clinically unmeaningful predictions. Missing patient findings can also produce biased model behavior, including capturable but nonrandomly missing data, such as diagnosis codes, and data that is not usually or not easily captured, such as social determinants of health. Expertly annotated labels used to train supervised learning models may reflect implicit cognitive biases or substandard care practices. Overreliance on performance metrics during model development may obscure bias and diminish a model’s clinical utility. When applied to data outside the training cohort, model performance can deteriorate from previous validation and can do so differentially across subgroups. How end users interact with deployed solutions can introduce bias. Finally, where models are developed and published, and by whom, impacts the trajectories and priorities of future medical AI development. Solutions to mitigate bias must be implemented with care, which include the collection of large and diverse data sets, statistical debiasing methods, thorough model evaluation, emphasis on model interpretability, and standardized bias reporting and transparency requirements. Prior to real-world implementation in clinical settings, rigorous validation through clinical trials is critical to demonstrate unbiased application. Addressing biases across model development stages is crucial for ensuring all patients benefit equitably from the future of medical AI.

In this work, we explore the challenges of biases that emerge in medical artificial intelligence (AI). These biases, if not adequately addressed, can lead to poor clinical decisions and worsen existing healthcare inequalities by influencing an AI’s decisions in ways that disadvantage some patient groups over others. We discuss several stages in the process of developing a medical AI model where bias can emerge, including collecting data, training a model, and real-world application. For instance, the way data is collected can exclude or misrepresent certain patient populations, leading to less effective and inequitable AI systems. We provide examples, both hypothetical and real, to illustrate how these biases can alter clinical outcomes. These examples show that biases are not just possible; they are a significant risk if not actively countered. Our review stresses the importance of diverse and comprehensive data sets, sophisticated statistical methods to remove biases, and clear reporting standards—key components of a future where medical AI works equitably and supports high-quality clinical care for everyone.

[end paper 3]

[begin paper 4]

PMCID = 11966900

Title = The generative revolution: AI foundation models in geospatial health—applications, challenges and future research

In an era of rapid technological advancements, generative artificial intelligence and foundation models are reshaping industries and offering new advanced solutions in a wide range of scientific areas, particularly in public and environmental health. However, foundation models have previously mostly focused on understanding and generating text, while geospatial features, interrelations, flows and correlations have been neglected. Thus, this paper outlines the importance of research into Geospatial Foundation Models, which have the potential to revolutionise digital health surveillance and public health. We examine the latest advances, opportunities, challenges, and ethical considerations of geospatial foundation models for research and applications in digital health. We focus on the specific challenges of integrating geospatial context with foundation models and lay out the future potential for multimodal geospatial foundation models for a variety of research avenues in digital health surveillance and health assessment.

[end paper 4]

[begin paper 5]

PMCID = 11763430

Title = Artificial Intelligence in Pediatric Electrocardiography: A Comprehensive Review

Artificial intelligence (AI) is revolutionizing healthcare by offering innovative solutions for diagnosis, treatment, and patient management. Only recently has the field of pediatric cardiology begun to explore the use of deep learning methods to analyze electrocardiogram (ECG) data, aiming to enhance diagnostic accuracy, expedite workflows, and improve patient outcomes. This review examines the current state of AI-enhanced ECG interpretation in pediatric cardiology applications, drawing insights from adult AI-ECG research given the progress in this field. It describes a broad range of AI methodologies, investigates the unique challenges inherent in pediatric ECG analysis, reviews the current state of the literature in pediatric AI-ECG, and discusses potential future directions for research and clinical practice. While AI-ECG applications have demonstrated considerable promise, widespread clinical adoption necessitates further research, rigorous validation, and careful consideration of equity, ethical, legal, and practical challenges.

[end paper 5]



Here are the top 4 articles on PubMed Central for the query "Building clinician trust through dashboard design for LLMs":

[begin paper 1]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 1]

[begin paper 2]

PMCID = 11650087

Title = Digital Information Ecosystems in Modern Care Coordination and Patient Care Pathways and the Challenges and Opportunities for AI Solutions

The integration of digital technologies into health care has significantly enhanced the efficiency and effectiveness of care coordination. Our perspective paper explores the digital information ecosystems in modern care coordination, focusing on the processes of information generation, updating, transmission, and exchange along a patient’s care pathway. We identify several challenges within this ecosystem, including interoperability issues, information silos, hard-to-map patient care journeys, increased workload on health care professionals, coordination and communication gaps, and compliance with privacy regulations. These challenges are often associated with inefficiencies and diminished care quality. We also examine how emerging artificial intelligence (AI) tools have the potential to enhance the management of patient information flow. Specifically, AI can boost interoperability across diverse health systems; optimize and monitor patient care pathways; improve information retrieval and care transitions; humanize health care by integrating patients’ desired outcomes and patient-reported outcome measures; and optimize clinical workflows, resource allocation, and digital tool usability and user experiences. By strategically leveraging AI, health care systems can establish a more robust and responsive digital information ecosystem, improving care coordination and patient outcomes. This perspective underscores the importance of continued research and investment in AI technologies in patient care pathways. We advocate for a thoughtful integration of AI into health care practices to fully realize its potential in revolutionizing care coordination.

[end paper 2]

[begin paper 3]

PMCID = 11257057

Title = 2023 MCBK global meeting—Lightning talk abstracts



[end paper 3]

[begin paper 4]

PMCID = 11536614

Title = Big data in breast cancer: Towards precision treatment

Breast cancer is the most prevalent and deadliest cancer among women globally, representing a major threat to public health. In response, the World Health Organization has established the Global Breast Cancer Initiative framework to reduce breast cancer mortality through global collaboration. The integration of big data analytics (BDA) and precision medicine has transformed our understanding of breast cancer's biological traits and treatment responses. By harnessing large-scale datasets – encompassing genetic, clinical, and environmental data – BDA has enhanced strategies for breast cancer prevention, diagnosis, and treatment, driving the advancement of precision oncology and personalised care. Despite the increasing importance of big data in breast cancer research, comprehensive studies remain sparse, underscoring the need for more systematic investigation. This review evaluates the contributions of big data to breast cancer precision medicine while addressing the associated opportunities and challenges. Through the application of big data, we aim to deepen insights into breast cancer pathogenesis, optimise therapeutic approaches, improve patient outcomes, and ultimately contribute to better survival rates and quality of life. This review seeks to provide a foundation for future research in breast cancer prevention, treatment, and management.

[end paper 4]



No articles found on PubMed Central for the query "Integrating SNOMED CT in LLM interpretability dashboards for healthcare".

