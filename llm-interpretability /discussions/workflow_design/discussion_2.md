## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use software techniques to develop a tool for large language model (LLM) interpretability in the context of creating electronic phenotype definitions, ideally, also incorporating a visual perspective to foster trust between the clinician and the model. To develop a tool for LLM interpretability in electronic phenotype definitions, we will adopt a machine learning approach, leveraging existing open-source interpretability libraries. Our focus will be on integrating SNOMED CT to enhance reasoning and reduce hallucinations, while incorporating visual elements to build clinician trust. 

Your team has developed four tools to improve the interpretability of large language models (LLMs) used for electronic phenotype definition in clinical notes: 
1. A BioBERT fine-tuning script (`bioBERT.py`) for token-level clinical concept extraction.
2. A SNOMED CT concept normalization tool (`snomed.py`) that maps extracted text spans to medical ontologies.
3. A SHAP/LIME visualization tool (`shap_lime.py`) that attributes importance to tokens.
4. An interactive Plotly dashboard (`plotly.py`) for clinicians to explore model outputs, token attributions, and provide feedback.

Your goal is to design a workflow that takes raw clinical notes and produces an interpretable output containing extracted phenotypes, linked SNOMED terms, SHAP/LIME token attributions, and a visual dashboard for feedback and inspection. This entire process should be modular, support batch processing, and minimize turnaround time for clinicians. 

In particular, interpretability must be maximized **without compromising reliability or traceability**, and outputs should be aligned with real-world ontologies (e.g., SNOMED CT) to support clinical integration. The dashboard should allow end-users (e.g., clinicians, data stewards) to review and comment on model outputs and explanations.

Please determine the ideal order of operations, data flow, feedback loop, and automation opportunities across all four tools. Assume that clinical notes come from a CSV, and model outputs are stored as JSON and CSV files. Be mindful of the time and resource constraints of real-world deployments.

Here are the agenda questions that must be answered:

1. What is the ideal order of operations for using bioBERT, SNOMED normalization, SHAP/LIME explanation, and Plotly visualization on a batch of clinical notes?

2. At what point in the workflow should token-level explanations (e.g., SHAP) be computed—before or after SNOMED mapping—and why?

3. How should outputs from the bioBERT extraction script be formatted and passed to the SNOMED and SHAP/LIME tools to ensure seamless integration?

4. What is the best way to incorporate clinician feedback from the Plotly dashboard back into the system to improve model performance or reliability?

5. How will you handle conflicting or ambiguous SNOMED matches for a given extracted phrase? Should confidence scores guide final mappings?

6. How will this workflow support both batch processing (many notes) and interactive use (single note review)? Should there be a switching mechanism?

7. At the end of the pipeline, how will the system log and store provenance information—i.e., which model produced which outputs using which parameters—for future auditing?

Principal Investigator, please provide your response to the agenda.

## Principal Investigator

### Agenda Responses:

1. **Ideal Order of Operations:**

   The ideal workflow begins with the **BioBERT fine-tuning script** (`bioBERT.py`) for token-level clinical concept extraction from raw clinical notes. Once the concepts are extracted, the next step is **SNOMED CT concept normalization** (`snomed.py`) to map these extracted text spans to standardized medical ontologies. Following normalization, we compute **token-level explanations** using SHAP/LIME (`shap_lime.py`) to attribute importance to the tokens. Finally, the results are visualized and made interactive using the **Plotly dashboard** (`plotly.py`), where clinicians can explore model outputs and provide feedback.

2. **Timing of Token-Level Explanations:**

   Token-level explanations (e.g., SHAP) should be computed **after SNOMED mapping**. The rationale is that after mapping, the model’s output is closer to a real-world application, thus providing clinicians with explanations tied directly to clinically relevant concepts. This ensures interpretability in a context clinicians understand and maximizes trust by aligning explanations with standardized terms.

3. **Integration Formatting:**

   Outputs from the BioBERT extraction should be formatted as JSON to ensure structured data flow. This JSON should include token spans and their corresponding confidence scores. This format will seamlessly integrate with SNOMED and SHAP/LIME tools by providing structured data for mapping and explanation. The JSON can then be enriched with SNOMED IDs and explanation scores before visualization.

4. **Incorporating Clinician Feedback:**

   Clinician feedback from the Plotly dashboard can be incorporated through an annotation mechanism embedded within the dashboard. Feedback can be recorded as JSON, which specifies the clinician’s comments on interpretations, corrections, or confirmations. This data should be fed back into the model training pipeline to update the weights and improve future model iterations, enhancing reliability and accuracy.

5. **Handling Conflicting SNOMED Matches:**

   In cases of conflicting or ambiguous SNOMED matches, confidence scores should guide the final mappings. A decision threshold can be established wherein matches with scores below a certain level are flagged for clinician review. This ensures that less confident mappings are verified by experts before integration into clinical workflows.

6. **Supporting Batch and Interactive Processes:**

   The workflow can support both batch processing and interactive use by implementing a flexible processing framework that includes a switching mechanism. This can be done through command-line arguments or a configuration file that specifies the batch or single-note mode. Batch processes can run through a queue system, while interactive use can be handled in near real-time within the dashboard.

7. **Logging and Storing Provenance Information:**

   At the end of the pipeline, provenance information, such as the model version, parameter settings, and timestamp, should be logged alongside the outputs in a database or structured log file. This information should be linked with a unique identifier for each processed note, ensuring transparency and traceability for future auditing and analysis.

By structuring the workflow in this way, we ensure that the tool is robust, scalable, and aligned with clinical needs while addressing interpretability and reliability concerns.

