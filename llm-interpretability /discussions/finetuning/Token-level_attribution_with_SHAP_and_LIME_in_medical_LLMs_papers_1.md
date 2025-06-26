## User

This is the beginning of an individual meeting with Computational Linguist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Token-level attribution with SHAP and LIME in medical LLMs in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Token-level attribution with SHAP and LIME in medical LLMs to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Token-level attribution with SHAP and LIME in medical LLMs. Include both general queries about Token-level attribution with SHAP and LIME in medical LLMs and queries that specifically relate Token-level attribution with SHAP and LIME in medical LLMs to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Computational Linguist, please provide your response to the agenda.

## Computational Linguist

Here is a Python dictionary mapping PMCIDs to titles for the papers that are relevant to your research project on Token-level attribution with SHAP and LIME in medical LLMs:

```python
{
    "11213143": "Prospector Heads: Generalized Feature Attribution for Large Models & Data",
    "11300430": "From outputs to insights: a survey of rationalization approaches for explainable text classification",
    "10521578": "Machine learning in precision diabetes care and cardiovascular risk prediction",
    "11739813": "A review of large language models and autonomous agents in chemistry",
    "10582733": "Organizational preparedness for the use of large language models in pathology informatics",
    "11436130": "Enhancing the Interpretability of Malaria and Typhoid Diagnosis with Explainable AI and Large Language Models",
    "11983615": "Machine learning and artificial intelligence in type 2 diabetes prediction: a comprehensive 33-year bibliometric and literature analysis",
    "11228775": "Applications of large language models in psychiatry: a systematic review",
    "11900311": "Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI",
    "11972358": "Explainable artificial intelligence to diagnose early Parkinson’s disease via voice analysis",
    "11984408": "Artificial intelligence in chronic kidney disease management: a scoping review",
    "11592288": "Potential Applications and Ethical Considerations for Artificial Intelligence in Traumatic Brain Injury Management"
}
```

These articles cover a range of topics related to SHAP and LIME in medical LLMs, including their applications in clinical settings, interpretability, and building clinician trust.

## User

Tool Output:

Here are the top 2 articles on PubMed Central for the query "Token-level attribution with SHAP and LIME in medical LLMs":

[begin paper 1]

PMCID = 11213143

Title = Prospector Heads: Generalized Feature Attribution for Large Models & Data

Feature attribution, the ability to localize regions of the input data that are relevant for classification, is an important capability for ML models in scientific and biomedical domains. Current methods for feature attribution, which rely on “explaining” the predictions of end-to-end classifiers, suffer from imprecise feature localization and are inadequate for use with small sample sizes and high-dimensional datasets due to computational challenges. We introduce prospector heads, an efficient and interpretable alternative to explanation-based attribution methods that can be applied to any encoder and any data modality. Prospector heads generalize across modalities through experiments on sequences (text), images (pathology), and graphs (protein structures), outperforming baseline attribution methods by up to 26.3 points in mean localization AUPRC. We also demonstrate how prospector heads enable improved interpretation and discovery of class-specific patterns in input data. Through their high performance, flexibility, and generalizability, prospectors provide a framework for improving trust and transparency for ML models in complex domains.

[end paper 1]

[begin paper 2]

PMCID = 11300430

Title = From outputs to insights: a survey of rationalization approaches for explainable text classification

Deep learning models have achieved state-of-the-art performance for text classification in the last two decades. However, this has come at the expense of models becoming less understandable, limiting their application scope in high-stakes domains. The increased interest in explainability has resulted in many proposed forms of explanation. Nevertheless, recent studies have shown that rationales, or language explanations, are more intuitive and human-understandable, especially for non-technical stakeholders. This survey provides an overview of the progress the community has achieved thus far in rationalization approaches for text classification. We first describe and compare techniques for producing extractive and abstractive rationales. Next, we present various rationale-annotated data sets that facilitate the training and evaluation of rationalization models. Then, we detail proxy-based and human-grounded metrics to evaluate machine-generated rationales. Finally, we outline current challenges and encourage directions for future work.

[end paper 2]



Here are the top 1 articles on PubMed Central for the query "LLM interpretability with SHAP and LIME for electronic phenotype definition":

[begin paper 1]

PMCID = 10521578

Title = Machine learning in precision diabetes care and cardiovascular risk prediction

Artificial intelligence and machine learning are driving a paradigm shift in medicine, promising data-driven, personalized solutions for managing diabetes and the excess cardiovascular risk it poses. In this comprehensive review of machine learning applications in the care of patients with diabetes at increased cardiovascular risk, we offer a broad overview of various data-driven methods and how they may be leveraged in developing predictive models for personalized care. We review existing as well as expected artificial intelligence solutions in the context of diagnosis, prognostication, phenotyping, and treatment of diabetes and its cardiovascular complications. In addition to discussing the key properties of such models that enable their successful application in complex risk prediction, we define challenges that arise from their misuse and the role of methodological standards in overcoming these limitations. We also identify key issues in equity and bias mitigation in healthcare and discuss how the current regulatory framework should ensure the efficacy and safety of medical artificial intelligence products in transforming cardiovascular care and outcomes in diabetes.

The online version contains supplementary material available at 10.1186/s12933-023-01985-3.

[end paper 1]



Here are the top 5 articles on PubMed Central for the query "Clinical applications of SHAP and LIME in medical LLMs":

[begin paper 1]

PMCID = 11739813

Title = A review of large language models and autonomous agents in chemistry

Large language models (LLMs) have emerged as powerful tools in chemistry, significantly impacting molecule design, property prediction, and synthesis optimization. This review highlights LLM capabilities in these domains and their potential to accelerate scientific discovery through automation. We also review LLM-based autonomous agents: LLMs with a broader set of tools to interact with their surrounding environment. These agents perform diverse tasks such as paper scraping, interfacing with automated laboratories, and synthesis planning. As agents are an emerging topic, we extend the scope of our review of agents beyond chemistry and discuss across any scientific domains. This review covers the recent history, current capabilities, and design of LLMs and autonomous agents, addressing specific challenges, opportunities, and future directions in chemistry. Key challenges include data quality and integration, model interpretability, and the need for standard benchmarks, while future directions point towards more sophisticated multi-modal agents and enhanced collaboration between agents and experimental methods. Due to the quick pace of this field, a repository has been built to keep track of the latest studies: .

This review examines the roles of large language models (LLMs) and autonomous agents in chemistry, exploring advancements in molecule design, property prediction, and synthesis automation.

[end paper 1]

[begin paper 2]

PMCID = 10582733

Title = Organizational preparedness for the use of large language models in pathology informatics

In this paper, we consider the current and potential role of the latest generation of Large Language Models (LLMs) in medical informatics, particularly within the realms of clinical and anatomic pathology. We aim to provide a thorough understanding of the considerations that arise when employing LLMs in healthcare settings, such as determining appropriate use cases and evaluating the advantages and limitations of these models.

Furthermore, this paper will consider the infrastructural and organizational requirements necessary for the successful implementation and utilization of LLMs in healthcare environments. We will discuss the importance of addressing education, security, bias, and privacy concerns associated with LLMs in clinical informatics, as well as the need for a robust framework to overcome regulatory, compliance, and legal challenges.

[end paper 2]

[begin paper 3]

PMCID = 11436130

Title = Enhancing the Interpretability of Malaria and Typhoid Diagnosis with Explainable AI and Large Language Models

Malaria and Typhoid fever are prevalent diseases in tropical regions, and both are exacerbated by unclear protocols, drug resistance, and environmental factors. Prompt and accurate diagnosis is crucial to improve accessibility and reduce mortality rates. Traditional diagnosis methods cannot effectively capture the complexities of these diseases due to the presence of similar symptoms. Although machine learning (ML) models offer accurate predictions, they operate as “black boxes” with non-interpretable decision-making processes, making it challenging for healthcare providers to comprehend how the conclusions are reached. This study employs explainable AI (XAI) models such as Local Interpretable Model-agnostic Explanations (LIME), and Large Language Models (LLMs) like GPT to clarify diagnostic results for healthcare workers, building trust and transparency in medical diagnostics by describing which symptoms had the greatest impact on the model’s decisions and providing clear, understandable explanations. The models were implemented on Google Colab and Visual Studio Code because of their rich libraries and extensions. Results showed that the Random Forest model outperformed the other tested models; in addition, important features were identified with the LIME plots while ChatGPT 3.5 had a comparative advantage over other LLMs. The study integrates RF, LIME, and GPT in building a mobile app to enhance the interpretability and transparency in malaria and typhoid diagnosis system. Despite its promising results, the system’s performance is constrained by the quality of the dataset. Additionally, while LIME and GPT improve transparency, they may introduce complexities in real-time deployment due to computational demands and the need for internet service to maintain relevance and accuracy. The findings suggest that AI-driven diagnostic systems can significantly enhance healthcare delivery in environments with limited resources, and future works can explore the applicability of this framework to other medical conditions and datasets.

[end paper 3]

[begin paper 4]

PMCID = 11983615

Title = Machine learning and artificial intelligence in type 2 diabetes prediction: a comprehensive 33-year bibliometric and literature analysis

Type 2 Diabetes Mellitus (T2DM) remains a critical global health challenge, necessitating robust predictive models to enable early detection and personalized interventions. This study presents a comprehensive bibliometric and systematic review of 33 years (1991-2024) of research on machine learning (ML) and artificial intelligence (AI) applications in T2DM prediction. It highlights the growing complexity of the field and identifies key trends, methodologies, and research gaps.

A systematic methodology guided the literature selection process, starting with keyword identification using Term Frequency-Inverse Document Frequency (TF-IDF) and expert input. Based on these refined keywords, literature was systematically selected using PRISMA guidelines, resulting in a dataset of 2,351 articles from Web of Science and Scopus databases. Bibliometric analysis was performed on the entire selected dataset using tools such as VOSviewer and Bibliometrix, enabling thematic clustering, co-citation analysis, and network visualization. To assess the most impactful literature, a dual-criteria methodology combining relevance and impact scores was applied. Articles were qualitatively assessed on their alignment with T2DM prediction using a four-point relevance scale and quantitatively evaluated based on citation metrics normalized within subject, journal, and publication year. Articles scoring above a predefined threshold were selected for detailed review. The selected literature spans four time periods: 1991–2000, 2001–2010, 2011–2020, and 2021–2024.

The bibliometric findings reveal exponential growth in publications since 2010, with the USA and UK leading contributions, followed by emerging players like Singapore and India. Key thematic clusters include foundational ML techniques, epidemiological forecasting, predictive modelling, and clinical applications. Ensemble methods (e.g., Random Forest, Gradient Boosting) and deep learning models (e.g., Convolutional Neural Networks) dominate recent advancements. Literature analysis reveals that, early studies primarily used demographic and clinical variables, while recent efforts integrate genetic, lifestyle, and environmental predictors. Additionally, literature analysis highlights advances in integrating real-world datasets, emerging trends like federated learning, and explainability tools such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations).

Future work should address gaps in generalizability, interdisciplinary T2DM prediction research, and psychosocial integration, while also focusing on clinically actionable solutions and real-world applicability to combat the growing diabetes epidemic effectively.

[end paper 4]

[begin paper 5]

PMCID = 11228775

Title = Applications of large language models in psychiatry: a systematic review

With their unmatched ability to interpret and engage with human language and context, large language models (LLMs) hint at the potential to bridge AI and human cognitive processes. This review explores the current application of LLMs, such as ChatGPT, in the field of psychiatry.

We followed PRISMA guidelines and searched through PubMed, Embase, Web of Science, and Scopus, up until March 2024.

From 771 retrieved articles, we included 16 that directly examine LLMs’ use in psychiatry. LLMs, particularly ChatGPT and GPT-4, showed diverse applications in clinical reasoning, social media, and education within psychiatry. They can assist in diagnosing mental health issues, managing depression, evaluating suicide risk, and supporting education in the field. However, our review also points out their limitations, such as difficulties with complex cases and potential underestimation of suicide risks.

Early research in psychiatry reveals LLMs’ versatile applications, from diagnostic support to educational roles. Given the rapid pace of advancement, future investigations are poised to explore the extent to which these models might redefine traditional roles in mental health care.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Building clinician trust with SHAP and LIME in medical LLMs":

[begin paper 1]

PMCID = 11436130

Title = Enhancing the Interpretability of Malaria and Typhoid Diagnosis with Explainable AI and Large Language Models

Malaria and Typhoid fever are prevalent diseases in tropical regions, and both are exacerbated by unclear protocols, drug resistance, and environmental factors. Prompt and accurate diagnosis is crucial to improve accessibility and reduce mortality rates. Traditional diagnosis methods cannot effectively capture the complexities of these diseases due to the presence of similar symptoms. Although machine learning (ML) models offer accurate predictions, they operate as “black boxes” with non-interpretable decision-making processes, making it challenging for healthcare providers to comprehend how the conclusions are reached. This study employs explainable AI (XAI) models such as Local Interpretable Model-agnostic Explanations (LIME), and Large Language Models (LLMs) like GPT to clarify diagnostic results for healthcare workers, building trust and transparency in medical diagnostics by describing which symptoms had the greatest impact on the model’s decisions and providing clear, understandable explanations. The models were implemented on Google Colab and Visual Studio Code because of their rich libraries and extensions. Results showed that the Random Forest model outperformed the other tested models; in addition, important features were identified with the LIME plots while ChatGPT 3.5 had a comparative advantage over other LLMs. The study integrates RF, LIME, and GPT in building a mobile app to enhance the interpretability and transparency in malaria and typhoid diagnosis system. Despite its promising results, the system’s performance is constrained by the quality of the dataset. Additionally, while LIME and GPT improve transparency, they may introduce complexities in real-time deployment due to computational demands and the need for internet service to maintain relevance and accuracy. The findings suggest that AI-driven diagnostic systems can significantly enhance healthcare delivery in environments with limited resources, and future works can explore the applicability of this framework to other medical conditions and datasets.

[end paper 1]

[begin paper 2]

PMCID = 11900311

Title = Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI

Background/Objectives: Artificial intelligence (AI) is transforming healthcare, enabling advances in diagnostics, treatment optimization, and patient care. Yet, its integration raises ethical, regulatory, and societal challenges. Key concerns include data privacy risks, algorithmic bias, and regulatory gaps that struggle to keep pace with AI advancements. This study aims to synthesize a multidisciplinary framework for trustworthy AI in healthcare, focusing on transparency, accountability, fairness, sustainability, and global collaboration. It moves beyond high-level ethical discussions to provide actionable strategies for implementing trustworthy AI in clinical contexts. Methods: A structured literature review was conducted using PubMed, Scopus, and Web of Science. Studies were selected based on relevance to AI ethics, governance, and policy in healthcare, prioritizing peer-reviewed articles, policy analyses, case studies, and ethical guidelines from authoritative sources published within the last decade. The conceptual approach integrates perspectives from clinicians, ethicists, policymakers, and technologists, offering a holistic “ecosystem” view of AI. No clinical trials or patient-level interventions were conducted. Results: The analysis identifies key gaps in current AI governance and introduces the Regulatory Genome—an adaptive AI oversight framework aligned with global policy trends and Sustainable Development Goals. It introduces quantifiable trustworthiness metrics, a comparative analysis of AI categories for clinical applications, and bias mitigation strategies. Additionally, it presents interdisciplinary policy recommendations for aligning AI deployment with ethical, regulatory, and environmental sustainability goals. This study emphasizes measurable standards, multi-stakeholder engagement strategies, and global partnerships to ensure that future AI innovations meet ethical and practical healthcare needs. Conclusions: Trustworthy AI in healthcare requires more than technical advancements—it demands robust ethical safeguards, proactive regulation, and continuous collaboration. By adopting the recommended roadmap, stakeholders can foster responsible innovation, improve patient outcomes, and maintain public trust in AI-driven healthcare.

[end paper 2]

[begin paper 3]

PMCID = 11972358

Title = Explainable artificial intelligence to diagnose early Parkinson’s disease via voice analysis

Parkinson’s disease (PD) is a neurodegenerative disorder affecting motor control, leading to symptoms such as tremors and stiffness. Early diagnosis is essential for effective treatment, but traditional methods are often time-consuming and expensive. This study leverages Artificial Intelligence (AI) and Machine Learning (ML) techniques, using voice analysis to detect early signs of PD. We applied a hybrid model combining Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Multiple Kernel Learning (MKL), and Multilayer Perceptron (MLP) to a dataset of 81 voice recordings. Acoustic features such as Mel-Frequency Cepstral Coefficients (MFCCs), jitter, and shimmer were analyzed. The model achieved 91.11% accuracy, 92.50% recall, 89.84% precision, 91.13% F1 score, and an area-under-the-curve (AUC) of 0.9125. SHapley Additive exPlanations (SHAP) provided data explainability, identifying key features driving the PD diagnosis, thus enhancing AI interpretability and trustability. Furthermore, a probability-based scoring system was developed to enable PD patients and clinicians to track disease progression. This AI-driven approach offers a non-invasive, cost-effective, and rapid tool for early PD detection, facilitating personalized treatment through vocal biomarkers.

The online version contains supplementary material available at 10.1038/s41598-025-96575-6.

[end paper 3]

[begin paper 4]

PMCID = 11984408

Title = Artificial intelligence in chronic kidney disease management: a scoping review

Rationale: Chronic kidney disease (CKD) is a major public health problem worldwide associated with cardiovascular disease, renal failure, and mortality. To effectively address this growing burden, innovative solutions to management are urgently required. We conducted a scoping review to identify key use cases in which artificial intelligence (AI) could be leveraged for improving management of CKD. Additionally, we examined the challenges faced by AI in CKD management, proposed potential solutions to overcome these barriers.

Methods: We reviewed 41 articles published between 2014-2024 which examined various AI techniques including machine learning (ML) and deep learning (DL), unsupervised clustering, digital twin, natural language processing (NLP) and large language models (LLMs) in CKD management. We focused on four areas: early detection, risk stratification and prediction, treatment recommendations and patient care and communication.

Results: We identified 41 articles published between 2014-2024 that assessed image-based DL models for early detection (n = 6), ML models for risk stratification and prediction (n = 14) and treatment recommendations (n = 4), and NLP and LLMs for patient care and communication (n = 17). Key challenges in integrating AI models into healthcare include technical issues such as data quality and access, model accuracy, and interpretability, alongside adoption barriers like workflow integration, user training, and regulatory approval.

Conclusions: There is tremendous potential of integrating AI into clinical care of CKD patients to enable early detection, prediction, and improved patient outcomes. Collaboration among healthcare providers, researchers, regulators, and industries is crucial to developing robust protocols that ensure compliance with legal standards, while minimizing risks and maintaining patient safety.

[end paper 4]

[begin paper 5]

PMCID = 11592288

Title = Potential Applications and Ethical Considerations for Artificial Intelligence in Traumatic Brain Injury Management

Artificial intelligence (AI) systems have emerged as promising tools for rapidly identifying patterns in large amounts of healthcare data to help guide clinical decision making, as well as to assist with medical education and the planning of research studies. Accumulating evidence suggests AI techniques may be particularly useful for aiding the diagnosis and clinical management of traumatic brain injury (TBI)—a considerably heterogeneous neurologic condition that can be challenging to detect and treat. However, important methodological and ethical concerns with the use of AI in medicine necessitate close monitoring and regulation of these techniques as advancements continue. The purpose of this narrative review is to provide an overview of common AI techniques in medical research and describe recent studies on the possible clinical applications of AI in the context of TBI. Finally, the review describes the ethical challenges with the use of AI in medicine, as well as guidelines from the White House, the Department of Defense (DOD), the National Academies of Sciences, Engineering, and Medicine (NASEM), and other organizations on the appropriate uses of AI in research.

[end paper 5]



No articles found on PubMed Central for the query "Token-level attribution in LLMs for phenotype definition".

