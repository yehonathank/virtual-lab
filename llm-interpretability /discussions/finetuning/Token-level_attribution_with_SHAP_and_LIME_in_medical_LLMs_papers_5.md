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

To address the agenda, I will first create a series of search queries to find relevant scientific papers on Token-level attribution with SHAP and LIME in medical LLMs. These queries will focus on general aspects as well as specific applications related to LLM interpretability, phenotype definition, clinical applications, and clinician trust.

Here are the search queries in Python syntax:

```python
queries = [
    "Token-level attribution SHAP LIME medical LLMs",
    "LLM interpretability SHAP LIME electronic phenotype definition",
    "Token-level attribution SHAP LIME clinical applications",
    "SHAP LIME clinician trust medical LLMs",
    "Token-level attribution SHAP LIME phenotype definition"
]
```

Next, I will use these queries to search for relevant scientific papers. Let's proceed with the search using these queries.

## Computational Linguist

Here are the PMCIDs and titles of the papers that are relevant to our research project on Token-level attribution with SHAP and LIME in medical LLMs:

```python
papers = {
    "11213143": "Prospector Heads: Generalized Feature Attribution for Large Models & Data",
    "11300430": "From outputs to insights: a survey of rationalization approaches for explainable text classification",
    "10521578": "Machine learning in precision diabetes care and cardiovascular risk prediction",
    "11157010": "Human-annotated rationales and explainable text classification: a survey",
    "11436130": "Enhancing the Interpretability of Malaria and Typhoid Diagnosis with Explainable AI and Large Language Models",
    "11877768": "The role of explainable artificial intelligence in disease prediction: a systematic literature review and future research directions",
    "11900311": "Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI",
    "11972358": "Explainable artificial intelligence to diagnose early Parkinson’s disease via voice analysis",
    "11765989": "Explainable AI in Digestive Healthcare and Gastrointestinal Endoscopy"
}
```

These papers cover various aspects of explainable AI, SHAP, LIME, and their applications in medical contexts, which will be beneficial for developing a transparent, clinically grounded, and visually intuitive interpretability tool.

## User

Tool Output:

Here are the top 2 articles on PubMed Central for the query "Token-level attribution SHAP LIME medical LLMs":

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



Here are the top 1 articles on PubMed Central for the query "LLM interpretability SHAP LIME electronic phenotype definition":

[begin paper 1]

PMCID = 10521578

Title = Machine learning in precision diabetes care and cardiovascular risk prediction

Artificial intelligence and machine learning are driving a paradigm shift in medicine, promising data-driven, personalized solutions for managing diabetes and the excess cardiovascular risk it poses. In this comprehensive review of machine learning applications in the care of patients with diabetes at increased cardiovascular risk, we offer a broad overview of various data-driven methods and how they may be leveraged in developing predictive models for personalized care. We review existing as well as expected artificial intelligence solutions in the context of diagnosis, prognostication, phenotyping, and treatment of diabetes and its cardiovascular complications. In addition to discussing the key properties of such models that enable their successful application in complex risk prediction, we define challenges that arise from their misuse and the role of methodological standards in overcoming these limitations. We also identify key issues in equity and bias mitigation in healthcare and discuss how the current regulatory framework should ensure the efficacy and safety of medical artificial intelligence products in transforming cardiovascular care and outcomes in diabetes.

The online version contains supplementary material available at 10.1186/s12933-023-01985-3.

[end paper 1]



Here are the top 2 articles on PubMed Central for the query "Token-level attribution SHAP LIME clinical applications":

[begin paper 1]

PMCID = 11213143

Title = Prospector Heads: Generalized Feature Attribution for Large Models & Data

Feature attribution, the ability to localize regions of the input data that are relevant for classification, is an important capability for ML models in scientific and biomedical domains. Current methods for feature attribution, which rely on “explaining” the predictions of end-to-end classifiers, suffer from imprecise feature localization and are inadequate for use with small sample sizes and high-dimensional datasets due to computational challenges. We introduce prospector heads, an efficient and interpretable alternative to explanation-based attribution methods that can be applied to any encoder and any data modality. Prospector heads generalize across modalities through experiments on sequences (text), images (pathology), and graphs (protein structures), outperforming baseline attribution methods by up to 26.3 points in mean localization AUPRC. We also demonstrate how prospector heads enable improved interpretation and discovery of class-specific patterns in input data. Through their high performance, flexibility, and generalizability, prospectors provide a framework for improving trust and transparency for ML models in complex domains.

[end paper 1]

[begin paper 2]

PMCID = 11157010

Title = Human-annotated rationales and explainable text classification: a survey

Asking annotators to explain “why” they labeled an instance yields annotator rationales: natural language explanations that provide reasons for classifications. In this work, we survey the collection and use of annotator rationales. Human-annotated rationales can improve data quality and form a valuable resource for improving machine learning models. Moreover, human-annotated rationales can inspire the construction and evaluation of model-annotated rationales, which can play an important role in explainable artificial intelligence.

[end paper 2]



Here are the top 5 articles on PubMed Central for the query "SHAP LIME clinician trust medical LLMs":

[begin paper 1]

PMCID = 11436130

Title = Enhancing the Interpretability of Malaria and Typhoid Diagnosis with Explainable AI and Large Language Models

Malaria and Typhoid fever are prevalent diseases in tropical regions, and both are exacerbated by unclear protocols, drug resistance, and environmental factors. Prompt and accurate diagnosis is crucial to improve accessibility and reduce mortality rates. Traditional diagnosis methods cannot effectively capture the complexities of these diseases due to the presence of similar symptoms. Although machine learning (ML) models offer accurate predictions, they operate as “black boxes” with non-interpretable decision-making processes, making it challenging for healthcare providers to comprehend how the conclusions are reached. This study employs explainable AI (XAI) models such as Local Interpretable Model-agnostic Explanations (LIME), and Large Language Models (LLMs) like GPT to clarify diagnostic results for healthcare workers, building trust and transparency in medical diagnostics by describing which symptoms had the greatest impact on the model’s decisions and providing clear, understandable explanations. The models were implemented on Google Colab and Visual Studio Code because of their rich libraries and extensions. Results showed that the Random Forest model outperformed the other tested models; in addition, important features were identified with the LIME plots while ChatGPT 3.5 had a comparative advantage over other LLMs. The study integrates RF, LIME, and GPT in building a mobile app to enhance the interpretability and transparency in malaria and typhoid diagnosis system. Despite its promising results, the system’s performance is constrained by the quality of the dataset. Additionally, while LIME and GPT improve transparency, they may introduce complexities in real-time deployment due to computational demands and the need for internet service to maintain relevance and accuracy. The findings suggest that AI-driven diagnostic systems can significantly enhance healthcare delivery in environments with limited resources, and future works can explore the applicability of this framework to other medical conditions and datasets.

[end paper 1]

[begin paper 2]

PMCID = 11877768

Title = The role of explainable artificial intelligence in disease prediction: a systematic literature review and future research directions

Explainable Artificial Intelligence (XAI) enhances transparency and interpretability in AI models, which is crucial for trust and accountability in healthcare. A potential application of XAI is disease prediction using various data modalities. This study conducts a Systematic Literature Review (SLR) following the PRISMA protocol, synthesizing findings from 30 selected studies to examine XAI’s evolving role in disease prediction. It explores commonly used XAI methods, such as Shapley Additive Explanations (SHAP) and Local Interpretable Model-agnostic Explanations (LIME), and their impact across medical fields in disease prediction. The review highlights key gaps, including limited dataset diversity, model complexity, and reliance on single data types, emphasizing the need for greater interpretability and data integration. Addressing these issues is crucial for advancing AI in healthcare. This study contributes by outlining current challenges and potential solutions, suggesting directions for future research to develop more reliable and robust XAI methods.

[end paper 2]

[begin paper 3]

PMCID = 11900311

Title = Shaping the Future of Healthcare: Ethical Clinical Challenges and Pathways to Trustworthy AI

Background/Objectives: Artificial intelligence (AI) is transforming healthcare, enabling advances in diagnostics, treatment optimization, and patient care. Yet, its integration raises ethical, regulatory, and societal challenges. Key concerns include data privacy risks, algorithmic bias, and regulatory gaps that struggle to keep pace with AI advancements. This study aims to synthesize a multidisciplinary framework for trustworthy AI in healthcare, focusing on transparency, accountability, fairness, sustainability, and global collaboration. It moves beyond high-level ethical discussions to provide actionable strategies for implementing trustworthy AI in clinical contexts. Methods: A structured literature review was conducted using PubMed, Scopus, and Web of Science. Studies were selected based on relevance to AI ethics, governance, and policy in healthcare, prioritizing peer-reviewed articles, policy analyses, case studies, and ethical guidelines from authoritative sources published within the last decade. The conceptual approach integrates perspectives from clinicians, ethicists, policymakers, and technologists, offering a holistic “ecosystem” view of AI. No clinical trials or patient-level interventions were conducted. Results: The analysis identifies key gaps in current AI governance and introduces the Regulatory Genome—an adaptive AI oversight framework aligned with global policy trends and Sustainable Development Goals. It introduces quantifiable trustworthiness metrics, a comparative analysis of AI categories for clinical applications, and bias mitigation strategies. Additionally, it presents interdisciplinary policy recommendations for aligning AI deployment with ethical, regulatory, and environmental sustainability goals. This study emphasizes measurable standards, multi-stakeholder engagement strategies, and global partnerships to ensure that future AI innovations meet ethical and practical healthcare needs. Conclusions: Trustworthy AI in healthcare requires more than technical advancements—it demands robust ethical safeguards, proactive regulation, and continuous collaboration. By adopting the recommended roadmap, stakeholders can foster responsible innovation, improve patient outcomes, and maintain public trust in AI-driven healthcare.

[end paper 3]

[begin paper 4]

PMCID = 11972358

Title = Explainable artificial intelligence to diagnose early Parkinson’s disease via voice analysis

Parkinson’s disease (PD) is a neurodegenerative disorder affecting motor control, leading to symptoms such as tremors and stiffness. Early diagnosis is essential for effective treatment, but traditional methods are often time-consuming and expensive. This study leverages Artificial Intelligence (AI) and Machine Learning (ML) techniques, using voice analysis to detect early signs of PD. We applied a hybrid model combining Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Multiple Kernel Learning (MKL), and Multilayer Perceptron (MLP) to a dataset of 81 voice recordings. Acoustic features such as Mel-Frequency Cepstral Coefficients (MFCCs), jitter, and shimmer were analyzed. The model achieved 91.11% accuracy, 92.50% recall, 89.84% precision, 91.13% F1 score, and an area-under-the-curve (AUC) of 0.9125. SHapley Additive exPlanations (SHAP) provided data explainability, identifying key features driving the PD diagnosis, thus enhancing AI interpretability and trustability. Furthermore, a probability-based scoring system was developed to enable PD patients and clinicians to track disease progression. This AI-driven approach offers a non-invasive, cost-effective, and rapid tool for early PD detection, facilitating personalized treatment through vocal biomarkers.

The online version contains supplementary material available at 10.1038/s41598-025-96575-6.

[end paper 4]

[begin paper 5]

PMCID = 11765989

Title = Explainable AI in Digestive Healthcare and Gastrointestinal Endoscopy

An important impediment to the incorporation of artificial intelligence-based tools into healthcare is their association with so-called black box medicine, a concept arising due to their complexity and the difficulties in understanding how they reach a decision. This situation may compromise the clinician’s trust in these tools, should any errors occur, and the inability to explain how decisions are reached may affect their relationship with patients. Explainable AI (XAI) aims to overcome this limitation by facilitating a better understanding of how AI models reach their conclusions for users, thereby enhancing trust in the decisions reached. This review first defined the concepts underlying XAI, establishing the tools available and how they can benefit digestive healthcare. Examples of the application of XAI in digestive healthcare were provided, and potential future uses were proposed. In addition, aspects of the regulatory frameworks that must be established and the ethical concerns that must be borne in mind during the development of these tools were discussed. Finally, we considered the challenges that this technology faces to ensure that optimal benefits are reaped, highlighting the need for more research into the use of XAI in this field.

[end paper 5]



No articles found on PubMed Central for the query "Token-level attribution SHAP LIME phenotype definition".

