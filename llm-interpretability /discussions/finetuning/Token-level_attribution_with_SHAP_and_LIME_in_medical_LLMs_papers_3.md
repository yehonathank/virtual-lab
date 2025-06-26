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

Here is a Python dictionary mapping PMCID to the title of the papers that are relevant to your research on Token-level attribution with SHAP and LIME in medical LLMs:

```python
{
    "11213143": "Prospector Heads: Generalized Feature Attribution for Large Models & Data",
    "11300430": "From outputs to insights: a survey of rationalization approaches for explainable text classification",
    "11623222": "Understanding hate speech: the HateInsights dataset and model interpretability",
    "11157010": "Human-annotated rationales and explainable text classification: a survey"
}
```

These articles cover various aspects of feature attribution, rationalization approaches, and model interpretability, which are relevant to your research project on LLM interpretability in electronic phenotype definitions.

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



Here are the top 2 articles on PubMed Central for the query "Token-level attribution with SHAP and LIME in LLM interpretability":

[begin paper 1]

PMCID = 11213143

Title = Prospector Heads: Generalized Feature Attribution for Large Models & Data

Feature attribution, the ability to localize regions of the input data that are relevant for classification, is an important capability for ML models in scientific and biomedical domains. Current methods for feature attribution, which rely on “explaining” the predictions of end-to-end classifiers, suffer from imprecise feature localization and are inadequate for use with small sample sizes and high-dimensional datasets due to computational challenges. We introduce prospector heads, an efficient and interpretable alternative to explanation-based attribution methods that can be applied to any encoder and any data modality. Prospector heads generalize across modalities through experiments on sequences (text), images (pathology), and graphs (protein structures), outperforming baseline attribution methods by up to 26.3 points in mean localization AUPRC. We also demonstrate how prospector heads enable improved interpretation and discovery of class-specific patterns in input data. Through their high performance, flexibility, and generalizability, prospectors provide a framework for improving trust and transparency for ML models in complex domains.

[end paper 1]

[begin paper 2]

PMCID = 11623222

Title = Understanding hate speech: the HateInsights dataset and model interpretability

The persistence of hate speech continues to pose an obstacle in the realm of online social media. Despite the continuous evolution of advanced models for identifying hate speech, the critical dimensions of interpretability and explainability have not received proportional scholarly attention. In this article, we introduce the HateInsights dataset, a groundbreaking benchmark in the field of hate speech datasets, encompassing diverse aspects of this widespread issue. Within our dataset, each individual post undergoes thorough annotation from dual perspectives: firstly, conforming to the established 3-class classification paradigm that includes hate speech, offensive language, and normal discourse; secondly, incorporating rationales that outline specific segments of a post supporting the assigned label (categorized as hate speech, offensive language, or normal discourse). Our exploration yields a significant finding by harnessing cutting-edge state-of-the-art models: even models demonstrating exceptional proficiency in classification tasks yield suboptimal outcomes in crucial explainability metrics, such as model plausibility and faithfulness. Furthermore, our analysis underscores a promising revelation concerning models trained using human-annotated rationales. To facilitate scholarly progress in this realm, we have made both our dataset and codebase accessible to fellow researchers. This initiative aims to encourage collaborative involvement and inspire the advancement of the hate speech detection approach characterized by increased transparency, clarity, and fairness.

[end paper 2]



No articles found on PubMed Central for the query "Token-level attribution with SHAP and LIME in phenotype definition".

Here are the top 2 articles on PubMed Central for the query "Token-level attribution with SHAP and LIME in clinical applications":

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



No articles found on PubMed Central for the query "Token-level attribution with SHAP and LIME and clinician trust".

