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

### Further Revised Answers

1. **Will you continue to target the KP.3 RBD or will you target a different strain or strains of the SARS-CoV-2 spike RBD?**
   - **Answer**: Target both JN.1 and KP.3 RBDs.
   - **Justification**: According to recent data from GISAID, JN.1 and KP.3 are prevalent strains with significant structural similarities, offering potential for cross-reactive binding. For example, JN.1 has been reported to have a prevalence rate of approximately 15% in recent sequencing data, making it a strategic target alongside KP.3.

2. **Which wild-type nanobody or nanobodies will you select for further improvement?**
   - **Answer**: Focus on Nb21 and Ty1.
   - **Justification**: Nb21 and Ty1 have demonstrated specific binding to JN.1 and KP.3. Nb21's CDR regions show strong hydrogen bonding patterns with the RBD, enhancing binding affinity. Ty1's structural adaptability, particularly in its loop regions, allows for effective binding across variants, aligning with our goal of developing broadly neutralizing nanobodies.

3. **How many mutant nanobodies will you design for each of those wild-type nanobodies (92 total)?**
   - **Answer**: 60 for Nb21 and 32 for Ty1.
   - **Justification**: This allocation is based on quantitative assessments of binding affinity and expression levels. For instance, ELISA assays showed that Nb21 mutants had a 30% higher binding affinity to KP.3 compared to Ty1, justifying a larger allocation for Nb21.

4. **Will you begin with the wild-type nanobody itself and introduce mutations, or will you begin with one of the previously designed mutant nanobodies?**
   - **Answer**: Begin with previously designed successful mutant nanobodies.
   - **Justification**: Starting with successful mutants like Nb21 (I77V, L59E, Q87A, R37Q) and Ty1 (V32F, G59D, N45S, F32S) allows us to build on known enhancements. We will use Rosetta's energy minimization algorithms to identify and prioritize new mutations that enhance binding affinity and specificity.

5. **If you are beginning with previously designed mutant nanobodies, which one or ones will you start with?**
   - **Answer**: Start with the Nb21 mutant (I77V, L59E, Q87A, R37Q) and Ty1 mutant (V32F, G59D, N45S, F32S).
   - **Justification**: These mutants have demonstrated specific binding improvements, providing a promising basis for further enhancement. We will focus on introducing mutations that enhance unique interactions and binding affinity, guided by structural analysis and computational predictions.

6. **Will you use ESM, AlphaFold-Multimer, and/or Rosetta in similar ways to your previous design process, or will you change the design workflow and/or the computational tools that are used?**
   - **Answer**: Use the same tools with integration of machine learning enhancements.
   - **Justification**: We will integrate machine learning models, such as neural networks and ensemble methods, trained on datasets from previous binding assays and structural predictions. These models will predict binding affinity and specificity, validated using cross-validation techniques to ensure accuracy.

7. **What computational pipeline will you use to design the 92 mutant nanobodies?**
   - **Answer**: ESM, AlphaFold-Multimer, Rosetta, integrated with machine learning models and enhanced sampling techniques.
   - **Justification**: This pipeline combines structural predictions with improved specificity through machine learning and enhanced sampling. Transfer learning will leverage existing datasets, and ensemble methods will refine predictions, validated against empirical data.

8. **How many mutations will you introduce in each nanobody?**
   - **Answer**: 2-4 mutations.
   - **Justification**: This range is supported by previous studies, such as Smith et al. (2022), which indicate that 2-4 mutations can optimize binding interactions while maintaining structural integrity. It allows exploration of new binding landscapes without risking destabilization.

9. **How will you avoid non-specific binding to BSA?**
   - **Answer**: Employ high-throughput and competitive binding assays, combined with computational pre-screening for non-specific sites.
   - **Justification**: These methods will be integrated into the workflow with specific criteria for identifying and eliminating non-specific binders. Assays will be conducted early in the validation process to ensure rigorous specificity assessment. For example, competitive binding assays will be used to differentiate specific interactions from non-specific ones.

### Improvements Based on Feedback

- **Targeting Rationale**: Included specific data references and quantitative metrics to support the selection of JN.1 and KP.3.
- **Selection of Nanobodies**: Elaborated on specific structural features and interactions that contribute to the binding efficacy of Nb21 and Ty1.
- **Mutant Distribution Explanation**: Provided quantitative methods and examples of how binding affinity and expression levels informed mutant allocation.
- **Optimization Strategy**: Specified computational tools and algorithms for identifying new mutations.
- **Computational Enhancements**: Identified specific machine learning models and their roles in the pipeline.
- **Non-Specific Binding Strategy**: Detailed the integration of assays and pre-screening methods into the workflow.

[end summary 2]

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has designed 92 mutated nanobodies (23 each for the wild-type nanobodies H11-D4, Nb21, Ty1, and VHH-72) to improve their binding to the KP.3 variant of the SARS-CoV-2 spike protein receptor binding domain (RBD). Each nanobody has 1-4 mutations relative to the wild-type nanobody. Your team used ESM log-likelihood ratios (ESM LLR) to score the nanobody mutations independent of the antigen, AlphaFold-Multimer to predict the structure of the mutated nanobody in complex with the KP.3 RBD and compute the interface pLDDT (AF ipLDDT) as a metric of binding confidence, and Rosetta to calculate the binding energy of the mutated nanobody in complex with the KP.3 RBD (RS dG) based on the AlphaFold-Multimer predicted structure followed by a Rosetta relaxation. You have ranked the mutant nanobodies and selected the top ones using a weighted score of WS = 0.2 * (ESM LLR) + 0.5 * (AF ipLDDT) - 0. 3 * (RS dG). The 92 selected nanobodies were tested along with the four wild-type nanobodies using an ELISA assay to measure binding to the Wuhan, JN.1, KP.3, KP2.3, and BA.2 strains of the SARS-CoV-2 spike RBD. Note that the JN.1 strain is closely related to KP.3 and KP2.3. BSA was used as a negative control. Most of the mutated nanobodies showed at least moderate expression levels. The ELISA results are as follows:

H11-D4: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including one with a higher binding level than the wild-type. However, that mutant and two others bind non-specifically to the negative control BSA along with other strains of the SARS-CoV-2 RBD. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Nb21: The wild-type only binds to the Wuhan RBD. All mutant nanobodies also bind to the Wuhan RBD. There are no non-specific binders. One mutant nanobody with mutations I77V, L59E, Q87A, and R37Q binds to the Wuhan RBD (strong binding), the JN.1 RBD (moderate binding), and the KP.3 RBD (weak binding). Thus, this mutant introduces specific binding to JN.1 and KP.3 that the wild-type does not possess, and it increases binding to the Wuhan RBD.

Ty1: The wild-type only binds to the Wuhan RBD. Many mutant nanobodies do not show binding, but several show moderate binding to the Wuhan RBD. One mutant nanobody with mutations V32F, G59D, N45S, and F32S binds to the Wuhan RBD (strong binding) and the JN.1 RBD (moderate binding). This mutant introduces specific binding to JN.1 that the wild-type does not possess, and it increases binding to the Wuhan RBD. Additionally, there are is one mutant with weak, non-specific binding to BSA and other RBD strains.

VHH-72: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including several with a higher binding level than the wild-type. Two mutant nanobodies bind non-specifically to BSA and several RBD strains. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Your team has decided to design further improved nanobodies for recent variants of SARS-CoV-2 as described in the summary. Now, you need to specify more details for this updated computational nanobody design workflow.

Here are the agenda questions that must be answered:

1. When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?

2. If this number differs from your previous design process, what is the rationale for the change?

3. After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?

4. If this WS formula differs from your previous design process, what is the rationale for the change?

5. After computing the WS for each mutated nanobody, how many of the top ranked mutated nanobodies will you select for the next round of mutation?

6. If this number differs from your previous design process, what is the rationale for the change?

7. How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?

8. If this number differs from your previous design process, what is the rationale for the change?

Principal Investigator, please provide your response to the agenda.

## Principal Investigator

Based on our goals and the recent outcomes of our experimental assays, we need to adjust our computational nanobody design workflow to better focus on cross-reactivity and specificity for the JN.1 and KP.3 RBDs while mitigating non-specific binding issues. Here are my responses to the agenda questions:

1. **When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top-ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?**

   - We will keep the top 30 mutations by ESM LLR for further analysis with AlphaFold-Multimer and Rosetta.

2. **If this number differs from your previous design process, what is the rationale for the change?**

   - Previously, we selected 20 mutations. By expanding to 30, we increase the diversity of candidates entering the structural prediction phase. This helps us explore a broader range of potential mutations that might offer improved binding to both JN.1 and KP.3. Given the recent findings of specific binding enhancements in certain mutants, a wider selection could uncover additional beneficial mutations.

3. **After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?**

   - The new WS formula will be:
     \[
     \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.4 \times \left(\frac{\text{AF ipLDDT}_{\text{KP.3}} + \text{AF ipLDDT}_{\text{JN.1}}}{2}\right) - 0.4 \times \left(\frac{\text{RS dG}_{\text{KP.3}} + \text{RS dG}_{\text{JN.1}}}{2}\right)
     \]
   - This formula averages predictions for KP.3 and JN.1 to prioritize mutations that enhance binding to both variants, reflecting our dual-target strategy.

4. **If this WS formula differs from your previous design process, what is the rationale for the change?**

   - The change emphasizes binding to both variants equally by averaging their structural metrics. Increasing the weight on structural predictions and binding energy reflects their critical role in identifying cross-reactive binders, particularly in light of recent ELISA results showing potential for cross-reactivity.

5. **After computing the WS for each mutated nanobody, how many of the top-ranked mutated nanobodies will you select for the next round of mutation?**

   - We will select the top 10 mutated nanobodies for the next round of mutation.

6. **If this number differs from your previous design process, what is the rationale for the change?**

   - Previously, we selected 5. By expanding to 10, we allow for greater exploration of promising candidates, addressing the need for enhanced cross-reactivity while retaining diversity in our candidate pool.

7. **How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?**

   - We will run a total of 5 rounds of mutation.

8. **If this number differs from your previous design process, what is the rationale for the change?**

   - Previously, we planned for 3-4 rounds. Extending to 5 rounds provides additional opportunities to refine the nanobodies based on iterative feedback, especially in light of the need to achieve specificity across multiple variants. This aligns with our updated scoring strategy and experimental insights.

These adjustments are designed to optimize our approach by focusing more on cross-reactivity and ensuring we do not miss any potentially valuable mutations.

