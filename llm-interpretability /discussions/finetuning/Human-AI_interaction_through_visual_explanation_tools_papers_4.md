## User

This is the beginning of an individual meeting with Data Visualization Expert to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Human-AI interaction through visual explanation tools in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Human-AI interaction through visual explanation tools to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Human-AI interaction through visual explanation tools. Include both general queries about Human-AI interaction through visual explanation tools and queries that specifically relate Human-AI interaction through visual explanation tools to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Data Visualization Expert, please provide your response to the agenda.

## Data Visualization Expert

To address the agenda and effectively contribute to building a transparent, clinically grounded, and visually intuitive interpretability tool, I will start by crafting a series of search queries to find relevant scientific papers. These queries will focus on Human-AI interaction through visual explanation tools, with a specific emphasis on LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
search_queries = [
    "Human-AI interaction through visual explanation tools",
    "LLM interpretability in electronic phenotype definitions",
    "Visual explanation tools in clinical applications",
    "Building clinician trust through AI visualizations",
    "SNOMED CT integration in AI interpretability tools"
]
```

Next, I will use these queries to search for relevant scientific papers. Let's proceed with retrieving the abstracts or full texts of these papers to identify the PMCIDs and titles.

## Data Visualization Expert

Here are the PMCIDs and titles of the papers that are relevant to the research project on Human-AI interaction through visual explanation tools, particularly in the context of LLM interpretability, phenotype definition, clinical applications, and clinician trust:

```python
papers = {
    "7926732": "A Review on Human–AI Interaction in Machine Learning and Insights for Medical Applications",
    "10570436": "Defining human-AI teaming the human-centered way: a scoping review and network analysis",
    "11525002": "Human-centered evaluation of explainable AI applications: a systematic review",
    "11008604": "Ascribing consciousness to artificial intelligence: human-AI interaction and its carry-over effects on human-human interaction",
    "11586345": "Managing human-AI collaborations within Industry 5.0 scenarios via knowledge graphs: key challenges and lessons learned",
    "11422740": "Prompt Engineering Paradigms for Medical Applications: Scoping Review",
    "10689487": "Zero-shot interpretable phenotyping of postpartum hemorrhage using large language models",
    "11545079": "The Evolution of Artificial Intelligence in Medical Imaging: From Computer Science to Machine and Deep Learning",
    "3302143": "Proximal correlates of metabolic phenotypes during ‘at-risk' and ‘case' stages of the metabolic disease continuum",
    "11460004": "A hybrid framework with large language models for rare disease phenotyping",
    "8792348": "Benchmarking off-the-shelf statistical shape modeling tools in clinical applications",
    "9859710": "From data to deployment: the Collaborative Communities on Ophthalmic Imaging roadmap for artificial intelligence in age-related macular degeneration",
    "8833140": "Clinical applications of personalising the neural components of visual image quality metrics for individual eyes",
    "11852121": "A Future Picture: A Review of Current Generative Adversarial Neural Networks in Vitreoretinal Pathologies and Their Future Potentials",
    "7180744": "Situation Awareness-Oriented Patient Monitoring with Visual Patient Technology: A Qualitative Review of the Primary Research",
    "11041414": "The Impact of Expectation Management and Model Transparency on Radiologists’ Trust and Utilization of AI Recommendations for Lung Nodule Assessment on Computed Tomography: Simulated Use Study",
    "11900311": "Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI",
    "11463756": "Evaluating Explainable Artificial Intelligence (XAI) techniques in chest radiology imaging through a human-centered Lens",
    "11561425": "How Explainable Artificial Intelligence Can Increase or Decrease Clinicians’ Trust in AI Applications in Health Care: Systematic Review",
    "11988467": "AI and Interventional Radiology: A Narrative Review of Reviews on Opportunities, Challenges, and Future Directions",
    "10767798": "Natural Language Processing to extract SNOMED-CT codes from pathological reports",
    "6849172": "Exploring semantic deep learning for building reliable and reusable one health knowledge from PubMed systematic reviews and veterinary clinical notes",
    "9931276": "Diseasomics: Actionable machine interpretable disease knowledge at the point-of-care",
    "11795397": "FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare",
    "8480545": "A natural language processing pipeline to synthesize patient-generated notes toward improving remote care and chronic disease management: a cystic fibrosis case study"
}
```

These papers provide a comprehensive overview of the current research landscape and will be instrumental in fine-tuning the understanding of Human-AI interaction through visual explanation tools in clinical settings.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Human-AI interaction through visual explanation tools":

[begin paper 1]

PMCID = 7926732

Title = A Review on Human–AI Interaction in Machine Learning and Insights for Medical Applications

Objective: To provide a human–Artificial Intelligence (AI) interaction review for Machine Learning (ML) applications to inform how to best combine both human domain expertise and computational power of ML methods. The review focuses on the medical field, as the medical ML application literature highlights a special necessity of medical experts collaborating with ML approaches. Methods: A scoping literature review is performed on Scopus and Google Scholar using the terms “human in the loop”, “human in the loop machine learning”, and “interactive machine learning”. Peer-reviewed papers published from 2015 to 2020 are included in our review. Results: We design four questions to investigate and describe human–AI interaction in ML applications. These questions are “Why should humans be in the loop?”, “Where does human–AI interaction occur in the ML processes?”, “Who are the humans in the loop?”, and “How do humans interact with ML in Human-In-the-Loop ML (HILML)?”. To answer the first question, we describe three main reasons regarding the importance of human involvement in ML applications. To address the second question, human–AI interaction is investigated in three main algorithmic stages: 1. data producing and pre-processing; 2. ML modelling; and 3. ML evaluation and refinement. The importance of the expertise level of the humans in human–AI interaction is described to answer the third question. The number of human interactions in HILML is grouped into three categories to address the fourth question. We conclude the paper by offering a discussion on open opportunities for future research in HILML.

[end paper 1]

[begin paper 2]

PMCID = 10570436

Title = Defining human-AI teaming the human-centered way: a scoping review and network analysis

With the advancement of technology and the increasing utilization of AI, the nature of human work is evolving, requiring individuals to collaborate not only with other humans but also with AI technologies to accomplish complex goals. This requires a shift in perspective from technology-driven questions to a human-centered research and design agenda putting people and evolving teams in the center of attention. A socio-technical approach is needed to view AI as more than just a technological tool, but as a team member, leading to the emergence of human-AI teaming (HAIT). In this new form of work, humans and AI synergistically combine their respective capabilities to accomplish shared goals.

The aim of our work is to uncover current research streams on HAIT and derive a unified understanding of the construct through a bibliometric network analysis, a scoping review and synthetization of a definition from a socio-technical point of view. In addition, antecedents and outcomes examined in the literature are extracted to guide future research in this field.

Through network analysis, five clusters with different research focuses on HAIT were identified. These clusters revolve around (1) human and (2) task-dependent variables, (3) AI explainability, (4) AI-driven robotic systems, and (5) the effects of AI performance on human perception. Despite these diverse research focuses, the current body of literature is predominantly driven by a technology-centric and engineering perspective, with no consistent definition or terminology of HAIT emerging to date.

We propose a unifying definition combining a human-centered and team-oriented perspective as well as summarize what is still needed in future research regarding HAIT. Thus, this work contributes to support the idea of the Frontiers Research Topic of a theoretical and conceptual basis for human work with AI systems.

[end paper 2]

[begin paper 3]

PMCID = 11525002

Title = Human-centered evaluation of explainable AI applications: a systematic review

Explainable Artificial Intelligence (XAI) aims to provide insights into the inner workings and the outputs of AI systems. Recently, there's been growing recognition that explainability is inherently human-centric, tied to how people perceive explanations. Despite this, there is no consensus in the research community on whether user evaluation is crucial in XAI, and if so, what exactly needs to be evaluated and how. This systematic literature review addresses this gap by providing a detailed overview of the current state of affairs in human-centered XAI evaluation. We reviewed 73 papers across various domains where XAI was evaluated with users. These studies assessed what makes an explanation “good” from a user's perspective, i.e., what makes an explanation meaningful to a user of an AI system. We identified 30 components of meaningful explanations that were evaluated in the reviewed papers and categorized them into a taxonomy of human-centered XAI evaluation, based on: (a) the contextualized quality of the explanation, (b) the contribution of the explanation to human-AI interaction, and (c) the contribution of the explanation to human-AI performance. Our analysis also revealed a lack of standardization in the methodologies applied in XAI user studies, with only 19 of the 73 papers applying an evaluation framework used by at least one other study in the sample. These inconsistencies hinder cross-study comparisons and broader insights. Our findings contribute to understanding what makes explanations meaningful to users and how to measure this, guiding the XAI community toward a more unified approach in human-centered explainability.

[end paper 3]

[begin paper 4]

PMCID = 11008604

Title = Ascribing consciousness to artificial intelligence: human-AI interaction and its carry-over effects on human-human interaction

The question of whether artificial intelligence (AI) can be considered conscious and therefore should be evaluated through a moral lens has surfaced in recent years. In this paper, we argue that whether AI is conscious is less of a concern than the fact that AI can be considered conscious by users during human-AI interaction, because this ascription of consciousness can lead to carry-over effects on human-human interaction. When AI is viewed as conscious like a human, then how people treat AI appears to carry over into how they treat other people due to activating schemas that are congruent to those activated during interactions with humans. In light of this potential, we might consider regulating how we treat AI, or how we build AI to evoke certain kinds of treatment from users, but not because AI is inherently sentient. This argument focuses on humanlike, social actor AI such as chatbots, digital voice assistants, and social robots. In the first part of the paper, we provide evidence for carry-over effects between perceptions of AI consciousness and behavior toward humans through literature on human-computer interaction, human-AI interaction, and the psychology of artificial agents. In the second part of the paper, we detail how the mechanism of schema activation can allow us to test consciousness perception as a driver of carry-over effects between human-AI interaction and human-human interaction. In essence, perceiving AI as conscious like a human, thereby activating congruent mind schemas during interaction, is a driver for behaviors and perceptions of AI that can carry over into how we treat humans. Therefore, the fact that people can ascribe humanlike consciousness to AI is worth considering, and moral protection for AI is also worth considering, regardless of AI’s inherent conscious or moral status.

[end paper 4]

[begin paper 5]

PMCID = 11586345

Title = Managing human-AI collaborations within Industry 5.0 scenarios via knowledge graphs: key challenges and lessons learned

In this paper, we discuss technologies and approaches based on Knowledge Graphs (KGs) that enable the management of inline human interventions in AI-assisted manufacturing processes in Industry 5.0 under potentially changing conditions in order to maintain or improve the overall system performance. Whereas KG-based systems are commonly based on a static view with their structure fixed at design time, we argue that the dynamic challenge of inline Human-AI (H-AI) collaboration in industrial settings calls for a late shaping design principle. In contrast to early shaping, which determines the system's behavior at design time in a fine granular manner, late shaping is a coarse-to-fine approach that leaves more space for fine-tuning, adaptation and integration of human intelligence at runtime. In this context we discuss approaches and lessons learned from the European manufacturing project Teaming.AI, https://www.teamingai-project.eu/, addressing general challenges like the modeling of domain expertise with particular focus on vertical knowledge integration, as well as challenges linked to an industrial KG of choice, such as its dynamic population and the late shaping of KG embeddings as the foundation of relational machine learning models which have emerged as an effective tool for exploiting graph-structured data to infer new insights.

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



Here are the top 5 articles on PubMed Central for the query "Visual explanation tools in clinical applications":

[begin paper 1]

PMCID = 8792348

Title = Benchmarking off-the-shelf statistical shape modeling tools in clinical applications

Statistical shape modeling (SSM) is widely used in biology and medicine as a new generation of morphometric approaches for the quantitative analysis of anatomical shapes. Technological advancements of in vivo imaging have led to the development of open-source computational tools that automate the modeling of anatomical shapes and their population-level variability. However, little work has been done on the evaluation and validation of such tools in clinical applications that rely on morphometric quantifications. Here, we systematically assess the outcome of widely used, state-of-the-art SSM tools, namely ShapeWorks, Deformetrica, and SPHARM-PDM. We use both quantitative and qualitative metrics to evaluate shape models from different tools. We propose validation frameworks for anatomical landmark/measurement inference and lesion screening. We also present a lesion screening method to objectively characterize subtle abnormal shape changes with respect to learned population-level statistics of controls. Results demonstrate that SSM tools display different levels of consistencies, where ShapeWorks and Deformetrica models are more consistent compared to models from SPHARM-PDM due to the groupwise approach of estimating surface correspondences. Furthermore, ShapeWorks and Deformetrica shape models are found to capture clinically relevant population-level variability compared to SPHARM-PDM models.

[end paper 1]

[begin paper 2]

PMCID = 9859710

Title = From data to deployment: the Collaborative Communities on Ophthalmic Imaging roadmap for artificial intelligence in age-related macular degeneration

Healthcare systems worldwide are challenged to provide adequate care for the 200 million individuals with age-related macular degeneration (AMD). Artificial intelligence (AI) has the potential to make a significant positive impact on the diagnosis and management of patients with AMD. However, the development of effective AI devices for clinical care faces numerous considerations and challenges, a fact evidenced by a current absence of FDA-approved AI devices for AMD.

To delineate the state of AI for AMD including current data, standards, achievements, and challenges.

EVIDENCE Members of the Collaborative Community on Ophthalmic Imaging working group for AI in AMD attended an inaugural meeting on September 7, 2020 to discuss the topic. Subsequently, they undertook a comprehensive review of the medical literature relevant to the topic. Members engaged in meetings and discussion through December 2021 to synthesize the information and arrive at consensus.

Existing infrastructure for robust AI development for AMD includes several large, labeled datasets of color fundus photography (CFP) and optical coherence tomography (OCT) images. However, image data often does not contain meta-data necessary for the development of reliable, valid, and generalizable models. Data sharing for AMD model development is made difficult by restrictions on data privacy and security, although potential solutions are under investigation. Computing resources may be adequate for current applications, but knowledge of machine learning (ML) development may be scarce in many clinical ophthalmology settings. Despite these challenges, researchers have produced promising AI models for AMD for screening, diagnosis, prediction, and monitoring. Future goals include defining benchmarks to facilitate regulatory authorization and subsequent real-world generalization.

Delivering an FDA-authorized, AI-based device for clinical care in AMD involves numerous considerations including the identification of an appropriate clinical application, acquisition and curation of a large, high-quality data set, development of the AI architecture, training and validation of the model, and functional interactions between the model output and clinical end-user. The research efforts undertaken to date represent starting points for the medical devices that will eventually benefit providers, healthcare systems, and patients.

[end paper 2]

[begin paper 3]

PMCID = 8833140

Title = Clinical applications of personalising the neural components of visual image quality metrics for individual eyes

Eyecare is evolving increasingly personalised corrections and increasingly personalised evaluations of corrections on-eye. This report describes individualising optical and neural components of the VSX (visual Strehl) metric and evaluates personalisation using two clinical applications. (1) Better understanding visual experience: While VSX tracks visual performance in typical eyes, non-individualised metrics underestimated visual performance in highly aberrated eyes – could this be understood by personalising metrics? (2) Metric-optimised objective spherocylindrical refractions in typical and atypical eyes have used neural weighting functions of typical eyes – will personalisation affect the outcome in clinical 0.25D steps?

Orientation-specific neural contrast sensitivity was measured in four typical myopic and astigmatic eyes and six eyes with keratoconus. Wavefront error was measured in all eyes while uncorrected and when the keratoconic eyes wore wavefront-guided scleral lenses. Total experiment duration was 24–28 h per subject. Two versions of VSX were calculated for each application: one weighted ocular optics with measured neural contrast sensitivity data from that eye, another weighted optics with a representative neural function of typical eyes. Wavefront-guided corrections were evaluated using the two metric values. Spherocylindrical corrections that optimised each metric were identified.

Metric values for keratoconic eyes improved by a mean factor of 1.99 (~0.3 log units) when personalised. Applying this factor to a larger sample of eyes from a previous keratoconus study reconciled dissonances between the percentage of eyes reaching normative best-corrected metric levels and the percentages of eyes reaching normative levels of visual acuity and contrast sensitivity. Spherocylindrical corrections that optimised both versions of VSX were clinically equivalent (mean ± SD Euclidean dioptric difference 0.13 ± 0.18 D).

Personalising visual image quality metrics is beneficial when actual metric values are used (evaluating ophthalmic corrections on-eye against norms) and when fine increments in visual quality are imparted (wavefront-guided corrections). However, partially individualised metrics appear adequate when metrics relatively rank spherocylindrical corrections in 0.25 D steps.

[end paper 3]

[begin paper 4]

PMCID = 11852121

Title = A Future Picture: A Review of Current Generative Adversarial Neural Networks in Vitreoretinal Pathologies and Their Future Potentials

Machine learning has transformed ophthalmology, particularly in predictive and discriminatory models for vitreoretinal pathologies. However, generative modeling, especially generative adversarial networks (GANs), remains underexplored. GANs consist of two neural networks—the generator and discriminator—that work in opposition to synthesize highly realistic images. These synthetic images can enhance diagnostic accuracy, expand the capabilities of imaging technologies, and predict treatment responses. GANs have already been applied to fundus imaging, optical coherence tomography (OCT), and fluorescein autofluorescence (FA). Despite their potential, GANs face challenges in reliability and accuracy. This review explores GAN architecture, their advantages over other deep learning models, and their clinical applications in retinal disease diagnosis and treatment monitoring. Furthermore, we discuss the limitations of current GAN models and propose novel applications combining GANs with OCT, OCT-angiography, fluorescein angiography, fundus imaging, electroretinograms, visual fields, and indocyanine green angiography.

[end paper 4]

[begin paper 5]

PMCID = 7180744

Title = Situation Awareness-Oriented Patient Monitoring with Visual Patient Technology: A Qualitative Review of the Primary Research

Visual Patient technology is a situation awareness-oriented visualization technology that translates numerical and waveform patient monitoring data into a new user-centered visual language. Vital sign values are converted into colors, shapes, and rhythmic movements—a language humans can easily perceive and interpret—on a patient avatar model in real time. In this review, we summarize the current state of the research on the Visual Patient, including the technology, its history, and its scientific context. We also provide a summary of our primary research and a brief overview of research work on similar user-centered visualizations in medicine. In several computer-based studies under various experimental conditions, Visual Patient transferred more information per unit time, increased perceived diagnostic certainty, and lowered perceived workload. Eye tracking showed the technology worked because of the way it synthesizes and transforms vital sign information into new and logical forms corresponding to the real phenomena. The technology could be particularly useful for improving situation awareness in settings with high cognitive demand or when users must make quick decisions. This comprehensive review of Visual Patient research is the foundation for an evaluation of the technology in clinical applications, starting with a high-fidelity simulation study in early 2020.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Building clinician trust through AI visualizations":

[begin paper 1]

PMCID = 11041414

Title = The Impact of Expectation Management and Model Transparency on Radiologists’ Trust and Utilization of AI Recommendations for Lung Nodule Assessment on Computed Tomography: Simulated Use Study

Many promising artificial intelligence (AI) and computer-aided detection and diagnosis systems have been developed, but few have been successfully integrated into clinical practice. This is partially owing to a lack of user-centered design of AI-based computer-aided detection or diagnosis (AI-CAD) systems.

We aimed to assess the impact of different onboarding tutorials and levels of AI model explainability on radiologists’ trust in AI and the use of AI recommendations in lung nodule assessment on computed tomography (CT) scans.

In total, 20 radiologists from 7 Dutch medical centers performed lung nodule assessment on CT scans under different conditions in a simulated use study as part of a 2×2 repeated-measures quasi-experimental design. Two types of AI onboarding tutorials (reflective vs informative) and 2 levels of AI output (black box vs explainable) were designed. The radiologists first received an onboarding tutorial that was either informative or reflective. Subsequently, each radiologist assessed 7 CT scans, first without AI recommendations. AI recommendations were shown to the radiologist, and they could adjust their initial assessment. Half of the participants received the recommendations via black box AI output and half received explainable AI output. Mental model and psychological trust were measured before onboarding, after onboarding, and after assessing the 7 CT scans. We recorded whether radiologists changed their assessment on found nodules, malignancy prediction, and follow-up advice for each CT assessment. In addition, we analyzed whether radiologists’ trust in their assessments had changed based on the AI recommendations.

Both variations of onboarding tutorials resulted in a significantly improved mental model of the AI-CAD system (informative P=.01 and reflective P=.01). After using AI-CAD, psychological trust significantly decreased for the group with explainable AI output (P=.02). On the basis of the AI recommendations, radiologists changed the number of reported nodules in 27 of 140 assessments, malignancy prediction in 32 of 140 assessments, and follow-up advice in 12 of 140 assessments. The changes were mostly an increased number of reported nodules, a higher estimated probability of malignancy, and earlier follow-up. The radiologists’ confidence in their found nodules changed in 82 of 140 assessments, in their estimated probability of malignancy in 50 of 140 assessments, and in their follow-up advice in 28 of 140 assessments. These changes were predominantly increases in confidence. The number of changed assessments and radiologists’ confidence did not significantly differ between the groups that received different onboarding tutorials and AI outputs.

Onboarding tutorials help radiologists gain a better understanding of AI-CAD and facilitate the formation of a correct mental model. If AI explanations do not consistently substantiate the probability of malignancy across patient cases, radiologists’ trust in the AI-CAD system can be impaired. Radiologists’ confidence in their assessments was improved by using the AI recommendations.

[end paper 1]

[begin paper 2]

PMCID = 11900311

Title = Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI

Background/Objectives: Artificial intelligence (AI) is transforming healthcare, enabling advances in diagnostics, treatment optimization, and patient care. Yet, its integration raises ethical, regulatory, and societal challenges. Key concerns include data privacy risks, algorithmic bias, and regulatory gaps that struggle to keep pace with AI advancements. This study aims to synthesize a multidisciplinary framework for trustworthy AI in healthcare, focusing on transparency, accountability, fairness, sustainability, and global collaboration. It moves beyond high-level ethical discussions to provide actionable strategies for implementing trustworthy AI in clinical contexts. Methods: A structured literature review was conducted using PubMed, Scopus, and Web of Science. Studies were selected based on relevance to AI ethics, governance, and policy in healthcare, prioritizing peer-reviewed articles, policy analyses, case studies, and ethical guidelines from authoritative sources published within the last decade. The conceptual approach integrates perspectives from clinicians, ethicists, policymakers, and technologists, offering a holistic “ecosystem” view of AI. No clinical trials or patient-level interventions were conducted. Results: The analysis identifies key gaps in current AI governance and introduces the Regulatory Genome—an adaptive AI oversight framework aligned with global policy trends and Sustainable Development Goals. It introduces quantifiable trustworthiness metrics, a comparative analysis of AI categories for clinical applications, and bias mitigation strategies. Additionally, it presents interdisciplinary policy recommendations for aligning AI deployment with ethical, regulatory, and environmental sustainability goals. This study emphasizes measurable standards, multi-stakeholder engagement strategies, and global partnerships to ensure that future AI innovations meet ethical and practical healthcare needs. Conclusions: Trustworthy AI in healthcare requires more than technical advancements—it demands robust ethical safeguards, proactive regulation, and continuous collaboration. By adopting the recommended roadmap, stakeholders can foster responsible innovation, improve patient outcomes, and maintain public trust in AI-driven healthcare.

[end paper 2]

[begin paper 3]

PMCID = 11463756

Title = Evaluating Explainable Artificial Intelligence (XAI) techniques in chest radiology imaging through a human-centered Lens

The field of radiology imaging has experienced a remarkable increase in using of deep learning (DL) algorithms to support diagnostic and treatment decisions. This rise has led to the development of Explainable AI (XAI) system to improve the transparency and trust of complex DL methods. However, XAI systems face challenges in gaining acceptance within the healthcare sector, mainly due to technical hurdles in utilizing these systems in practice and the lack of human-centered evaluation/validation. In this study, we focus on visual XAI systems applied to DL-enabled diagnostic system in chest radiography. In particular, we conduct a user study to evaluate two prominent visual XAI techniques from the human perspective. To this end, we created two clinical scenarios for diagnosing pneumonia and COVID-19 using DL techniques applied to chest X-ray and CT scans. The achieved accuracy rates were 90% for pneumonia and 98% for COVID-19. Subsequently, we employed two well-known XAI methods, Grad-CAM (Gradient-weighted Class Activation Mapping) and LIME (Local Interpretable Model-agnostic Explanations), to generate visual explanations elucidating the AI decision-making process. The visual explainability results were shared through a user study, undergoing evaluation by medical professionals in terms of clinical relevance, coherency, and user trust. In general, participants expressed a positive perception of the use of XAI systems in chest radiography. However, there was a noticeable lack of awareness regarding their value and practical aspects. Regarding preferences, Grad-CAM showed superior performance over LIME in terms of coherency and trust, although concerns were raised about its clinical usability. Our findings highlight key user-driven explainability requirements, emphasizing the importance of multi-modal explainability and the necessity to increase awareness of XAI systems among medical practitioners. Inclusive design was also identified as a crucial need to ensure better alignment of these systems with user needs.

[end paper 3]

[begin paper 4]

PMCID = 11561425

Title = How Explainable Artificial Intelligence Can Increase or Decrease Clinicians’ Trust in AI Applications in Health Care: Systematic Review

Artificial intelligence (AI) has significant potential in clinical practice. However, its “black box” nature can lead clinicians to question its value. The challenge is to create sufficient trust for clinicians to feel comfortable using AI, but not so much that they defer to it even when it produces results that conflict with their clinical judgment in ways that lead to incorrect decisions. Explainable AI (XAI) aims to address this by providing explanations of how AI algorithms reach their conclusions. However, it remains unclear whether such explanations foster an appropriate degree of trust to ensure the optimal use of AI in clinical practice.

This study aims to systematically review and synthesize empirical evidence on the impact of XAI on clinicians’ trust in AI-driven clinical decision-making.

A systematic review was conducted in accordance with PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines, searching PubMed and Web of Science databases. Studies were included if they empirically measured the impact of XAI on clinicians’ trust using cognition- or affect-based measures. Out of 778 articles screened, 10 met the inclusion criteria. We assessed the risk of bias using standard tools appropriate to the methodology of each paper.

The risk of bias in all papers was moderate or moderate to high. All included studies operationalized trust primarily through cognitive-based definitions, with 2 also incorporating affect-based measures. Out of these, 5 studies reported that XAI increased clinicians’ trust compared with standard AI, particularly when the explanations were clear, concise, and relevant to clinical practice. In addition, 3 studies found no significant effect of XAI on trust, and the presence of explanations does not automatically improve trust. Notably, 2 studies highlighted that XAI could either enhance or diminish trust, depending on the complexity and coherence of the provided explanations. The majority of studies suggest that XAI has the potential to enhance clinicians’ trust in recommendations generated by AI. However, complex or contradictory explanations can undermine this trust. More critically, trust in AI is not inherently beneficial, as AI recommendations are not infallible. These findings underscore the nuanced role of explanation quality and suggest that trust can be modulated through the careful design of XAI systems.

Excessive trust in incorrect advice generated by AI can adversely impact clinical accuracy, just as can happen when correct advice is distrusted. Future research should focus on refining both cognitive and affect-based measures of trust and on developing strategies to achieve an appropriate balance in terms of trust, preventing both blind trust and undue skepticism. Optimizing trust in AI systems is essential for their effective integration into clinical practice.

[end paper 4]

[begin paper 5]

PMCID = 11988467

Title = AI and Interventional Radiology: A Narrative Review of Reviews on Opportunities, Challenges, and Future Directions

The integration of artificial intelligence in interventional radiology is an emerging field with transformative potential, aiming to make a great contribution to the health domain. This overview of reviews seeks to identify prevailing themes, opportunities, challenges, and recommendations related to the process of integration. Utilizing a standardized checklist and quality control procedures, this review examines recent advancements in, and future implications of, this domain. In total, 27 review studies were selected through the systematic process. Based on the overview, the integration of artificial intelligence (AI) in interventional radiology (IR) presents significant opportunities to enhance precision, efficiency, and personalization of procedures. AI automates tasks like catheter manipulation and needle placement, improving accuracy and reducing variability. It also integrates multiple imaging modalities, optimizing treatment planning and outcomes. AI aids intra-procedural guidance with advanced needle tracking and real-time image fusion. Robotics and automation in IR are advancing, though full autonomy in AI-guided systems has not been achieved. Despite these advancements, the integration of AI in IR is complex, involving imaging systems, robotics, and other technologies. This complexity requires a comprehensive certification and integration process. The role of regulatory bodies, scientific societies, and clinicians is essential to address these challenges. Standardized guidelines, clinician education, and careful AI assessment are necessary for safe integration. The future of AI in IR depends on developing standardized guidelines for medical devices and AI applications. Collaboration between certifying bodies, scientific societies, and legislative entities, as seen in the EU AI Act, will be crucial to tackling AI-specific challenges. Focusing on transparency, data governance, human oversight, and post-market monitoring will ensure AI integration in IR proceeds with safeguards, benefiting patient outcomes and advancing the field.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in AI interpretability tools":

[begin paper 1]

PMCID = 10767798

Title = Natural Language Processing to extract SNOMED-CT codes from pathological reports

The use of standardized structured reports (SSR) and suitable terminologies like SNOMED-CT can enhance data retrieval and analysis, fostering large-scale studies and collaboration. However, the still large prevalence of narrative reports in our laboratories warrants alternative and automated labeling approaches. In this project, natural language processing (NLP) methods were used to associate SNOMED-CT codes to structured and unstructured reports from an Italian Digital Pathology Department.

Two NLP-based automatic coding systems (support vector machine, SVM, and long-short term memory, LSTM) were trained and applied to a series of narrative reports.

The 1163 cases were tested with both algorithms, showing good performances in terms of accuracy, precision, recall, and F1 score, with SVM showing slightly better performances as compared to LSTM (0.84, 0.87, 0.83, 0.82 vs 0.83, 0.85, 0.83, 0.82, respectively). The integration of an explainability allowed identification of terms and groups of words of importance, enabling fine-tuning, balancing semantic meaning and model performance.

AI tools allow the automatic SNOMED-CT labeling of the pathology archives, providing a retrospective fix to the large lack of organization of narrative reports.

[end paper 1]

[begin paper 2]

PMCID = 6849172

Title = Exploring semantic deep learning for building reliable and reusable one health knowledge from PubMed systematic reviews and veterinary clinical notes

Deep Learning opens up opportunities for routinely scanning large bodies of biomedical literature and clinical narratives to represent the meaning of biomedical and clinical terms. However, the validation and integration of this knowledge on a scale requires cross checking with ground truths (i.e. evidence-based resources) that are unavailable in an actionable or computable form. In this paper we explore how to turn information about diagnoses, prognoses, therapies and other clinical concepts into computable knowledge using free-text data about human and animal health. We used a Semantic Deep Learning approach that combines the Semantic Web technologies and Deep Learning to acquire and validate knowledge about 11 well-known medical conditions mined from two sets of unstructured free-text data: 300 K PubMed Systematic Review articles (the PMSB dataset) and 2.5 M veterinary clinical notes (the VetCN dataset). For each target condition we obtained 20 related clinical concepts using two deep learning methods applied separately on the two datasets, resulting in 880 term pairs (target term, candidate term). Each concept, represented by an n-gram, is mapped to UMLS using MetaMap; we also developed a bespoke method for mapping short forms (e.g. abbreviations and acronyms). Existing ontologies were used to formally represent associations. We also create ontological modules and illustrate how the extracted knowledge can be queried. The evaluation was performed using the content within BMJ Best Practice.

MetaMap achieves an F measure of 88% (precision 85%, recall 91%) when applied directly to the total of 613 unique candidate terms for the 880 term pairs. When the processing of short forms is included, MetaMap achieves an F measure of 94% (precision 92%, recall 96%). Validation of the term pairs with BMJ Best Practice yields precision between 98 and 99%.

The Semantic Deep Learning approach can transform neural embeddings built from unstructured free-text data into reliable and reusable One Health knowledge using ontologies and content from BMJ Best Practice.

[end paper 2]

[begin paper 3]

PMCID = 9931276

Title = Diseasomics: Actionable machine interpretable disease knowledge at the point-of-care

Physicians establish diagnosis by assessing a patient’s signs, symptoms, age, sex, laboratory test findings and the disease history. All this must be done in limited time and against the backdrop of an increasing overall workload. In the era of evidence-based medicine it is utmost important for a clinician to be abreast of the latest guidelines and treatment protocols which are changing rapidly. In resource limited settings, the updated knowledge often does not reach the point-of-care. This paper presents an artificial intelligence (AI)-based approach for integrating comprehensive disease knowledge, to support physicians and healthcare workers in arriving at accurate diagnoses at the point-of-care. We integrated different disease-related knowledge bodies to construct a comprehensive, machine interpretable diseasomics knowledge-graph that includes the Disease Ontology, disease symptoms, SNOMED CT, DisGeNET, and PharmGKB data. The resulting disease-symptom network comprises knowledge from the Symptom Ontology, electronic health records (EHR), human symptom disease network, Disease Ontology, Wikipedia, PubMed, textbooks, and symptomology knowledge sources with 84.56% accuracy. We also integrated spatial and temporal comorbidity knowledge obtained from EHR for two population data sets from Spain and Sweden respectively. The knowledge graph is stored in a graph database as a digital twin of the disease knowledge. We use node2vec (node embedding) as digital triplet for link prediction in disease-symptom networks to identify missing associations. This diseasomics knowledge graph is expected to democratize the medical knowledge and empower non-specialist health workers to make evidence based informed decisions and help achieve the goal of universal health coverage (UHC). The machine interpretable knowledge graphs presented in this paper are associations between various entities and do not imply causation. Our differential diagnostic tool focusses on signs and symptoms and does not include a complete assessment of patient’s lifestyle and health history which would typically be necessary to rule out conditions and to arrive at a final diagnosis. The predicted diseases are ordered according to the specific disease burden in South Asia. The knowledge graphs and the tools presented here can be used as a guide.

A doctor at the point-of-care is expected to have the complete medical knowledge with latest updates in evidence-based medicine (EBM). The doctor is also expected to use this complete knowledge accurately during a medical interaction with a patient. In reality this is not the case—there are gaps in knowledge acquisition and gaps in clinical decision making. To address these gaps, in the past AI based expert driven rule-based clinical decision support systems were developed. Rule-based systems are rigid and often fail in case of complex diseases. We therefore built an AI based evidence driven clinical decision support system. We mined PubMed, Wikipedia, textbooks, medical records, etc. to extract clinical knowledge. We used this clinical knowledge as glue to connect ontologies to construct a machine interpretable antireductionistic diseasomics knowledge graph. The diseasomics knowledge graph is stored in a Neo4j property graph database in a cloud for online and realtime access using JSON-RPC API and works like the physicians’ brain digital twin. We used the digital triplet node2vec techniques to mine unknown knowledge and to create a learning healthcare system. The integrated diseasomics knowledge system is available for use at https://triage.cyberneticcare.com/diseasePrediction.

[end paper 3]

[begin paper 4]

PMCID = 11795397

Title = FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare

Despite major advances in artificial intelligence (AI) research for healthcare, the deployment and adoption of AI technologies remain limited in clinical practice. This paper describes the FUTURE-AI framework, which provides guidance for the development and deployment of trustworthy AI tools in healthcare. The FUTURE-AI Consortium was founded in 2021 and comprises 117 interdisciplinary experts from 50 countries representing all continents, including AI scientists, clinical researchers, biomedical ethicists, and social scientists. Over a two year period, the FUTURE-AI guideline was established through consensus based on six guiding principles—fairness, universality, traceability, usability, robustness, and explainability. To operationalise trustworthy AI in healthcare, a set of 30 best practices were defined, addressing technical, clinical, socioethical, and legal dimensions. The recommendations cover the entire lifecycle of healthcare AI, from design, development, and validation to regulation, deployment, and monitoring.

[end paper 4]

[begin paper 5]

PMCID = 8480545

Title = A natural language processing pipeline to synthesize patient-generated notes toward improving remote care and chronic disease management: a cystic fibrosis case study

Patient-generated health data (PGHD) are important for tracking and monitoring out of clinic health events and supporting shared clinical decisions. Unstructured text as PGHD (eg, medical diary notes and transcriptions) may encapsulate rich information through narratives which can be critical to better understand a patient’s condition. We propose a natural language processing (NLP) supported data synthesis pipeline for unstructured PGHD, focusing on children with special healthcare needs (CSHCN), and demonstrate it with a case study on cystic fibrosis (CF).

The proposed unstructured data synthesis and information extraction pipeline extract a broad range of health information by combining rule-based approaches with pretrained deep-learning models. Particularly, we build upon the scispaCy biomedical model suite, leveraging its named entity recognition capabilities to identify and link clinically relevant entities to established ontologies such as Systematized Nomenclature of Medicine (SNOMED) and RXNORM. We then use scispaCy’s syntax (grammar) parsing tools to retrieve phrases associated with the entities in medication, dose, therapies, symptoms, bowel movements, and nutrition ontological categories. The pipeline is illustrated and tested with simulated CF patient notes.

The proposed hybrid deep-learning rule-based approach can operate over a variety of natural language note types and allow customization for a given patient or cohort. Viable information was successfully extracted from simulated CF notes. This hybrid pipeline is robust to misspellings and varied word representations and can be tailored to accommodate the needs of a specific patient, cohort, or clinician.

The NLP pipeline can extract predefined or ontology-based entities from free-text PGHD, aiming to facilitate remote care and improve chronic disease management. Our implementation makes use of open source models, allowing for this solution to be easily replicated and integrated in different health systems. Outside of the clinic, the use of the NLP pipeline may increase the amount of clinical data recorded by families of CSHCN and ease the process to identify health events from the notes. Similarly, care coordinators, nurses and clinicians would be able to track adherence with medications, identify symptoms, and effectively intervene to improve clinical care. Furthermore, visualization tools can be applied to digest the structured data produced by the pipeline in support of the decision-making process for a patient, caregiver, or provider.

Our study demonstrated that an NLP pipeline can be used to create an automated analysis and reporting mechanism for unstructured PGHD. Further studies are suggested with real-world data to assess pipeline performance and further implications.

[end paper 5]



