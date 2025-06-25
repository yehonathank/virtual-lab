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

### Response to the Agenda

1. **Ideal Order of Operations:**

   - **Step 1: Data Ingestion and Preprocessing**
     - Clinical notes are read from a CSV file and preprocessed for tokenization and normalization (e.g., handling misspellings, standardizing terms).

   - **Step 2: BioBERT Token-Level Clinical Concept Extraction**
     - Use `bioBERT.py` to extract token-level clinical concepts from the preprocessed notes.

   - **Step 3: SNOMED CT Concept Normalization**
     - Pass the extracted concepts to `snomed.py` to map them to SNOMED CT terms, reducing ambiguity and enhancing interpretability.

   - **Step 4: SHAP/LIME Token-Level Explanation**
     - Apply `shap_lime.py` to compute token-level importance scores, which can be performed either before or after SNOMED mapping, depending on the desired granularity of explanations.

   - **Step 5: Data Packaging for Visualization**
     - Format all outputs (extracted phenotypes, SNOMED terms, SHAP/LIME attributions) into a JSON file for visual inspection.

   - **Step 6: Interactive Visualization and Feedback**
     - Load data into the `plotly.py` dashboard for clinician exploration, review, and feedback.

2. **Timing of Token-Level Explanations:**

   - Token-level explanations should ideally be computed **after SNOMED mapping**. This ensures that the importance scores are aligned with clinically meaningful concepts, providing clearer insights into the reasoning behind the model’s predictions and allowing clinicians to trace back from standardized terms.

3. **Output Formatting and Integration:**

   - The output from `bioBERT.py` should be formatted as a JSON object containing the extracted tokens, their positions, and preliminary confidence scores. This object is then passed to `snomed.py`, where each concept is mapped to a SNOMED CT term, creating a structured JSON enriched with semantic information.
   - This enriched JSON is subsequently used by `shap_lime.py` to generate importance scores, which are merged back into the JSON structure, ready for visualization.

4. **Incorporating Clinician Feedback:**

   - The Plotly dashboard should include a feature that allows clinicians to annotate outputs, suggest corrections, and indicate trust levels. This feedback can be logged and processed to refine model performance by retraining BioBERT with clinician-approved annotations or adjusting SNOMED mappings based on ground truth corrections.

5. **Handling Conflicting SNOMED Matches:**

   - Implement a confidence scoring system for SNOMED matches. When conflicts arise, prioritize matches with higher confidence scores. If ambiguity persists, flag these cases for manual review by clinicians, who can provide input through the dashboard.

6. **Support for Batch and Interactive Processing:**

   - Design the workflow to accommodate both **batch processing** and **interactive use cases**. Batch processing can be scheduled to run on a server, processing multiple notes and generating comprehensive reports. For interactive use, incorporate a real-time processing option within the dashboard, enabling clinicians to analyze individual notes as needed.
   - Implement a switching mechanism that allows users to toggle between batch and interactive modes, ensuring flexibility depending on the clinical context.

7. **Logging and Storing Provenance Information:**

   - Establish a logging system that captures details about each operation, including model versions, parameters, and timestamps. Store this provenance information in a database, linked to each output file, enabling future audits and reproducibility.
   - Ensure that all modifications, including clinician feedback and any resulting changes to model parameters or mappings, are logged to maintain a comprehensive history of the system’s evolution.

This structured approach aims to maximize interpretability, reliability, and clinician trust while supporting scalability and adaptability for different clinical environments.

