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

Let's address each of the agenda questions systematically:

1. **Ideal Order of Operations:**
   - **Step 1:** Preprocess Clinical Notes - Extract clinical notes from the CSV and prepare them for processing.
   - **Step 2:** BioBERT Token-Level Clinical Concept Extraction - Use `bioBERT.py` to extract relevant clinical concepts from the notes.
   - **Step 3:** SNOMED CT Concept Normalization - Pass extracted concepts from BioBERT to `snomed.py` for mapping to SNOMED CT terms.
   - **Step 4:** SHAP/LIME Explanation - Use the `shap_lime.py` tool to compute token-level explanations for the mapped SNOMED concepts.
   - **Step 5:** Plotly Visualization - Load results into the `plotly.py` dashboard for interactive review, visualization, and feedback from clinicians.
   - **Step 6:** Feedback Integration - Gather clinician feedback from the dashboard to iterate and improve the models.

2. **Timing for Token-Level Explanations (SHAP/LIME):**
   - Token-level explanations should ideally be computed **after SNOMED mapping**. This ensures that explanations are focused on standardized medical concepts, making them more interpretable and relevant to clinicians. This approach also helps in identifying which SNOMED terms are most influential in the decision-making process.

3. **Output Formatting for Seamless Integration:**
   - Outputs from `bioBERT.py` should be structured as JSON files containing token-level information with associated scores. These should include metadata like sentence position and context. This JSON can be directly ingested by `snomed.py` to map to SNOMED terms, which will, in turn, output another JSON with SNOMED IDs and descriptions for `shap_lime.py`. Consistency in the data structure is key.

4. **Incorporating Clinician Feedback:**
   - Clinician feedback should be collected through the Plotly dashboard and stored in a database with links to the specific model outputs they reviewed. This feedback can be used to retrain models or adjust SNOMED mappings. Implement a mechanism for annotators to flag incorrect mappings or explanations directly, and prioritize recurring feedback in model updates.

5. **Handling Conflicting SNOMED Matches:**
   - For conflicting or ambiguous SNOMED matches, use confidence scores to guide final decisions. Incorporate a threshold below which a match is flagged for review. Additionally, provide clinicians with options to select the most appropriate term from a list of probable matches via the dashboard.

6. **Supporting Batch Processing and Interactive Use:**
   - Implement a mode-switching mechanism within the application to toggle between batch processing and interactive single-note review. For batch processing, enable parallel processing of notes to enhance efficiency. For single-note review, prioritize real-time processing and immediate feedback integration within the dashboard.

7. **Logging and Storing Provenance Information:**
   - Create a logging mechanism to store details about the models used (e.g., BioBERT version, SNOMED database version), parameters, timestamps, and data transformations in a database. Each output should be tagged with a unique identifier linking back to these logs for auditing purposes. Ensure this provenance information can be easily retrieved and reviewed by stakeholders.

By following this structured workflow, we maximize interpretability and reliability while effectively integrating clinician feedback. This setup also allows for continuous improvement and scalability in both batch and interactive settings.

