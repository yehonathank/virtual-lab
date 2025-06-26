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

To address the agenda, I'll start by crafting a series of search queries to find relevant scientific papers on the topic of Dashboard design for LLM interpretability in healthcare. These queries will cover both general aspects and specific connections to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
search_queries = [
    "Dashboard design for LLM interpretability in healthcare",
    "LLM interpretability and electronic phenotype definition",
    "Dashboard design for clinical applications of LLMs",
    "Visual tools for clinician trust in AI healthcare models",
    "Integrating SNOMED CT in LLM interpretability dashboards"
]
```

Next, I will execute these queries to find relevant scientific papers.

## Data Visualization Expert

Here are the PMCIDs and titles of the papers I found relevant to the topic of Dashboard design for LLM interpretability in healthcare:

```python
papers = {
    "11413421": "Prompt engineering on leveraging large language models in generating response to InBasket messages",
    "11762383": "Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules",
    "11511449": "AI Applications in Adult Stroke Recovery and Rehabilitation: A Scoping Review Using AI",
    "4959395": "The Mining Minds digital health and wellness framework",
    "11502405": "Exploring generative AI in higher education: a RAG system to enhance student engagement with scientific literature",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "11480249": "Confronting the data deluge: How artificial intelligence can be used in the study of plant stress",
    "11639975": "EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy",
    "11545079": "The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning",
    "10689487": "Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models",
    "11285660": "Introduction to Large Language Models (LLMs) for dementia care and research",
    "11666565": "The RepVig framework for designing use-case specific representative vignettes and evaluating triage accuracy of laypeople and symptom assessment applications",
    "11701538": "PanKB: An interactive microbial pangenome knowledgebase for research, biotechnological innovation, and knowledge mining",
    "11953325": "A scoping review on generative AI and large language models in mitigating medication related harm",
    "11840377": "AI for IMPACTS Framework for Evaluating the Long-Term Real-World Impacts of AI-Powered Clinician Tools: Systematic Review and Narrative Synthesis",
    "11309043": "Clinical Evaluation of Artificial Intelligence-Enabled Interventions",
    "10941464": "Generative AI in healthcare: an implementation science informed translational path on application, integration and governance",
    "11668905": "Tackling algorithmic bias and promoting transparency in health datasets: the STANDING Together consensus recommendations"
}
```

These papers cover various aspects of LLM interpretability, clinical applications, and the integration of AI in healthcare, which are relevant to your research project.

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



Here are the top 5 articles on PubMed Central for the query "LLM interpretability and electronic phenotype definition":

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



Here are the top 5 articles on PubMed Central for the query "Dashboard design for clinical applications of LLMs":

[begin paper 1]

PMCID = 11285660

Title = Introduction to Large Language Models (LLMs) for dementia care and research

Dementia is a progressive neurodegenerative disorder that affects cognitive abilities including memory, reasoning, and communication skills, leading to gradual decline in daily activities and social engagement. In light of the recent advent of Large Language Models (LLMs) such as ChatGPT, this paper aims to thoroughly analyse their potential applications and usefulness in dementia care and research.

To this end, we offer an introduction into LLMs, outlining the key features, capabilities, limitations, potential risks, and practical considerations for deployment as easy-to-use software (e.g., smartphone apps). We then explore various domains related to dementia, identifying opportunities for LLMs to enhance understanding, diagnostics, and treatment, with a broader emphasis on improving patient care. For each domain, the specific contributions of LLMs are examined, such as their ability to engage users in meaningful conversations, deliver personalized support, and offer cognitive enrichment. Potential benefits encompass improved social interaction, enhanced cognitive functioning, increased emotional well-being, and reduced caregiver burden. The deployment of LLMs in caregiving frameworks also raises a number of concerns and considerations. These include privacy and safety concerns, the need for empirical validation, user-centered design, adaptation to the user's unique needs, and the integration of multimodal inputs to create more immersive and personalized experiences. Additionally, ethical guidelines and privacy protocols must be established to ensure responsible and ethical deployment of LLMs.

We report the results on a questionnaire filled in by people with dementia (PwD) and their supporters wherein we surveyed the usefulness of different application scenarios of LLMs as well as the features that LLM-powered apps should have. Both PwD and supporters were largely positive regarding the prospect of LLMs in care, although concerns were raised regarding bias, data privacy and transparency.

Overall, this review corroborates the promising utilization of LLMs to positively impact dementia care by boosting cognitive abilities, enriching social interaction, and supporting caregivers. The findings underscore the importance of further research and development in this field to fully harness the benefits of LLMs and maximize their potential for improving the lives of individuals living with dementia.

[end paper 1]

[begin paper 2]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 2]

[begin paper 3]

PMCID = 11666565

Title = The RepVig framework for designing use-case specific representative vignettes and evaluating triage accuracy of laypeople and symptom assessment applications

Most studies evaluating symptom-assessment applications (SAAs) rely on a common set of case vignettes that are authored by clinicians and devoid of context, which may be representative of clinical settings but not of situations where patients use SAAs. Assuming the use case of self-triage, we used representative design principles to sample case vignettes from online platforms where patients describe their symptoms to obtain professional advice and compared triage performance of laypeople, SAAs (e.g., WebMD or NHS 111), and Large Language Models (LLMs, e.g., GPT-4 or Claude) on representative versus standard vignettes. We found performance differences in all three groups depending on vignette type: When using representative vignettes, accuracy was higher (OR = 1.52 to 2.00, p < .001 to .03 in binary decisions, i.e., correct or incorrect), safety was higher (OR = 1.81 to 3.41, p < .001 to .002 in binary decisions, i.e., safe or unsafe), and the inclination to overtriage was also higher (OR = 1.80 to 2.66, p < .001 to p = .035 in binary decisions, overtriage or undertriage error). Additionally, we found changed rankings of best-performing SAAs and LLMs. Based on these results, we argue that our representative vignette sampling approach (that we call the RepVig Framework) should replace the practice of using a fixed vignette set as standard for SAA evaluation studies.

[end paper 3]

[begin paper 4]

PMCID = 11701538

Title = PanKB: An interactive microbial pangenome knowledgebase for research, biotechnological innovation, and knowledge mining

The exponential growth of microbial genome data presents unprecedented opportunities for unlocking the potential of microorganisms. The burgeoning field of pangenomics offers a framework for extracting insights from this big biological data. Recent advances in microbial pangenomic research have generated substantial data and literature, yielding valuable knowledge across diverse microbial species. PanKB (pankb.org), a knowledgebase designed for microbial pangenomics research and biotechnological applications, was built to capitalize on this wealth of information. PanKB currently includes 51 pangenomes from 8 industrially relevant microbial families, comprising 8402 genomes, over 500 000 genes and over 7M mutations. To describe this data, PanKB implements four main components: (1) Interactive pangenomic analytics to facilitate exploration, intuition, and potential discoveries; (2) Alleleomic analytics, a pangenomic-scale analysis of variants, providing insights into intra-species sequence variation and potential mutations for applications; (3) A global search function enabling broad and deep investigations across pangenomes to power research and bioengineering workflows; (4) A bibliome of 833 open-access pangenomic papers and an interface with an LLM that can answer in-depth questions using its knowledge. PanKB empowers researchers and bioengineers to harness the potential of microbial pangenomics and serves as a valuable resource bridging the gap between pangenomic data and practical applications.

[end paper 4]

[begin paper 5]

PMCID = 11953325

Title = A scoping review on generative AI and large language models in mitigating medication related harm

Medication-related harm has a significant impact on global healthcare costs and patient outcomes. Generative artificial intelligence (GenAI) and large language models (LLM) have emerged as a promising tool in mitigating risks of medication-related harm. This review evaluates the scope and effectiveness of GenAI and LLM in reducing medication-related harm. We screened 4 databases for literature published from 1st January 2012 to 15th October 2024. A total of 3988 articles were identified, and 30 met the criteria for inclusion into the final review. Generative AI and LLMs were applied in three key applications: drug-drug interaction identification and prediction, clinical decision support, and pharmacovigilance. While the performance and utility of these models varied, they generally showed promise in early identification, classification of adverse drug events, and supporting decision-making for medication management. However, no studies tested these models prospectively, suggesting a need for further investigation into integration and real-world application.

[end paper 5]



Here are the top 4 articles on PubMed Central for the query "Visual tools for clinician trust in AI healthcare models":

[begin paper 1]

PMCID = 11840377

Title = AI for IMPACTS Framework for Evaluating the Long-Term Real-World Impacts of AI-Powered Clinician Tools: Systematic Review and Narrative Synthesis

Artificial intelligence (AI) has the potential to revolutionize health care by enhancing both clinical outcomes and operational efficiency. However, its clinical adoption has been slower than anticipated, largely due to the absence of comprehensive evaluation frameworks. Existing frameworks remain insufficient and tend to emphasize technical metrics such as accuracy and validation, while overlooking critical real-world factors such as clinical impact, integration, and economic sustainability. This narrow focus prevents AI tools from being effectively implemented, limiting their broader impact and long-term viability in clinical practice.

This study aimed to create a framework for assessing AI in health care, extending beyond technical metrics to incorporate social and organizational dimensions. The framework was developed by systematically reviewing, analyzing, and synthesizing the evaluation criteria necessary for successful implementation, focusing on the long-term real-world impact of AI in clinical practice.

A search was performed in July 2024 across the PubMed, Cochrane, Scopus, and IEEE Xplore databases to identify relevant studies published in English between January 2019 and mid-July 2024, yielding 3528 results, among which 44 studies met the inclusion criteria. The systematic review followed PRISMA (Preferred Reporting Items for Systematic reviews and Meta-Analyses) guidelines and the Cochrane Handbook for Systematic Reviews. Data were analyzed using NVivo through thematic analysis and narrative synthesis to identify key emergent themes in the studies.

By synthesizing the included studies, we developed a framework that goes beyond the traditional focus on technical metrics or study-level methodologies. It integrates clinical context and real-world implementation factors, offering a more comprehensive approach to evaluating AI tools. With our focus on assessing the long-term real-world impact of AI technologies in health care, we named the framework AI for IMPACTS. The criteria are organized into seven key clusters, each corresponding to a letter in the acronym: (1) I—integration, interoperability, and workflow; (2) M—monitoring, governance, and accountability; (3) P—performance and quality metrics; (4) A—acceptability, trust, and training; (5) C—cost and economic evaluation; (6) T—technological safety and transparency; and (7) S—scalability and impact. These are further broken down into 28 specific subcriteria.

The AI for IMPACTS framework offers a holistic approach to evaluate the long-term real-world impact of AI tools in the heterogeneous and challenging health care context and lays the groundwork for further validation through expert consensus and testing of the framework in real-world health care settings. It is important to emphasize that multidisciplinary expertise is essential for assessment, yet many assessors lack the necessary training. In addition, traditional evaluation methods struggle to keep pace with AI’s rapid development. To ensure successful AI integration, flexible, fast-tracked assessment processes and proper assessor training are needed to maintain rigorous standards while adapting to AI’s dynamic evolution.

reviewregistry1859; https://tinyurl.com/ysn2d7sh

[end paper 1]

[begin paper 2]

PMCID = 11309043

Title = Clinical Evaluation of Artificial Intelligence-Enabled Interventions

Artificial intelligence (AI) health technologies are increasingly available for use in real-world care. This emerging opportunity is accompanied by a need for decision makers and practitioners across healthcare systems to evaluate the safety and effectiveness of these interventions against the needs of their own setting. To meet this need, high-quality evidence regarding AI-enabled interventions must be made available, and decision makers in varying roles and settings must be empowered to evaluate that evidence within the context in which they work. This article summarizes good practices across four stages of evidence generation for AI health technologies: study design, study conduct, study reporting, and study appraisal.

[end paper 2]

[begin paper 3]

PMCID = 10941464

Title = Generative AI in healthcare: an implementation science informed translational path on application, integration and governance

Artificial intelligence (AI), particularly generative AI, has emerged as a transformative tool in healthcare, with the potential to revolutionize clinical decision-making and improve health outcomes. Generative AI, capable of generating new data such as text and images, holds promise in enhancing patient care, revolutionizing disease diagnosis and expanding treatment options. However, the utility and impact of generative AI in healthcare remain poorly understood, with concerns around ethical and medico-legal implications, integration into healthcare service delivery and workforce utilisation. Also, there is not a clear pathway to implement and integrate generative AI in healthcare delivery.

This article aims to provide a comprehensive overview of the use of generative AI in healthcare, focusing on the utility of the technology in healthcare and its translational application highlighting the need for careful planning, execution and management of expectations in adopting generative AI in clinical medicine. Key considerations include factors such as data privacy, security and the irreplaceable role of clinicians’ expertise. Frameworks like the technology acceptance model (TAM) and the Non-Adoption, Abandonment, Scale-up, Spread and Sustainability (NASSS) model are considered to promote responsible integration. These frameworks allow anticipating and proactively addressing barriers to adoption, facilitating stakeholder participation and responsibly transitioning care systems to harness generative AI’s potential.

Generative AI has the potential to transform healthcare through automated systems, enhanced clinical decision-making and democratization of expertise with diagnostic support tools providing timely, personalized suggestions. Generative AI applications across billing, diagnosis, treatment and research can also make healthcare delivery more efficient, equitable and effective. However, integration of generative AI necessitates meticulous change management and risk mitigation strategies. Technological capabilities alone cannot shift complex care ecosystems overnight; rather, structured adoption programs grounded in implementation science are imperative.

It is strongly argued in this article that generative AI can usher in tremendous healthcare progress, if introduced responsibly. Strategic adoption based on implementation science, incremental deployment and balanced messaging around opportunities versus limitations helps promote safe, ethical generative AI integration. Extensive real-world piloting and iteration aligned to clinical priorities should drive development. With conscientious governance centred on human wellbeing over technological novelty, generative AI can enhance accessibility, affordability and quality of care. As these models continue advancing rapidly, ongoing reassessment and transparent communication around their strengths and weaknesses remain vital to restoring trust, realizing positive potential and, most importantly, improving patient outcomes.

[end paper 3]

[begin paper 4]

PMCID = 11668905

Title = Tackling algorithmic bias and promoting transparency in health datasets: the STANDING Together consensus recommendations

Without careful dissection of the ways in which biases can be encoded into artificial intelligence (AI) health technologies, there is a risk of perpetuating existing health inequalities at scale. One major source of bias is the data that underpins such technologies. The STANDING Together recommendations aim to encourage transparency regarding limitations of health datasets and proactive evaluation of their effect across population groups. Draft recommendation items were informed by a systematic review and stakeholder survey. The recommendations were developed using a Delphi approach, supplemented by a public consultation and international interview study. Overall, more than 350 representatives from 58 countries provided input into this initiative. 194 Delphi participants from 25 countries voted and provided comments on 32 candidate items across three electronic survey rounds and one in-person consensus meeting. The 29 STANDING Together consensus recommendations are presented here in two parts. Recommendations for Documentation of Health Datasets provide guidance for dataset curators to enable transparency around data composition and limitations. Recommendations for Use of Health Datasets aim to enable identification and mitigation of algorithmic biases that might exacerbate health inequalities. These recommendations are intended to prompt proactive inquiry rather than acting as a checklist. We hope to raise awareness that no dataset is free of limitations, so transparent communication of data limitations should be perceived as valuable, and absence of this information as a limitation. We hope that adoption of the STANDING Together recommendations by stakeholders across the AI health technology lifecycle will enable everyone in society to benefit from technologies which are safe and effective.

[end paper 4]



No articles found on PubMed Central for the query "Integrating SNOMED CT in LLM interpretability dashboards".

