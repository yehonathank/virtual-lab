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

Let's address each agenda question systematically to design an efficient and effective workflow for enhancing LLM interpretability in electronic phenotype definitions:

1. **Ideal Order of Operations:**
   - **Step 1:** **BioBERT Fine-Tuning and Concept Extraction:** Start by processing the batch of clinical notes with the `bioBERT.py` script to perform token-level clinical concept extraction.
   - **Step 2:** **SNOMED CT Concept Normalization:** Use the `snomed.py` tool to map the extracted text spans to their corresponding SNOMED CT terms. This ensures alignment with medical ontologies early in the process.
   - **Step 3:** **SHAP/LIME Explanation:** Apply the `shap_lime.py` tool to generate token-level explanations. By doing this after SNOMED mapping, explanations are more contextually relevant to standardized clinical terms.
   - **Step 4:** **Plotly Visualization:** Finally, visualize the results in the `plotly.py` dashboard, where clinicians can interact with outputs and provide feedback.

2. **Timing for Token-Level Explanations:**
   - Compute token-level explanations **after SNOMED mapping**. This ensures that the attribution of importance is directly linked to standardized clinical concepts, making the explanations more meaningful and reliable from a clinical standpoint.

3. **Formatting and Integration of Outputs:**
   - The output from `bioBERT.py` should be a structured JSON file containing extracted tokens and their predicted clinical concepts. This JSON can be directly consumed by `snomed.py` for normalization and then passed to `shap_lime.py` for generating explanations. Consistent JSON object keys must be maintained across scripts for seamless integration.

4. **Incorporating Clinician Feedback:**
   - Design the Plotly dashboard to capture clinician feedback on both the accuracy of extracted phenotypes and the relevance of SHAP/LIME attributions. Feedback should be logged in a structured format (e.g., JSON) and processed by a feedback module that can fine-tune the BioBERT model and adjust the mapping rules in `snomed.py`.

5. **Handling Conflicting SNOMED Matches:**
   - Use confidence scores to guide the final mapping of extracted phrases to SNOMED terms. In cases of conflict or ambiguity, the system should present options to the clinician for manual selection in the dashboard. Additionally, maintain a log of such instances to improve the normalization tool.

6. **Supporting Batch and Interactive Use:**
   - Implement a dual-mode system:
     - **Batch Mode:** For processing multiple notes, automate the complete pipeline, from extraction to dashboard visualization, minimizing manual intervention.
     - **Interactive Mode:** Allow clinicians to input a single note and immediately receive processed outputs in the dashboard, facilitating detailed review. A user interface toggle or command-line parameter can switch between modes.

7. **Logging and Storing Provenance Information:**
   - Implement a logging mechanism that records the model version, parameter settings, input data, and output results for each run. Store this provenance information in a centralized database or a structured log file (e.g., JSON) to ensure traceability and facilitate future audits.

By following this workflow, we can ensure that the tool maximizes interpretability while maintaining reliability and traceability, ultimately fostering clinician trust in the system.

