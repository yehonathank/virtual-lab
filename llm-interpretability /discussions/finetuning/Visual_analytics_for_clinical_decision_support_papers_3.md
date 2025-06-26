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

Here are the search queries in Python syntax:

```python
queries = [
    "\"Visual analytics for clinical decision support\"",
    "\"Visual analytics\" AND \"LLM interpretability\" AND \"clinical decision support\"",
    "\"Visual analytics\" AND \"phenotype definition\" AND \"clinical decision support\"",
    "\"Visual analytics\" AND \"clinical applications\" AND \"decision support\"",
    "\"Visual analytics\" AND \"clinician trust\" AND \"decision support\""
]
```

For the agenda question regarding the PMCIDs and titles of the papers, here is a Python dictionary mapping PMCID to title:

```python
papers = {
    "8977763": "Human factors applications in the design of decision support systems for population health: a scoping review",
    "7551124": "Marrying Medical Domain Knowledge With Deep Learning on Electronic Health Records: A Deep Visual Analytics Approach",
    "11769936": "Current state and promise of user-centered design to harness explainable AI in clinical decision-support systems for patients with CNS tumors",
    "9773032": "A Framework for Modeling and Interpreting Patient Subgroups Applied to Hospital Readmission: Visual Analytical Approach",
    "7677017": "Amplifying Domain Expertise in Clinical Data Pipelines",
    "9022040": "Inclusion of Clinicians in the Development and Evaluation of Clinical Artificial Intelligence Tools: A Systematic Literature Review"
}
```

These papers will provide insights into visual analytics for clinical decision support, focusing on aspects like clinician trust, clinical applications, and the integration of AI interpretability.

## User

Tool Output:

No articles found on PubMed Central for the query ""Visual analytics for clinical decision support"".

No articles found on PubMed Central for the query ""Visual analytics" AND "LLM interpretability" AND "clinical decision support"".

No articles found on PubMed Central for the query ""Visual analytics" AND "phenotype definition" AND "clinical decision support"".

Here are the top 5 articles on PubMed Central for the query ""Visual analytics" AND "clinical applications" AND "decision support"":

[begin paper 1]

PMCID = 8977763

Title = Human factors applications in the design of decision support systems for population health: a scoping review

Public health professionals engage in complex cognitive tasks, often using evidence-based decision support tools to bolster their decision-making. Human factors methods take a user-centred approach to improve the design of systems, processes, and interfaces to better support planning and decision-making. While human factors methods have been applied to the design of clinical health tools, these methods are limited in the design of tools for population health. The objective of this scoping review is to develop a comprehensive understanding of how human factors techniques have been applied in the design of population health decision support tools.

The scoping review will follow the methodology and framework proposed by Arksey and O’Malley. We include English-language documents between January 1990 and August 2021 describing the development, validation or application of human factors principles to decision support tools in population health. The search will include Ovid MEDLINE: Epub Ahead of Print, In-Process and Other Non-Indexed Citations, Ovid MEDLINE Daily and Ovid MEDLINE 1946–present; EMBASE, Scopus, PsycINFO, Compendex, IEEE Xplore and Inspec. The results will be integrated into Covidence. First, the abstract of all identified articles will be screened independently by two reviewers with disagreements being resolved by a third reviewer. Next, the full text for articles identified as include or inconclusive will be reviewed by two independent reviewers, leading to a final decision regarding inclusion. Reference lists of included articles will be manually screened to identify additional studies. Data will be extracted by one reviewer, verified by a second, and presented according to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for scoping reviews.

Ethics approval is not required for this work as human participants are not involved. The completed review will be published in a peer-reviewed, interdisciplinary journal.

[end paper 1]

[begin paper 2]

PMCID = 7551124

Title = Marrying Medical Domain Knowledge With Deep Learning on Electronic Health Records: A Deep Visual Analytics Approach

Deep learning models have attracted significant interest from health care researchers during the last few decades. There have been many studies that apply deep learning to medical applications and achieve promising results. However, there are three limitations to the existing models: (1) most clinicians are unable to interpret the results from the existing models, (2) existing models cannot incorporate complicated medical domain knowledge (eg, a disease causes another disease), and (3) most existing models lack visual exploration and interaction. Both the electronic health record (EHR) data set and the deep model results are complex and abstract, which impedes clinicians from exploring and communicating with the model directly.

The objective of this study is to develop an interpretable and accurate risk prediction model as well as an interactive clinical prediction system to support EHR data exploration, knowledge graph demonstration, and model interpretation.

A domain-knowledge–guided recurrent neural network (DG-RNN) model is proposed to predict clinical risks. The model takes medical event sequences as input and incorporates medical domain knowledge by attending to a subgraph of the whole medical knowledge graph. A global pooling operation and a fully connected layer are used to output the clinical outcomes. The middle results and the parameters of the fully connected layer are helpful in identifying which medical events cause clinical risks. DG-Viz is also designed to support EHR data exploration, knowledge graph demonstration, and model interpretation.

We conducted both risk prediction experiments and a case study on a real-world data set. A total of 554 patients with heart failure and 1662 control patients without heart failure were selected from the data set. The experimental results show that the proposed DG-RNN outperforms the state-of-the-art approaches by approximately 1.5%. The case study demonstrates how our medical physician collaborator can effectively explore the data and interpret the prediction results using DG-Viz.

In this study, we present DG-Viz, an interactive clinical prediction system, which brings together the power of deep learning (ie, a DG-RNN–based model) and visual analytics to predict clinical risks and visually interpret the EHR prediction results. Experimental results and a case study on heart failure risk prediction tasks demonstrate the effectiveness and usefulness of the DG-Viz system. This study will pave the way for interactive, interpretable, and accurate clinical risk predictions.

[end paper 2]

[begin paper 3]

PMCID = 11769936

Title = Current state and promise of user-centered design to harness explainable AI in clinical decision-support systems for patients with CNS tumors

In neuro-oncology, MR imaging is crucial for obtaining detailed brain images to identify neoplasms, plan treatment, guide surgical intervention, and monitor the tumor's response. Recent AI advances in neuroimaging have promising applications in neuro-oncology, including guiding clinical decisions and improving patient management. However, the lack of clarity on how AI arrives at predictions has hindered its clinical translation. Explainable AI (XAI) methods aim to improve trustworthiness and informativeness, but their success depends on considering end-users’ (clinicians') specific context and preferences. User-Centered Design (UCD) prioritizes user needs in an iterative design process, involving users throughout, providing an opportunity to design XAI systems tailored to clinical neuro-oncology. This review focuses on the intersection of MR imaging interpretation for neuro-oncology patient management, explainable AI for clinical decision support, and user-centered design. We provide a resource that organizes the necessary concepts, including design and evaluation, clinical translation, user experience and efficiency enhancement, and AI for improved clinical outcomes in neuro-oncology patient management. We discuss the importance of multi-disciplinary skills and user-centered design in creating successful neuro-oncology AI systems. We also discuss how explainable AI tools, embedded in a human-centered decision-making process and different from fully automated solutions, can potentially enhance clinician performance. Following UCD principles to build trust, minimize errors and bias, and create adaptable software has the promise of meeting the needs and expectations of healthcare professionals.

[end paper 3]

[begin paper 4]

PMCID = 9773032

Title = A Framework for Modeling and Interpreting Patient Subgroups Applied to Hospital Readmission: Visual Analytical Approach

A primary goal of precision medicine is to identify patient subgroups and infer their underlying disease processes with the aim of designing targeted interventions. Although several studies have identified patient subgroups, there is a considerable gap between the identification of patient subgroups and their modeling and interpretation for clinical applications.

This study aimed to develop and evaluate a novel analytical framework for modeling and interpreting patient subgroups (MIPS) using a 3-step modeling approach: visual analytical modeling to automatically identify patient subgroups and their co-occurring comorbidities and determine their statistical significance and clinical interpretability; classification modeling to classify patients into subgroups and measure its accuracy; and prediction modeling to predict a patient’s risk of an adverse outcome and compare its accuracy with and without patient subgroup information.

The MIPS framework was developed using bipartite networks to identify patient subgroups based on frequently co-occurring high-risk comorbidities, multinomial logistic regression to classify patients into subgroups, and hierarchical logistic regression to predict the risk of an adverse outcome using subgroup membership compared with standard logistic regression without subgroup membership. The MIPS framework was evaluated for 3 hospital readmission conditions: chronic obstructive pulmonary disease (COPD), congestive heart failure (CHF), and total hip arthroplasty/total knee arthroplasty (THA/TKA) (COPD: n=29,016; CHF: n=51,550; THA/TKA: n=16,498). For each condition, we extracted cases defined as patients readmitted within 30 days of hospital discharge. Controls were defined as patients not readmitted within 90 days of discharge, matched by age, sex, race, and Medicaid eligibility.

In each condition, the visual analytical model identified patient subgroups that were statistically significant (Q=0.17, 0.17, 0.31; P<.001, <.001, <.05), significantly replicated (Rand Index=0.92, 0.94, 0.89; P<.001, <.001, <.01), and clinically meaningful to clinicians. In each condition, the classification model had high accuracy in classifying patients into subgroups (mean accuracy=99.6%, 99.34%, 99.86%). In 2 conditions (COPD and THA/TKA), the hierarchical prediction model had a small but statistically significant improvement in discriminating between readmitted and not readmitted patients as measured by net reclassification improvement (0.059, 0.11) but not as measured by the C-statistic or integrated discrimination improvement.

Although the visual analytical models identified statistically and clinically significant patient subgroups, the results pinpoint the need to analyze subgroups at different levels of granularity for improving the interpretability of intra- and intercluster associations. The high accuracy of the classification models reflects the strong separation of patient subgroups, despite the size and density of the data sets. Finally, the small improvement in predictive accuracy suggests that comorbidities alone were not strong predictors of hospital readmission, and the need for more sophisticated subgroup modeling methods. Such advances could improve the interpretability and predictive accuracy of patient subgroup models for reducing the risk of hospital readmission, and beyond.

[end paper 4]

[begin paper 5]

PMCID = 7677017

Title = Amplifying Domain Expertise in Clinical Data Pipelines

Digitization of health records has allowed the health care domain to adopt data-driven algorithms for decision support. There are multiple people involved in this process: a data engineer who processes and restructures the data, a data scientist who develops statistical models, and a domain expert who informs the design of the data pipeline and consumes its results for decision support. Although there are multiple data interaction tools for data scientists, few exist to allow domain experts to interact with data meaningfully. Designing systems for domain experts requires careful thought because they have different needs and characteristics from other end users. There should be an increased emphasis on the system to optimize the experts’ interaction by directing them to high-impact data tasks and reducing the total task completion time. We refer to this optimization as amplifying domain expertise. Although there is active research in making machine learning models more explainable and usable, it focuses on the final outputs of the model. However, in the clinical domain, expert involvement is needed at every pipeline step: curation, cleaning, and analysis. To this end, we review literature from the database, human-computer information, and visualization communities to demonstrate the challenges and solutions at each of the data pipeline stages. Next, we present a taxonomy of expertise amplification, which can be applied when building systems for domain experts. This includes summarization, guidance, interaction, and acceleration. Finally, we demonstrate the use of our taxonomy with a case study.

[end paper 5]



Here are the top 2 articles on PubMed Central for the query ""Visual analytics" AND "clinician trust" AND "decision support"":

[begin paper 1]

PMCID = 11769936

Title = Current state and promise of user-centered design to harness explainable AI in clinical decision-support systems for patients with CNS tumors

In neuro-oncology, MR imaging is crucial for obtaining detailed brain images to identify neoplasms, plan treatment, guide surgical intervention, and monitor the tumor's response. Recent AI advances in neuroimaging have promising applications in neuro-oncology, including guiding clinical decisions and improving patient management. However, the lack of clarity on how AI arrives at predictions has hindered its clinical translation. Explainable AI (XAI) methods aim to improve trustworthiness and informativeness, but their success depends on considering end-users’ (clinicians') specific context and preferences. User-Centered Design (UCD) prioritizes user needs in an iterative design process, involving users throughout, providing an opportunity to design XAI systems tailored to clinical neuro-oncology. This review focuses on the intersection of MR imaging interpretation for neuro-oncology patient management, explainable AI for clinical decision support, and user-centered design. We provide a resource that organizes the necessary concepts, including design and evaluation, clinical translation, user experience and efficiency enhancement, and AI for improved clinical outcomes in neuro-oncology patient management. We discuss the importance of multi-disciplinary skills and user-centered design in creating successful neuro-oncology AI systems. We also discuss how explainable AI tools, embedded in a human-centered decision-making process and different from fully automated solutions, can potentially enhance clinician performance. Following UCD principles to build trust, minimize errors and bias, and create adaptable software has the promise of meeting the needs and expectations of healthcare professionals.

[end paper 1]

[begin paper 2]

PMCID = 9022040

Title = Inclusion of Clinicians in the Development and Evaluation of Clinical Artificial Intelligence Tools: A Systematic Literature Review

The application of machine learning (ML) and artificial intelligence (AI) in healthcare domains has received much attention in recent years, yet significant questions remain about how these new tools integrate into frontline user workflow, and how their design will impact implementation. Lack of acceptance among clinicians is a major barrier to the translation of healthcare innovations into clinical practice. In this systematic review, we examine when and how clinicians are consulted about their needs and desires for clinical AI tools. Forty-five articles met criteria for inclusion, of which 24 were considered design studies. The design studies used a variety of methods to solicit and gather user feedback, with interviews, surveys, and user evaluations. Our findings show that tool designers consult clinicians at various but inconsistent points during the design process, and most typically at later stages in the design cycle (82%, 19/24 design studies). We also observed a smaller amount of studies adopting a human-centered approach and where clinician input was solicited throughout the design process (22%, 5/24). A third (15/45) of all studies reported on clinician trust in clinical AI algorithms and tools. The surveyed articles did not universally report validation against the “gold standard” of clinical expertise or provide detailed descriptions of the algorithms or computational methods used in their work. To realize the full potential of AI tools within healthcare settings, our review suggests there are opportunities to more thoroughly integrate frontline users’ needs and feedback in the design process.

[end paper 2]



