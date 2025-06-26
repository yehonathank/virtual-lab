## User

This is the beginning of an individual meeting with Data Visualization Expert to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic Visualization of token attribution in NLP models in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on Visualization of token attribution in NLP models to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on Visualization of token attribution in NLP models. Include both general queries about Visualization of token attribution in NLP models and queries that specifically relate Visualization of token attribution in NLP models to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Data Visualization Expert, please provide your response to the agenda.

## Data Visualization Expert

Here are the PMCIDs and titles of the papers I wish to fine-tune myself on, based on the search queries related to Visualization of token attribution in NLP models:

```python
{
    "10560994": "Rationalization for explainable NLP: a survey",
    "11939797": "Benchmarking Interpretability in Healthcare Using Pattern Discovery and Disentanglement",
    "7658441": "Illuminating the Black Box: Interpreting Deep Neural Network Models for Psychiatric Research",
    "10557887": "An interpretable deep learning framework for predicting liver metastases in postoperative colorectal cancer patients using natural language processing and clinical data integration",
    "10426047": "Building a trustworthy AI differential diagnosis application for Crohn’s disease and intestinal tuberculosis"
}
```

These papers cover a range of topics from general visualization of token attribution in NLP models to specific applications in clinical settings, which will help in developing a transparent and clinically grounded interpretability tool.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "Visualization of token attribution in NLP models":

[begin paper 1]

PMCID = 10560994

Title = Rationalization for explainable NLP: a survey

Recent advances in deep learning have improved the performance of many Natural Language Processing (NLP) tasks such as translation, question-answering, and text classification. However, this improvement comes at the expense of model explainability. Black-box models make it difficult to understand the internals of a system and the process it takes to arrive at an output. Numerical (LIME, Shapley) and visualization (saliency heatmap) explainability techniques are helpful; however, they are insufficient because they require specialized knowledge. These factors led rationalization to emerge as a more accessible explainable technique in NLP. Rationalization justifies a model's output by providing a natural language explanation (rationale). Recent improvements in natural language generation have made rationalization an attractive technique because it is intuitive, human-comprehensible, and accessible to non-technical users. Since rationalization is a relatively new field, it is disorganized. As the first survey, rationalization literature in NLP from 2007 to 2022 is analyzed. This survey presents available methods, explainable evaluations, code, and datasets used across various NLP tasks that use rationalization. Further, a new subfield in Explainable AI (XAI), namely, Rational AI (RAI), is introduced to advance the current state of rationalization. A discussion on observed insights, challenges, and future directions is provided to point to promising research opportunities.

[end paper 1]

[begin paper 2]

PMCID = 9839963

Title = Vision transformer-based weakly supervised histopathological image analysis of primary brain tumors

Diagnosis of primary brain tumors relies heavily on histopathology. Although various computational pathology methods have been developed for automated diagnosis of primary brain tumors, they usually require neuropathologists’ annotation of region of interests or selection of image patches on whole-slide images (WSI). We developed an end-to-end Vision Transformer (ViT) – based deep learning architecture for brain tumor WSI analysis, yielding a highly interpretable deep-learning model, ViT-WSI. Based on the principle of weakly supervised machine learning, ViT-WSI accomplishes the task of major primary brain tumor type and subtype classification. Using a systematic gradient-based attribution analysis procedure, ViT-WSI can discover diagnostic histopathological features for primary brain tumors. Furthermore, we demonstrated that ViT-WSI has high predictive power of inferring the status of three diagnostic glioma molecular markers, IDH1 mutation, p53 mutation, and MGMT methylation, directly from H&E-stained histopathological images, with patient level AUC scores of 0.960, 0.874, and 0.845, respectively.

ViT-WSI, is suitable for weakly supervised learning on histopathological images

ViT-WSI performs tumor typing, subtyping and molecular marker prediction

ViT-WSI automatically discovers brain tumor histological features

Pathology; Cancer; Machine learning

[end paper 2]

[begin paper 3]

PMCID = 11734698

Title = GENA-LM: a family of open-source foundational DNA language models for long sequences

Recent advancements in genomics, propelled by artificial intelligence, have unlocked unprecedented capabilities in interpreting genomic sequences, mitigating the need for exhaustive experimental analysis of complex, intertwined molecular processes inherent in DNA function. A significant challenge, however, resides in accurately decoding genomic sequences, which inherently involves comprehending rich contextual information dispersed across thousands of nucleotides. To address this need, we introduce GENA language model (GENA-LM), a suite of transformer-based foundational DNA language models capable of handling input lengths up to 36 000 base pairs. Notably, integrating the newly developed recurrent memory mechanism allows these models to process even larger DNA segments. We provide pre-trained versions of GENA-LM, including multispecies and taxon-specific models, demonstrating their capability for fine-tuning and addressing a spectrum of complex biological tasks with modest computational demands. While language models have already achieved significant breakthroughs in protein biology, GENA-LM showcases a similarly promising potential for reshaping the landscape of genomics and multi-omics data analysis. All models are publicly available on GitHub (https://github.com/AIRI-Institute/GENA_LM) and on HuggingFace (https://huggingface.co/AIRI-Institute). In addition, we provide a web service (https://dnalm.airi.net/) allowing user-friendly DNA annotation with GENA-LM models.

[end paper 3]

[begin paper 4]

PMCID = 9745317

Title = TSSNote-CyaPromBERT: Development of an integrated platform for highly accurate promoter prediction and visualization of Synechococcus sp. and Synechocystis sp. through a state-of-the-art natural language processing model BERT

Since the introduction of the first transformer model with a unique self-attention mechanism, natural language processing (NLP) models have attained state-of-the-art (SOTA) performance on various tasks. As DNA is the blueprint of life, it can be viewed as an unusual language, with its characteristic lexicon and grammar. Therefore, NLP models may provide insights into the meaning of the sequential structure of DNA. In the current study, we employed and compared the performance of popular SOTA NLP models (i.e., XLNET, BERT, and a variant DNABERT trained on the human genome) to predict and analyze the promoters in freshwater cyanobacterium Synechocystis sp. PCC 6803 and the fastest growing cyanobacterium Synechococcus elongatus sp. UTEX 2973. These freshwater cyanobacteria are promising hosts for phototrophically producing value-added compounds from CO2. Through a custom pipeline, promoters and non-promoters from Synechococcus elongatus sp. UTEX 2973 were used to train the model. The trained model achieved an AUROC score of 0.97 and F1 score of 0.92. During cross-validation with promoters from Synechocystis sp. PCC 6803, the model achieved an AUROC score of 0.96 and F1 score of 0.91. To increase accessibility, we developed an integrated platform (TSSNote-CyaPromBERT) to facilitate large dataset extraction, model training, and promoter prediction from public dRNA-seq datasets. Furthermore, various visualization tools have been incorporated to address the “black box” issue of deep learning and feature analysis. The learning transfer ability of large language models may help identify and analyze promoter regions for newly isolated strains with similar lineages.

[end paper 4]

[begin paper 5]

PMCID = 10950482

Title = Insights into the inner workings of transformer models for protein function prediction

We explored how explainable artificial intelligence (XAI) can help to shed light into the inner workings of neural networks for protein function prediction, by extending the widely used XAI method of integrated gradients such that latent representations inside of transformer models, which were finetuned to Gene Ontology term and Enzyme Commission number prediction, can be inspected too.

The approach enabled us to identify amino acids in the sequences that the transformers pay particular attention to, and to show that these relevant sequence parts reflect expectations from biology and chemistry, both in the embedding layer and inside of the model, where we identified transformer heads with a statistically significant correspondence of attribution maps with ground truth sequence annotations (e.g. transmembrane regions, active sites) across many proteins.

Source code can be accessed at https://github.com/markuswenzel/xai-proteins.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Visualization of token attribution in NLP models for LLM interpretability":

[begin paper 1]

PMCID = 11939797

Title = Benchmarking Interpretability in Healthcare Using Pattern Discovery and Disentanglement

The healthcare industry seeks to integrate AI into clinical applications, yet understanding AI decision making remains a challenge for healthcare practitioners as these systems often function as black boxes. Our work benchmarks the Pattern Discovery and Disentanglement (PDD) system’s unsupervised learning algorithm, which provides interpretable outputs and clustering results from clinical notes to aid decision making. Using the MIMIC-IV dataset, we process free-text clinical notes and ICD-9 codes with Term Frequency-Inverse Document Frequency and Topic Modeling. The PDD algorithm discretizes numerical features into event-based features, discovers association patterns from a disentangled statistical feature value association space, and clusters clinical records. The output is an interpretable knowledge base linking knowledge, patterns, and data to support decision making. Despite being unsupervised, PDD demonstrated performance comparable to supervised deep learning models, validating its clustering ability and knowledge representation. We benchmark interpretability techniques—Feature Permutation, Gradient SHAP, and Integrated Gradients—on the best-performing models (in terms of F1, ROC AUC, balanced accuracy, etc.), evaluating these based on sufficiency, comprehensiveness, and sensitivity metrics. Our findings highlight the limitations of feature importance ranking and post hoc analysis for clinical diagnosis. Meanwhile, PDD’s global interpretability effectively compensates for these issues, helping healthcare practitioners understand the decision-making process and providing suggestive clusters of diseases to assist their diagnosis.

[end paper 1]

[begin paper 2]

PMCID = 11783891

Title = A survey of multilingual large language models

Multilingual large language models (MLLMs) leverage advanced large language models to process and respond to queries across multiple languages, achieving significant success in polyglot tasks. Despite these breakthroughs, a comprehensive survey summarizing existing approaches and recent developments remains absent. To this end, this paper presents a unified and thorough review of the field, highlighting recent progress and emerging trends in MLLM research. The contributions of this paper are as follows. (1) Extensive survey: to our knowledge, this is the pioneering thorough review of multilingual alignment in MLLMs. (2) Unified taxonomy: we provide a unified framework to summarize the current progress in MLLMs. (3) Emerging frontiers: key emerging frontiers are identified, alongside a discussion of associated challenges. (4) Abundant resources: we collect abundant open-source resources, including relevant papers, data corpora, and leaderboards. We hope our work can provide the community quick access and spur breakthrough research in MLLMs.

The rapid advancement of large language models (LLMs) has significantly transformed natural language processing (NLP), enabling machines to understand and generate human-like text. However, most LLMs are predominantly English centric, limiting their applicability in our linguistically diverse world. With over 7,000 languages spoken globally, there is a pressing need for models that can comprehend and generate text across multiple languages. Multilingual large language models (MLLMs) address this gap by processing and producing content in various languages, thereby enhancing global communication and accessibility. This survey provides a comprehensive overview of MLLMs, introducing a systematic taxonomy based on alignment strategies to deepen understanding in this field. By highlighting emerging trends and challenges, this survey aims to guide future research and development, fostering the creation of more inclusive and effective language models that cater to the diverse linguistic landscape of our world.

This survey explores the growing field of multilingual large language models (MLLMs), addressing the challenges of linguistic diversity in natural language processing. By introducing a systematic taxonomy based on alignment strategies, the authors provide a structured understanding of MLLMs' capabilities. The paper reviews current advancements, identifies emerging trends, and outlines challenges in building inclusive language models. This comprehensive overview offers critical insights to guide future research and development, promoting more equitable and effective multilingual communication in an increasingly interconnected world.

[end paper 2]

[begin paper 3]

PMCID = 8361807

Title = Data extraction methods for systematic review (semi)automation: Update of a living systematic review

The reliable and usable (semi) automation of data extraction can support the field of systematic review by reducing the workload required to gather information about the conduct and results of the included studies. This living systematic review examines published approaches for data extraction from reports of clinical studies.

We systematically and continually search PubMed, ACL Anthology, arXiv, OpenAlex via EPPI-Reviewer, and the dblp computer science bibliography databases. Full text screening and data extraction are conducted using a mix of open-source and commercial tools. This living review update includes publications up to August 2024 and OpenAlex content up to September 2024.

117 publications are included in this review. Of these, 30 (26%) used full texts while the rest used titles and abstracts. A total of 112 (96%) publications developed classifiers for randomised controlled trials. Over 30 entities were extracted, with PICOs (population, intervention, comparator, outcome) being the most frequently extracted. Data are available from 53 (45%), and code from 49 (42%) publications. Nine (8%) implemented publicly available tools.

This living systematic review presents an overview of (semi)automated data-extraction literature of interest to different types of literature review. We identified a broad evidence base of publications describing data extraction for interventional reviews and a small number of publications extracting other study types. Between review updates, large language models emerged as a new tool for data extraction. While facilitating access to automated extraction, they showed a trend of decreasing quality of results reporting, especially quantitative results such as recall and lower reproducibility of results. Compared with the previous update, trends such as transition to relation extraction and sharing of code and datasets stayed similar.

[end paper 3]

[begin paper 4]

PMCID = 11880557

Title = Knowledge graph construction for intelligent cockpits based on large language models

As intelligent cockpits rapidly evolve towards “proactive natural interaction,” traditional rule-based user behavior inference methods are facing scalability, generalization, and accuracy bottlenecks, leading to the development and deployment of functions oriented towards pseudo-demands. Effectively capturing and representing the hidden associative knowledge in intelligent cockpits can enhance the system’s understanding of user behavior and environmental contexts, thereby precisely discerning real user needs. In this context, knowledge graphs (KGs) have emerged as an effective tool, enabling the retrieval and organization of vast amounts of information within interconnected and interpretable structures. However, rapidly and flexibly generating domain-specific KGs still poses significant challenges. To address this, this paper introduces a novel knowledge graph construction (KGC) model, GLM-TripleGen, dedicated to analyzing the states and behaviors within intelligent cockpits. This model aims to precisely mine the latent relationships between cockpit state factors and behavioral sequences, effectively addressing key challenges such as the ambiguity in entity recognition and the complexity of relationship extraction within cockpit data. To enhance the adaptability of GLM-TripleGen to the intelligent cockpit domain, this paper constructs an instruction-following dataset based on vehicle states and in-cockpit interaction behaviors, containing a large number of prompt texts paired with corresponding triple labels, to support model fine-tuning. During the fine-tuning process, the Low-Rank Adaptation (LoRA) method is employed to effectively optimize model parameters, significantly reducing training costs. Extensive experiments demonstrate that GLM-TripleGen outperforms existing state-of-the-art KGC methods, accurately generating normalized cockpit triple units. Furthermore, GLM-TripleGen exhibits exceptional robustness and generalization ability, handling various unknown entities and relationships with minimal generalization processing.

[end paper 4]

[begin paper 5]

PMCID = 11623714

Title = Deciphering genomic codes using advanced NLP techniques: a scoping review

The vast and complex nature of human genomic sequencing data presents challenges for effective analysis. This review aims to investigate the application of Natural Language Processing (NLP) techniques, particularly Large Language Models (LLMs) and transformer architectures, in deciphering genomic codes, focusing on tokenization, transformer models, and regulatory annotation prediction. This review aims to assess data and model accessibility in the most recent literature, gaining a better understanding of the existing capabilities and constraints of these tools in processing genomic sequencing data.

Following Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines, our scoping review was conducted across PubMed, Medline, Scopus, Web of Science, Embase, and ACM Digital Library. Studies were included if they focused on NLP methodologies applied to genomic sequencing data analysis, without restrictions on publication date or article type.

A total of 26 studies published between 2021 and April 2024 were selected for review. The review highlights that tokenization and transformer models enhance the processing and understanding of genomic data, with applications in predicting regulatory annotations like transcription-factor binding sites and chromatin accessibility.

The application of NLP and LLMs to genomic sequencing data interpretation is a promising field that can help streamline the processing of large-scale genomic data while providing a better understanding of its complex structures. It can potentially drive advancements in personalized medicine by offering more efficient and scalable solutions for genomic analysis. Further research is needed to discuss and overcome limitations, enhancing model transparency and applicability.

[end paper 5]



Here are the top 3 articles on PubMed Central for the query "Visualization of token attribution in NLP models for phenotype definition":

[begin paper 1]

PMCID = 7658441

Title = Illuminating the Black Box: Interpreting Deep Neural Network Models for Psychiatric Research

Psychiatric research is often confronted with complex abstractions and dynamics that are not readily accessible or well-defined to our perception and measurements, making data-driven methods an appealing approach. Deep neural networks (DNNs) are capable of automatically learning abstractions in the data that can be entirely novel and have demonstrated superior performance over classical machine learning models across a range of tasks and, therefore, serve as a promising tool for making new discoveries in psychiatry. A key concern for the wider application of DNNs is their reputation as a “black box” approach—i.e., they are said to lack transparency or interpretability of how input data are transformed to model outputs. In fact, several existing and emerging tools are providing improvements in interpretability. However, most reviews of interpretability for DNNs focus on theoretical and/or engineering perspectives. This article reviews approaches to DNN interpretability issues that may be relevant to their application in psychiatric research and practice. It describes a framework for understanding these methods, reviews the conceptual basis of specific methods and their potential limitations, and discusses prospects for their implementation and future directions.

[end paper 1]

[begin paper 2]

PMCID = 7426805

Title = Identifying and Predicting Intentional Self-Harm in Electronic Health Record Clinical Notes: Deep Learning Approach

Suicide is an important public health concern in the United States and around the world. There has been significant work examining machine learning approaches to identify and predict intentional self-harm and suicide using existing data sets. With recent advances in computing, deep learning applications in health care are gaining momentum.

This study aimed to leverage the information in clinical notes using deep neural networks (DNNs) to (1) improve the identification of patients treated for intentional self-harm and (2) predict future self-harm events.

We extracted clinical text notes from electronic health records (EHRs) of 835 patients with International Classification of Diseases (ICD) codes for intentional self-harm and 1670 matched controls who never had any intentional self-harm ICD codes. The data were divided into training and holdout test sets. We tested a number of algorithms on clinical notes associated with the intentional self-harm codes using the training set, including several traditional bag-of-words–based models and 2 DNN models: a convolutional neural network (CNN) and a long short-term memory model. We also evaluated the predictive performance of the DNNs on a subset of patients who had clinical notes 1 to 6 months before the first intentional self-harm event. Finally, we evaluated the impact of a pretrained model using Word2vec (W2V) on performance.

The area under the receiver operating characteristic curve (AUC) for the CNN on the phenotyping task, that is, the detection of intentional self-harm in clinical notes concurrent with the events was 0.999, with an F1 score of 0.985. In the predictive task, the CNN achieved the highest performance with an AUC of 0.882 and an F1 score of 0.769. Although pretraining with W2V shortened the DNN training time, it did not improve performance.

The strong performance on the first task, namely, phenotyping based on clinical notes, suggests that such models could be used effectively for surveillance of intentional self-harm in clinical text in an EHR. The modest performance on the predictive task notwithstanding, the results using DNN models on clinical text alone are competitive with other reports in the literature using risk factors from structured EHR data.

[end paper 2]

[begin paper 3]

PMCID = 5391321

Title = Abstracts from the 2017 Society of General Internal Medicine Annual Meeting



[end paper 3]



Here are the top 5 articles on PubMed Central for the query "Visualization of token attribution in NLP models for clinical applications":

[begin paper 1]

PMCID = 10557887

Title = An interpretable deep learning framework for predicting liver metastases in postoperative colorectal cancer patients using natural language processing and clinical data integration

The significance of liver metastasis (LM) in increasing the risk of death for postoperative colorectal cancer (CRC) patients necessitates innovative approaches to predict LM.

Our study presents a novel and significant contribution by developing an interpretable fusion model that effectively integrates both free‐text medical record data and structured laboratory data to predict LM in postoperative CRC patients.

We used a robust dataset of 1463 patients and leveraged state‐of‐the‐art natural language processing (NLP) and machine learning techniques to construct a two‐layer fusion framework that demonstrates superior predictive performance compared to single modal models. Our innovative two‐tier algorithm fuses the results from different data modalities, achieving balanced prediction results on test data and significantly enhancing the predictive ability of the model. To increase interpretability, we employed Shapley additive explanations to elucidate the contributions of free‐text clinical data and structured clinical data to the final model. Furthermore, we translated our findings into practical clinical applications by creating a novel NLP score‐based nomogram using the top 13 valid predictors identified in our study.

The proposed fusion models demonstrated superior predictive performance with an accuracy of 80.8%, precision of 80.3%, recall of 80.5%, and an F1 score of 80.8% in predicting LMs.

This fusion model represents a notable advancement in predicting LMs for postoperative CRC patients, offering the potential to enhance patient outcomes and support clinical decision‐making.

[end paper 1]

[begin paper 2]

PMCID = 11734698

Title = GENA-LM: a family of open-source foundational DNA language models for long sequences

Recent advancements in genomics, propelled by artificial intelligence, have unlocked unprecedented capabilities in interpreting genomic sequences, mitigating the need for exhaustive experimental analysis of complex, intertwined molecular processes inherent in DNA function. A significant challenge, however, resides in accurately decoding genomic sequences, which inherently involves comprehending rich contextual information dispersed across thousands of nucleotides. To address this need, we introduce GENA language model (GENA-LM), a suite of transformer-based foundational DNA language models capable of handling input lengths up to 36 000 base pairs. Notably, integrating the newly developed recurrent memory mechanism allows these models to process even larger DNA segments. We provide pre-trained versions of GENA-LM, including multispecies and taxon-specific models, demonstrating their capability for fine-tuning and addressing a spectrum of complex biological tasks with modest computational demands. While language models have already achieved significant breakthroughs in protein biology, GENA-LM showcases a similarly promising potential for reshaping the landscape of genomics and multi-omics data analysis. All models are publicly available on GitHub (https://github.com/AIRI-Institute/GENA_LM) and on HuggingFace (https://huggingface.co/AIRI-Institute). In addition, we provide a web service (https://dnalm.airi.net/) allowing user-friendly DNA annotation with GENA-LM models.

[end paper 2]

[begin paper 3]

PMCID = 9839963

Title = Vision transformer-based weakly supervised histopathological image analysis of primary brain tumors

Diagnosis of primary brain tumors relies heavily on histopathology. Although various computational pathology methods have been developed for automated diagnosis of primary brain tumors, they usually require neuropathologists’ annotation of region of interests or selection of image patches on whole-slide images (WSI). We developed an end-to-end Vision Transformer (ViT) – based deep learning architecture for brain tumor WSI analysis, yielding a highly interpretable deep-learning model, ViT-WSI. Based on the principle of weakly supervised machine learning, ViT-WSI accomplishes the task of major primary brain tumor type and subtype classification. Using a systematic gradient-based attribution analysis procedure, ViT-WSI can discover diagnostic histopathological features for primary brain tumors. Furthermore, we demonstrated that ViT-WSI has high predictive power of inferring the status of three diagnostic glioma molecular markers, IDH1 mutation, p53 mutation, and MGMT methylation, directly from H&E-stained histopathological images, with patient level AUC scores of 0.960, 0.874, and 0.845, respectively.

ViT-WSI, is suitable for weakly supervised learning on histopathological images

ViT-WSI performs tumor typing, subtyping and molecular marker prediction

ViT-WSI automatically discovers brain tumor histological features

Pathology; Cancer; Machine learning

[end paper 3]

[begin paper 4]

PMCID = 11623714

Title = Deciphering genomic codes using advanced NLP techniques: a scoping review

The vast and complex nature of human genomic sequencing data presents challenges for effective analysis. This review aims to investigate the application of Natural Language Processing (NLP) techniques, particularly Large Language Models (LLMs) and transformer architectures, in deciphering genomic codes, focusing on tokenization, transformer models, and regulatory annotation prediction. This review aims to assess data and model accessibility in the most recent literature, gaining a better understanding of the existing capabilities and constraints of these tools in processing genomic sequencing data.

Following Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines, our scoping review was conducted across PubMed, Medline, Scopus, Web of Science, Embase, and ACM Digital Library. Studies were included if they focused on NLP methodologies applied to genomic sequencing data analysis, without restrictions on publication date or article type.

A total of 26 studies published between 2021 and April 2024 were selected for review. The review highlights that tokenization and transformer models enhance the processing and understanding of genomic data, with applications in predicting regulatory annotations like transcription-factor binding sites and chromatin accessibility.

The application of NLP and LLMs to genomic sequencing data interpretation is a promising field that can help streamline the processing of large-scale genomic data while providing a better understanding of its complex structures. It can potentially drive advancements in personalized medicine by offering more efficient and scalable solutions for genomic analysis. Further research is needed to discuss and overcome limitations, enhancing model transparency and applicability.

[end paper 4]

[begin paper 5]

PMCID = 7797891

Title = Deep Learning applications for COVID-19

This survey explores how Deep Learning has battled the COVID-19 pandemic and provides directions for future research on COVID-19. We cover Deep Learning applications in Natural Language Processing, Computer Vision, Life Sciences, and Epidemiology. We describe how each of these applications vary with the availability of big data and how learning tasks are constructed. We begin by evaluating the current state of Deep Learning and conclude with key limitations of Deep Learning for COVID-19 applications. These limitations include Interpretability, Generalization Metrics, Learning from Limited Labeled Data, and Data Privacy. Natural Language Processing applications include mining COVID-19 research for Information Retrieval and Question Answering, as well as Misinformation Detection, and Public Sentiment Analysis. Computer Vision applications cover Medical Image Analysis, Ambient Intelligence, and Vision-based Robotics. Within Life Sciences, our survey looks at how Deep Learning can be applied to Precision Diagnostics, Protein Structure Prediction, and Drug Repurposing. Deep Learning has additionally been utilized in Spread Forecasting for Epidemiology. Our literature review has found many examples of Deep Learning systems to fight COVID-19. We hope that this survey will help accelerate the use of Deep Learning for COVID-19 research.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "Visualization of token attribution in NLP models for clinician trust":

[begin paper 1]

PMCID = 10426047

Title = Building a trustworthy AI differential diagnosis application for Crohn’s disease and intestinal tuberculosis

Differentiating between Crohn’s disease (CD) and intestinal tuberculosis (ITB) with endoscopy is challenging. We aim to perform more accurate endoscopic diagnosis between CD and ITB by building a trustworthy AI differential diagnosis application.

A total of 1271 electronic health record (EHR) patients who had undergone colonoscopies at Peking Union Medical College Hospital (PUMCH) and were clinically diagnosed with CD (n = 875) or ITB (n = 396) were used in this study. We build a workflow to make diagnoses with EHRs and mine differential diagnosis features; this involves finetuning the pretrained language models, distilling them into a light and efficient TextCNN model, interpreting the neural network and selecting differential attribution features, and then adopting manual feature checking and carrying out debias training.

The accuracy of debiased TextCNN on differential diagnosis between CD and ITB is 0.83 (CR F1: 0.87, ITB F1: 0.77), which is the best among the baselines. On the noisy validation set, its accuracy was 0.70 (CR F1: 0.87, ITB: 0.69), which was significantly higher than that of models without debias. We also find that the debiased model more easily mines the diagnostically significant features. The debiased TextCNN unearthed 39 diagnostic features in the form of phrases, 17 of which were key diagnostic features recognized by the guidelines.

We build a trustworthy AI differential diagnosis application for differentiating between CD and ITB focusing on accuracy, interpretability and robustness. The classifiers perform well, and the features which had statistical significance were in agreement with clinical guidelines.

The online version contains supplementary material available at 10.1186/s12911-023-02257-6.

[end paper 1]

[begin paper 2]

PMCID = 7658441

Title = Illuminating the Black Box: Interpreting Deep Neural Network Models for Psychiatric Research

Psychiatric research is often confronted with complex abstractions and dynamics that are not readily accessible or well-defined to our perception and measurements, making data-driven methods an appealing approach. Deep neural networks (DNNs) are capable of automatically learning abstractions in the data that can be entirely novel and have demonstrated superior performance over classical machine learning models across a range of tasks and, therefore, serve as a promising tool for making new discoveries in psychiatry. A key concern for the wider application of DNNs is their reputation as a “black box” approach—i.e., they are said to lack transparency or interpretability of how input data are transformed to model outputs. In fact, several existing and emerging tools are providing improvements in interpretability. However, most reviews of interpretability for DNNs focus on theoretical and/or engineering perspectives. This article reviews approaches to DNN interpretability issues that may be relevant to their application in psychiatric research and practice. It describes a framework for understanding these methods, reviews the conceptual basis of specific methods and their potential limitations, and discusses prospects for their implementation and future directions.

[end paper 2]

[begin paper 3]

PMCID = 11275579

Title = Four Transformer-Based Deep Learning Classifiers Embedded with an Attention U-Net-Based Lung Segmenter and Layer-Wise Relevance Propagation-Based Heatmaps for COVID-19 X-ray Scans

Background: Diagnosing lung diseases accurately is crucial for proper treatment. Convolutional neural networks (CNNs) have advanced medical image processing, but challenges remain in their accurate explainability and reliability. This study combines U-Net with attention and Vision Transformers (ViTs) to enhance lung disease segmentation and classification. We hypothesize that Attention U-Net will enhance segmentation accuracy and that ViTs will improve classification performance. The explainability methodologies will shed light on model decision-making processes, aiding in clinical acceptance. Methodology: A comparative approach was used to evaluate deep learning models for segmenting and classifying lung illnesses using chest X-rays. The Attention U-Net model is used for segmentation, and architectures consisting of four CNNs and four ViTs were investigated for classification. Methods like Gradient-weighted Class Activation Mapping plus plus (Grad-CAM++) and Layer-wise Relevance Propagation (LRP) provide explainability by identifying crucial areas influencing model decisions. Results: The results support the conclusion that ViTs are outstanding in identifying lung disorders. Attention U-Net obtained a Dice Coefficient of 98.54% and a Jaccard Index of 97.12%. ViTs outperformed CNNs in classification tasks by 9.26%, reaching an accuracy of 98.52% with MobileViT. An 8.3% increase in accuracy was seen while moving from raw data classification to segmented image classification. Techniques like Grad-CAM++ and LRP provided insights into the decision-making processes of the models. Conclusions: This study highlights the benefits of integrating Attention U-Net and ViTs for analyzing lung diseases, demonstrating their importance in clinical settings. Emphasizing explainability clarifies deep learning processes, enhancing confidence in AI solutions and perhaps enhancing clinical acceptance for improved healthcare results.

[end paper 3]

[begin paper 4]

PMCID = 5391321

Title = Abstracts from the 2017 Society of General Internal Medicine Annual Meeting



[end paper 4]

[begin paper 5]

PMCID = 10660543

Title = Evaluating the Efficacy of ChatGPT in Navigating the Spanish Medical Residency Entrance Examination (MIR): Promising Horizons for AI in Clinical Medicine

The rapid progress in artificial intelligence, machine learning, and natural language processing has led to increasingly sophisticated large language models (LLMs) for use in healthcare. This study assesses the performance of two LLMs, the GPT-3.5 and GPT-4 models, in passing the MIR medical examination for access to medical specialist training in Spain. Our objectives included gauging the model’s overall performance, analyzing discrepancies across different medical specialties, discerning between theoretical and practical questions, estimating error proportions, and assessing the hypothetical severity of errors committed by a physician. Material and methods: We studied the 2022 Spanish MIR examination results after excluding those questions requiring image evaluations or having acknowledged errors. The remaining 182 questions were presented to the LLM GPT-4 and GPT-3.5 in Spanish and English. Logistic regression models analyzed the relationships between question length, sequence, and performance. We also analyzed the 23 questions with images, using GPT-4’s new image analysis capability. Results: GPT-4 outperformed GPT-3.5, scoring 86.81% in Spanish (p < 0.001). English translations had a slightly enhanced performance. GPT-4 scored 26.1% of the questions with images in English. The results were worse when the questions were in Spanish, 13.0%, although the differences were not statistically significant (p = 0.250). Among medical specialties, GPT-4 achieved a 100% correct response rate in several areas, and the Pharmacology, Critical Care, and Infectious Diseases specialties showed lower performance. The error analysis revealed that while a 13.2% error rate existed, the gravest categories, such as “error requiring intervention to sustain life” and “error resulting in death”, had a 0% rate. Conclusions: GPT-4 performs robustly on the Spanish MIR examination, with varying capabilities to discriminate knowledge across specialties. While the model’s high success rate is commendable, understanding the error severity is critical, especially when considering AI’s potential role in real-world medical practice and its implications for patient safety.

[end paper 5]



