## User

This is the beginning of an individual meeting with Data Visualization Expert to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Visual analytics for clinical decision support in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Visual analytics for clinical decision support to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Visual analytics for clinical decision support. Include both general queries about Visual analytics for clinical decision support and queries that specifically relate Visual analytics for clinical decision support to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Data Visualization Expert, please provide your response to the agenda.

## Data Visualization Expert

To address the agenda and help in developing a tool for LLM interpretability in electronic phenotype definitions, I'll start by crafting a series of search queries to find relevant scientific papers. These queries will focus on visual analytics for clinical decision support, LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
queries = [
    "Visual analytics for clinical decision support",
    "LLM interpretability in clinical decision support",
    "Electronic phenotype definition and visual analytics",
    "Clinician trust in AI-driven clinical decision support",
    "SNOMED CT integration in visual analytics for clinical applications"
]
```

Next, I'll use these queries to search for relevant scientific papers. Let's proceed with the search to gather the PMCIDs and titles of the papers.

## Data Visualization Expert

Here are the PMCIDs and titles of the papers I found relevant to the research project on visual analytics for clinical decision support, focusing on LLM interpretability, phenotype definition, clinical applications, and clinician trust:

```python
papers = {
    "9377614": "Towards effective clinical decision support systems: A systematic review",
    "10620641": "Using Theories, Models, and Frameworks to Inform Implementation Cycles of Computerized Clinical Decision Support Systems in Tertiary Health Care Settings: Scoping Review",
    "7072392": "Clinical Decision Support Systems in Breast Cancer: A Systematic Review",
    "11993431": "Advancing Obstetric Care Through Artificial Intelligence-Enhanced Clinical Decision Support Systems: A Systematic Review",
    "6444220": "A Human(e) Factor in Clinical Decision Support Systems",
    "11245653": "Resilient Artificial Intelligence in Health: Synthesis and Research Agenda Toward Next-Generation Trustworthy Clinical Decision Support",
    "11762383": "Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules",
    "11923455": "Retrieval Augmented Therapy Suggestion for Molecular Tumor Boards: Algorithmic Development and Validation Study",
    "11960180": "Utilizing large language models for gastroenterology research: a conceptual framework",
    "7350392": "Guidelines for the use of flow cytometry and cell sorting in immunological studies (second edition)",
    "9256599": "Virtual reality for the observation of oncology models (VROOM): immersive analytics for oncology patient cohorts",
    "4919856": "Making sense of big data in health research: Towards an EU action plan",
    "11737733": "CohortDiagnostics: Phenotype evaluation across a network of observational data sources using population-level characterization",
    "11073764": "AI-Driven Clinical Decision Support Systems: An Ongoing Pursuit of Potential",
    "10685930": "Harnessing the power of clinical decision support systems: challenges and opportunities",
    "11618115": "Scoping review of clinical decision support systems for multiple sclerosis management: Leveraging information technology and massive health data",
    "8785388": "Diffused responsibility: attributions of responsibility in the use of AI-driven clinical decision support systems",
    "10454426": "Clinicians’ Perceptions of Artificial Intelligence: Focus on Workload, Risk, Trust, Clinical Decision Making, and Clinical Integration",
    "8415558": "A Fine-Tuned Bidirectional Encoder Representations From Transformers Model for Food Named-Entity Recognition: Algorithm Development and Validation",
    "6849172": "Exploring semantic deep learning for building reliable and reusable one health knowledge from PubMed systematic reviews and veterinary clinical notes",
    "10495848": "Initiatives, Concepts, and Implementation Practices of the Findable, Accessible, Interoperable, and Reusable Data Principles in Health Data Stewardship: Scoping Review",
    "9135051": "Surgical data science – from concepts toward clinical translation",
    "9455941": "Pathling: analytics on FHIR"
}
```

These papers cover a range of topics relevant to your research, including clinical decision support systems, LLM interpretability, phenotype definition, and clinician trust in AI-driven systems. They should provide a solid foundation for understanding the current landscape and challenges in developing a transparent, clinically grounded, and visually intuitive interpretability tool.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Visual analytics for clinical decision support":

[begin paper 1]

PMCID = 9377614

Title = Towards effective clinical decision support systems: A systematic review

Clinical Decision Support Systems (CDSS) are used to assist the decision-making process in the healthcare field. Developing an effective CDSS is an arduous task that can take advantage from prior assessment of the most promising theories, techniques and methods used at the present time.

To identify the features of Clinical Decision Support Systems and provide an analysis of their effectiveness. Thus, two research questions were formulated: RQ1—What are the most common trend characteristics in a CDSS? RQ2—What is the maturity level of the CDSS based on the decision-making theory proposed by Simon?

AIS e-library, Decision Support Systems journal, Nature, PlosOne and PubMed were selected as information sources to conduct this systematic literature review. Studies from 2000 to 2020 were chosen covering search terms in CDSS, selected according to defined eligibility criteria. The data were extracted and managed in a worksheet, based on the defined criteria. PRISMA statements were used to report the systematic review.

The outcomes showed that rule-based module was the most used approach regarding knowledge management and representation. The most common technological feature adopted by the CDSS were the recommendations and suggestions. 19,23% of studies adopt the type of system as a web-based application, and 51,92% are standalone CDSS. Temporal evolution was also possible to visualize. This study contributed to the development of a Maturity Staging Model, where it was possible to verify that most CDSS do not exceed level 2 of maturity.

The trend characteristics addressed in the revised CDSS were identified, compared to the four predefined groups. A maturity stage model was developed based on Simon’s decision-making theory, allowing to assess the level of maturity of the most common features of the CDSS. With the application of the model, it was noticed that the phases of choice and implementation are underrepresented. This constitutes the main gap in the development of an effective CDSS.

[end paper 1]

[begin paper 2]

PMCID = 10620641

Title = Using Theories, Models, and Frameworks to Inform Implementation Cycles of Computerized Clinical Decision Support Systems in Tertiary Health Care Settings: Scoping Review

Computerized clinical decision support systems (CDSSs) are essential components of modern health system service delivery, particularly within acute care settings such as hospitals. Theories, models, and frameworks may assist in facilitating the implementation processes associated with CDSS innovation and its use within these care settings. These processes include context assessments to identify key determinants, implementation plans for adoption, promoting ongoing uptake, adherence, and long-term evaluation. However, there has been no prior review synthesizing the literature regarding the theories, models, and frameworks that have informed the implementation and adoption of CDSSs within hospitals.

This scoping review aims to identify the theory, model, and framework approaches that have been used to facilitate the implementation and adoption of CDSSs in tertiary health care settings, including hospitals. The rationales reported for selecting these approaches, including the limitations and strengths, are described.

A total of 5 electronic databases were searched (CINAHL via EBSCOhost, PubMed, Scopus, PsycINFO, and Embase) to identify studies that implemented or adopted a CDSS in a tertiary health care setting using an implementation theory, model, or framework. No date or language limits were applied. A narrative synthesis was conducted using full-text publications and abstracts. Implementation phases were classified according to the “Active Implementation Framework stages”: exploration (feasibility and organizational readiness), installation (organizational preparation), initial implementation (initiating implementation, ie, training), full implementation (sustainment), and nontranslational effectiveness studies.

A total of 81 records (42 full text and 39 abstracts) were included. Full-text studies and abstracts are reported separately. For full-text studies, models (18/42, 43%), followed by determinants frameworks (14/42,33%), were most frequently used to guide adoption and evaluation strategies. Most studies (36/42, 86%) did not list the limitations associated with applying a specific theory, model, or framework.

Models and related quality improvement methods were most frequently used to inform CDSS adoption. Models were not typically combined with each other or with theory to inform full-cycle implementation strategies. The findings highlight a gap in the application of implementation methods including theories, models, and frameworks to facilitate full-cycle implementation strategies for hospital CDSSs.

[end paper 2]

[begin paper 3]

PMCID = 7072392

Title = Clinical Decision Support Systems in Breast Cancer: A Systematic Review

Breast cancer is the most frequently diagnosed cancer in women, with more than 2.1 million new diagnoses worldwide every year. Personalised treatment is critical to optimising outcomes for patients with breast cancer. A major advance in medical practice is the incorporation of Clinical Decision Support Systems (CDSSs) to assist and support healthcare staff in clinical decision-making, thus improving the quality of decisions and overall patient care whilst minimising costs. The usage and availability of CDSSs in breast cancer care in healthcare settings is increasing. However, there may be differences in how particular CDSSs are developed, the information they include, the decisions they recommend, and how they are used in practice. This systematic review examines various CDSSs to determine their availability, intended use, medical characteristics, and expected outputs concerning breast cancer therapeutic decisions, an area that is known to have varying degrees of subjectivity in clinical practice. Utilising the methodology of Kitchenham and Charter, a systematic search of the literature was performed in Springer, Science Direct, Google Scholar, PubMed, ACM, IEEE, and Scopus. An overview of CDSS which supports decision-making in breast cancer treatment is provided along with a critical appraisal of their benefits, limitations, and opportunities for improvement.

[end paper 3]

[begin paper 4]

PMCID = 11993431

Title = Advancing Obstetric Care Through Artificial Intelligence-Enhanced Clinical Decision Support Systems: A Systematic Review

Although artificial intelligence (AI) has grown over the past 10 years and clinical decision support systems (CDSS) have begun to be used in obstetric care, little is known about how AI functions in obstetric care-specific CDSS. We conducted a systematic review based on research studies that looked at AI-augmented CDSS in obstetric care to identify and synthesize CDSS functionality, AI techniques, clinical implementation, and AI-augmented CDSS in obstetric care. We searched four different databases (Scopus, PubMed, Web of Science, and IEEE Xplore) for relevant studies, and we found 354 studies. The studies were evaluated for eligibility based on predefined inclusion and exclusion criteria. The systematic review incorporated 30 studies after conducting an eligibility assessment of all studies. We used the Newcastle Ottawa Scale for risk bias assessment of all included studies. Medical prediction, therapeutic recommendations, diagnostic support, and knowledge dissemination constitute the key features of CDSS service offerings. The current research on CDSS included findings about early fetal anomaly detection, economical surveillance, prenatal ultrasonography assistance, and ontology development methodologies according to our study findings.

[end paper 4]

[begin paper 5]

PMCID = 6444220

Title = A Human(e) Factor in Clinical Decision Support Systems

The overwhelming amount, production speed, multidimensionality, and potential value of data currently available—often simplified and referred to as big data —exceed the limits of understanding of the human brain. At the same time, developments in data analytics and computational power provide the opportunity to obtain new insights and transfer data-provided added value to clinical practice in real time. What is the role of the health care professional in collaboration with the data scientist in the changing landscape of modern care? We discuss how health care professionals should provide expert knowledge in each of the stages of clinical decision support design: data level, algorithm level, and decision support level. Including various ethical considerations, we advocate for health care professionals to responsibly initiate and guide interprofessional teams, including patients, and embrace novel analytic technologies to translate big data into patient benefit driven by human(e) values.

[end paper 5]



Here are the top 4 articles on PubMed Central for the query "LLM interpretability in clinical decision support":

[begin paper 1]

PMCID = 11245653

Title = Resilient Artificial Intelligence in Health: Synthesis and Research Agenda Toward Next-Generation Trustworthy Clinical Decision Support

Artificial intelligence (AI)–based clinical decision support systems are gaining momentum by relying on a greater volume and variety of secondary use data. However, the uncertainty, variability, and biases in real-world data environments still pose significant challenges to the development of health AI, its routine clinical use, and its regulatory frameworks. Health AI should be resilient against real-world environments throughout its lifecycle, including the training and prediction phases and maintenance during production, and health AI regulations should evolve accordingly. Data quality issues, variability over time or across sites, information uncertainty, human-computer interaction, and fundamental rights assurance are among the most relevant challenges. If health AI is not designed resiliently with regard to these real-world data effects, potentially biased data-driven medical decisions can risk the safety and fundamental rights of millions of people. In this viewpoint, we review the challenges, requirements, and methods for resilient AI in health and provide a research framework to improve the trustworthiness of next-generation AI-based clinical decision support.

[end paper 1]

[begin paper 2]

PMCID = 11762383

Title = Using Large Language Models to Retrieve Critical Data from Clinical Processes and Business Rules

Current clinical care relies heavily on complex, rule-based systems for tasks like diagnosis and treatment. However, these systems can be cumbersome and require constant updates. This study explores the potential of the large language model (LLM), LLaMA 2, to address these limitations. We tested LLaMA 2′s performance in interpreting complex clinical process models, such as Mayo Clinic Care Pathway Models (CPMs), and providing accurate clinical recommendations. LLM was trained on encoded pathways versions using DOT language, embedding them with SentenceTransformer, and then presented with hypothetical patient cases. We compared the token-level accuracy between LLM output and the ground truth by measuring both node and edge accuracy. LLaMA 2 accurately retrieved the diagnosis, suggested further evaluation, and delivered appropriate management steps, all based on the pathways. The average node accuracy across the different pathways was 0.91 (SD ± 0.045), while the average edge accuracy was 0.92 (SD ± 0.122). This study highlights the potential of LLMs for healthcare information retrieval, especially when relevant data are provided. Future research should focus on improving these models’ interpretability and their integration into existing clinical workflows.

[end paper 2]

[begin paper 3]

PMCID = 11923455

Title = Retrieval Augmented Therapy Suggestion for Molecular Tumor Boards: Algorithmic Development and Validation Study

Molecular tumor boards (MTBs) require intensive manual investigation to generate optimal treatment recommendations for patients. Large language models (LLMs) can catalyze MTB recommendations, decrease human error, improve accessibility to care, and enhance the efficiency of precision oncology.

In this study, we aimed to investigate the efficacy of LLM-generated treatments for MTB patients. We specifically investigate the LLMs’ ability to generate evidence-based treatment recommendations using PubMed references.

We built a retrieval augmented generation pipeline using PubMed data. We prompted the resulting LLM to generate treatment recommendations with PubMed references using a test set of patients from an MTB conference at a large comprehensive cancer center at a tertiary care institution. Members of the MTB manually assessed the relevancy and correctness of the generated responses.

A total of 75% of the referenced articles were properly cited from PubMed, while 17% of the referenced articles were hallucinations, and the remaining were not properly cited from PubMed. Clinician-generated LLM queries achieved higher accuracy through clinician evaluation than automated queries, with clinicians labeling 25% of LLM responses as equal to their recommendations and 37.5% as alternative plausible treatments.

This study demonstrates how retrieval augmented generation–enhanced LLMs can be a powerful tool in accelerating MTB conferences, as LLMs are sometimes capable of achieving clinician-equal treatment recommendations. However, further investigation is required to achieve stable results with zero hallucinations. LLMs signify a scalable solution to the time-intensive process of MTB investigations. However, LLM performance demonstrates that they must be used with heavy clinician supervision, and cannot yet fully automate the MTB pipeline.

[end paper 3]

[begin paper 4]

PMCID = 11960180

Title = Utilizing large language models for gastroenterology research: a conceptual framework

Large language models (LLMs) transform healthcare by assisting clinicians with decision-making, research, and patient management. In gastroenterology, LLMs have shown potential in clinical decision support, data extraction, and patient education. However, challenges such as bias, hallucinations, integration with clinical workflows, and regulatory compliance must be addressed for safe and effective implementation. This manuscript presents a structured framework for integrating LLMs into gastroenterology, using Hepatitis C treatment as a real-world application. The framework outlines key steps to ensure accuracy, safety, and clinical relevance while mitigating risks associated with artificial intelligence (AI)-driven healthcare tools. The framework includes defining clinical goals, assembling a multidisciplinary team, data collection and preparation, model selection, fine-tuning, calibration, hallucination mitigation, user interface development, integration with electronic health records, real-world validation, and continuous improvement. Retrieval-augmented generation and fine-tuning approaches are evaluated for optimizing model adaptability. Bias detection, reinforcement learning from human feedback, and structured prompt engineering are incorporated to enhance reliability. Ethical and regulatory considerations, including the Health Insurance Portability and Accountability Act, General Data Protection Regulation, and AI-specific guidelines (DECIDE-AI, SPIRIT-AI, CONSORT-AI), are addressed to ensure responsible AI deployment. LLMs have the potential to enhance decision-making, research efficiency, and patient care in gastroenterology, but responsible deployment requires bias mitigation, transparency, and ongoing validation. Future research should focus on multi-institutional validation and AI-assisted clinical trials to establish LLMs as reliable tools in gastroenterology.

 How large language models could transform gastroenterology: a framework for future research and care 

Artificial intelligence (AI) is transforming healthcare by helping doctors make better decisions, analyze research faster, and improve patient care. Large language models (LLMs) are a type of AI that process and generate human-like text, making them useful in gastroenterology. This paper presents a structured framework for safely using LLMs in clinical practice, using Hepatitis C treatment as an example. The framework begins by setting clear goals, such as improving Hepatitis C treatment recommendations or making patient education easier to understand. A team of doctors, AI specialists, and data experts is assembled to ensure the model is medically accurate and practical. Next, relevant medical data from electronic health records (EHRs), clinical guidelines, and research studies is gathered and prepared to improve AI, ensuring it provides useful and fair recommendations. The right AI model is then chosen and improved to specialize in gastroenterology. To make sure the model is reliable and makes correct suggestions, its performance is checked and adjusted before use. A user-friendly interface is created so doctors can access AI-generated recommendations directly in EHRs and decision-support tools, making it easy to integrate into daily practice. Before full use, the AI is tested in real-world settings, where gastroenterologists review its recommendations for safety and accuracy. Once in use, ongoing updates based on doctor feedback help improve its performance. Ethical and legal safeguards, such as protecting patient privacy and ensuring fairness, guide its responsible use. Findings are then shared with the medical community, allowing for further testing and broader adoption. By following this framework, LLMs can help doctors make better decisions, personalize treatments, and improve efficiency, ultimately leading to better patient outcomes in gastroenterology.

[end paper 4]



Here are the top 5 articles on PubMed Central for the query "Electronic phenotype definition and visual analytics":

[begin paper 1]

PMCID = 7350392

Title = Guidelines for the use of flow cytometry and cell sorting in immunological studies (second edition)

These guidelines are a consensus work of a considerable number of members of the immunology and flow cytometry community. They provide the theory and key practical aspects of flow cytometry enabling immunologists to avoid the common errors that often undermine immunological data. Notably, there are comprehensive sections of all major immune cell types with helpful Tables detailing phenotypes in murine and human cells. The latest flow cytometry techniques and applications are also described, featuring examples of the data that can be generated and, importantly, how the data can be analysed. Furthermore, there are sections detailing tips, tricks and pitfalls to avoid, all written and peer-reviewed by leading experts in the field, making this an essential research companion.

[end paper 1]

[begin paper 2]

PMCID = 9256599

Title = Virtual reality for the observation of oncology models (VROOM): immersive analytics for oncology patient cohorts

The significant advancement of inexpensive and portable virtual reality (VR) and augmented reality devices has re-energised the research in the immersive analytics field. The immersive environment is different from a traditional 2D display used to analyse 3D data as it provides a unified environment that supports immersion in a 3D scene, gestural interaction, haptic feedback and spatial audio. Genomic data analysis has been used in oncology to understand better the relationship between genetic profile, cancer type, and treatment option. This paper proposes a novel immersive analytics tool for cancer patient cohorts in a virtual reality environment, virtual reality to observe oncology data models. We utilise immersive technologies to analyse the gene expression and clinical data of a cohort of cancer patients. Various machine learning algorithms and visualisation methods have also been deployed in VR to enhance the data interrogation process. This is supported with established 2D visual analytics and graphical methods in bioinformatics, such as scatter plots, descriptive statistical information, linear regression, box plot and heatmap into our visualisation. Our approach allows the clinician to interrogate the information that is familiar and meaningful to them while providing them immersive analytics capabilities to make new discoveries toward personalised medicine.

[end paper 2]

[begin paper 3]

PMCID = 9165548

Title = Guidelines for the use of flow cytometry and cell sorting in immunological studies



[end paper 3]

[begin paper 4]

PMCID = 4919856

Title = Making sense of big data in health research: Towards an EU action plan

Medicine and healthcare are undergoing profound changes. Whole-genome sequencing and high-resolution imaging technologies are key drivers of this rapid and crucial transformation. Technological innovation combined with automation and miniaturization has triggered an explosion in data production that will soon reach exabyte proportions. How are we going to deal with this exponential increase in data production? The potential of “big data” for improving health is enormous but, at the same time, we face a wide range of challenges to overcome urgently. Europe is very proud of its cultural diversity; however, exploitation of the data made available through advances in genomic medicine, imaging, and a wide range of mobile health applications or connected devices is hampered by numerous historical, technical, legal, and political barriers. European health systems and databases are diverse and fragmented. There is a lack of harmonization of data formats, processing, analysis, and data transfer, which leads to incompatibilities and lost opportunities. Legal frameworks for data sharing are evolving. Clinicians, researchers, and citizens need improved methods, tools, and training to generate, analyze, and query data effectively. Addressing these barriers will contribute to creating the European Single Market for health, which will improve health and healthcare for all Europeans.

[end paper 4]

[begin paper 5]

PMCID = 11737733

Title = CohortDiagnostics: Phenotype evaluation across a network of observational data sources using population-level characterization

This paper introduces a novel framework for evaluating phenotype algorithms (PAs) using the open-source tool, Cohort Diagnostics.

The method is based on several diagnostic criteria to evaluate a patient cohort returned by a PA. Diagnostics include estimates of incidence rate, index date entry code breakdown, and prevalence of all observed clinical events prior to, on, and after index date. We test our framework by evaluating one PA for systemic lupus erythematosus (SLE) and two PAs for Alzheimer’s disease (AD) across 10 different observational data sources.

By utilizing CohortDiagnostics, we found that the population-level characteristics of individuals in the cohort of SLE closely matched the disease’s anticipated clinical profile. Specifically, the incidence rate of SLE was consistently higher in occurrence among females. Moreover, expected clinical events like laboratory tests, treatments, and repeated diagnoses were also observed. For AD, although one PA identified considerably fewer patients, absence of notable differences in clinical characteristics between the two cohorts suggested similar specificity.

We provide a practical and data-driven approach to evaluate PAs, using two clinical diseases as examples, across a network of OMOP data sources. Cohort Diagnostics can ensure the subjects identified by a specific PA align with those intended for inclusion in a research study.

Diagnostics based on large-scale population-level characterization can offer insights into the misclassification errors of PAs.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Clinician trust in AI-driven clinical decision support":

[begin paper 1]

PMCID = 11073764

Title = AI-Driven Clinical Decision Support Systems: An Ongoing Pursuit of Potential

Clinical Decision Support Systems (CDSS) are essential tools in contemporary healthcare, enhancing clinicians' decisions and patient outcomes. The integration of artificial intelligence (AI) is now revolutionizing CDSS even further. This review delves into AI technologies transforming CDSS, their applications in healthcare decision-making, associated challenges, and the potential trajectory toward fully realizing AI-CDSS's potential. The review begins by laying the groundwork with a definition of CDSS and its function within the healthcare field. It then highlights the increasingly significant role that AI is playing in enhancing CDSS effectiveness and efficiency, underlining its evolving prominence in shaping healthcare practices. It examines the integration of AI technologies into CDSS, including machine learning algorithms like neural networks and decision trees, natural language processing, and deep learning. It also addresses the challenges associated with AI integration, such as interpretability and bias. We then shift to AI applications within CDSS, with real-life examples of AI-driven diagnostics, personalized treatment recommendations, risk prediction, early intervention, and AI-assisted clinical documentation. The review emphasizes user-centered design in AI-CDSS integration, addressing usability, trust, workflow, and ethical and legal considerations. It acknowledges prevailing obstacles and suggests strategies for successful AI-CDSS adoption, highlighting the need for workflow alignment and interdisciplinary collaboration. The review concludes by summarizing key findings, underscoring AI's transformative potential in CDSS, and advocating for continued research and innovation. It emphasizes the need for collaborative efforts to realize a future where AI-powered CDSS optimizes healthcare delivery and improves patient outcomes.

[end paper 1]

[begin paper 2]

PMCID = 10685930

Title = Harnessing the power of clinical decision support systems: challenges and opportunities

Clinical decision support systems (CDSSs) are increasingly integrated into healthcare settings to improve patient outcomes, reduce medical errors and enhance clinical efficiency by providing clinicians with evidence-based recommendations at the point of care. However, the adoption and optimisation of these systems remain a challenge. This review aims to provide an overview of the current state of CDSS, discussing their development, implementation, benefits, limitations and future directions. We also explore the potential for enhancing their effectiveness and provide an outlook for future developments in this field. There are several challenges in CDSS implementation, including data privacy concerns, system integration and clinician acceptance. While CDSS have demonstrated significant potential, their adoption and optimisation remain a challenge.

[end paper 2]

[begin paper 3]

PMCID = 11618115

Title = Scoping review of clinical decision support systems for multiple sclerosis management: Leveraging information technology and massive health data

Multiple sclerosis (MS) is a complex autoimmune disease of the central nervous system, with numerous therapeutic options, but a lack of biomarkers to support a mechanistic approach to precision medicine. A computational approach to precision medicine could proceed from clinical decision support systems (CDSSs). They are digital tools aiming to empower physicians through the clinical applications of information technology and massive data. However, the process of their clinical development is still maturing; we aimed to review it in the field of MS.

For this scoping review, we screened systematically the PubMed database. We identified 24 articles reporting 14 CDSS projects and compared their technical and software development aspects.

The projects position themselves in various contexts of usage with various algorithmic approaches: expert systems, CDSSs based on similar patients' data visualization, and model‐based CDSSs implementing mathematical predictive models. So far, no project has completed its clinical development up to certification for clinical use with global release. Some CDSSs have been replaced at subsequent project iterations. The most advanced projects did not necessarily report every step of clinical development in a dedicated article (proof of concept, offline validation, refined prototype, live clinical evaluation, comparative prospective evaluation). They seek different software distribution options to integrate into health care: internal usage, “peer‐to‐peer,” and marketing distribution.

This review illustrates the potential of clinical applications of information technology and massive data to support MS management and helps clarify the roadmap for future projects as a multidisciplinary and multistep process.

[end paper 3]

[begin paper 4]

PMCID = 8785388

Title = Diffused responsibility: attributions of responsibility in the use of AI-driven clinical decision support systems

Good decision-making is a complex endeavor, and particularly so in a health context. The possibilities for day-to-day clinical practice opened up by AI-driven clinical decision support systems (AI-CDSS) give rise to fundamental questions around responsibility. In causal, moral and legal terms the application of AI-CDSS is challenging existing attributions of responsibility. In this context, responsibility gaps are often identified as main problem. Mapping out the changing dynamics and levels of attributing responsibility, we argue in this article that the application of AI-CDSS causes diffusions of responsibility with respect to a causal, moral, and legal dimension. Responsibility diffusion describes the situation where multiple options and several agents can be considered for attributing responsibility. Using the example of an AI-driven ‘digital tumor board’, we illustrate how clinical decision-making is changed and diffusions of responsibility take place. Not denying or attempting to bridge responsibility gaps, we argue that dynamics and ambivalences are inherent in responsibility, which is based on normative considerations such as avoiding experiences of disregard and vulnerability of human life, which are inherently accompanied by a moment of uncertainty, and is characterized by revision openness. Against this background and to avoid responsibility gaps, the article concludes with suggestions for managing responsibility diffusions in clinical decision-making with AI-CDSS.

[end paper 4]

[begin paper 5]

PMCID = 10454426

Title = Clinicians’ Perceptions of Artificial Intelligence: Focus on Workload, Risk, Trust, Clinical Decision Making, and Clinical Integration

Artificial intelligence (AI) offers the potential to revolutionize healthcare, from improving diagnoses to patient safety. However, many healthcare practitioners are hesitant to adopt AI technologies fully. To understand why, this research explored clinicians’ views on AI, especially their level of trust, their concerns about potential risks, and how they believe AI might affect their day-to-day workload. We surveyed 265 healthcare professionals from various specialties in the U.S. The survey aimed to understand their perceptions and any concerns they might have about AI in their clinical practice. We further examined how these perceptions might align with three hypothetical approaches to integrating AI into healthcare: no integration, sequential (step-by-step) integration, and parallel (side-by-side with current practices) integration. The results reveal that clinicians who view AI as a workload reducer are more inclined to trust it and are more likely to use it in clinical decision making. However, those perceiving higher risks with AI are less inclined to adopt it in decision making. While the role of clinical experience was found to be statistically insignificant in influencing trust in AI and AI-driven decision making, further research might explore other potential moderating variables, such as technical aptitude, previous exposure to AI, or the specific medical specialty of the clinician. By evaluating three hypothetical scenarios of AI integration in healthcare, our study elucidates the potential pitfalls of sequential AI integration and the comparative advantages of parallel integration. In conclusion, this study underscores the necessity of strategic AI integration into healthcare. AI should be perceived as a supportive tool rather than an intrusive entity, augmenting the clinicians’ skills and facilitating their workflow rather than disrupting it. As we move towards an increasingly digitized future in healthcare, comprehending the among AI technology, clinician perception, trust, and decision making is fundamental. 

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "SNOMED CT integration in visual analytics for clinical applications":

[begin paper 1]

PMCID = 8415558

Title = A Fine-Tuned Bidirectional Encoder Representations From Transformers Model for Food Named-Entity Recognition: Algorithm Development and Validation

Recently, food science has been garnering a lot of attention. There are many open research questions on food interactions, as one of the main environmental factors, with other health-related entities such as diseases, treatments, and drugs. In the last 2 decades, a large amount of work has been done in natural language processing and machine learning to enable biomedical information extraction. However, machine learning in food science domains remains inadequately resourced, which brings to attention the problem of developing methods for food information extraction. There are only few food semantic resources and few rule-based methods for food information extraction, which often depend on some external resources. However, an annotated corpus with food entities along with their normalization was published in 2019 by using several food semantic resources.

In this study, we investigated how the recently published bidirectional encoder representations from transformers (BERT) model, which provides state-of-the-art results in information extraction, can be fine-tuned for food information extraction.

We introduce FoodNER, which is a collection of corpus-based food named-entity recognition methods. It consists of 15 different models obtained by fine-tuning 3 pretrained BERT models on 5 groups of semantic resources: food versus nonfood entity, 2 subsets of Hansard food semantic tags, FoodOn semantic tags, and Systematized Nomenclature of Medicine Clinical Terms food semantic tags.

All BERT models provided very promising results with 93.30% to 94.31% macro F1 scores in the task of distinguishing food versus nonfood entity, which represents the new state-of-the-art technology in food information extraction. Considering the tasks where semantic tags are predicted, all BERT models obtained very promising results once again, with their macro F1 scores ranging from 73.39% to 78.96%.

FoodNER can be used to extract and annotate food entities in 5 different tasks: food versus nonfood entities and distinguishing food entities on the level of food groups by using the closest Hansard semantic tags, the parent Hansard semantic tags, the FoodOn semantic tags, or the Systematized Nomenclature of Medicine Clinical Terms semantic tags.

[end paper 1]

[begin paper 2]

PMCID = 6849172

Title = Exploring semantic deep learning for building reliable and reusable one health knowledge from PubMed systematic reviews and veterinary clinical notes

Deep Learning opens up opportunities for routinely scanning large bodies of biomedical literature and clinical narratives to represent the meaning of biomedical and clinical terms. However, the validation and integration of this knowledge on a scale requires cross checking with ground truths (i.e. evidence-based resources) that are unavailable in an actionable or computable form. In this paper we explore how to turn information about diagnoses, prognoses, therapies and other clinical concepts into computable knowledge using free-text data about human and animal health. We used a Semantic Deep Learning approach that combines the Semantic Web technologies and Deep Learning to acquire and validate knowledge about 11 well-known medical conditions mined from two sets of unstructured free-text data: 300 K PubMed Systematic Review articles (the PMSB dataset) and 2.5 M veterinary clinical notes (the VetCN dataset). For each target condition we obtained 20 related clinical concepts using two deep learning methods applied separately on the two datasets, resulting in 880 term pairs (target term, candidate term). Each concept, represented by an n-gram, is mapped to UMLS using MetaMap; we also developed a bespoke method for mapping short forms (e.g. abbreviations and acronyms). Existing ontologies were used to formally represent associations. We also create ontological modules and illustrate how the extracted knowledge can be queried. The evaluation was performed using the content within BMJ Best Practice.

MetaMap achieves an F measure of 88% (precision 85%, recall 91%) when applied directly to the total of 613 unique candidate terms for the 880 term pairs. When the processing of short forms is included, MetaMap achieves an F measure of 94% (precision 92%, recall 96%). Validation of the term pairs with BMJ Best Practice yields precision between 98 and 99%.

The Semantic Deep Learning approach can transform neural embeddings built from unstructured free-text data into reliable and reusable One Health knowledge using ontologies and content from BMJ Best Practice.

[end paper 2]

[begin paper 3]

PMCID = 10495848

Title = Initiatives, Concepts, and Implementation Practices of the Findable, Accessible, Interoperable, and Reusable Data Principles in Health Data Stewardship: Scoping Review

Thorough data stewardship is a key enabler of comprehensive health research. Processes such as data collection, storage, access, sharing, and analytics require researchers to follow elaborate data management strategies properly and consistently. Studies have shown that findable, accessible, interoperable, and reusable (FAIR) data leads to improved data sharing in different scientific domains.

This scoping review identifies and discusses concepts, approaches, implementation experiences, and lessons learned in FAIR initiatives in health research data.

The Arksey and O’Malley stage-based methodological framework for scoping reviews was applied. PubMed, Web of Science, and Google Scholar were searched to access relevant publications. Articles written in English, published between 2014 and 2020, and addressing FAIR concepts or practices in the health domain were included. The 3 data sources were deduplicated using a reference management software. In total, 2 independent authors reviewed the eligibility of each article based on defined inclusion and exclusion criteria. A charting tool was used to extract information from the full-text papers. The results were reported using the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) guidelines.

A total of 2.18% (34/1561) of the screened articles were included in the final review. The authors reported FAIRification approaches, which include interpolation, inclusion of comprehensive data dictionaries, repository design, semantic interoperability, ontologies, data quality, linked data, and requirement gathering for FAIRification tools. Challenges and mitigation strategies associated with FAIRification, such as high setup costs, data politics, technical and administrative issues, privacy concerns, and difficulties encountered in sharing health data despite its sensitive nature were also reported. We found various workflows, tools, and infrastructures designed by different groups worldwide to facilitate the FAIRification of health research data. We also uncovered a wide range of problems and questions that researchers are trying to address by using the different workflows, tools, and infrastructures. Although the concept of FAIR data stewardship in the health research domain is relatively new, almost all continents have been reached by at least one network trying to achieve health data FAIRness. Documented outcomes of FAIRification efforts include peer-reviewed publications, improved data sharing, facilitated data reuse, return on investment, and new treatments. Successful FAIRification of data has informed the management and prognosis of various diseases such as cancer, cardiovascular diseases, and neurological diseases. Efforts to FAIRify data on a wider variety of diseases have been ongoing since the COVID-19 pandemic.

This work summarises projects, tools, and workflows for the FAIRification of health research data. The comprehensive review shows that implementing the FAIR concept in health data stewardship carries the promise of improved research data management and transparency in the era of big data and open research publishing.

RR2-10.2196/22505

[end paper 3]

[begin paper 4]

PMCID = 9135051

Title = Surgical data science – from concepts toward clinical translation

Recent developments in data science in general and machine learning in particular have transformed the way experts envision the future of surgery. Surgical Data Science (SDS) is a new research field that aims to improve the quality of interventional healthcare through the capture, organization, analysis and modeling of data. While an increasing number of data-driven approaches and clinical applications have been studied in the fields of radiological and clinical data science, translational success stories are still lacking in surgery. In this publication, we shed light on the underlying reasons and provide a roadmap for future advances in the field. Based on an international workshop involving leading researchers in the field of SDS, we review current practice, key achievements and initiatives as well as available standards and tools for a number of topics relevant to the field, namely (1) infrastructure for data acquisition, storage and access in the presence of regulatory constraints, (2) data annotation and sharing and (3) data analytics. We further complement this technical perspective with (4) a review of currently available SDS products and the translational progress from academia and (5) a roadmap for faster clinical translation and exploitation of the full potential of SDS, based on an international multi-round Delphi process.

[end paper 4]

[begin paper 5]

PMCID = 9455941

Title = Pathling: analytics on FHIR

Health data analytics is an area that is facing rapid change due to the acceleration of digitization of the health sector, and the changing landscape of health data and clinical terminology standards. Our research has identified a need for improved tooling to support analytics users in the task of analyzing Fast Healthcare Interoperability Resources (FHIR®) data and associated clinical terminology.

A server implementation was developed, featuring a FHIR API with new operations designed to support exploratory data analysis (EDA), advanced patient cohort selection and data preparation tasks. Integration with a FHIR Terminology Service is also supported, allowing users to incorporate knowledge from rich terminologies such as SNOMED CT within their queries. A prototype user interface for EDA was developed, along with visualizations in support of a health data analysis project.

Experience with applying this technology within research projects and towards the development of analytics-enabled applications provides a preliminary indication that the FHIR Analytics API pattern implemented by Pathling is a valuable abstraction for data scientists and software developers within the health care domain. Pathling contributes towards the value proposition for the use of FHIR within health data analytics, and assists with the use of complex clinical terminologies in that context.

The online version contains supplementary material available at 10.1186/s13326-022-00277-1.

[end paper 5]



