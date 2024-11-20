## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

Based on the summaries provided, here is a consolidated plan for using ESM, AlphaFold-Multimer, and Rosetta in the iterative design process to develop modified nanobodies for the newest variant of the SARS-CoV-2 spike protein:

### 1. Order of Operations for Evaluating Mutations
In each iteration, the order of operations will be:
- **Step 1: ESM Evaluation** - Use ESM to evaluate all potential single-point mutations to the nanobody. This step is computationally efficient and provides an initial filter based on log-likelihood ratios.
- **Step 2: AlphaFold-Multimer Evaluation** - Select the top mutations based on ESM scores and use AlphaFold-Multimer to predict the nanobody-antigen complex structure. This step refines the selection by modeling structural interactions.
- **Step 3: Rosetta Evaluation** - Use Rosetta to evaluate the binding energy of the nanobody-antigen complex based on the structure predicted by AlphaFold-Multimer.

### 2. Number of Mutations to Evaluate
- **ESM**: Evaluate all possible single-point mutations in the nanobody sequence.
- **AlphaFold-Multimer and Rosetta**: Evaluate the top 20 mutations from the ESM step. This balances computational resources and the need for detailed structural predictions.

### 3. Scoring Formula and Ranking
At the end of each iteration, mutations will be ranked using a weighted scoring system:
\[ \text{Score} = w_1 \times \text{(ESM Log-Likelihood Ratio)} + w_2 \times \text{(AlphaFold-Multimer Interface pLDDT)} - w_3 \times \text{(Rosetta Binding Energy)} \]
- Initial weights: \( w_1 = 0.2 \), \( w_2 = 0.5 \), \( w_3 = 0.3 \). These weights reflect the relative importance of each score, with a focus on structural stability and binding affinity.

### 4. Number of Top-Ranked Mutations to Keep
- Keep the top 5 mutations from each iteration for further consideration. This ensures a manageable number of candidates while maintaining diversity.

### 5. Deciding on the Number of Iterations
- Plan for 3-4 iterations, allowing for refinement of nanobody candidates while maintaining a practical timeline. Monitor the convergence of scores and diversity of mutations; stop if improvements plateau or if time/resources become constrained.

### 6. Selecting the Final Set of 24 Modified Nanobodies
- **Step 1**: Compile all top mutations from each iteration.
- **Step 2**: Rank these mutations using the combined score formula.
- **Step 3**: Select the top 24 unique nanobody sequences with the highest scores, ensuring diversity by selecting different mutation sites whenever possible.
- **Step 4**: Use domain expertise to further refine this list, considering potential cross-reactivity and structural integrity.
- **Step 5**: Validate these computer-generated designs experimentally to confirm enhanced binding across variants.

### Explanation of Component Selection
- **Order of Operations**: Consistently across summaries, ESM is used first for its speed, followed by AlphaFold-Multimer and Rosetta, which require structural predictions.
- **Number of Mutations**: The choice of evaluating 20 mutations with AlphaFold-Multimer and Rosetta balances computational constraints and the need for detailed analysis (from summaries 1, 3, and 5).
- **Scoring Formula**: The weights \( w_1 = 0.2 \), \( w_2 = 0.5 \), \( w_3 = 0.3 \) are chosen based on summaries 2, 3, and 5, emphasizing structural predictions and binding energy.
- **Number of Top Mutations**: Keeping 5 mutations per iteration is a compromise between summaries 1, 3, and 4, ensuring diversity and manageability.
- **Iterations**: 3-4 iterations are suggested in summaries 2, 4, and 5, balancing exploration and resource constraints.
- **Final Selection**: Steps for selecting the final set are synthesized from summaries 3, 4, and 5, focusing on diversity and expert validation.

This plan optimizes the use of computational tools within the given constraints, aiming to identify promising nanobody candidates efficiently.

[end summary 1]

[begin summary 2]

### Revised Answers

1. **Will you continue to target the KP.3 RBD or will you target a different strain or strains of the SARS-CoV-2 spike RBD?**

   - **Answer**: Target both KP.3 and JN.1 RBDs.
   - **Justification**: KP.3 and JN.1 are not only epidemiologically significant but also closely related, enhancing the potential for cross-reactivity and broader neutralization capabilities. To address potential challenges such as future mutations, we will implement regular genomic surveillance and collaborate with epidemiologists to monitor emerging variants. This proactive approach will allow us to adapt our research strategy as needed.

2. **Which wild-type nanobody or nanobodies will you select for further improvement?**

   - **Answer**: Nb21 and Ty1.
   - **Justification**: These nanobodies have demonstrated enhanced binding profiles in the ELISA results, making them ideal candidates for further improvement. H11-D4 and VHH-72 were excluded because their mutants did not show specific binding to strains other than the Wuhan RBD, and some exhibited non-specific binding. However, if new data suggests improved specificity or if new variants emerge that these nanobodies can target effectively, we will reconsider their inclusion.

3. **How many mutant nanobodies will you design for each of those wild-type nanobodies (92 total)?**

   - **Answer**: 60 for Nb21 and 32 for Ty1.
   - **Justification**: The allocation is based on the stronger binding profile of Nb21 mutants across multiple strains, as shown in the ELISA results. Binding strength and specificity were quantitatively assessed by measuring absorbance values in ELISA, with higher values indicating stronger binding. These assessments will guide future iterations of mutant design, ensuring continuous improvement by focusing on enhancing binding affinity and specificity.

4. **Will you begin with the wild-type nanobody itself and introduce mutations, or will you begin with one of the previously designed mutant nanobodies?**

   - **Answer**: Begin with previously designed mutant nanobodies.
   - **Justification**: Starting with successful mutants allows us to build on known improvements, enhancing efficiency and effectiveness. Success is defined by the ability of mutants to bind specifically to multiple RBDs, as demonstrated in ELISA results, without non-specific binding to BSA. Additional metrics such as binding kinetics and thermodynamic stability will also be considered in future evaluations.

5. **If you are beginning with previously designed mutant nanobodies, which one or ones will you start with?**

   - **Answer**: Start with the Nb21 mutant (I77V, L59E, Q87A, R37Q) and the Ty1 mutant (V32F, G59D, N45S, F32S).
   - **Justification**: These mutants have shown specific binding improvements and cross-variant potential, making them solid foundations for further modifications. The ELISA results confirm their enhanced binding profiles to JN.1 and KP.3.

6. **Will you continue to use the same general ESM, AlphaFold-Multimer, and Rosetta design pipeline you previously used, or will you design a new computational pipeline?**

   - **Answer**: Enhance the existing pipeline with additional simulations and machine learning techniques.
   - **Justification**: We will integrate molecular dynamics simulations using GROMACS and AMBER to evaluate binding interactions and stability, chosen for their robust capabilities in simulating biomolecular systems. Additionally, we will incorporate graph neural networks and ensemble learning to refine predictions of non-specific binding and cross-reactivity, selected for their ability to handle complex data and improve model accuracy. While these techniques are powerful, we will address potential limitations such as computational cost and model interpretability by optimizing simulation parameters and ensuring transparent reporting of model predictions.

### Additional Improvements

- **Strategies for Monitoring Mutations**: By implementing genomic surveillance and collaborating with epidemiologists, we ensure a proactive approach to adapting our research strategy in response to emerging variants.

- **Criteria for Reconsideration of Excluded Nanobodies**: Specifying the types of data or developments that would prompt a reevaluation of H11-D4 and VHH-72 provides clear criteria for their potential inclusion.

- **Informing Future Iterations**: Quantitative assessments of binding will guide future mutant design, focusing on enhancing binding affinity and specificity to ensure continuous improvement.

- **Comprehensive Evaluation of Mutants**: Including additional metrics such as binding kinetics and thermodynamic stability ensures a thorough evaluation process for continuing with successful mutants.

- **Addressing Limitations of Techniques**: By discussing potential limitations and how they will be addressed, we ensure that the pipeline remains robust and adaptable to the project's needs.

By incorporating these improvements, the revised answer is more detailed, transparent, and aligned with the research project's objectives.

[end summary 2]

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has designed 92 mutated nanobodies (23 each for the wild-type nanobodies H11-D4, Nb21, Ty1, and VHH-72) to improve their binding to the KP.3 variant of the SARS-CoV-2 spike protein receptor binding domain (RBD). Each nanobody has 1-4 mutations relative to the wild-type nanobody. Your team used ESM log-likelihood ratios (ESM LLR) to score the nanobody mutations independent of the antigen, AlphaFold-Multimer to predict the structure of the mutated nanobody in complex with the KP.3 RBD and compute the interface pLDDT (AF ipLDDT) as a metric of binding confidence, and Rosetta to calculate the binding energy of the mutated nanobody in complex with the KP.3 RBD (RS dG) based on the AlphaFold-Multimer predicted structure followed by a Rosetta relaxation. You have ranked the mutant nanobodies and selected the top ones using a weighted score of WS = 0.2 * (ESM LLR) + 0.5 * (AF ipLDDT) - 0. 3 * (RS dG). The 92 selected nanobodies were tested along with the four wild-type nanobodies using an ELISA assay to measure binding to the Wuhan, JN.1, KP.3, KP2.3, and BA.2 strains of the SARS-CoV-2 spike RBD. Note that the JN.1 strain is closely related to KP.3 and KP2.3. BSA was used as a negative control. Most of the mutated nanobodies showed at least moderate expression levels. The ELISA results are as follows:

H11-D4: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including one with a higher binding level than the wild-type. However, that mutant and two others bind non-specifically to the negative control BSA along with other strains of the SARS-CoV-2 RBD. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Nb21: The wild-type only binds to the Wuhan RBD. All mutant nanobodies also bind to the Wuhan RBD. There are no non-specific binders. One mutant nanobody with mutations I77V, L59E, Q87A, and R37Q binds to the Wuhan RBD (strong binding), the JN.1 RBD (moderate binding), and the KP.3 RBD (weak binding). Thus, this mutant introduces specific binding to JN.1 and KP.3 that the wild-type does not possess, and it increases binding to the Wuhan RBD.

Ty1: The wild-type only binds to the Wuhan RBD. Many mutant nanobodies do not show binding, but several show moderate binding to the Wuhan RBD. One mutant nanobody with mutations V32F, G59D, N45S, and F32S binds to the Wuhan RBD (strong binding) and the JN.1 RBD (moderate binding). This mutant introduces specific binding to JN.1 that the wild-type does not possess, and it increases binding to the Wuhan RBD. Additionally, there are is one mutant with weak, non-specific binding to BSA and other RBD strains.

VHH-72: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including several with a higher binding level than the wild-type. Two mutant nanobodies bind non-specifically to BSA and several RBD strains. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Your team has decided to design further improved nanobodies for recent variants of SARS-CoV-2 as described in the summary using the same general ESM, AlphaFold-Multimer, and Rosetta computational design pipeline. ESM will again be used to evaluate the overall quality of mutated nanobodies while AlphaFold-Multimer and Rosetta will be used to determine their specific binding to your selected SARS-CoV-2 variants. Now, you need to specify more details for this updated design workflow.

Here are the agenda questions that must be answered:

1. When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta out of the ~2,000 possible mutations?

2. If this number differs from your previous design process, what is the rationale for the change?

3. After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?

4. If this WS formula differs from your previous design process, what is the rationale for the change?

5. After computing the WS for each mutated nanobody, how many of the top ranked mutated nanobodies will you select for the next round of mutation?

6. If this number differs from your previous design process, what is the rationale for the change?

7. How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?

8. If this number differs from your previous design process, what is the rationale for the change?

Principal Investigator, please provide your response to the agenda.

## Principal Investigator

Based on the provided project summaries and the agenda for this meeting, here are my responses to the questions:

1. **When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta out of the ~2,000 possible mutations?**

   - We will keep the top 50 mutations ranked by ESM LLR for further analysis by AlphaFold-Multimer and Rosetta.

2. **If this number differs from your previous design process, what is the rationale for the change?**

   - This is an increase from the previous top 20 mutations. The rationale for this change is to expand the exploration space in light of the complex nature of binding to multiple RBD variants (JN.1 and KP.3). This allows us to capture a broader range of potential beneficial mutations that may confer enhanced cross-variant binding, considering the moderate binding improvements observed based on ELISA results.

3. **After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?**

   - The new weighted score (WS) formula will be:
     \[
     \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.25 \times (\text{AF ipLDDT for JN.1}) + 0.25 \times (\text{AF ipLDDT for KP.3}) - 0.15 \times (\text{RS dG for JN.1}) - 0.15 \times (\text{RS dG for KP.3})
     \]
   - This formula separately accounts for the structural confidence (ipLDDT) and binding energy (dG) for both the JN.1 and KP.3 RBDs to ensure each variant's interactions are equally weighted.

4. **If this WS formula differs from your previous design process, what is the rationale for the change?**

   - The adjustment in the formula reflects the need to balance enhancements across both RBD variants, given their epidemiological significance. By splitting the AlphaFold-Multimer and Rosetta components equally between JN.1 and KP.3, we ensure that the design pipeline accommodates potential trade-offs in binding affinity and structural stability between the two variants, thus broadening the therapeutic potential.

5. **After computing the WS for each mutated nanobody, how many of the top ranked mutated nanobodies will you select for the next round of mutation?**

   - We will select the top 10 mutated nanobodies for the next round of mutation.

6. **If this number differs from your previous design process, what is the rationale for the change?**

   - This is a reduction from the previously suggested 5 nanobodies per iteration. The decision to keep more candidates caters to exploring a diverse array of promising mutations early in the design process, which may later be refined and downselected based on comprehensive binding and specificity profiles.

7. **How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?**

   - We will conduct 3 rounds of mutation.

8. **If this number differs from your previous design process, what is the rationale for the change?**

   - This aligns with our previous plan of 3-4 iterations, but now explicitly set to 3 based on the current project timeline and computational resources. The aim is to ensure sufficient exploration and refinement while being pragmatic about the iterative cycle's complexity given the dual variant focus.

These responses optimize our design and validation strategy in seeking nanobodies with the desired cross-variant binding properties, ensuring the project's scientific robustness and efficiency.

