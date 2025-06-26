## User

This is the beginning of an individual meeting with Computational Linguist to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust.
                You are responsible for understanding the topic BioBERT fine-tuning for clinical concept extraction in the context of designing an LLM-based interpretability pipeline for electronic phenotype definition.
                You need to fine-tune yourself on the relevant literature on BioBERT fine-tuning for clinical concept extraction to improve your ability to contribute effectively to building a transparent, clinically grounded, and visually intuitive interpretability tool.
                Please write out a series of five distinct search queries that you want to run to find relevant scientific papers on BioBERT fine-tuning for clinical concept extraction. Include both general queries about BioBERT fine-tuning for clinical concept extraction and queries that specifically relate BioBERT fine-tuning for clinical concept extraction to LLM interpretability, phenotype definition, clinical applications, and clinician trust.
                Please provide the queries in Python syntax as a list of double-quoted strings.

Here are the agenda questions that must be answered:

1. What are the PMCIDs and titles of the papers you wish to fine-tune yourself on (as a Python dictionary mapping PMCID as a double-quoted string to title as double-quoted string)?

Computational Linguist, please provide your response to the agenda.

## Computational Linguist

Here is a Python dictionary mapping PMCIDs to titles for the papers relevant to BioBERT fine-tuning for clinical concept extraction across various contexts:

```python
{
    "9408061": "Do syntactic trees enhance Bidirectional Encoder Representations from Transformers (BERT) models for chemical–drug relation extraction?",
    "7703786": "BioBERT: a pre-trained biomedical language representation model for biomedical text mining",
    "10140607": "Fine-tuning large neural language models for biomedical natural language processing",
    "9972634": "Precision information extraction for rare disease epidemiology at scale",
    "9907889": "A prefix and attention map discrimination fusion guided attention for biomedical named entity recognition",
    "11739813": "A review of large language models and autonomous agents in chemistry",
    "11464944": "Multimodal Large Language Models in Health Care: Applications, Challenges, and Future Outlook",
    "11960180": "Utilizing large language models for gastroenterology research: a conceptual framework",
    "11494256": "Use of SNOMED CT in Large Language Models: Scoping Review",
    "11456558": "Large language model to multimodal large language model: A journey to shape the biological macromolecules to biological sciences and medicine",
    "11539635": "Multifaceted Natural Language Processing Task–Based Evaluation of Bidirectional Encoder Representations From Transformers Models for Bilingual (Korean and English) Clinical Notes: Algorithm Development and Validation",
    "11772291": "Clinical entity-aware domain adaptation in low resource setting for inflammatory bowel disease",
    "9141535": "Discovering Thematically Coherent Biomedical Documents Using Contextualized Bidirectional Encoder Representations from Transformers-Based Clustering",
    "11586117": "Lightweight transformers for clinical natural language processing",
    "8135980": "A neuro-symbolic method for understanding free-text medical evidence"
}
```

These papers cover a range of topics from the general application of BioBERT in clinical concept extraction to its integration with large language models for interpretability, phenotype definition, clinical applications, and building clinician trust.

## User

Tool Output:

Here are the top 5 articles on PubMed Central for the query "BioBERT fine-tuning for clinical concept extraction":

[begin paper 1]

PMCID = 9408061

Title = Do syntactic trees enhance Bidirectional Encoder Representations from Transformers (BERT) models for chemical–drug relation extraction?

Collecting relations between chemicals and drugs is crucial in biomedical research. The pre-trained transformer model, e.g. Bidirectional Encoder Representations from Transformers (BERT), is shown to have limitations on biomedical texts; more specifically, the lack of annotated data makes relation extraction (RE) from biomedical texts very challenging. In this paper, we hypothesize that enriching a pre-trained transformer model with syntactic information may help improve its performance on chemical–drug RE tasks. For this purpose, we propose three syntax-enhanced models based on the domain-specific BioBERT model: Chunking-Enhanced-BioBERT and Constituency-Tree-BioBERT in which constituency information is integrated and a Multi-Task-Learning framework Multi-Task-Syntactic (MTS)-BioBERT in which syntactic information is injected implicitly by adding syntax-related tasks as training objectives. Besides, we test an existing model Late-Fusion which is enhanced by syntactic dependency information and build ensemble systems combining syntax-enhanced models and non-syntax-enhanced models. Experiments are conducted on the BioCreative VII DrugProt corpus, a manually annotated corpus for the development and evaluation of RE systems. Our results reveal that syntax-enhanced models in general degrade the performance of BioBERT in the scenario of biomedical RE but improve the performance when the subject–object distance of candidate semantic relation is long. We also explore the impact of quality of dependency parses. [Our code is available at: https://github.com/Maple177/syntax-enhanced-RE/tree/drugprot (for only MTS-BioBERT); https://github.com/Maple177/drugprot-relation-extraction (for the rest of experiments)]

 Database URL https://github.com/Maple177/drugprot-relation-extraction 

[end paper 1]

[begin paper 2]

PMCID = 7703786

Title = BioBERT: a pre-trained biomedical language representation model for biomedical text mining

Biomedical text mining is becoming increasingly important as the number of biomedical documents rapidly grows. With the progress in natural language processing (NLP), extracting valuable information from biomedical literature has gained popularity among researchers, and deep learning has boosted the development of effective biomedical text mining models. However, directly applying the advancements in NLP to biomedical text mining often yields unsatisfactory results due to a word distribution shift from general domain corpora to biomedical corpora. In this article, we investigate how the recently introduced pre-trained language model BERT can be adapted for biomedical corpora.

We introduce BioBERT (Bidirectional Encoder Representations from Transformers for Biomedical Text Mining), which is a domain-specific language representation model pre-trained on large-scale biomedical corpora. With almost the same architecture across tasks, BioBERT largely outperforms BERT and previous state-of-the-art models in a variety of biomedical text mining tasks when pre-trained on biomedical corpora. While BERT obtains performance comparable to that of previous state-of-the-art models, BioBERT significantly outperforms them on the following three representative biomedical text mining tasks: biomedical named entity recognition (0.62% F1 score improvement), biomedical relation extraction (2.80% F1 score improvement) and biomedical question answering (12.24% MRR improvement). Our analysis results show that pre-training BERT on biomedical corpora helps it to understand complex biomedical texts.

We make the pre-trained weights of BioBERT freely available at https://github.com/naver/biobert-pretrained, and the source code for fine-tuning BioBERT available at https://github.com/dmis-lab/biobert.

[end paper 2]

[begin paper 3]

PMCID = 10140607

Title = Fine-tuning large neural language models for biomedical natural language processing

Large neural language models have transformed modern natural language processing (NLP) applications. However, fine-tuning such models for specific tasks remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP. We conduct a systematic study on fine-tuning stability in biomedical NLP. We show that fine-tuning performance may be sensitive to pretraining settings and conduct an exploration of techniques for addressing fine-tuning instability. We show that these techniques can substantially improve fine-tuning performance for low-resource biomedical NLP applications. Specifically, freezing lower layers is helpful for standard BERT- models, while layerwise decay is more effective for BERT- and ELECTRA models. For low-resource text similarity tasks, such as BIOSSES, reinitializing the top layers is the optimal strategy. Overall, domain-specific vocabulary and pretraining facilitate robust models for fine-tuning. Based on these findings, we establish a new state of the art on a wide range of biomedical NLP applications.

Systematic exploration of fine-tuning stability in biomedical NLP

Domain-specific vocabulary and pretraining facilitate robust models for fine-tuning

PubMedBERT-large and PubMedELECTRA models advance state-of-the-art in biomedical NLP

Large neural language models have transformed modern natural language processing (NLP) and have recently become a focus of public attention. However, fine-tuning these models for specific tasks of interest remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP.

This study conducts a systematic exploration of fine-tuning stability in biomedical NLP and identifies techniques that address instability and improve performance. The findings highlight the importance of domain-specific vocabulary and pretraining for creating robust models and establish a new state of the art on a wide range of biomedical NLP applications in the Biomedical Language Understanding and Reasoning Benchmark (BLURB).

Large neural language models have transformed modern natural language processing (NLP). However, fine-tuning these models for specific tasks remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP. This systematic exploration of fine-tuning stability in biomedical NLP highlights the importance of domain-specific vocabulary and pretraining for creating robust models and establishes a new state of the art on a wide range of biomedical NLP applications.

[end paper 3]

[begin paper 4]

PMCID = 9972634

Title = Precision information extraction for rare disease epidemiology at scale

The United Nations recently made a call to address the challenges of an estimated 300 million persons worldwide living with a rare disease through the collection, analysis, and dissemination of disaggregated data. Epidemiologic Information (EI) regarding prevalence and incidence data of rare diseases is sparse and current paradigms of identifying, extracting, and curating EI rely upon time-intensive, error-prone manual processes. With these limitations, a clear understanding of the variation in epidemiology and outcomes for rare disease patients is hampered. This challenges the public health of rare diseases patients through a lack of information necessary to prioritize research, policy decisions, therapeutic development, and health system allocations.

In this study, we developed a newly curated epidemiology corpus for Named Entity Recognition (NER), a deep learning framework, and a novel rare disease epidemiologic information pipeline named EpiPipeline4RD consisting of a web interface and Restful API. For the corpus creation, we programmatically gathered a representative sample of rare disease epidemiologic abstracts, utilized weakly-supervised machine learning techniques to label the dataset, and manually validated the labeled dataset. For the deep learning framework development, we fine-tuned our dataset and adapted the BioBERT model for NER. We measured the performance of our BioBERT model for epidemiology entity recognition quantitatively with precision, recall, and F1 and qualitatively through a comparison with Orphanet. We demonstrated the ability for our pipeline to gather, identify, and extract epidemiology information from rare disease abstracts through three case studies.

We developed a deep learning model to extract EI with overall F1 scores of 0.817 and 0.878, evaluated at the entity-level and token-level respectively, and which achieved comparable qualitative results to Orphanet’s collection paradigm. Additionally, case studies of the rare diseases Classic homocystinuria, GRACILE syndrome, Phenylketonuria demonstrated the adequate recall of abstracts with epidemiology information, high precision of epidemiology information extraction through our deep learning model, and the increased efficiency of EpiPipeline4RD compared to a manual curation paradigm.

EpiPipeline4RD demonstrated high performance of EI extraction from rare disease literature to augment manual curation processes. This automated information curation paradigm will not only effectively empower development of the NIH Genetic and Rare Diseases Information Center (GARD), but also support the public health of the rare disease community.

The online version contains supplementary material available at 10.1186/s12967-023-04011-y.

[end paper 4]

[begin paper 5]

PMCID = 9907889

Title = A prefix and attention map discrimination fusion guided attention for biomedical named entity recognition

The biomedical literature is growing rapidly, and it is increasingly important to extract meaningful information from the vast amount of literature. Biomedical named entity recognition (BioNER) is one of the key and fundamental tasks in biomedical text mining. It also acts as a primitive step for many downstream applications such as relation extraction and knowledge base completion. Therefore, the accurate identification of entities in biomedical literature has certain research value. However, this task is challenging due to the insufficiency of sequence labeling and the lack of large-scale labeled training data and domain knowledge.

In this paper, we use a novel word-pair classification method, design a simple attention mechanism and propose a novel architecture to solve the research difficulties of BioNER more efficiently without leveraging any external knowledge. Specifically, we break down the limitations of sequence labeling-based approaches by predicting the relationship between word pairs. Based on this, we enhance the pre-trained model BioBERT, through the proposed prefix and attention map dscrimination fusion guided attention and propose the E-BioBERT. Our proposed attention differentiates the distribution of different heads in different layers in the BioBERT, which enriches the diversity of self-attention. Our model is superior to state-of-the-art compared models on five available datasets: BC4CHEMD, BC2GM, BC5CDR-Disease, BC5CDR-Chem, and NCBI-Disease, achieving F1-score of 92.55%, 85.45%, 87.53%, 94.16% and 90.55%, respectively.

Compared with many previous various models, our method does not require additional training datasets, external knowledge, and complex training process. The experimental results on five BioNER benchmark datasets demonstrate that our model is better at mining semantic information, alleviating the problem of label inconsistency, and has higher entity recognition ability. More importantly, we analyze and demonstrate the effectiveness of our proposed attention.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "BioBERT fine-tuning clinical concept extraction LLM interpretability":

[begin paper 1]

PMCID = 11739813

Title = A review of large language models and autonomous agents in chemistry

Large language models (LLMs) have emerged as powerful tools in chemistry, significantly impacting molecule design, property prediction, and synthesis optimization. This review highlights LLM capabilities in these domains and their potential to accelerate scientific discovery through automation. We also review LLM-based autonomous agents: LLMs with a broader set of tools to interact with their surrounding environment. These agents perform diverse tasks such as paper scraping, interfacing with automated laboratories, and synthesis planning. As agents are an emerging topic, we extend the scope of our review of agents beyond chemistry and discuss across any scientific domains. This review covers the recent history, current capabilities, and design of LLMs and autonomous agents, addressing specific challenges, opportunities, and future directions in chemistry. Key challenges include data quality and integration, model interpretability, and the need for standard benchmarks, while future directions point towards more sophisticated multi-modal agents and enhanced collaboration between agents and experimental methods. Due to the quick pace of this field, a repository has been built to keep track of the latest studies: .

This review examines the roles of large language models (LLMs) and autonomous agents in chemistry, exploring advancements in molecule design, property prediction, and synthesis automation.

[end paper 1]

[begin paper 2]

PMCID = 11464944

Title = Multimodal Large Language Models in Health Care: Applications, Challenges, and Future Outlook

In the complex and multidimensional field of medicine, multimodal data are prevalent and crucial for informed clinical decisions. Multimodal data span a broad spectrum of data types, including medical images (eg, MRI and CT scans), time-series data (eg, sensor data from wearable devices and electronic health records), audio recordings (eg, heart and respiratory sounds and patient interviews), text (eg, clinical notes and research articles), videos (eg, surgical procedures), and omics data (eg, genomics and proteomics). While advancements in large language models (LLMs) have enabled new applications for knowledge retrieval and processing in the medical field, most LLMs remain limited to processing unimodal data, typically text-based content, and often overlook the importance of integrating the diverse data modalities encountered in clinical practice. This paper aims to present a detailed, practical, and solution-oriented perspective on the use of multimodal LLMs (M-LLMs) in the medical field. Our investigation spanned M-LLM foundational principles, current and potential applications, technical and ethical challenges, and future research directions. By connecting these elements, we aimed to provide a comprehensive framework that links diverse aspects of M-LLMs, offering a unified vision for their future in health care. This approach aims to guide both future research and practical implementations of M-LLMs in health care, positioning them as a paradigm shift toward integrated, multimodal data–driven medical practice. We anticipate that this work will spark further discussion and inspire the development of innovative approaches in the next generation of medical M-LLM systems.

[end paper 2]

[begin paper 3]

PMCID = 11960180

Title = Utilizing large language models for gastroenterology research: a conceptual framework

Large language models (LLMs) transform healthcare by assisting clinicians with decision-making, research, and patient management. In gastroenterology, LLMs have shown potential in clinical decision support, data extraction, and patient education. However, challenges such as bias, hallucinations, integration with clinical workflows, and regulatory compliance must be addressed for safe and effective implementation. This manuscript presents a structured framework for integrating LLMs into gastroenterology, using Hepatitis C treatment as a real-world application. The framework outlines key steps to ensure accuracy, safety, and clinical relevance while mitigating risks associated with artificial intelligence (AI)-driven healthcare tools. The framework includes defining clinical goals, assembling a multidisciplinary team, data collection and preparation, model selection, fine-tuning, calibration, hallucination mitigation, user interface development, integration with electronic health records, real-world validation, and continuous improvement. Retrieval-augmented generation and fine-tuning approaches are evaluated for optimizing model adaptability. Bias detection, reinforcement learning from human feedback, and structured prompt engineering are incorporated to enhance reliability. Ethical and regulatory considerations, including the Health Insurance Portability and Accountability Act, General Data Protection Regulation, and AI-specific guidelines (DECIDE-AI, SPIRIT-AI, CONSORT-AI), are addressed to ensure responsible AI deployment. LLMs have the potential to enhance decision-making, research efficiency, and patient care in gastroenterology, but responsible deployment requires bias mitigation, transparency, and ongoing validation. Future research should focus on multi-institutional validation and AI-assisted clinical trials to establish LLMs as reliable tools in gastroenterology.

 How large language models could transform gastroenterology: a framework for future research and care 

Artificial intelligence (AI) is transforming healthcare by helping doctors make better decisions, analyze research faster, and improve patient care. Large language models (LLMs) are a type of AI that process and generate human-like text, making them useful in gastroenterology. This paper presents a structured framework for safely using LLMs in clinical practice, using Hepatitis C treatment as an example. The framework begins by setting clear goals, such as improving Hepatitis C treatment recommendations or making patient education easier to understand. A team of doctors, AI specialists, and data experts is assembled to ensure the model is medically accurate and practical. Next, relevant medical data from electronic health records (EHRs), clinical guidelines, and research studies is gathered and prepared to improve AI, ensuring it provides useful and fair recommendations. The right AI model is then chosen and improved to specialize in gastroenterology. To make sure the model is reliable and makes correct suggestions, its performance is checked and adjusted before use. A user-friendly interface is created so doctors can access AI-generated recommendations directly in EHRs and decision-support tools, making it easy to integrate into daily practice. Before full use, the AI is tested in real-world settings, where gastroenterologists review its recommendations for safety and accuracy. Once in use, ongoing updates based on doctor feedback help improve its performance. Ethical and legal safeguards, such as protecting patient privacy and ensuring fairness, guide its responsible use. Findings are then shared with the medical community, allowing for further testing and broader adoption. By following this framework, LLMs can help doctors make better decisions, personalize treatments, and improve efficiency, ultimately leading to better patient outcomes in gastroenterology.

[end paper 3]

[begin paper 4]

PMCID = 11494256

Title = Use of SNOMED CT in Large Language Models: Scoping Review

Large language models (LLMs) have substantially advanced natural language processing (NLP) capabilities but often struggle with knowledge-driven tasks in specialized domains such as biomedicine. Integrating biomedical knowledge sources such as SNOMED CT into LLMs may enhance their performance on biomedical tasks. However, the methodologies and effectiveness of incorporating SNOMED CT into LLMs have not been systematically reviewed.

This scoping review aims to examine how SNOMED CT is integrated into LLMs, focusing on (1) the types and components of LLMs being integrated with SNOMED CT, (2) which contents of SNOMED CT are being integrated, and (3) whether this integration improves LLM performance on NLP tasks.

Following the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) guidelines, we searched ACM Digital Library, ACL Anthology, IEEE Xplore, PubMed, and Embase for relevant studies published from 2018 to 2023. Studies were included if they incorporated SNOMED CT into LLM pipelines for natural language understanding or generation tasks. Data on LLM types, SNOMED CT integration methods, end tasks, and performance metrics were extracted and synthesized.

The review included 37 studies. Bidirectional Encoder Representations from Transformers and its biomedical variants were the most commonly used LLMs. Three main approaches for integrating SNOMED CT were identified: (1) incorporating SNOMED CT into LLM inputs (28/37, 76%), primarily using concept descriptions to expand training corpora; (2) integrating SNOMED CT into additional fusion modules (5/37, 14%); and (3) using SNOMED CT as an external knowledge retriever during inference (5/37, 14%). The most frequent end task was medical concept normalization (15/37, 41%), followed by entity extraction or typing and classification. While most studies (17/19, 89%) reported performance improvements after SNOMED CT integration, only a small fraction (19/37, 51%) provided direct comparisons. The reported gains varied widely across different metrics and tasks, ranging from 0.87% to 131.66%. However, some studies showed either no improvement or a decline in certain performance metrics.

This review demonstrates diverse approaches for integrating SNOMED CT into LLMs, with a focus on using concept descriptions to enhance biomedical language understanding and generation. While the results suggest potential benefits of SNOMED CT integration, the lack of standardized evaluation methods and comprehensive performance reporting hinders definitive conclusions about its effectiveness. Future research should prioritize consistent reporting of performance comparisons and explore more sophisticated methods for incorporating SNOMED CT’s relational structure into LLMs. In addition, the biomedical NLP community should develop standardized evaluation frameworks to better assess the impact of ontology integration on LLM performance.

[end paper 4]

[begin paper 5]

PMCID = 11456558

Title = Large language model to multimodal large language model: A journey to shape the biological macromolecules to biological sciences and medicine

After ChatGPT was released, large language models (LLMs) became more popular. Academicians use ChatGPT or LLM models for different purposes, and the use of ChatGPT or LLM is increasing from medical science to diversified areas. Recently, the multimodal LLM (MLLM) has also become popular. Therefore, we comprehensively illustrate the LLM and MLLM models for a complete understanding. We also aim for simple and extended reviews of LLMs and MLLMs for a broad category of readers, such as researchers, students in diversified fields, and other academicians. The review article illustrates the LLM and MLLM models, their working principles, and their applications in diversified fields. First, we demonstrate the technical concept of LLMs, working principle, Black Box, and the evolution of LLMs. To explain the working principle, we discuss the tokenization process, token representation, and token relationships. We also extensively demonstrate the application of LLMs in biological macromolecules, medical science, biological science, and other areas. We illustrate the multimodal applications of LLMs or MLLMs. Finally, we illustrate the limitations, challenges, and future prospects of LLMs. The review acts as a booster dose for clinicians, a primer for molecular biologists, and a catalyst for scientists, and also benefits diversified academicians.

Chakraborty and colleagues extensively illustrate LMMs and MLLMs for a better understanding, along with the working principle of an LLM with the tokenization process, token representation, and token relationships. Moreover, the diversified applications of LLMs and MLLMs are discussed in biological macromolecules, biological sciences, medical science, and other areas.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "BioBERT fine-tuning clinical concept extraction phenotype definition":

[begin paper 1]

PMCID = 9972634

Title = Precision information extraction for rare disease epidemiology at scale

The United Nations recently made a call to address the challenges of an estimated 300 million persons worldwide living with a rare disease through the collection, analysis, and dissemination of disaggregated data. Epidemiologic Information (EI) regarding prevalence and incidence data of rare diseases is sparse and current paradigms of identifying, extracting, and curating EI rely upon time-intensive, error-prone manual processes. With these limitations, a clear understanding of the variation in epidemiology and outcomes for rare disease patients is hampered. This challenges the public health of rare diseases patients through a lack of information necessary to prioritize research, policy decisions, therapeutic development, and health system allocations.

In this study, we developed a newly curated epidemiology corpus for Named Entity Recognition (NER), a deep learning framework, and a novel rare disease epidemiologic information pipeline named EpiPipeline4RD consisting of a web interface and Restful API. For the corpus creation, we programmatically gathered a representative sample of rare disease epidemiologic abstracts, utilized weakly-supervised machine learning techniques to label the dataset, and manually validated the labeled dataset. For the deep learning framework development, we fine-tuned our dataset and adapted the BioBERT model for NER. We measured the performance of our BioBERT model for epidemiology entity recognition quantitatively with precision, recall, and F1 and qualitatively through a comparison with Orphanet. We demonstrated the ability for our pipeline to gather, identify, and extract epidemiology information from rare disease abstracts through three case studies.

We developed a deep learning model to extract EI with overall F1 scores of 0.817 and 0.878, evaluated at the entity-level and token-level respectively, and which achieved comparable qualitative results to Orphanet’s collection paradigm. Additionally, case studies of the rare diseases Classic homocystinuria, GRACILE syndrome, Phenylketonuria demonstrated the adequate recall of abstracts with epidemiology information, high precision of epidemiology information extraction through our deep learning model, and the increased efficiency of EpiPipeline4RD compared to a manual curation paradigm.

EpiPipeline4RD demonstrated high performance of EI extraction from rare disease literature to augment manual curation processes. This automated information curation paradigm will not only effectively empower development of the NIH Genetic and Rare Diseases Information Center (GARD), but also support the public health of the rare disease community.

The online version contains supplementary material available at 10.1186/s12967-023-04011-y.

[end paper 1]

[begin paper 2]

PMCID = 9135735

Title = Plant phenotype relationship corpus for biomedical relationships between plants and phenotypes

Medicinal plants have demonstrated therapeutic potential for applicability for a wide range of observable characteristics in the human body, known as “phenotype,” and have been considered favorably in clinical treatment. With an ever increasing interest in plants, many researchers have attempted to extract meaningful information by identifying relationships between plants and phenotypes from the existing literature. Although natural language processing (NLP) aims to extract useful information from unstructured textual data, there is no appropriate corpus available to train and evaluate the NLP model for plants and phenotypes. Therefore, in the present study, we have presented the plant-phenotype relationship (PPR) corpus, a high-quality resource that supports the development of various NLP fields; it includes information derived from 600 PubMed abstracts corresponding to 5,668 plant and 11,282 phenotype entities, and demonstrates a total of 9,709 relationships. We have also described benchmark results through named entity recognition and relation extraction systems to verify the quality of our data and to show the significant performance of NLP tasks in the PPR test set.

[end paper 2]

[begin paper 3]

PMCID = 10246054

Title = ARCH: Large-scale Knowledge Graph via Aggregated Narrative Codified Health Records Analysis

Electronic health record (EHR) systems contain a wealth of clinical data stored as both codified data and free-text narrative notes, covering hundreds of thousands of clinical concepts available for research and clinical care. The complex, massive, heterogeneous, and noisy nature of EHR data imposes significant challenges for feature representation, information extraction, and uncertainty quantification. To address these challenges, we proposed an efficient Aggregated naRrative Codified Health (ARCH) records analysis to generate a large-scale knowledge graph (KG) for a comprehensive set of EHR codified and narrative features.

The ARCH algorithm first derives embedding vectors from a co-occurrence matrix of all EHR concepts and then generates cosine similarities along with associated -values to measure the strength of relatedness between clinical features with statistical certainty quantification. In the final step, ARCH performs a sparse embedding regression to remove indirect linkage between entity pairs. We validated the clinical utility of the ARCH knowledge graph, generated from 12.5 million patients in the Veterans Affairs (VA) healthcare system, through downstream tasks including detecting known relationships between entity pairs, predicting drug side effects, disease phenotyping, as well as sub-typing Alzheimer’s disease patients.

ARCH produces high-quality clinical embeddings and KG for over 60,000 EHR concepts, as visualized in the R-shiny powered web-API (https://celehs.hms.harvard.edu/ARCH/). The ARCH embeddings attained an average area under the ROC curve (AUC) of 0.926 and 0.861 for detecting pairs of similar EHR concepts when the concepts are mapped to codified data and to NLP data; and 0.810 (codified) and 0.843 (NLP) for detecting related pairs. Based on the -values computed by ARCH, the sensitivity of detecting similar and related entity pairs are 0.906 and 0.888 under false discovery rate (FDR) control of 5%. For detecting drug side effects, the cosine similarity based on the ARCH semantic representations achieved an AUC of 0.723 while the AUC improved to 0.826 after few-shot training via minimizing the loss function on the training data set. Incorporating NLP data substantially improved the ability to detect side effects in the EHR. For example, based on unsupervised ARCH embeddings, the power of detecting drug-side effects pairs when using codified data only was 0.15, much lower than the power of 0.51 when using both codified and NLP concepts. Compared to existing large-scale representation learning methods including PubmedBERT, BioBERT and SAPBERT, ARCH attains the most robust performance and substantially higher accuracy in detecting these relationships. Incorporating ARCH selected features in weakly supervised phenotyping algorithms can improve the robustness of algorithm performance, especially for diseases that benefit from NLP features as supporting evidence. For example, the phenotyping algorithm for depression attained an AUC of 0.927 when using ARCH selected features but only 0.857 when using codified features selected via the KESER network. In addition, embeddings and knowledge graphs generated from the ARCH network were able to cluster AD patients into two subgroups, where the fast progression subgroup had a much higher mortality rate.

The proposed ARCH algorithm generates large-scale high-quality semantic representations and knowledge graph for both codified and NLP EHR features, useful for a wide range of predictive modeling tasks.

[end paper 3]

[begin paper 4]

PMCID = 11165580

Title = Vocabulary Matters: An Annotation Pipeline and Four Deep Learning Algorithms for Enzyme Named Entity Recognition

Enzymes are indispensable in many biological processes, and with biomedical literature growing exponentially, effective literature review becomes increasingly challenging. Natural language processing methods offer solutions to streamline this process. This study aims to develop an annotated enzyme corpus for training and evaluating enzyme named entity recognition (NER) models. A novel pipeline, combining dictionary matching and rule-based keyword searching, automatically annotated enzyme entities in >4800 full-text publications. Four deep learning NER models were created with different vocabularies (BioBERT/SciBERT) and architectures (BiLSTM/transformer) and evaluated on 526 manually annotated full-text publications. The annotation pipeline achieved an F1-score of 0.86 (precision = 1.00, recall = 0.76), surpassed by fine-tuned transformers for F1-score (BioBERT: 0.89, SciBERT: 0.88) and recall (0.86) with BiLSTM models having higher precision (0.94) than transformers (0.92). The annotation pipeline runs in seconds on standard laptops with almost perfect precision, but was outperformed by fine-tuned transformers in terms of F1-score and recall, demonstrating generalizability beyond the training data. In comparison, SciBERT-based models exhibited higher precision, and BioBERT-based models exhibited higher recall, highlighting the importance of vocabulary and architecture. These models, representing the first enzyme NER algorithms, enable more effective enzyme text mining and information extraction. Codes for automated annotation and model generation are available from  and .

[end paper 4]

[begin paper 5]

PMCID = 7665985

Title = Multi-Ontology Refined Embeddings (MORE): A Hybrid Multi-Ontology and Corpus-based Semantic Representation Model for Biomedical Concepts

Currently, a major limitation for natural language processing (NLP) analyses in clinical applications is that concepts are not effectively referenced in various forms across different texts. This paper introduces Multi-Ontology Refined Embeddings (MORE), a novel hybrid framework that incorporates domain knowledge from multiple ontologies into a distributional semantic model, learned from a corpus of clinical text.

We use the RadCore and MIMIC-III free-text datasets for the corpus-based component of MORE. For the ontology-based part, we use the Medical Subject Headings (MeSH) ontology and three state-of-the-art ontology-based similarity measures. In our approach, we propose a new learning objective, modified from the sigmoid cross-entropy objective function.

We used two established datasets of semantic similarities among biomedical concept pairs to evaluate the quality of the generated word embeddings. On the first dataset with 29 concept pairs, with similarity scores established by physicians and medical coders, MORE’s similarity scores have the highest combined correlation (0.633), which is 5.0% higher than that of the baseline model, and 12.4% higher than that of the best ontology-based similarity measure. On the second dataset with 449 concept pairs, MORE’s similarity scores have a correlation of 0.481, based on the average of four medical residents’ similarity ratings, and that outperforms the skip-gram model by 8.1%, and the best ontology measure by 6.9%. Furthermore, MORE outperforms three pre-trained transformer-based word embedding models (i.e., BERT, ClinicalBERT, and BioBERT) on both datasets.

MORE incorporates knowledge from several biomedical ontologies into an existing corpus-based distributional semantics model, improving both the accuracy of the learned word embeddings and the extensibility of the model to a broader range of biomedical concepts. MORE allows for more accurate clustering of concepts across a wide range of applications, such as analyzing patient health records to identify subjects with similar pathologies, or integrating heterogeneous clinical data to improve interoperability between hospitals.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "BioBERT fine-tuning clinical concept extraction clinical applications":

[begin paper 1]

PMCID = 11539635

Title = Multifaceted Natural Language Processing Task–Based Evaluation of Bidirectional Encoder Representations From Transformers Models for Bilingual (Korean and English) Clinical Notes: Algorithm Development and Validation

The bidirectional encoder representations from transformers (BERT) model has attracted considerable attention in clinical applications, such as patient classification and disease prediction. However, current studies have typically progressed to application development without a thorough assessment of the model’s comprehension of clinical context. Furthermore, limited comparative studies have been conducted on BERT models using medical documents from non–English-speaking countries. Therefore, the applicability of BERT models trained on English clinical notes to non-English contexts is yet to be confirmed. To address these gaps in literature, this study focused on identifying the most effective BERT model for non-English clinical notes.

In this study, we evaluated the contextual understanding abilities of various BERT models applied to mixed Korean and English clinical notes. The objective of this study was to identify the BERT model that excels in understanding the context of such documents.

Using data from 164,460 patients in a South Korean tertiary hospital, we pretrained BERT-base, BERT for Biomedical Text Mining (BioBERT), Korean BERT (KoBERT), and Multilingual BERT (M-BERT) to improve their contextual comprehension capabilities and subsequently compared their performances in 7 fine-tuning tasks.

The model performance varied based on the task and token usage. First, BERT-base and BioBERT excelled in tasks using classification ([CLS]) token embeddings, such as document classification. BioBERT achieved the highest F1-score of 89.32. Both BERT-base and BioBERT demonstrated their effectiveness in document pattern recognition, even with limited Korean tokens in the dictionary. Second, M-BERT exhibited a superior performance in reading comprehension tasks, achieving an F1-score of 93.77. Better results were obtained when fewer words were replaced with unknown ([UNK]) tokens. Third, M-BERT excelled in the knowledge inference task in which correct disease names were inferred from 63 candidate disease names in a document with disease names replaced with [MASK] tokens. M-BERT achieved the highest hit@10 score of 95.41.

This study highlighted the effectiveness of various BERT models in a multilingual clinical domain. The findings can be used as a reference in clinical and language-based applications.

[end paper 1]

[begin paper 2]

PMCID = 11772291

Title = Clinical entity-aware domain adaptation in low resource setting for inflammatory bowel disease

The digitization of healthcare records has revolutionized medical research and patient care, with electronic health records (EHRs) containing a wealth of structured and unstructured data. Extracting valuable information from unstructured clinical text presents a significant challenge, necessitating automated tools for efficient data mining. Natural language processing (NLP) methods have been pivotal in this endeavor, aiming to extract crucial clinical concepts embedded within free-form text. Our research addresses the imperative for robust biomedical entity extraction, focusing specifically on inflammatory bowel disease (IBD). Leveraging novel domain-specific pre-training and entity-aware masking strategies with contrastive learning, we fine-tune and adapt a general language model to be better adapted to IBD-related information extraction scenarios. Our named entity recognition (NER) tool streamlines the retrieval process, supporting annotation, correction, and visualization functionalities. In summary, we developed a comprehensive pipeline for clinical Dutch NER encompassing an efficient domain adaptation strategy with domain-aware masking and model fine-tuning enhancements, and an end-to-end entity extraction tool, significantly advancing medical record curation and clinical workflows.

[end paper 2]

[begin paper 3]

PMCID = 10140607

Title = Fine-tuning large neural language models for biomedical natural language processing

Large neural language models have transformed modern natural language processing (NLP) applications. However, fine-tuning such models for specific tasks remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP. We conduct a systematic study on fine-tuning stability in biomedical NLP. We show that fine-tuning performance may be sensitive to pretraining settings and conduct an exploration of techniques for addressing fine-tuning instability. We show that these techniques can substantially improve fine-tuning performance for low-resource biomedical NLP applications. Specifically, freezing lower layers is helpful for standard BERT- models, while layerwise decay is more effective for BERT- and ELECTRA models. For low-resource text similarity tasks, such as BIOSSES, reinitializing the top layers is the optimal strategy. Overall, domain-specific vocabulary and pretraining facilitate robust models for fine-tuning. Based on these findings, we establish a new state of the art on a wide range of biomedical NLP applications.

Systematic exploration of fine-tuning stability in biomedical NLP

Domain-specific vocabulary and pretraining facilitate robust models for fine-tuning

PubMedBERT-large and PubMedELECTRA models advance state-of-the-art in biomedical NLP

Large neural language models have transformed modern natural language processing (NLP) and have recently become a focus of public attention. However, fine-tuning these models for specific tasks of interest remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP.

This study conducts a systematic exploration of fine-tuning stability in biomedical NLP and identifies techniques that address instability and improve performance. The findings highlight the importance of domain-specific vocabulary and pretraining for creating robust models and establish a new state of the art on a wide range of biomedical NLP applications in the Biomedical Language Understanding and Reasoning Benchmark (BLURB).

Large neural language models have transformed modern natural language processing (NLP). However, fine-tuning these models for specific tasks remains challenging as model size increases, especially with small labeled datasets, which are common in biomedical NLP. This systematic exploration of fine-tuning stability in biomedical NLP highlights the importance of domain-specific vocabulary and pretraining for creating robust models and establishes a new state of the art on a wide range of biomedical NLP applications.

[end paper 3]

[begin paper 4]

PMCID = 9907889

Title = A prefix and attention map discrimination fusion guided attention for biomedical named entity recognition

The biomedical literature is growing rapidly, and it is increasingly important to extract meaningful information from the vast amount of literature. Biomedical named entity recognition (BioNER) is one of the key and fundamental tasks in biomedical text mining. It also acts as a primitive step for many downstream applications such as relation extraction and knowledge base completion. Therefore, the accurate identification of entities in biomedical literature has certain research value. However, this task is challenging due to the insufficiency of sequence labeling and the lack of large-scale labeled training data and domain knowledge.

In this paper, we use a novel word-pair classification method, design a simple attention mechanism and propose a novel architecture to solve the research difficulties of BioNER more efficiently without leveraging any external knowledge. Specifically, we break down the limitations of sequence labeling-based approaches by predicting the relationship between word pairs. Based on this, we enhance the pre-trained model BioBERT, through the proposed prefix and attention map dscrimination fusion guided attention and propose the E-BioBERT. Our proposed attention differentiates the distribution of different heads in different layers in the BioBERT, which enriches the diversity of self-attention. Our model is superior to state-of-the-art compared models on five available datasets: BC4CHEMD, BC2GM, BC5CDR-Disease, BC5CDR-Chem, and NCBI-Disease, achieving F1-score of 92.55%, 85.45%, 87.53%, 94.16% and 90.55%, respectively.

Compared with many previous various models, our method does not require additional training datasets, external knowledge, and complex training process. The experimental results on five BioNER benchmark datasets demonstrate that our model is better at mining semantic information, alleviating the problem of label inconsistency, and has higher entity recognition ability. More importantly, we analyze and demonstrate the effectiveness of our proposed attention.

[end paper 4]

[begin paper 5]

PMCID = 9141535

Title = Discovering Thematically Coherent Biomedical Documents Using Contextualized Bidirectional Encoder Representations from Transformers-Based Clustering

The increasing expansion of biomedical documents has increased the number of natural language textual resources related to the current applications. Meanwhile, there has been a great interest in extracting useful information from meaningful coherent groupings of textual content documents in the last decade. However, it is challenging to discover informative representations and define relevant articles from the rapidly growing biomedical literature due to the unsupervised nature of document clustering. Moreover, empirical investigations demonstrated that traditional text clustering methods produce unsatisfactory results in terms of non-contextualized vector space representations because that neglect the semantic relationship between biomedical texts. Recently, pre-trained language models have emerged as successful in a wide range of natural language processing applications. In this paper, we propose the Gaussian Mixture Model-based efficient clustering framework that incorporates substantially pre-trained (Bidirectional Encoder Representations from Transformers for Biomedical Text Mining) BioBERT domain-specific language representations to enhance the clustering accuracy. Our proposed framework consists of main three phases. First, classic text pre-processing techniques are used biomedical document data, which crawled from the PubMed repository. Second, representative vectors are extracted from a pre-trained BioBERT language model for biomedical text mining. Third, we employ the Gaussian Mixture Model as a clustering algorithm, which allows us to assign labels for each biomedical document. In order to prove the efficiency of our proposed model, we conducted a comprehensive experimental analysis utilizing several clustering algorithms while combining diverse embedding techniques. Consequently, the experimental results show that the proposed model outperforms the benchmark models by reaching performance measures of Fowlkes mallows score, silhouette coefficient, adjusted rand index, Davies-Bouldin score of 0.7817, 0.3765, 0.4478, 1.6849, respectively. We expect the outcomes of this study will assist domain specialists in comprehending thematically cohesive documents in the healthcare field.

[end paper 5]



Here are the top 5 articles on PubMed Central for the query "BioBERT fine-tuning clinical concept extraction clinician trust":

[begin paper 1]

PMCID = 11960180

Title = Utilizing large language models for gastroenterology research: a conceptual framework

Large language models (LLMs) transform healthcare by assisting clinicians with decision-making, research, and patient management. In gastroenterology, LLMs have shown potential in clinical decision support, data extraction, and patient education. However, challenges such as bias, hallucinations, integration with clinical workflows, and regulatory compliance must be addressed for safe and effective implementation. This manuscript presents a structured framework for integrating LLMs into gastroenterology, using Hepatitis C treatment as a real-world application. The framework outlines key steps to ensure accuracy, safety, and clinical relevance while mitigating risks associated with artificial intelligence (AI)-driven healthcare tools. The framework includes defining clinical goals, assembling a multidisciplinary team, data collection and preparation, model selection, fine-tuning, calibration, hallucination mitigation, user interface development, integration with electronic health records, real-world validation, and continuous improvement. Retrieval-augmented generation and fine-tuning approaches are evaluated for optimizing model adaptability. Bias detection, reinforcement learning from human feedback, and structured prompt engineering are incorporated to enhance reliability. Ethical and regulatory considerations, including the Health Insurance Portability and Accountability Act, General Data Protection Regulation, and AI-specific guidelines (DECIDE-AI, SPIRIT-AI, CONSORT-AI), are addressed to ensure responsible AI deployment. LLMs have the potential to enhance decision-making, research efficiency, and patient care in gastroenterology, but responsible deployment requires bias mitigation, transparency, and ongoing validation. Future research should focus on multi-institutional validation and AI-assisted clinical trials to establish LLMs as reliable tools in gastroenterology.

 How large language models could transform gastroenterology: a framework for future research and care 

Artificial intelligence (AI) is transforming healthcare by helping doctors make better decisions, analyze research faster, and improve patient care. Large language models (LLMs) are a type of AI that process and generate human-like text, making them useful in gastroenterology. This paper presents a structured framework for safely using LLMs in clinical practice, using Hepatitis C treatment as an example. The framework begins by setting clear goals, such as improving Hepatitis C treatment recommendations or making patient education easier to understand. A team of doctors, AI specialists, and data experts is assembled to ensure the model is medically accurate and practical. Next, relevant medical data from electronic health records (EHRs), clinical guidelines, and research studies is gathered and prepared to improve AI, ensuring it provides useful and fair recommendations. The right AI model is then chosen and improved to specialize in gastroenterology. To make sure the model is reliable and makes correct suggestions, its performance is checked and adjusted before use. A user-friendly interface is created so doctors can access AI-generated recommendations directly in EHRs and decision-support tools, making it easy to integrate into daily practice. Before full use, the AI is tested in real-world settings, where gastroenterologists review its recommendations for safety and accuracy. Once in use, ongoing updates based on doctor feedback help improve its performance. Ethical and legal safeguards, such as protecting patient privacy and ensuring fairness, guide its responsible use. Findings are then shared with the medical community, allowing for further testing and broader adoption. By following this framework, LLMs can help doctors make better decisions, personalize treatments, and improve efficiency, ultimately leading to better patient outcomes in gastroenterology.

[end paper 1]

[begin paper 2]

PMCID = 11586117

Title = Lightweight transformers for clinical natural language processing

Specialised pre-trained language models are becoming more frequent in Natural language Processing (NLP) since they can potentially outperform models trained on generic texts. BioBERT (Sanh et al., Distilbert, a distilled version of bert: smaller, faster, cheaper and lighter. arXiv preprint arXiv: 1910.01108, 2019) and BioClinicalBERT (Alsentzer et al., Publicly available clinical bert embeddings. In Proceedings of the 2nd Clinical Natural Language Processing Workshop, pp. 72–78, 2019) are two examples of such models that have shown promise in medical NLP tasks. Many of these models are overparametrised and resource-intensive, but thanks to techniques like knowledge distillation, it is possible to create smaller versions that perform almost as well as their larger counterparts. In this work, we specifically focus on development of compact language models for processing clinical texts (i.e. progress notes, discharge summaries, etc). We developed a number of efficient lightweight clinical transformers using knowledge distillation and continual learning, with the number of parameters ranging from  million to  million. These models performed comparably to larger models such as BioBERT and ClinicalBioBERT and significantly outperformed other compact models trained on general or biomedical data. Our extensive evaluation was done across several standard datasets and covered a wide range of clinical text-mining tasks, including natural language inference, relation extraction, named entity recognition and sequence classification. To our knowledge, this is the first comprehensive study specifically focused on creating efficient and compact transformers for clinical NLP tasks. The models and code used in this study can be found on our Huggingface profile at  and Github page at , respectively, promoting reproducibility of our results.

[end paper 2]

[begin paper 3]

PMCID = 8135980

Title = A neuro-symbolic method for understanding free-text medical evidence

We introduce Medical evidence Dependency (MD)–informed attention, a novel neuro-symbolic model for understanding free-text clinical trial publications with generalizability and interpretability.

We trained one head in the multi-head self-attention model to attend to the Medical evidence Ddependency (MD) and to pass linguistic and domain knowledge on to later layers (MD informed). This MD-informed attention model was integrated into BioBERT and tested on 2 public machine reading comprehension benchmarks for clinical trial publications: Evidence Inference 2.0 and PubMedQA. We also curated a small set of recently published articles reporting randomized controlled trials on COVID-19 (coronavirus disease 2019) following the Evidence Inference 2.0 guidelines to evaluate the model’s robustness to unseen data. 

The integration of MD-informed attention head improves BioBERT substantially in both benchmark tasks—as large as an increase of +30% in the F1 score—and achieves the new state-of-the-art performance on the Evidence Inference 2.0. It achieves 84% and 82% in overall accuracy and F1 score, respectively, on the unseen COVID-19 data.

 MD-informed attention empowers neural reading comprehension models with interpretability and generalizability via reusable domain knowledge. Its compositionality can benefit any transformer-based architecture for machine reading comprehension of free-text medical evidence.

[end paper 3]

[begin paper 4]

PMCID = 11464944

Title = Multimodal Large Language Models in Health Care: Applications, Challenges, and Future Outlook

In the complex and multidimensional field of medicine, multimodal data are prevalent and crucial for informed clinical decisions. Multimodal data span a broad spectrum of data types, including medical images (eg, MRI and CT scans), time-series data (eg, sensor data from wearable devices and electronic health records), audio recordings (eg, heart and respiratory sounds and patient interviews), text (eg, clinical notes and research articles), videos (eg, surgical procedures), and omics data (eg, genomics and proteomics). While advancements in large language models (LLMs) have enabled new applications for knowledge retrieval and processing in the medical field, most LLMs remain limited to processing unimodal data, typically text-based content, and often overlook the importance of integrating the diverse data modalities encountered in clinical practice. This paper aims to present a detailed, practical, and solution-oriented perspective on the use of multimodal LLMs (M-LLMs) in the medical field. Our investigation spanned M-LLM foundational principles, current and potential applications, technical and ethical challenges, and future research directions. By connecting these elements, we aimed to provide a comprehensive framework that links diverse aspects of M-LLMs, offering a unified vision for their future in health care. This approach aims to guide both future research and practical implementations of M-LLMs in health care, positioning them as a paradigm shift toward integrated, multimodal data–driven medical practice. We anticipate that this work will spark further discussion and inspire the development of innovative approaches in the next generation of medical M-LLM systems.

[end paper 4]

[begin paper 5]

PMCID = 11075180

Title = Advancing medical imaging with language models: featuring a spotlight on ChatGPT

This review paper aims to serve as a comprehensive guide and instructional resource for researchers seeking to effectively implement language models in medical imaging research. First, we presented the fundamental principles and evolution of language models, dedicating particular attention to large language models. We then reviewed the current literature on how language models are being used to improve medical imaging, emphasizing a range of applications such as image captioning, report generation, report classification, findings extraction, visual question response systems, interpretable diagnosis and so on. Notably, the capabilities of ChatGPT were spotlighted for researchers to explore its further applications. Furthermore, we covered the advantageous impacts of accurate and efficient language models in medical imaging analysis, such as the enhancement of clinical workflow efficiency, reduction of diagnostic errors, and assistance of clinicians in providing timely and accurate diagnoses. Overall, our goal is to have better integration of language models with medical imaging, thereby inspiring new ideas and innovations. It is our aspiration that this review can serve as a useful resource for researchers in this field, stimulating continued investigative and innovative pursuits of the application of language models in medical imaging.

[end paper 5]



