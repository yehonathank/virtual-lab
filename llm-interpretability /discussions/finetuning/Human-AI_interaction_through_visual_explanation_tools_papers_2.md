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

Here is a list of search queries in Python syntax that I would like to run to find relevant scientific papers on Human-AI interaction through visual explanation tools:

```python
queries = [
    "Human-AI interaction through visual explanation tools",
    "Human-AI interaction visual explanation tools LLM interpretability",
    "Human-AI interaction visual explanation tools phenotype definition",
    "Human-AI interaction visual explanation tools clinical applications",
    "Human-AI interaction visual explanation tools clinician trust"
]
```

For the agenda question regarding PMCIDs and titles of the papers, here is a Python dictionary mapping PMCID to title:

```python
papers = {
    "7926732": "A Review on Human–AI Interaction in Machine Learning and Insights for Medical Applications",
    "10570436": "Defining human-AI teaming the human-centered way: a scoping review and network analysis",
    "11525002": "Human-centered evaluation of explainable AI applications: a systematic review",
    "11008604": "Ascribing consciousness to artificial intelligence: human-AI interaction and its carry-over effects on human-human interaction",
    "11586345": "Managing human-AI collaborations within Industry 5.0 scenarios via knowledge graphs: key challenges and lessons learned",
    "11739813": "A review of large language models and autonomous agents in chemistry",
    "11844495": "Spike sorting AI agent",
    "10989254": "Human-artificial intelligence interaction in gastrointestinal endoscopy",
    "11068733": "FFA-GPT: an automated pipeline for fundus fluorescein angiography interpretation and question-answer",
    "11751657": "Revolutionizing Health Care: The Transformative Impact of Large Language Models in Medicine",
    "10831521": "Developing, Purchasing, Implementing and Monitoring AI Tools in Radiology: Practical Considerations. A Multi-Society Statement from the ACR, CAR, ESR, RANZCR and RSNA",
    "10800328": "Developing, purchasing, implementing and monitoring AI tools in radiology: practical considerations. A multi-society statement from the ACR, CAR, ESR, RANZCR & RSNA",
    "11908149": "Chemoarchitectural studies of the rat hypothalamus and zona incerta.Chemopleth 1.0 – A downloadable interactive Brain Maps spatial database of five co-visualizable neurochemical systems, with novel feature- and grid-based mapping tools",
    "11782883": "Demystifying the black box: A survey on explainable artificial intelligence (XAI) in bioinformatics",
    "9581990": "Explainable medical imaging AI needs human-centered design: guidelines and evidence from a systematic review",
    "11301121": "Human-AI Teaming in Critical Care: A Comparative Analysis of Data Scientists’ and Clinicians’ Perspectives on AI Augmentation and Automation",
    "11849858": "Safety of human-AI cooperative decision-making within intensive care: A physical simulation study",
    "11041414": "The Impact of Expectation Management and Model Transparency on Radiologists’ Trust and Utilization of AI Recommendations for Lung Nodule Assessment on Computed Tomography: Simulated Use Study",
    "8832512": "Lessons Learned About Designing and Conducting Studies From HRI Experts"
}
```

These papers cover a range of topics related to Human-AI interaction, visual explanation tools, and their applications in clinical settings, which will be beneficial for your research project.

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



Here are the top 5 articles on PubMed Central for the query "Human-AI interaction visual explanation tools LLM interpretability":

[begin paper 1]

PMCID = 11739813

Title = A review of large language models and autonomous agents in chemistry

Large language models (LLMs) have emerged as powerful tools in chemistry, significantly impacting molecule design, property prediction, and synthesis optimization. This review highlights LLM capabilities in these domains and their potential to accelerate scientific discovery through automation. We also review LLM-based autonomous agents: LLMs with a broader set of tools to interact with their surrounding environment. These agents perform diverse tasks such as paper scraping, interfacing with automated laboratories, and synthesis planning. As agents are an emerging topic, we extend the scope of our review of agents beyond chemistry and discuss across any scientific domains. This review covers the recent history, current capabilities, and design of LLMs and autonomous agents, addressing specific challenges, opportunities, and future directions in chemistry. Key challenges include data quality and integration, model interpretability, and the need for standard benchmarks, while future directions point towards more sophisticated multi-modal agents and enhanced collaboration between agents and experimental methods. Due to the quick pace of this field, a repository has been built to keep track of the latest studies: .

This review examines the roles of large language models (LLMs) and autonomous agents in chemistry, exploring advancements in molecule design, property prediction, and synthesis automation.

[end paper 1]

[begin paper 2]

PMCID = 11844495

Title = Spike sorting AI agent

Spike sorting is a fundamental process for decoding neural activity, involving preprocessing, spike detection, feature extraction, clustering, and validation. However, conventional spike sorting methods are highly fragmented, labor-intensive, and heavily reliant on expert manual curation, limiting their scalability and reproducibility. This challenge has become more pressing with advances in neural recording technology, such as high-density Neuropixels for large-scale neural recording or flexible electrodes for long-term stable recording over months to years. The volume and complexity of these datasets make manual curation infeasible, requiring an automated and scalable solution. Here, we introduce SpikeAgent, a multimodal large language model (LLM)-based AI agent that automates and standardizes the entire spike sorting pipeline. Unlike traditional approaches, SpikeAgent integrates multiple LLM backends, coding functions, and established algorithms, autonomously performing spike sorting with reasoning-based decision-making and real-time interaction with intermediate results. It generates interpretable reports, providing transparent justifications for each sorting decision, enhancing transparency and reliability. We benchmarked SpikeAgent against human experts across various neural recording technology, demonstrating its versatility and ability to achieve curation consistency that are equal to, or even higher than human experts. It also drastically reduces the expertise barrier and accelerates the curation and validation time by orders of magnitude. Moreover, it enables automated interpretability of the neural spiking data, which cannot be achieved by any conventional methods. SpikeAgent presents a paradigm shift in processing signals for neuroscience and brain-computer interfaces, while laying the ground for AI agent-augmented science across various domains.

[end paper 2]

[begin paper 3]

PMCID = 10989254

Title = Human-artificial intelligence interaction in gastrointestinal endoscopy

The number and variety of applications of artificial intelligence (AI) in gastrointestinal (GI) endoscopy is growing rapidly. New technologies based on machine learning (ML) and convolutional neural networks (CNNs) are at various stages of development and deployment to assist patients and endoscopists in preparing for endoscopic procedures, in detection, diagnosis and classification of pathology during endoscopy and in confirmation of key performance indicators. Platforms based on ML and CNNs require regulatory approval as medical devices. Interactions between humans and the technologies we use are complex and are influenced by design, behavioural and psychological elements. Due to the substantial differences between AI and prior technologies, important differences may be expected in how we interact with advice from AI technologies. Human–AI interaction (HAII) may be optimised by developing AI algorithms to minimise false positives and designing platform interfaces to maximise usability. Human factors influencing HAII may include automation bias, alarm fatigue, algorithm aversion, learning effect and deskilling. Each of these areas merits further study in the specific setting of AI applications in GI endoscopy and professional societies should engage to ensure that sufficient emphasis is placed on human-centred design in development of new AI technologies.

[end paper 3]

[begin paper 4]

PMCID = 11068733

Title = FFA-GPT: an automated pipeline for fundus fluorescein angiography interpretation and question-answer

Fundus fluorescein angiography (FFA) is a crucial diagnostic tool for chorioretinal diseases, but its interpretation requires significant expertise and time. Prior studies have used Artificial Intelligence (AI)-based systems to assist FFA interpretation, but these systems lack user interaction and comprehensive evaluation by ophthalmologists. Here, we used large language models (LLMs) to develop an automated interpretation pipeline for both report generation and medical question-answering (QA) for FFA images. The pipeline comprises two parts: an image-text alignment module (Bootstrapping Language-Image Pre-training) for report generation and an LLM (Llama 2) for interactive QA. The model was developed using 654,343 FFA images with 9392 reports. It was evaluated both automatically, using language-based and classification-based metrics, and manually by three experienced ophthalmologists. The automatic evaluation of the generated reports demonstrated that the system can generate coherent and comprehensible free-text reports, achieving a BERTScore of 0.70 and F1 scores ranging from 0.64 to 0.82 for detecting top-5 retinal conditions. The manual evaluation revealed acceptable accuracy (68.3%, Kappa 0.746) and completeness (62.3%, Kappa 0.739) of the generated reports. The generated free-form answers were evaluated manually, with the majority meeting the ophthalmologists’ criteria (error-free: 70.7%, complete: 84.0%, harmless: 93.7%, satisfied: 65.3%, Kappa: 0.762–0.834). This study introduces an innovative framework that combines multi-modal transformers and LLMs, enhancing ophthalmic image interpretation, and facilitating interactive communications during medical consultation.

[end paper 4]

[begin paper 5]

PMCID = 11751657

Title = Revolutionizing Health Care: The Transformative Impact of Large Language Models in Medicine

Large language models (LLMs) are rapidly advancing medical artificial intelligence, offering revolutionary changes in health care. These models excel in natural language processing (NLP), enhancing clinical support, diagnosis, treatment, and medical research. Breakthroughs, like GPT-4 and BERT (Bidirectional Encoder Representations from Transformer), demonstrate LLMs’ evolution through improved computing power and data. However, their high hardware requirements are being addressed through technological advancements. LLMs are unique in processing multimodal data, thereby improving emergency, elder care, and digital medical procedures. Challenges include ensuring their empirical reliability, addressing ethical and societal implications, especially data privacy, and mitigating biases while maintaining privacy and accountability. The paper emphasizes the need for human-centric, bias-free LLMs for personalized medicine and advocates for equitable development and access. LLMs hold promise for transformative impacts in health care.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Human-AI interaction visual explanation tools phenotype definition":

[begin paper 1]

PMCID = 10831521

Title = Developing, Purchasing, Implementing and Monitoring AI Tools in Radiology: Practical Considerations. A Multi-Society Statement from the ACR, CAR, ESR, RANZCR and RSNA

Artificial Intelligence (AI) carries the potential for unprecedented disruption in radiology, with possible positive and negative consequences. The integration of AI in radiology holds the potential to revolutionize healthcare practices by advancing diagnosis, quantification, and management of multiple medical conditions. Nevertheless, the ever-growing availability of AI tools in radiology highlights an increasing need to critically evaluate claims for its utility and to differentiate safe product offerings from potentially harmful, or fundamentally unhelpful ones. This multi-society paper, presenting the views of Radiology Societies in the USA, Canada, Europe, Australia, and New Zealand, defines the potential practical problems and ethical issues surrounding the incorporation of AI into radiological practice. In addition to delineating the main points of concern that developers, regulators, and purchasers of AI tools should consider prior to their introduction into clinical practice, this statement also suggests methods to monitor their stability and safety in clinical use, and their suitability for possible autonomous function. This statement is intended to serve as a useful summary of the practical issues which should be considered by all parties involved in the development of radiology AI resources, and their implementation as clinical tools.

 This article is simultaneously published in Insights into Imaging (DOI https://doi.org/10.1186/s13244-023-01541-3), Journal of Medical Imaging and Radiation Oncology (DOI https://doi.org/10.1111/1754-9485.13612), Canadian Association of Radiologists Journal (DOI https://doi.org/10.1177/08465371231222229), Journal of the American College of Radiology (DOI https://doi.org/10.1016/j.jacr.2023.12.005), and Radiology: Artificial Intelligence (DOI https://doi.org/10.1148/ryai.230513). 

Keywords: Artificial Intelligence, Radiology, Automation, Machine Learning

Published under a CC BY 4.0 license. ©The Author(s) 2024.

Editor’s Note: The RSNA Board of Directors has endorsed this article. It has not undergone review or editing by this journal.

[end paper 1]

[begin paper 2]

PMCID = 10800328

Title = Developing, purchasing, implementing and monitoring AI tools in radiology: practical considerations. A multi-society statement from the ACR, CAR, ESR, RANZCR & RSNA

Artificial Intelligence (AI) carries the potential for unprecedented disruption in radiology, with possible positive and negative consequences. The integration of AI in radiology holds the potential to revolutionize healthcare practices by advancing diagnosis, quantification, and management of multiple medical conditions. Nevertheless, the ever-growing availability of AI tools in radiology highlights an increasing need to critically evaluate claims for its utility and to differentiate safe product offerings from potentially harmful, or fundamentally unhelpful ones.

This multi-society paper, presenting the views of Radiology Societies in the USA, Canada, Europe, Australia, and New Zealand, defines the potential practical problems and ethical issues surrounding the incorporation of AI into radiological practice. In addition to delineating the main points of concern that developers, regulators, and purchasers of AI tools should consider prior to their introduction into clinical practice, this statement also suggests methods to monitor their stability and safety in clinical use, and their suitability for possible autonomous function. This statement is intended to serve as a useful summary of the practical issues which should be considered by all parties involved in the development of radiology AI resources, and their implementation as clinical tools.

Key points • The incorporation of artificial intelligence (AI) in radiological practice demands increased monitoring of its utility and safety.

• Cooperation between developers, clinicians, and regulators will allow all involved to address ethical issues and monitor AI performance.

• AI can fulfil its promise to advance patient well-being if all steps from development to integration in healthcare are rigorously evaluated.

[end paper 2]

[begin paper 3]

PMCID = 11908149

Title = Chemoarchitectural studies of the rat hypothalamus and zona incerta.Chemopleth 1.0 – A downloadable interactive Brain Maps spatial database of five co-visualizable neurochemical systems, with novel feature- and grid-based mapping tools

The hypothalamus and zona incerta of the brown rat (Rattus norvegicus), a model organism important for translational neuroscience research, contain diverse neuronal populations essential for survival, but how these populations are structurally organized as systems remains elusive. With the advent of novel gene-editing technologies, there has been a growing need for high-spatial-resolution maps of rat hypothalamic neurochemical cell types to aid in their functional interrogation by virus-directed cell type-specific gene manipulation or to validate their expression in transgenic lines. Here, we present a draft report describing Chemopleth 1.0, a chemoarchitecture database for the rat hypothalamus (HY) and zona incerta (ZI), which will eventually feature downloadable interactive maps featuring the census distributions of five immunoreactive neurochemical systems: (1) vasopressin (as detected using its gene co-product, copeptin); (2) neuronal nitric oxide synthase (EC 1.14.13.39); (3) hypocretin 1/orexin A; (4) melanin-concentrating hormone; and (5) alpha-melanocyte-stimulating hormone. These maps are formatted for the widely used Brain Maps 4.0 (BM4.0) open-access rat brain atlas. Importantly, this dataset retains atlas stereotaxic coordinates that facilitate the precise targeting of the cell bodies and/or axonal fibers of these neurochemical systems, thereby potentially serving to streamline delivery of viral vectors for gene-directed manipulations. The maps will be presented together with novel open-access tools to visualize the data, including a new Python programming language-based workflow to quantify cell positions and fiber densities for BM4.0. The workflow produces “heat maps” of neurochemical distributions from multiple subjects: 1) isopleth maps that represent consensus distributions independent of underlying atlas boundary conditions, and 2) choropleth maps that provide distribution differences based on cytoarchitectonic boundaries. These multi-subject cartographic representations are produced in Python from exported atlas maps first generated in the Adobe® Illustrator® vector graphics environment, which are then reimported and placed directly into the Brain Maps atlas. The soon-to-be-released files can also be opened using the free vector graphics editor, Inkscape. We also introduce a refined grid-based coordinate system for this dataset, register it with previously published spatial data for the HY and ZI, and introduce FMRS (Frequencies Mapped with Reference to Stereotaxy), as a new adaptation of long-used ephemeris systems for grid-based annotation of experimental observations. This database, which includes all data described in greater detail in and, provides critical spatial targeting information for these neurochemical systems unavailable from mRNA-based maps and allows readers to place their own datasets in register with them. It also provides a space for the continued buildout of a community-driven atlas-based spatial model of rat hypothalamic chemoarchitecture, allowing experimental observations from multiple laboratories to be registered to a common spatial framework.

[end paper 3]

[begin paper 4]

PMCID = 11782883

Title = Demystifying the black box: A survey on explainable artificial intelligence (XAI) in bioinformatics

The widespread adoption of Artificial Intelligence (AI) and machine learning (ML) tools across various domains has showcased their remarkable capabilities and performance. Black-box AI models raise concerns about decision transparency and user confidence. Therefore, explainable AI (XAI) and explainability techniques have rapidly emerged in recent years. This paper aims to review existing works on explainability techniques in bioinformatics, with a particular focus on omics and imaging. We seek to analyze the growing demand for XAI in bioinformatics, identify current XAI approaches, and highlight their limitations. Our survey emphasizes the specific needs of both bioinformatics applications and users when developing XAI methods and we particularly focus on omics and imaging data. Our analysis reveals a significant demand for XAI in bioinformatics, driven by the need for transparency and user confidence in decision-making processes. At the end of the survey, we provided practical guidelines for system developers.

[end paper 4]

[begin paper 5]

PMCID = 9581990

Title = Explainable medical imaging AI needs human-centered design: guidelines and evidence from a systematic review

Transparency in Machine Learning (ML), often also referred to as interpretability or explainability, attempts to reveal the working mechanisms of complex models. From a human-centered design perspective, transparency is not a property of the ML model but an affordance, i.e., a relationship between algorithm and users. Thus, prototyping and user evaluations are critical to attaining solutions that afford transparency. Following human-centered design principles in highly specialized and high stakes domains, such as medical image analysis, is challenging due to the limited access to end users and the knowledge imbalance between those users and ML designers. To investigate the state of transparent ML in medical image analysis, we conducted a systematic review of the literature from 2012 to 2021 in PubMed, EMBASE, and Compendex databases. We identified 2508 records and 68 articles met the inclusion criteria. Current techniques in transparent ML are dominated by computational feasibility and barely consider end users, e.g. clinical stakeholders. Despite the different roles and knowledge of ML developers and end users, no study reported formative user research to inform the design and development of transparent ML models. Only a few studies validated transparency claims through empirical user evaluations. These shortcomings put contemporary research on transparent ML at risk of being incomprehensible to users, and thus, clinically irrelevant. To alleviate these shortcomings in forthcoming research, we introduce the INTRPRT guideline, a design directive for transparent ML systems in medical image analysis. The INTRPRT guideline suggests human-centered design principles, recommending formative user research as the first step to understand user needs and domain requirements. Following these guidelines increases the likelihood that the algorithms afford transparency and enable stakeholders to capitalize on the benefits of transparent ML.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Human-AI interaction visual explanation tools clinical applications":

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

PMCID = 11586345

Title = Managing human-AI collaborations within Industry 5.0 scenarios via knowledge graphs: key challenges and lessons learned

In this paper, we discuss technologies and approaches based on Knowledge Graphs (KGs) that enable the management of inline human interventions in AI-assisted manufacturing processes in Industry 5.0 under potentially changing conditions in order to maintain or improve the overall system performance. Whereas KG-based systems are commonly based on a static view with their structure fixed at design time, we argue that the dynamic challenge of inline Human-AI (H-AI) collaboration in industrial settings calls for a late shaping design principle. In contrast to early shaping, which determines the system's behavior at design time in a fine granular manner, late shaping is a coarse-to-fine approach that leaves more space for fine-tuning, adaptation and integration of human intelligence at runtime. In this context we discuss approaches and lessons learned from the European manufacturing project Teaming.AI, https://www.teamingai-project.eu/, addressing general challenges like the modeling of domain expertise with particular focus on vertical knowledge integration, as well as challenges linked to an industrial KG of choice, such as its dynamic population and the late shaping of KG embeddings as the foundation of relational machine learning models which have emerged as an effective tool for exploiting graph-structured data to infer new insights.

[end paper 4]

[begin paper 5]

PMCID = 11301121

Title = Human-AI Teaming in Critical Care: A Comparative Analysis of Data Scientists’ and Clinicians’ Perspectives on AI Augmentation and Automation

Artificial intelligence (AI) holds immense potential for enhancing clinical and administrative health care tasks. However, slow adoption and implementation challenges highlight the need to consider how humans can effectively collaborate with AI within broader socio-technical systems in health care.

In the example of intensive care units (ICUs), we compare data scientists’ and clinicians’ assessments of the optimal utilization of human and AI capabilities by determining suitable levels of human-AI teaming for safely and meaningfully augmenting or automating 6 core tasks. The goal is to provide actionable recommendations for policy makers and health care practitioners regarding AI design and implementation.

In this multimethod study, we combine a systematic task analysis across 6 ICUs with an international Delphi survey involving 19 health data scientists from the industry and academia and 61 ICU clinicians (25 physicians and 36 nurses) to define and assess optimal levels of human-AI teaming (level 1=no performance benefits; level 2=AI augments human performance; level 3=humans augment AI performance; level 4=AI performs without human input). Stakeholder groups also considered ethical and social implications.

Both stakeholder groups chose level 2 and 3 human-AI teaming for 4 out of 6 core tasks in the ICU. For one task (monitoring), level 4 was the preferred design choice. For the task of patient interactions, both data scientists and clinicians agreed that AI should not be used regardless of technological feasibility due to the importance of the physician-patient and nurse-patient relationship and ethical concerns. Human-AI design choices rely on interpretability, predictability, and control over AI systems. If these conditions are not met and AI performs below human-level reliability, a reduction to level 1 or shifting accountability away from human end users is advised. If AI performs at or beyond human-level reliability and these conditions are not met, shifting to level 4 automation should be considered to ensure safe and efficient human-AI teaming.

By considering the sociotechnical system and determining appropriate levels of human-AI teaming, our study showcases the potential for improving the safety and effectiveness of AI usage in ICUs and broader health care settings. Regulatory measures should prioritize interpretability, predictability, and control if clinicians hold full accountability. Ethical and social implications must be carefully evaluated to ensure effective collaboration between humans and AI, particularly considering the most recent advancements in generative AI.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Human-AI interaction visual explanation tools clinician trust":

[begin paper 1]

PMCID = 11849858

Title = Safety of human-AI cooperative decision-making within intensive care: A physical simulation study

The safety of Artificial Intelligence (AI) systems is as much one of human decision-making as a technological question. In AI-driven decision support systems, particularly in high-stakes settings such as healthcare, ensuring the safety of human-AI interactions is paramount, given the potential risks of following erroneous AI recommendations. To explore this question, we ran a safety-focused clinician-AI interaction study in a physical simulation suite. Physicians were placed in a simulated intensive care ward, with a human nurse (played by an experimenter), an ICU data chart, a high-fidelity patient mannequin and an AI recommender system on a display. Clinicians were asked to prescribe two drugs for the simulated patients suffering from sepsis and wore eye-tracking glasses to allow us to assess where their gaze was directed. We recorded clinician treatment plans before and after they saw the AI treatment recommendations, which could be either ‘safe’ or ‘unsafe’. 92% of clinicians rejected unsafe AI recommendations vs 29% of safe ones. Physicians paid increased attention (+37% gaze fixations) to unsafe AI recommendations vs safe ones. However, visual attention on AI explanations was not greater in unsafe scenarios. Similarly, clinical information (patient monitor, patient chart) did not receive more attention after an unsafe versus safe AI reveal suggesting that the physicians did not look back to these sources of information to investigate why the AI suggestion might be unsafe. Physicians were only successfully persuaded to change their dose by scripted comments from the bedside nurse 5% of the time. Our study emphasises the importance of human oversight in safety-critical AI and the value of evaluating human-AI systems in high-fidelity settings that more closely resemble real world practice.

Artificial intelligence (AI) demonstrates increasingly promising results for supporting medical decision-making. However, most systems are evaluated outside of the clinical context within which they will be used, predominantly to avoid incurring risks for patients. When used at the bedside, these AI systems will be part of larger human-computer decision teams and little work evaluates the safety of this tandem as a whole. Here, we use a physical simulation suite and eye-tracking glasses to analyse the interaction between doctors and an AI support tool. Using the examplar of cardiovascular management in patients with sepsis, we report clinician behaviour when facing both (intentionally crafted) ‘safe’ and ‘unsafe’ recommendations from the AI system. We show that unsafe recommendations capture the attention of clinicians, increase the number of requests for a second opinion, and would be stopped over 90% of the time. However, unsafe AI recommendations did not draw more attention to accompanying explanations so the cognitive process behind the decision to reject them is not elucidated here. Working in a simulation suite also allowed us to study the potential human factor of decision safety: an experimenter playing the role of a nurse was able to convince 5% of clinicians to adopt an unsafe AI recommendation using pre-set challenge arguments. Combined with an objective measure of attention via eye-tracking, our approach allows us to capture and analyse human-AI interactions in safety-critical medical settings.

[end paper 1]

[begin paper 2]

PMCID = 10989254

Title = Human-artificial intelligence interaction in gastrointestinal endoscopy

The number and variety of applications of artificial intelligence (AI) in gastrointestinal (GI) endoscopy is growing rapidly. New technologies based on machine learning (ML) and convolutional neural networks (CNNs) are at various stages of development and deployment to assist patients and endoscopists in preparing for endoscopic procedures, in detection, diagnosis and classification of pathology during endoscopy and in confirmation of key performance indicators. Platforms based on ML and CNNs require regulatory approval as medical devices. Interactions between humans and the technologies we use are complex and are influenced by design, behavioural and psychological elements. Due to the substantial differences between AI and prior technologies, important differences may be expected in how we interact with advice from AI technologies. Human–AI interaction (HAII) may be optimised by developing AI algorithms to minimise false positives and designing platform interfaces to maximise usability. Human factors influencing HAII may include automation bias, alarm fatigue, algorithm aversion, learning effect and deskilling. Each of these areas merits further study in the specific setting of AI applications in GI endoscopy and professional societies should engage to ensure that sufficient emphasis is placed on human-centred design in development of new AI technologies.

[end paper 2]

[begin paper 3]

PMCID = 11041414

Title = The Impact of Expectation Management and Model Transparency on Radiologists’ Trust and Utilization of AI Recommendations for Lung Nodule Assessment on Computed Tomography: Simulated Use Study

Many promising artificial intelligence (AI) and computer-aided detection and diagnosis systems have been developed, but few have been successfully integrated into clinical practice. This is partially owing to a lack of user-centered design of AI-based computer-aided detection or diagnosis (AI-CAD) systems.

We aimed to assess the impact of different onboarding tutorials and levels of AI model explainability on radiologists’ trust in AI and the use of AI recommendations in lung nodule assessment on computed tomography (CT) scans.

In total, 20 radiologists from 7 Dutch medical centers performed lung nodule assessment on CT scans under different conditions in a simulated use study as part of a 2×2 repeated-measures quasi-experimental design. Two types of AI onboarding tutorials (reflective vs informative) and 2 levels of AI output (black box vs explainable) were designed. The radiologists first received an onboarding tutorial that was either informative or reflective. Subsequently, each radiologist assessed 7 CT scans, first without AI recommendations. AI recommendations were shown to the radiologist, and they could adjust their initial assessment. Half of the participants received the recommendations via black box AI output and half received explainable AI output. Mental model and psychological trust were measured before onboarding, after onboarding, and after assessing the 7 CT scans. We recorded whether radiologists changed their assessment on found nodules, malignancy prediction, and follow-up advice for each CT assessment. In addition, we analyzed whether radiologists’ trust in their assessments had changed based on the AI recommendations.

Both variations of onboarding tutorials resulted in a significantly improved mental model of the AI-CAD system (informative P=.01 and reflective P=.01). After using AI-CAD, psychological trust significantly decreased for the group with explainable AI output (P=.02). On the basis of the AI recommendations, radiologists changed the number of reported nodules in 27 of 140 assessments, malignancy prediction in 32 of 140 assessments, and follow-up advice in 12 of 140 assessments. The changes were mostly an increased number of reported nodules, a higher estimated probability of malignancy, and earlier follow-up. The radiologists’ confidence in their found nodules changed in 82 of 140 assessments, in their estimated probability of malignancy in 50 of 140 assessments, and in their follow-up advice in 28 of 140 assessments. These changes were predominantly increases in confidence. The number of changed assessments and radiologists’ confidence did not significantly differ between the groups that received different onboarding tutorials and AI outputs.

Onboarding tutorials help radiologists gain a better understanding of AI-CAD and facilitate the formation of a correct mental model. If AI explanations do not consistently substantiate the probability of malignancy across patient cases, radiologists’ trust in the AI-CAD system can be impaired. Radiologists’ confidence in their assessments was improved by using the AI recommendations.

[end paper 3]

[begin paper 4]

PMCID = 8832512

Title = Lessons Learned About Designing and Conducting Studies From HRI Experts

The field of human-robot interaction (HRI) research is multidisciplinary and requires researchers to understand diverse fields including computer science, engineering, informatics, philosophy, psychology, and more disciplines. However, it is hard to be an expert in everything. To help HRI researchers develop methodological skills, especially in areas that are relatively new to them, we conducted a virtual workshop, Workshop Your Study Design (WYSD), at the 2021 International Conference on HRI. In this workshop, we grouped participants with mentors, who are experts in areas like real-world studies, empirical lab studies, questionnaire design, interview, participatory design, and statistics. During and after the workshop, participants discussed their proposed study methods, obtained feedback, and improved their work accordingly. In this paper, we present 1) Workshop attendees’ feedback about the workshop and 2) Lessons that the participants learned during their discussions with mentors. Participants’ responses about the workshop were positive, and future scholars who wish to run such a workshop can consider implementing their suggestions. The main contribution of this paper is the lessons learned section, where the workshop participants contributed to forming this section based on what participants discovered during the workshop. We organize lessons learned into themes of 1) Improving study design for HRI, 2) How to work with participants - especially children -, 3) Making the most of the study and robot’s limitations, and 4) How to collaborate well across fields as they were the areas of the papers submitted to the workshop. These themes include practical tips and guidelines to assist researchers to learn about fields of HRI research with which they have limited experience. We include specific examples, and researchers can adapt the tips and guidelines to their own areas to avoid some common mistakes and pitfalls in their research.

[end paper 4]

[begin paper 5]

PMCID = 10831521

Title = Developing, Purchasing, Implementing and Monitoring AI Tools in Radiology: Practical Considerations. A Multi-Society Statement from the ACR, CAR, ESR, RANZCR and RSNA

Artificial Intelligence (AI) carries the potential for unprecedented disruption in radiology, with possible positive and negative consequences. The integration of AI in radiology holds the potential to revolutionize healthcare practices by advancing diagnosis, quantification, and management of multiple medical conditions. Nevertheless, the ever-growing availability of AI tools in radiology highlights an increasing need to critically evaluate claims for its utility and to differentiate safe product offerings from potentially harmful, or fundamentally unhelpful ones. This multi-society paper, presenting the views of Radiology Societies in the USA, Canada, Europe, Australia, and New Zealand, defines the potential practical problems and ethical issues surrounding the incorporation of AI into radiological practice. In addition to delineating the main points of concern that developers, regulators, and purchasers of AI tools should consider prior to their introduction into clinical practice, this statement also suggests methods to monitor their stability and safety in clinical use, and their suitability for possible autonomous function. This statement is intended to serve as a useful summary of the practical issues which should be considered by all parties involved in the development of radiology AI resources, and their implementation as clinical tools.

 This article is simultaneously published in Insights into Imaging (DOI https://doi.org/10.1186/s13244-023-01541-3), Journal of Medical Imaging and Radiation Oncology (DOI https://doi.org/10.1111/1754-9485.13612), Canadian Association of Radiologists Journal (DOI https://doi.org/10.1177/08465371231222229), Journal of the American College of Radiology (DOI https://doi.org/10.1016/j.jacr.2023.12.005), and Radiology: Artificial Intelligence (DOI https://doi.org/10.1148/ryai.230513). 

Keywords: Artificial Intelligence, Radiology, Automation, Machine Learning

Published under a CC BY 4.0 license. ©The Author(s) 2024.

Editor’s Note: The RSNA Board of Directors has endorsed this article. It has not undergone review or editing by this journal.

[end paper 5]



