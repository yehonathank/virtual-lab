## User

This is the beginning of an individual meeting with Computational Linguist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Few-shot learning and domain adaptation in clinical NLP in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Few-shot learning and domain adaptation in clinical NLP to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Few-shot learning and domain adaptation in clinical NLP. Include both general queries about Few-shot learning and domain adaptation in clinical NLP and queries that specifically relate Few-shot learning and domain adaptation in clinical NLP to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Computational Linguist, please provide your response to the agenda.

## Computational Linguist

To address the agenda, I'll first create a series of search queries to find relevant scientific papers on Few-shot learning and domain adaptation in clinical NLP. These queries will cover both general topics and specific aspects related to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
search_queries = [
    "Few-shot learning in clinical NLP",
    "Domain adaptation in clinical NLP",
    "Few-shot learning and LLM interpretability in clinical phenotype definition",
    "Domain adaptation and clinical applications of LLMs",
    "Clinician trust in LLM-based clinical NLP tools"
]
```

Next, I'll use these queries to search for relevant scientific papers. Let's proceed with retrieving the PMCIDs and titles of the papers.

## Computational Linguist

Based on the search queries, here are the PMCIDs and titles of the papers that are relevant to the topic of Few-shot learning and domain adaptation in clinical NLP, specifically in the context of LLM interpretability, phenotype definition, clinical applications, and clinician trust:

```python
papers = {
    "11483110": "Learning to explain is a good biomedical few-shot learner",
    "11889813": "NLP modeling recommendations for restricted data availability in clinical settings",
    "7856273": "Discriminative ensemble learning for few-shot chest x-ray diagnosis",
    "11036183": "An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study",
    "11041484": "Few-Shot Learning for Clinical Natural Language Processing Using Siamese Neural Networks: Algorithm Development and Validation Study",
    "9144795": "Stemphylium lycopersici Nep1-like Protein (NLP) Is a Key Virulence Factor in Tomato Gray Leaf Spot Disease",
    "9281254": "Natural language processing: state of the art, current trends and challenges",
    "11839006": "Development and Validation of Natural Language Processing Algorithms in the ENACT National Electronic Health Record Research Network",
    "11923465": "Natural Language Processing Technologies for Public Health in Africa: Scoping Review",
    "11642228": "Revolutionizing Radiology with Natural Language Processing and Chatbot Technologies: A Narrative Umbrella Review on Current Trends and Future Directions",
    "11460004": "A hybrid framework with large language models for rare disease phenotyping",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "10967767": "A Comprehensive Review on Synergy of Multi-Modal Data and AI Technologies in Medical Diagnosis",
    "11639975": "EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy",
    "11076269": "A mini-review on perturbation modelling across single-cell omic modalities",
    "11285660": "Introduction to Large Language Models (LLMs) for dementia care and research",
    "11456558": "Large language model to multimodal large language model: A journey to shape the biological macromolecules to biological sciences and medicine",
    "11739813": "A review of large language models and autonomous agents in chemistry",
    "11464944": "Multimodal Large Language Models in Health Care: Applications, Challenges, and Future Outlook",
    "11701858": "Integration of large language models and federated learning",
    "10871446": "Realizing the Potential of Social Determinants Data: A Scoping Review of Approaches for Screening, Linkage, Extraction, Analysis and Interventions",
    "10834163": "Artificial intelligence: revolutionizing cardiology with large language models",
    "10883116": "Large language models: a primer and gastroenterology applications",
    "10829781": "Artificial intelligence, ChatGPT, and other large language models for social determinants of health: Current state and future directions"
}
```

These papers cover various aspects of Few-shot learning, domain adaptation, and the application of LLMs in clinical settings, providing a comprehensive foundation for understanding the current state of research in this area.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Few-shot learning in clinical NLP":

[begin paper 1]

PMCID = 11483110

Title = Learning to explain is a good biomedical few-shot learner

Significant progress has been achieved in biomedical text mining using deep learning methods, which rely heavily on large amounts of high-quality data annotated by human experts. However, the reality is that obtaining high-quality annotated data is extremely challenging due to data scarcity (e.g. rare or new diseases), data privacy and security concerns, and the high cost of data annotation. Additionally, nearly all researches focus on predicting labels without providing corresponding explanations. Therefore, in this paper, we investigate a more realistic scenario, biomedical few-shot learning, and explore the impact of interpretability on biomedical few-shot learning.

We present LetEx—Learning to explain—a novel multi-task generative approach that leverages reasoning explanations from large language models (LLMs) to enhance the inductive reasoning ability of few-shot learning. Our approach includes (1) collecting high-quality explanations by devising a suite of complete workflow based on LLMs through CoT prompting and self-training strategies, (2) converting various biomedical NLP tasks into a text-to-text generation task in a unified manner, where collected explanations serve as additional supervision between text-label pairs by multi-task training. Experiments are conducted on three few-shot settings across six biomedical benchmark datasets. The results show that learning to explain improves the performances of diverse biomedical NLP tasks in low-resource scenario, outperforming strong baseline models significantly by up to 6.41%. Notably, the proposed method makes the 220M LetEx perform superior reasoning explanation ability against LLMs.

Our source code and data are available at https://github.com/cpmss521/LetEx.

[end paper 1]

[begin paper 2]

PMCID = 11889813

Title = NLP modeling recommendations for restricted data availability in clinical settings

Clinical decision-making in healthcare often relies on unstructured text data, which can be challenging to analyze using traditional methods. Natural Language Processing (NLP) has emerged as a promising solution, but its application in clinical settings is hindered by restricted data availability and the need for domain-specific knowledge.

We conducted an experimental analysis to evaluate the performance of various NLP modeling paradigms on multiple clinical NLP tasks in Spanish. These tasks included referral prioritization and referral specialty classification. We simulated three clinical settings with varying levels of data availability and evaluated the performance of four foundation models.

Clinical-specific pre-trained language models (PLMs) achieved the highest performance across tasks. For referral prioritization, Clinical PLMs attained an 88.85 % macro F1 score when fine-tuned. In referral specialty classification, the same models achieved a 53.79 % macro F1 score, surpassing domain-agnostic models. Continuing pre-training with environment-specific data improved model performance, but the gains were marginal compared to the computational resources required. Few-shot learning with large language models (LLMs) demonstrated lower performance but showed potential in data-scarce scenarios.

Our study provides evidence-based recommendations for clinical NLP practitioners on selecting modeling paradigms based on data availability. We highlight the importance of considering data availability, task complexity, and institutional maturity when designing and training clinical NLP models. Our findings can inform the development of effective clinical NLP solutions in real-world settings.

The online version contains supplementary material available at 10.1186/s12911-025-02948-2.

[end paper 2]

[begin paper 3]

PMCID = 7856273

Title = Discriminative ensemble learning for few-shot chest x-ray diagnosis

Few-shot learning is an almost unexplored area in the field of medical image analysis. We propose a method for few-shot diagnosis of diseases and conditions from chest x-rays using discriminative ensemble learning. Our design involves a CNN-based coarse-learner in the first step to learn the general characteristics of chest x-rays. In the second step, we introduce a saliency-based classifier to extract disease-specific salient features from the output of the coarse-learner and classify based on the salient features. We propose a novel discriminative autoencoder ensemble to design the saliency-based classifier. The classification of the diseases is performed based on the salient features. Our algorithm proceeds through meta-training and meta-testing. During the training phase of meta-training, we train the coarse-learner. However, during the training phase of meta-testing, we train only the saliency-based classifier. Thus, our method is first-of-its-kind where the training phase of meta-training and the training phase of meta-testing are architecturally disjoint, making the method modular and easily adaptable to new tasks requiring the training of only the saliency-based classifier. Experiments show as high as ~ 19% improvement in terms of F1 score compared to the baseline in the diagnosis of chest x-rays from publicly available datasets.

[end paper 3]

[begin paper 4]

PMCID = 11036183

Title = An Empirical Evaluation of Prompting Strategies for Large Language Models in Zero-Shot Clinical Natural Language Processing: Algorithm Development and Validation Study

Large language models (LLMs) have shown remarkable capabilities in natural language processing (NLP), especially in domains where labeled data are scarce or expensive, such as the clinical domain. However, to unlock the clinical knowledge hidden in these LLMs, we need to design effective prompts that can guide them to perform specific clinical NLP tasks without any task-specific training data. This is known as in-context learning, which is an art and science that requires understanding the strengths and weaknesses of different LLMs and prompt engineering approaches.

The objective of this study is to assess the effectiveness of various prompt engineering techniques, including 2 newly introduced types—heuristic and ensemble prompts, for zero-shot and few-shot clinical information extraction using pretrained language models.

This comprehensive experimental study evaluated different prompt types (simple prefix, simple cloze, chain of thought, anticipatory, heuristic, and ensemble) across 5 clinical NLP tasks: clinical sense disambiguation, biomedical evidence extraction, coreference resolution, medication status extraction, and medication attribute extraction. The performance of these prompts was assessed using 3 state-of-the-art language models: GPT-3.5 (OpenAI), Gemini (Google), and LLaMA-2 (Meta). The study contrasted zero-shot with few-shot prompting and explored the effectiveness of ensemble approaches.

The study revealed that task-specific prompt tailoring is vital for the high performance of LLMs for zero-shot clinical NLP. In clinical sense disambiguation, GPT-3.5 achieved an accuracy of 0.96 with heuristic prompts and 0.94 in biomedical evidence extraction. Heuristic prompts, alongside chain of thought prompts, were highly effective across tasks. Few-shot prompting improved performance in complex scenarios, and ensemble approaches capitalized on multiple prompt strengths. GPT-3.5 consistently outperformed Gemini and LLaMA-2 across tasks and prompt types.

This study provides a rigorous evaluation of prompt engineering methodologies and introduces innovative techniques for clinical information extraction, demonstrating the potential of in-context learning in the clinical domain. These findings offer clear guidelines for future prompt-based clinical NLP research, facilitating engagement by non-NLP experts in clinical NLP advancements. To the best of our knowledge, this is one of the first works on the empirical evaluation of different prompt engineering approaches for clinical NLP in this era of generative artificial intelligence, and we hope that it will inspire and inform future research in this area.

[end paper 4]

[begin paper 5]

PMCID = 11041484

Title = Few-Shot Learning for Clinical Natural Language Processing Using Siamese Neural Networks: Algorithm Development and Validation Study

Natural language processing (NLP) has become an emerging technology in health care that leverages a large amount of free-text data in electronic health records to improve patient care, support clinical decisions, and facilitate clinical and translational science research. Recently, deep learning has achieved state-of-the-art performance in many clinical NLP tasks. However, training deep learning models often requires large, annotated data sets, which are normally not publicly available and can be time-consuming to build in clinical domains. Working with smaller annotated data sets is typical in clinical NLP; therefore, ensuring that deep learning models perform well is crucial for real-world clinical NLP applications. A widely adopted approach is fine-tuning existing pretrained language models, but these attempts fall short when the training data set contains only a few annotated samples. Few-shot learning (FSL) has recently been investigated to tackle this problem. Siamese neural network (SNN) has been widely used as an FSL approach in computer vision but has not been studied well in NLP. Furthermore, the literature on its applications in clinical domains is scarce.

The aim of our study is to propose and evaluate SNN-based approaches for few-shot clinical NLP tasks.

We propose 2 SNN-based FSL approaches, including pretrained SNN and SNN with second-order embeddings. We evaluate the proposed approaches on the clinical sentence classification task. We experiment with 3 few-shot settings, including 4-shot, 8-shot, and 16-shot learning. The clinical NLP task is benchmarked using the following 4 pretrained language models: bidirectional encoder representations from transformers (BERT), BERT for biomedical text mining (BioBERT), BioBERT trained on clinical notes (BioClinicalBERT), and generative pretrained transformer 2 (GPT-2). We also present a performance comparison between SNN-based approaches and the prompt-based GPT-2 approach.

In 4-shot sentence classification tasks, GPT-2 had the highest precision (0.63), but its recall (0.38) and F score (0.42) were lower than those of BioBERT-based pretrained SNN (0.45 and 0.46, respectively). In both 8-shot and 16-shot settings, SNN-based approaches outperformed GPT-2 in all 3 metrics of precision, recall, and F score.

The experimental results verified the effectiveness of the proposed SNN approaches for few-shot clinical NLP tasks.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Domain adaptation in clinical NLP":

[begin paper 1]

PMCID = 9144795

Title = Stemphylium lycopersici Nep1-like Protein (NLP) Is a Key Virulence Factor in Tomato Gray Leaf Spot Disease

The fungus Stemphylium lycopersici (S. lycopersici) is an economically important plant pathogen that causes grey leaf spot disease in tomato. However, functional genomic studies in S. lycopersici are lacking, and the factors influencing its pathogenicity remain largely unknown. Here, we present the first example of genetic transformation and targeted gene replacement in S. lycopersici. We functionally analyzed the NLP gene, which encodes a necrosis- and ethylene-inducing peptide 1 (Nep1)-like protein (NLP). We found that targeted disruption of the NLP gene in S. lycopersici significantly compromised its virulence on tomato. Moreover, our data suggest that NLP affects S. lycopersici conidiospore production and weakly affects its adaptation to osmotic and oxidative stress. Interestingly, we found that NLP suppressed the production of reactive oxygen species (ROS) in tomato leaves during S. lycopersici infection. Further, expressing the fungal NLP in tomato resulted in constitutive transcription of immune-responsive genes and inhibited plant growth. Through gene manipulation, we demonstrated the function of NLP in S. lycopersici virulence and development. Our work provides a paradigm for functional genomics studies in a non-model fungal pathogen system.

[end paper 1]

[begin paper 2]

PMCID = 9281254

Title = Natural language processing: state of the art, current trends and challenges

Natural language processing (NLP) has recently gained much attention for representing and analyzing human language computationally. It has spread its applications in various fields such as machine translation, email spam detection, information extraction, summarization, medical, and question answering etc. In this paper, we first distinguish four phases by discussing different levels of NLP and components of Natural Language Generation followed by presenting the history and evolution of NLP. We then discuss in detail the state of the art presenting the various applications of NLP, current trends, and challenges. Finally, we present a discussion on some available datasets, models, and evaluation metrics in NLP.

[end paper 2]

[begin paper 3]

PMCID = 11839006

Title = Development and Validation of Natural Language Processing Algorithms in the ENACT National Electronic Health Record Research Network

Electronic health record (EHR) data are a rich and invaluable source of real-world clinical information, enabling detailed insights into patient populations, treatment outcomes, and healthcare practices. The availability of large volumes of EHR data are critical for advancing translational research and developing innovative technologies such as artificial intelligence. The Evolve to Next-Gen Accrual to Clinical Trials (ENACT) network, established in 2015 with funding from the National Center for Advancing Translational Sciences (NCATS), aims to accelerate translational research by democratizing access to EHR data for all Clinical and Translational Science Awards (CTSA) hub investigators. The present ENACT network provides access to structured EHR data, enabling cohort discovery and translational research across the network. However, a substantial amount of critical information is contained in clinical narratives, and natural language processing (NLP) is required for extracting this information to support research. To address this need, the ENACT NLP Working Group was formed to make NLP-derived clinical information accessible and queryable across the network. This article describes the implementation and deployment of NLP infrastructure across ENACT. First, we describe the formation and goals of the Working Group, the practices and logistics involved in implementation and deployment, and the specific NLP tools and technologies utilized. Then, we describe how we extended the ENACT ontology to standardize and query NLP-derived data, as well as how we conducted multisite evaluations of the NLP algorithms. Finally, we reflect on the experience and lessons learnt, which may be useful for other national data networks that are deploying NLP to unlock the potential of clinical text for research.

[end paper 3]

[begin paper 4]

PMCID = 11923465

Title = Natural Language Processing Technologies for Public Health in Africa: Scoping Review

Natural language processing (NLP) has the potential to promote public health. However, applying these technologies in African health systems faces challenges, including limited digital and computational resources to support the continent’s diverse languages and needs.

This scoping review maps the evidence on NLP technologies for public health in Africa, addressing the following research questions: (1) What public health needs are being addressed by NLP technologies in Africa, and what unmet needs remain? (2) What factors influence the availability of public health NLP technologies across African countries and languages? (3) What stages of deployment have these technologies reached, and to what extent have they been integrated into health systems? (4) What measurable impact has these technologies had on public health outcomes, where such data are available? (5) What recommendations have been proposed to enhance the quality, cost, and accessibility of health-related NLP technologies in Africa?

This scoping review includes academic studies published between January 1, 2013, and October 3, 2024. A systematic search was conducted across databases, including MEDLINE via PubMed, ACL Anthology, Scopus, IEEE Xplore, and ACM Digital Library, supplemented by gray literature searches. Data were extracted and the NLP technology functions were mapped to the World Health Organization’s list of essential public health functions and the United Nations’ sustainable development goals (SDGs). The extracted data were analyzed to identify trends, gaps, and areas for future research. This scoping review follows the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses Extension for Scoping Reviews) reporting guidelines, and its protocol is publicly available.

Of 2186 citations screened, 54 studies were included. While existing NLP technologies support a subset of essential public health functions and SDGs, language coverage remains uneven, with limited support for widely spoken African languages, such as Kiswahili, Yoruba, Igbo, and Zulu, and no support for most of Africa’s >2000 languages. Most technologies are in prototyping phases, with only one fully deployed chatbot addressing vaccine hesitancy. Evidence of measurable impact is limited, with 15% (8/54) studies attempting health-related evaluations and 4% (2/54) demonstrating positive public health outcomes, including improved participants’ mood and increased vaccine intentions. Recommendations include expanding language coverage, targeting local health needs, enhancing trust, integrating solutions into health systems, and adopting participatory design approaches. The gray literature reveals industry- and nongovernmental organizations–led projects focused on deployable NLP applications. However, these projects tend to support only a few major languages and specific use cases, indicating a narrower scope than academic research.

Despite growth in NLP research for public health, major gaps remain in deployment, linguistic inclusivity, and health outcome evaluation. Future research should prioritize cross-sectoral and needs-based approaches that engage local communities, align with African health systems, and incorporate rigorous evaluations to enhance public health outcomes.

RR2-doi:10.1101/2024.07.02.24309815

[end paper 4]

[begin paper 5]

PMCID = 11642228

Title = Revolutionizing Radiology with Natural Language Processing and Chatbot Technologies: A Narrative Umbrella Review on Current Trends and Future Directions

The application of chatbots and NLP in radiology is an emerging field, currently characterized by a growing body of research. An umbrella review has been proposed utilizing a standardized checklist and quality control procedure for including scientific papers. This review explores the early developments and potential future impact of these technologies in radiology. The current literature, comprising 15 systematic reviews, highlights potentialities, opportunities, areas needing improvements, and recommendations. This umbrella review offers a comprehensive overview of the current landscape of natural language processing (NLP) and natural language models (NLMs), including chatbots, in healthcare. These technologies show potential for improving clinical decision-making, patient engagement, and communication across various medical fields. However, significant challenges remain, particularly the lack of standardized protocols, which raises concerns about the reliability and consistency of these tools in different clinical contexts. Without uniform guidelines, variability in outcomes may hinder the broader adoption of NLP/NLM technologies by healthcare providers. Moreover, the limited research on how these technologies intersect with medical devices (MDs) is a notable gap in the literature. Future research must address these challenges to fully realize the potential of NLP/NLM applications in healthcare. Key future research directions include the development of standardized protocols to ensure the consistent and safe deployment of NLP/NLM tools, particularly in high-stake areas like radiology. Investigating the integration of these technologies with MD workflows will be crucial to enhance clinical decision-making and patient care. Ethical concerns, such as data privacy, informed consent, and algorithmic bias, must also be explored to ensure responsible use in clinical settings. Longitudinal studies are needed to evaluate the long-term impact of these technologies on patient outcomes, while interdisciplinary collaboration between healthcare professionals, data scientists, and ethicists is essential for driving innovation in an ethically sound manner. Addressing these areas will advance the application of NLP/NLM technologies and improve patient care in this emerging field.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Few-shot learning and LLM interpretability in clinical phenotype definition":

[begin paper 1]

PMCID = 11460004

Title = A hybrid framework with large language models for rare disease phenotyping

Rare diseases pose significant challenges in diagnosis and treatment due to their low prevalence and heterogeneous clinical presentations. Unstructured clinical notes contain valuable information for identifying rare diseases, but manual curation is time-consuming and prone to subjectivity. This study aims to develop a hybrid approach combining dictionary-based natural language processing (NLP) tools with large language models (LLMs) to improve rare disease identification from unstructured clinical reports.

We propose a novel hybrid framework that integrates the Orphanet Rare Disease Ontology (ORDO) and the Unified Medical Language System (UMLS) to create a comprehensive rare disease vocabulary. SemEHR, a dictionary-based NLP tool, is employed to extract rare disease mentions from clinical notes. To refine the results and improve accuracy, we leverage various LLMs, including LLaMA3, Phi3-mini, and domain-specific models like OpenBioLLM and BioMistral. Different prompting strategies, such as zero-shot, few-shot, and knowledge-augmented generation, are explored to optimize the LLMs’ performance.

The proposed hybrid approach demonstrates superior performance compared to traditional NLP systems and standalone LLMs. LLaMA3 and Phi3-mini achieve the highest F1 scores in rare disease identification. Few-shot prompting with 1-3 examples yields the best results, while knowledge-augmented generation shows limited improvement. Notably, the approach uncovers a significant number of potential rare disease cases not documented in structured diagnostic records, highlighting its ability to identify previously unrecognized patients.

The hybrid approach combining dictionary-based NLP tools with LLMs shows great promise for improving rare disease identification from unstructured clinical reports. By leveraging the strengths of both techniques, the method demonstrates superior performance and the potential to uncover hidden rare disease cases. Further research is needed to address limitations related to ontology mapping and overlapping case identification, and to integrate the approach into clinical practice for early diagnosis and improved patient outcomes.

The online version contains supplementary material available at 10.1186/s12911-024-02698-7.

[end paper 1]

[begin paper 2]

PMCID = 11422740

Title = Prompt Engineering Paradigms for Medical Applications: Scoping Review

Prompt engineering, focusing on crafting effective prompts to large language models (LLMs), has garnered attention for its capabilities at harnessing the potential of LLMs. This is even more crucial in the medical domain due to its specialized terminology and language technicity. Clinical natural language processing applications must navigate complex language and ensure privacy compliance. Prompt engineering offers a novel approach by designing tailored prompts to guide models in exploiting clinically relevant information from complex medical texts. Despite its promise, the efficacy of prompt engineering in the medical domain remains to be fully explored.

The aim of the study is to review research efforts and technical approaches in prompt engineering for medical applications as well as provide an overview of opportunities and challenges for clinical practice.

Databases indexing the fields of medicine, computer science, and medical informatics were queried in order to identify relevant published papers. Since prompt engineering is an emerging field, preprint databases were also considered. Multiple data were extracted, such as the prompt paradigm, the involved LLMs, the languages of the study, the domain of the topic, the baselines, and several learning, design, and architecture strategies specific to prompt engineering. We include studies that apply prompt engineering–based methods to the medical domain, published between 2022 and 2024, and covering multiple prompt paradigms such as prompt learning (PL), prompt tuning (PT), and prompt design (PD).

We included 114 recent prompt engineering studies. Among the 3 prompt paradigms, we have observed that PD is the most prevalent (78 papers). In 12 papers, PD, PL, and PT terms were used interchangeably. While ChatGPT is the most commonly used LLM, we have identified 7 studies using this LLM on a sensitive clinical data set. Chain-of-thought, present in 17 studies, emerges as the most frequent PD technique. While PL and PT papers typically provide a baseline for evaluating prompt-based approaches, 61% (48/78) of the PD studies do not report any nonprompt-related baseline. Finally, we individually examine each of the key prompt engineering–specific information reported across papers and find that many studies neglect to explicitly mention them, posing a challenge for advancing prompt engineering research.

In addition to reporting on trends and the scientific landscape of prompt engineering, we provide reporting guidelines for future studies to help advance research in the medical field. We also disclose tables and figures summarizing medical prompt engineering papers available and hope that future contributions will leverage these existing works to better advance the field.

[end paper 2]

[begin paper 3]

PMCID = 10967767

Title = A Comprehensive Review on Synergy of Multi-Modal Data and AI Technologies in Medical Diagnosis

Disease diagnosis represents a critical and arduous endeavor within the medical field. Artificial intelligence (AI) techniques, spanning from machine learning and deep learning to large model paradigms, stand poised to significantly augment physicians in rendering more evidence-based decisions, thus presenting a pioneering solution for clinical practice. Traditionally, the amalgamation of diverse medical data modalities (e.g., image, text, speech, genetic data, physiological signals) is imperative to facilitate a comprehensive disease analysis, a topic of burgeoning interest among both researchers and clinicians in recent times. Hence, there exists a pressing need to synthesize the latest strides in multi-modal data and AI technologies in the realm of medical diagnosis. In this paper, we narrow our focus to five specific disorders (Alzheimer’s disease, breast cancer, depression, heart disease, epilepsy), elucidating advanced endeavors in their diagnosis and treatment through the lens of artificial intelligence. Our survey not only delineates detailed diagnostic methodologies across varying modalities but also underscores commonly utilized public datasets, the intricacies of feature engineering, prevalent classification models, and envisaged challenges for future endeavors. In essence, our research endeavors to contribute to the advancement of diagnostic methodologies, furnishing invaluable insights for clinical decision making.

[end paper 3]

[begin paper 4]

PMCID = 11639975

Title = EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy

In recent years, large language models have shown great potential to enhance traditional medical image processing by incorporating multimodality information into decision-making. Conventional artificial intelligence systems solely rely on images to make predictions or decisions. However, information from medical reports can provide invaluable information for the system to curate its decision. Here we are presenting a multimodality language-vision model and framework for accurate segmentation of medical images.

Background/Objectives: Lung cancer is a devastating disease with the highest mortality rate among cancer types. Over 60% of non-small cell lung cancer (NSCLC) patients, accounting for 87% of lung cancer diagnoses, require radiation therapy. Rapid treatment initiation significantly increases the patient’s survival rate and reduces the mortality rate. Accurate tumor segmentation is a critical step in diagnosing and treating NSCLC. Manual segmentation is time- and labor-consuming and causes delays in treatment initiation. Although many lung nodule detection methods, including deep learning-based models, have been proposed. Most of these methods still have a long-standing problem of high false positives (FPs). Methods: Here, we developed an electronic health record (EHR)-guided lung tumor auto-segmentation called EXACT-Net (EHR-enhanced eXACtitude in Tumor segmentation), where the extracted information from EHRs using a pre-trained large language model (LLM) was used to remove the FPs and keep the TP nodules only. Results: The auto-segmentation model was trained on NSCLC patients’ computed tomography (CT), and the pre-trained LLM was used with the zero-shot learning approach. Our approach resulted in a 250% boost in successful nodule detection using the data from ten NSCLC patients treated in our institution. Conclusions: We demonstrated that combining vision-language information in EXACT-Net multi-modal AI framework greatly enhances the performance of vision only models, paving the road to multimodal AI framework for medical image processing.

[end paper 4]

[begin paper 5]

PMCID = 11076269

Title = A mini-review on perturbation modelling across single-cell omic modalities

Recent advances in single-cell omics technology have transformed the landscape of cellular and molecular research, enriching the scope and intricacy of cellular characterisation. Perturbation modelling seeks to comprehensively grasp the effects of external influences like disease onset or molecular knock-outs or external stimulants on cellular physiology, specifically on transcription factors, signal transducers, biological pathways, and dynamic cell states. Machine and deep learning tools transform complex perturbational phenomena in algorithmically tractable tasks to formulate predictions based on various types of single-cell datasets. However, the recent surge in tools and datasets makes it challenging for experimental biologists and computational scientists to keep track of the recent advances in this rapidly expanding filed of single-cell modelling. Here, we recapitulate the main objectives of perturbation modelling and summarise novel single-cell perturbation technologies based on genetic manipulation like CRISPR or compounds, spanning across omic modalities. We then concisely review a burgeoning group of computational methods extending from classical statistical inference methodologies to various machine and deep learning architectures like shallow models or autoencoders, to biologically informed approaches based on gene regulatory networks, and to combinatorial efforts reminiscent of ensemble learning. We also discuss the rising trend of large foundational models in single-cell perturbation modelling inspired by large language models. Lastly, we critically assess the challenges that underline single-cell perturbation modelling while pointing towards relevant future perspectives like perturbation atlases, multi-omics and spatial datasets, causal machine learning for interpretability, multi-task learning for performance and explainability as well as prospects for solving interoperability and benchmarking pitfalls.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Domain adaptation and clinical applications of LLMs":

[begin paper 1]

PMCID = 11285660

Title = Introduction to Large Language Models (LLMs) for dementia care and research

Dementia is a progressive neurodegenerative disorder that affects cognitive abilities including memory, reasoning, and communication skills, leading to gradual decline in daily activities and social engagement. In light of the recent advent of Large Language Models (LLMs) such as ChatGPT, this paper aims to thoroughly analyse their potential applications and usefulness in dementia care and research.

To this end, we offer an introduction into LLMs, outlining the key features, capabilities, limitations, potential risks, and practical considerations for deployment as easy-to-use software (e.g., smartphone apps). We then explore various domains related to dementia, identifying opportunities for LLMs to enhance understanding, diagnostics, and treatment, with a broader emphasis on improving patient care. For each domain, the specific contributions of LLMs are examined, such as their ability to engage users in meaningful conversations, deliver personalized support, and offer cognitive enrichment. Potential benefits encompass improved social interaction, enhanced cognitive functioning, increased emotional well-being, and reduced caregiver burden. The deployment of LLMs in caregiving frameworks also raises a number of concerns and considerations. These include privacy and safety concerns, the need for empirical validation, user-centered design, adaptation to the user's unique needs, and the integration of multimodal inputs to create more immersive and personalized experiences. Additionally, ethical guidelines and privacy protocols must be established to ensure responsible and ethical deployment of LLMs.

We report the results on a questionnaire filled in by people with dementia (PwD) and their supporters wherein we surveyed the usefulness of different application scenarios of LLMs as well as the features that LLM-powered apps should have. Both PwD and supporters were largely positive regarding the prospect of LLMs in care, although concerns were raised regarding bias, data privacy and transparency.

Overall, this review corroborates the promising utilization of LLMs to positively impact dementia care by boosting cognitive abilities, enriching social interaction, and supporting caregivers. The findings underscore the importance of further research and development in this field to fully harness the benefits of LLMs and maximize their potential for improving the lives of individuals living with dementia.

[end paper 1]

[begin paper 2]

PMCID = 11456558

Title = Large language model to multimodal large language model: A journey to shape the biological macromolecules to biological sciences and medicine

After ChatGPT was released, large language models (LLMs) became more popular. Academicians use ChatGPT or LLM models for different purposes, and the use of ChatGPT or LLM is increasing from medical science to diversified areas. Recently, the multimodal LLM (MLLM) has also become popular. Therefore, we comprehensively illustrate the LLM and MLLM models for a complete understanding. We also aim for simple and extended reviews of LLMs and MLLMs for a broad category of readers, such as researchers, students in diversified fields, and other academicians. The review article illustrates the LLM and MLLM models, their working principles, and their applications in diversified fields. First, we demonstrate the technical concept of LLMs, working principle, Black Box, and the evolution of LLMs. To explain the working principle, we discuss the tokenization process, token representation, and token relationships. We also extensively demonstrate the application of LLMs in biological macromolecules, medical science, biological science, and other areas. We illustrate the multimodal applications of LLMs or MLLMs. Finally, we illustrate the limitations, challenges, and future prospects of LLMs. The review acts as a booster dose for clinicians, a primer for molecular biologists, and a catalyst for scientists, and also benefits diversified academicians.

Chakraborty and colleagues extensively illustrate LMMs and MLLMs for a better understanding, along with the working principle of an LLM with the tokenization process, token representation, and token relationships. Moreover, the diversified applications of LLMs and MLLMs are discussed in biological macromolecules, biological sciences, medical science, and other areas.

[end paper 2]

[begin paper 3]

PMCID = 11739813

Title = A review of large language models and autonomous agents in chemistry

Large language models (LLMs) have emerged as powerful tools in chemistry, significantly impacting molecule design, property prediction, and synthesis optimization. This review highlights LLM capabilities in these domains and their potential to accelerate scientific discovery through automation. We also review LLM-based autonomous agents: LLMs with a broader set of tools to interact with their surrounding environment. These agents perform diverse tasks such as paper scraping, interfacing with automated laboratories, and synthesis planning. As agents are an emerging topic, we extend the scope of our review of agents beyond chemistry and discuss across any scientific domains. This review covers the recent history, current capabilities, and design of LLMs and autonomous agents, addressing specific challenges, opportunities, and future directions in chemistry. Key challenges include data quality and integration, model interpretability, and the need for standard benchmarks, while future directions point towards more sophisticated multi-modal agents and enhanced collaboration between agents and experimental methods. Due to the quick pace of this field, a repository has been built to keep track of the latest studies: .

This review examines the roles of large language models (LLMs) and autonomous agents in chemistry, exploring advancements in molecule design, property prediction, and synthesis automation.

[end paper 3]

[begin paper 4]

PMCID = 11464944

Title = Multimodal Large Language Models in Health Care: Applications, Challenges, and Future Outlook

In the complex and multidimensional field of medicine, multimodal data are prevalent and crucial for informed clinical decisions. Multimodal data span a broad spectrum of data types, including medical images (eg, MRI and CT scans), time-series data (eg, sensor data from wearable devices and electronic health records), audio recordings (eg, heart and respiratory sounds and patient interviews), text (eg, clinical notes and research articles), videos (eg, surgical procedures), and omics data (eg, genomics and proteomics). While advancements in large language models (LLMs) have enabled new applications for knowledge retrieval and processing in the medical field, most LLMs remain limited to processing unimodal data, typically text-based content, and often overlook the importance of integrating the diverse data modalities encountered in clinical practice. This paper aims to present a detailed, practical, and solution-oriented perspective on the use of multimodal LLMs (M-LLMs) in the medical field. Our investigation spanned M-LLM foundational principles, current and potential applications, technical and ethical challenges, and future research directions. By connecting these elements, we aimed to provide a comprehensive framework that links diverse aspects of M-LLMs, offering a unified vision for their future in health care. This approach aims to guide both future research and practical implementations of M-LLMs in health care, positioning them as a paradigm shift toward integrated, multimodal data–driven medical practice. We anticipate that this work will spark further discussion and inspire the development of innovative approaches in the next generation of medical M-LLM systems.

[end paper 4]

[begin paper 5]

PMCID = 11701858

Title = Integration of large language models and federated learning

As the parameter size of large language models (LLMs) continues to expand, there is an urgent need to address the scarcity of high-quality data. In response, existing research has attempted to make a breakthrough by incorporating federated learning (FL) into LLMs. Conversely, considering the outstanding performance of LLMs in task generalization, researchers have also tried applying LLMs within FL to tackle challenges in relevant domains. The complementarity between LLMs and FL has already ignited widespread research interest. In this review, we aim to deeply explore the integration of LLMs and FL. We propose a research framework dividing the fusion of LLMs and FL into three parts: the combination of LLM sub-technologies with FL, the integration of FL sub-technologies with LLMs, and the overall merger of LLMs and FL. We first provide a comprehensive review of the current state of research in the domain of LLMs combined with FL, including their typical applications, integration advantages, challenges faced, and future directions for resolution. Subsequently, we discuss the practical applications of the combination of LLMs and FL in critical scenarios such as healthcare, finance, and education and provide new perspectives and insights into future research directions for LLMs and FL.

With the increasing size of large language models (LLMs), the scarcity of high-quality training data has become a significant hurdle. Federated learning (FL) offers a promising solution by enabling collaborative training across distributed data sources while preserving privacy. However, the potential of LLMs and FL goes beyond just enhancing LLMs. LLMs can also improve FL systems by leveraging their task generalization capabilities to address challenges in distributed learning environments. The integration of these two technologies has the potential to transform industries that rely heavily on sensitive data, such as healthcare, finance, and education, by enabling more secure, scalable, and effective AI applications. In the long term, this fusion could lead to more equitable access to LLMs, ensuring that powerful models can be trained and applied in diverse, privacy-sensitive contexts without relying on centralized data storage. This research opens the door to more sustainable and privacy-conscious LLM development, with significant societal implications across multiple sectors.

This review explores the integration of large language models (LLMs) and federated learning (FL), highlighting their complementarity. The authors propose a framework that categorizes the fusion into three parts: LLM sub-technologies with FL, FL sub-technologies with LLMs, and the overall merger of LLMs and FL. By exploring the current research landscape, existing challenges, future research directions, and applications in fields like healthcare, finance, and education, this work provides critical insights into advancing LLMs and FL together.

[end paper 5]



Here are the top 4 articles on PubMed Central for the query "Clinician trust in LLM-based clinical NLP tools":

[begin paper 1]

PMCID = 10871446

Title = Realizing the Potential of Social Determinants Data: A Scoping Review of Approaches for Screening, Linkage, Extraction, Analysis and Interventions

Social determinants of health (SDoH) like socioeconomics and neighborhoods strongly influence outcomes, yet standardized SDoH data is lacking in electronic health records (EHR), limiting research and care quality.

We searched PubMed using keywords “SDOH” and “EHR”, underwent title/abstract and full-text screening. Included records were analyzed under five domains: 1) SDoH screening and assessment approaches, 2) SDoH data collection and documentation, 3) Use of natural language processing (NLP) for extracting SDoH, 4) SDoH data and health outcomes, and 5) SDoH-driven interventions.

We identified 685 articles, of which 324 underwent full review. Key findings include tailored screening instruments implemented across settings, census and claims data linkage providing contextual SDoH profiles, rule-based and neural network systems extracting SDoH from notes using NLP, connections found between SDoH data and healthcare utilization/chronic disease control, and integrated care management programs executed. However, considerable variability persists across data sources, tools, and outcomes.

Despite progress identifying patient social needs, further development of standards, predictive models, and coordinated interventions is critical to fulfill the potential of SDoH-EHR integration. Additional database searches could strengthen this scoping review. Ultimately widespread capture, analysis, and translation of multidimensional SDoH data into clinical care is essential for promoting health equity.

[end paper 1]

[begin paper 2]

PMCID = 10834163

Title = Artificial intelligence: revolutionizing cardiology with large language models

Overview of input sources (top) to train or fine-tune cardio large language models and different applications (bottom). ECG, electrocardiogram; Q&A, questions and answers.

Natural language processing techniques are having an increasing impact on clinical care from patient, clinician, administrator, and research perspective. Among others are automated generation of clinical notes and discharge letters, medical term coding for billing, medical chatbots both for patients and clinicians, data enrichment in the identification of disease symptoms or diagnosis, cohort selection for clinical trial, and auditing purposes. In the review, an overview of the history in natural language processing techniques developed with brief technical background is presented. Subsequently, the review will discuss implementation strategies of natural language processing tools, thereby specifically focusing on large language models, and conclude with future opportunities in the application of such techniques in the field of cardiology.

[end paper 2]

[begin paper 3]

PMCID = 10883116

Title = Large language models: a primer and gastroenterology applications

Over the past year, the emergence of state-of-the-art large language models (LLMs) in tools like ChatGPT has ushered in a rapid acceleration in artificial intelligence (AI) innovation. These powerful AI models can generate tailored and high-quality text responses to instructions and questions without the need for labor-intensive task-specific training data or complex software engineering. As the technology continues to mature, LLMs hold immense potential for transforming clinical workflows, enhancing patient outcomes, improving medical education, and optimizing medical research. In this review, we provide a practical discussion of LLMs, tailored to gastroenterologists. We highlight the technical foundations of LLMs, emphasizing their key strengths and limitations as well as how to interact with them safely and effectively. We discuss some potential LLM use cases for clinical gastroenterology practice, education, and research. Finally, we review critical barriers to implementation and ongoing work to address these issues. This review aims to equip gastroenterologists with a foundational understanding of LLMs to facilitate a more active clinician role in the development and implementation of this rapidly emerging technology.

 Large language models in gastroenterology: a simplified overview for clinicians 

This text discusses the recent advancements in large language models (LLMs), like ChatGPT, which have significantly advanced artificial intelligence. These models can create specific, high-quality text responses without needing extensive training data or complex programming. They show great promise in transforming various aspects of clinical healthcare, particularly in improving patient care, medical education, and research. This article focuses on how LLMs can be applied in the field of gastroenterology. It explains the technical aspects of LLMs, their strengths and weaknesses, and how to use them effectively and safely. The text also explores how LLMs could be used in clinical practice, education, and research in gastroenterology. Finally, it discusses the challenges in implementing these models and the ongoing efforts to overcome them, aiming to provide gastroenterologists with the basic knowledge needed to engage more actively in the development and use of this emerging technology.

[end paper 3]

[begin paper 4]

PMCID = 10829781

Title = Artificial intelligence, ChatGPT, and other large language models for social determinants of health: Current state and future directions

This perspective highlights the importance of addressing social determinants of health (SDOH) in patient health outcomes and health inequity, a global problem exacerbated by the COVID-19 pandemic. We provide a broad discussion on current developments in digital health and artificial intelligence (AI), including large language models (LLMs), as transformative tools in addressing SDOH factors, offering new capabilities for disease surveillance and patient care. Simultaneously, we bring attention to challenges, such as data standardization, infrastructure limitations, digital literacy, and algorithmic bias, that could hinder equitable access to AI benefits. For LLMs, we highlight potential unique challenges and risks including environmental impact, unfair labor practices, inadvertent disinformation or “hallucinations,” proliferation of bias, and infringement of copyrights. We propose the need for a multitiered approach to digital inclusion as an SDOH and the development of ethical and responsible AI practice frameworks globally and provide suggestions on bridging the gap from development to implementation of equitable AI technologies.

Ong et al. discuss opportunities and limitations for AI and large language model (LLM)-based solutions in addressing social determinants of health (SDOH) factors and promoting global health equity. More work is needed to develop responsible AI frameworks and adopt a multitiered approach to digital inclusion.

[end paper 4]



