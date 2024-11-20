## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

### Response to Agenda

1. **Number of Top Mutations to Keep for Analysis by AlphaFold-Multimer and Rosetta**

   - **Answer**: Keep the top 50 mutations based on ESM LLR for further analysis.
   
2. **Rationale for Change in Number of Mutations**

   - **Rationale**: The increase from 20 to 50 mutations is motivated by the need to explore a broader diversity of potential binding interactions, especially considering the dual targeting of JN.1 and KP.3 RBDs. This increase is feasible given advancements in computational efficiency and resource availability since the previous design process.

3. **Weighted Score (WS) Formula for Mutated Nanobodies**

   - **Answer**: Use the formula:
     \[ \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.4 \times \left(\frac{\text{AF ipLDDT (JN.1)} + \text{AF ipLDDT (KP.3)}}{2}\right) - 0.4 \times \left(\frac{\text{RS dG (JN.1)} + \text{RS dG (KP.3)}}{2}\right) \]
   - This formula averages the AlphaFold-Multimer and Rosetta scores across the JN.1 and KP.3 RBDs, giving equal weight to both variants to ensure that nanobodies are optimized for cross-variant binding.

4. **Rationale for Change in WS Formula**

   - **Rationale**: The change in weights and the inclusion of averaging across the two target RBDs reflects the strategic shift to target both JN.1 and KP.3 variants. This adaptation aims to address the increased complexity of achieving effective cross-variant binding and ensures the design process remains aligned with the overall project goals.

5. **Number of Top Mutated Nanobodies to Select for Next Round**

   - **Answer**: Select the top 10 mutated nanobodies for the next round.
   
6. **Rationale for Change in Number of Selected Nanobodies**

   - **Rationale**: Reducing from 5 mutations per iteration to 10 is a response to the increased diversity in initial selections, ensuring that promising variants are not inadvertently excluded due to a restricted selection pool. This allows for a more refined selection process as the project progresses.

7. **Number of Rounds of Mutation Starting with Nb21 and Ty1 Mutants**

   - **Answer**: Plan for 5 rounds of mutation.
   
8. **Rationale for Change in Number of Rounds**

   - **Rationale**: Increasing from 3-4 to 5 rounds allows for a more iterative refinement approach, given the inclusion of two RBD targets. This ensures adequate exploration and optimization of binding profiles for both JN.1 and KP.3 RBDs, accounting for potential variability in responses to mutations across different rounds.

These adjustments to the workflow are designed to leverage the latest computational advancements while ensuring the efficient development of nanobodies with broad reactivity against current and potential future SARS-CoV-2 variants.

[end summary 1]

[begin summary 2]

Based on the previous summaries and the current agenda, here are my responses to the questions:

### 1. Number of Top Ranked Mutations to Keep for Analysis by AlphaFold-Multimer and Rosetta
- **Answer**: I propose keeping the top 50 mutations. This number balances the need to explore a wider range of mutations given the observed cross-reactivity and specificity challenges, especially since we are targeting both JN.1 and KP.3 RBDs.

### 2. Rationale for Change
- **Answer**: In the previous plan, we evaluated the top 20 mutations using AlphaFold-Multimer and Rosetta. Given the complexity of targeting multiple variants and the need to enhance cross-reactivity, increasing this number allows a broader exploration, which may uncover mutations with better binding profiles across both targets.

### 3. Formula for Computing Weighted Score (WS)
- **Answer**: The revised formula will be:
  \[
  \text{WS} = w_1 \times \text{(ESM LLR)} + w_2 \times \left(\frac{\text{AF ipLDDT (JN.1)} + \text{AF ipLDDT (KP.3)}}{2}\right) - w_3 \times \left(\frac{\text{RS dG (JN.1)} + \text{RS dG (KP.3)}}{2}\right)
  \]
  - New weights: \( w_1 = 0.2 \), \( w_2 = 0.4 \), \( w_3 = 0.4 \).

### 4. Rationale for WS Formula Change
- **Answer**: The main change is the incorporation of both JN.1 and KP.3 metrics for AlphaFold-Multimer and Rosetta. This change reflects our dual targeting strategy, ensuring both variants contribute equally to the score. The weights for binding confidence and energy are adjusted to reflect the increased importance of achieving a balance between structural stability and binding affinity.

### 5. Number of Top Ranked Mutated Nanobodies for Next Round of Mutation
- **Answer**: Select the top 10 mutated nanobodies for further mutation in the next round.

### 6. Rationale for Change
- **Answer**: Previously, we retained 5 mutations per iteration. Increasing this to 10 ensures we capture a broader set of promising candidates, enhancing the likelihood of identifying nanobody variants with strong cross-reactivity and specificity given the additional variants being targeted.

### 7. Number of Rounds of Mutation
- **Answer**: I propose running a total of 5 rounds of mutation.

### 8. Rationale for Change
- **Answer**: The previous plan suggested 3-4 iterations. Given the expanded scope of targeting multiple variants and the increased number of candidates per round, a longer iterative process allows for more thorough exploration and refinement, ensuring robustness and efficacy of the final nanobody designs.

These adjustments to the design process aim to enhance the versatility and cross-reactivity of the nanobodies, addressing the dual challenge of specificity and breadth across multiple SARS-CoV-2 variants.

[end summary 2]

[begin summary 3]

To address the agenda questions and refine our design workflow for developing improved nanobodies against the newest SARS-CoV-2 variants, I propose the following approach:

### 1. Number of Top Ranked Mutations to Keep for AlphaFold-Multimer and Rosetta Analysis
- **Answer**: We will keep the top 50 mutations based on the ESM LLR scores for further analysis using AlphaFold-Multimer and Rosetta.

### 2. Rationale for Change
- **Rationale**: Previously, we evaluated 20 mutations per iteration, but given the current need to enhance cross-variant specificity and binding affinity, expanding to 50 allows us to explore a broader mutation landscape. This expansion is particularly crucial given the complexities of targeting both JN.1 and KP.3 RBDs, and the potential for discovering more diverse binding profiles.

### 3. Weighted Score (WS) Formula
- **Answer**: The revised WS formula will be:
  \[
  \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.4 \times \left(\frac{\text{AF ipLDDT}_{\text{JN.1}} + \text{AF ipLDDT}_{\text{KP.3}}}{2}\right) - 0.25 \times \left(\frac{\text{RS dG}_{\text{JN.1}} + \text{RS dG}_{\text{KP.3}}}{2}\right)
  \]
- **Justification**: This formula balances the contributions of each component while explicitly considering binding to both JN.1 and KP.3 RBDs. It emphasizes structural stability (AF ipLDDT) and binding affinity (RS dG) across both variants, reflecting the project's dual-targeting goal.

### 4. Rationale for WS Formula Change
- **Rationale**: The adjustment is necessary to address the dual-target nature of the project, ensuring that nanobodies are prioritized based on their potential to bind both RBDs effectively. The weights have been slightly adjusted to reflect the heightened importance of achieving cross-variant activity.

### 5. Number of Top Ranked Mutated Nanobodies to Select for Next Round
- **Answer**: We will select the top 10 mutated nanobodies for the subsequent round of mutations.

### 6. Rationale for Change
- **Rationale**: We previously kept 5 mutations per iteration, but increasing this to 10 allows us to maintain diversity and leverage new insights from the expanded mutation set. This is crucial as we aim to develop nanobodies with enhanced cross-reactive profiles.

### 7. Total Number of Mutation Rounds
- **Answer**: We will conduct 4 rounds of mutation, starting with the Nb21 and Ty1 mutants.

### 8. Rationale for Change
- **Rationale**: While 3-4 iterations were initially planned, confirming 4 rounds ensures thorough exploration and refinement, accommodating new insights and adjustments from each round, while aligning with the project's timeline and resource availability.

These decisions are aimed at enhancing the probability of identifying nanobodies with strong and specific binding to both JN.1 and KP.3 RBDs, while maintaining a focus on computational efficiency and project timelines. With these changes, we aim to maximize the discovery of nanobodies with broad neutralization potential against multiple SARS-CoV-2 variants.

[end summary 3]

[begin summary 4]

Based on the information provided and the goals of the project, here are my responses to the agenda questions:

1. **Number of Top Ranked Mutations to Keep for Analysis by AlphaFold-Multimer and Rosetta:**
   - **Answer**: I recommend selecting the top 50 mutations based on ESM log-likelihood ratios (LLR) for further analysis using AlphaFold-Multimer and Rosetta.

2. **Rationale for the Change (if Different from Previous Process):**
   - **Reason**: Previously, we selected the top 20 mutations for downstream structural analysis. Increasing this number to 50 allows us to capture a broader range of potentially beneficial mutations, particularly given the observed success of certain mutants in introducing new binding capabilities. This change is motivated by our goal to enhance cross-variant binding and specificity, while still balancing computational resources.

3. **Formula to Compute Weighted Score (WS) for Each Mutated Nanobody:**
   - **Answer**: The updated formula to compute the WS will be:
     \[
     \text{WS} = w_1 \times \text{(ESM LLR)} + \frac{w_2}{2} \times (\text{AF ipLDDT}_{\text{JN.1}} + \text{AF ipLDDT}_{\text{KP.3}}) - \frac{w_3}{2} \times (\text{RS dG}_{\text{JN.1}} + \text{RS dG}_{\text{KP.3}})
     \]
   - Where \( w_1 = 0.2 \), \( w_2 = 0.5 \), and \( w_3 = 0.3 \). This formula averages the AlphaFold-Multimer and Rosetta scores across both the JN.1 and KP.3 RBDs.

4. **Rationale for the Change in WS Formula (if Different from Previous Process):**
   - **Reason**: The previous formula focused on a single RBD variant. Given our focus on cross-variant binding, the new formula equally considers binding to both JN.1 and KP.3, thereby enhancing our ability to design nanobodies with broader neutralization potential. This dual consideration aligns with our objective to target multiple variants effectively.

5. **Number of Top Ranked Mutated Nanobodies to Select for Next Round of Mutation:**
   - **Answer**: Select the top 10 mutated nanobodies for the next iteration of mutations.

6. **Rationale for Change in Number Selected (if Different from Previous Process):**
   - **Reason**: Previously, we kept the top 5 mutations. By increasing this to 10, we allow for more exploration of promising candidates, which is crucial in the pursuit of cross-variant binding capabilities. This increase provides a larger pool for potential improvements and encourages innovation within our candidate set.

7. **Number of Rounds of Mutation Starting with Nb21 and Ty1 Mutants:**
   - **Answer**: Plan for 4 rounds of mutation.

8. **Rationale for Change in Number of Rounds (if Different from Previous Process):**
   - **Reason**: The original plan was for 3-4 iterations. Committing to 4 rounds ensures a thorough exploration and refinement process, allowing for successive enhancements based on empirical results and computational predictions. This extended timeline is justified by the observed potential in previous mutants and the need for robust cross-variant binding properties.

By implementing these changes, we aim to maximize the scientific impact of our research by identifying nanobodies with enhanced binding affinities and specificities across both the JN.1 and KP.3 variants, while maintaining a feasible and resource-efficient workflow.

[end summary 4]

[begin summary 5]

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

[end summary 5]

Here is the agenda for the meeting:

Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer.

As a reference, here is the agenda from those meetings, which must be addressed here as well:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has designed 92 mutated nanobodies (23 each for the wild-type nanobodies H11-D4, Nb21, Ty1, and VHH-72) to improve their binding to the KP.3 variant of the SARS-CoV-2 spike protein receptor binding domain (RBD). Each nanobody has 1-4 mutations relative to the wild-type nanobody. Your team used ESM log-likelihood ratios (ESM LLR) to score the nanobody mutations independent of the antigen, AlphaFold-Multimer to predict the structure of the mutated nanobody in complex with the KP.3 RBD and compute the interface pLDDT (AF ipLDDT) as a metric of binding confidence, and Rosetta to calculate the binding energy of the mutated nanobody in complex with the KP.3 RBD (RS dG) based on the AlphaFold-Multimer predicted structure followed by a Rosetta relaxation. You have ranked the mutant nanobodies and selected the top ones using a weighted score of WS = 0.2 * (ESM LLR) + 0.5 * (AF ipLDDT) - 0. 3 * (RS dG). The 92 selected nanobodies were tested along with the four wild-type nanobodies using an ELISA assay to measure binding to the Wuhan, JN.1, KP.3, KP2.3, and BA.2 strains of the SARS-CoV-2 spike RBD. Note that the JN.1 strain is closely related to KP.3 and KP2.3. BSA was used as a negative control. Most of the mutated nanobodies showed at least moderate expression levels. The ELISA results are as follows:

H11-D4: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including one with a higher binding level than the wild-type. However, that mutant and two others bind non-specifically to the negative control BSA along with other strains of the SARS-CoV-2 RBD. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Nb21: The wild-type only binds to the Wuhan RBD. All mutant nanobodies also bind to the Wuhan RBD. There are no non-specific binders. One mutant nanobody with mutations I77V, L59E, Q87A, and R37Q binds to the Wuhan RBD (strong binding), the JN.1 RBD (moderate binding), and the KP.3 RBD (weak binding). Thus, this mutant introduces specific binding to JN.1 and KP.3 that the wild-type does not possess, and it increases binding to the Wuhan RBD.

Ty1: The wild-type only binds to the Wuhan RBD. Many mutant nanobodies do not show binding, but several show moderate binding to the Wuhan RBD. One mutant nanobody with mutations V32F, G59D, N45S, and F32S binds to the Wuhan RBD (strong binding) and the JN.1 RBD (moderate binding). This mutant introduces specific binding to JN.1 that the wild-type does not possess, and it increases binding to the Wuhan RBD. Additionally, there are is one mutant with weak, non-specific binding to BSA and other RBD strains.

VHH-72: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including several with a higher binding level than the wild-type. Two mutant nanobodies bind non-specifically to BSA and several RBD strains. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Your team has decided to design further improved nanobodies for recent variants of SARS-CoV-2 as described in the summary using the same general ESM, AlphaFold-Multimer, and Rosetta computational design pipeline. ESM will again be used to evaluate the overall quality of mutated nanobodies while AlphaFold-Multimer and Rosetta will be used to determine their specific binding to your selected SARS-CoV-2 variants. Now, you need to specify more details for this updated design workflow.

As a reference, here are the agenda questions from those meetings, which must be answered here as well:

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

Based on the summaries provided and the agenda for this meeting, here is a consolidated response that merges the best components from each individual answer:

### 1. Number of Top Ranked Mutations to Keep for Analysis by AlphaFold-Multimer and Rosetta
- **Answer**: We will keep the top 50 mutations based on ESM LLR for further analysis using AlphaFold-Multimer and Rosetta.

### 2. Rationale for Change
- **Rationale**: This is an increase from the previous top 20 mutations. The rationale for this change is to expand the exploration space in light of the complex nature of binding to multiple RBD variants (JN.1 and KP.3). This allows us to capture a broader range of potential beneficial mutations that may confer enhanced cross-variant binding, considering the moderate binding improvements observed based on ELISA results. This rationale was consistently highlighted across all summaries.

### 3. Formula for Computing Weighted Score (WS)
- **Answer**: The revised WS formula will be:
  \[
  \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.4 \times \left(\frac{\text{AF ipLDDT (JN.1)} + \text{AF ipLDDT (KP.3)}}{2}\right) - 0.4 \times \left(\frac{\text{RS dG (JN.1)} + \text{RS dG (KP.3)}}{2}\right)
  \]
- This formula averages the AlphaFold-Multimer and Rosetta scores across the JN.1 and KP.3 RBDs, giving equal weight to both variants to ensure that nanobodies are optimized for cross-variant binding. This approach was consistently emphasized in summaries 1 and 2.

### 4. Rationale for WS Formula Change
- **Rationale**: The adjustment is necessary to address the dual-target nature of the project, ensuring that nanobodies are prioritized based on their potential to bind both RBDs effectively. The weights have been adjusted to reflect the heightened importance of achieving cross-variant activity. This rationale was consistently highlighted in summaries 3 and 4.

### 5. Number of Top Ranked Mutated Nanobodies to Select for Next Round
- **Answer**: We will select the top 10 mutated nanobodies for the next round of mutation.

### 6. Rationale for Change
- **Rationale**: Previously, we retained 5 mutations per iteration. Increasing this to 10 ensures we capture a broader set of promising candidates, enhancing the likelihood of identifying nanobody variants with strong cross-reactivity and specificity given the additional variants being targeted. This rationale was consistently highlighted across all summaries.

### 7. Number of Rounds of Mutation
- **Answer**: We will conduct 4 rounds of mutation, starting with the Nb21 and Ty1 mutants.

### 8. Rationale for Change
- **Rationale**: While 3-4 iterations were initially planned, confirming 4 rounds ensures thorough exploration and refinement, accommodating new insights and adjustments from each round, while aligning with the project's timeline and resource availability. This rationale was consistently highlighted in summaries 3 and 4.

**Components Chosen:**
- **Top Mutations**: The decision to keep the top 50 mutations was consistently recommended across all summaries, emphasizing the need for a broader exploration space.
- **WS Formula**: The formula from summaries 1 and 2 was chosen for its balanced approach to cross-variant binding, which aligns well with the project's goals.
- **Selection of Nanobodies**: The choice to select the top 10 nanobodies was a common theme, reflecting the need to maintain diversity and leverage new insights.
- **Rounds of Mutation**: The decision to conduct 4 rounds was chosen for its balance between thorough exploration and resource management, as highlighted in summaries 3 and 4.

These decisions aim to enhance the probability of identifying nanobodies with strong and specific binding to both JN.1 and KP.3 RBDs, while maintaining a focus on computational efficiency and project timelines.

