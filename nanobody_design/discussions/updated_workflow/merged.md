## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

### Agenda Responses:

1. **Number of Top Ranked Mutations to Keep for AlphaFold-Multimer and Rosetta Analysis**: 
   - **Response**: We will keep the top 40 mutations based on ESM LLR for further analysis with AlphaFold-Multimer and Rosetta.
   
2. **Rationale for Change from Previous Design Process**:
   - **Response**: Previously, we kept only the top 20 mutations. The adjustment to 40 is to broaden our exploration of potential binding improvements, considering that we are now targeting two related RBDs (JN.1 and KP.3) simultaneously. This increase accounts for the additional complexity and diversity required to enhance binding across these variants.

3. **Formula for Computing Weighted Score (WS)**:
   - **Response**: The new WS formula will be:  
     \[ \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.4 \times \left[\frac{1}{2} \times (\text{AF ipLDDT}_{\text{JN.1}} + \text{AF ipLDDT}_{\text{KP.3}})\right] - 0.25 \times \left[\frac{1}{2} \times (\text{RS dG}_{\text{JN.1}} + \text{RS dG}_{\text{KP.3}})\right] \]
   - **Explanation**: This formula averages the AlphaFold-Multimer and Rosetta scores for both JN.1 and KP.3, reflecting the need to balance binding improvements between these two RBDs.

4. **Rationale for Change in WS Formula**:
   - **Response**: The previous formula focused on a single RBD target. The change to incorporate dual RBD scores ensures that the selected nanobodies are effective against both JN.1 and KP.3, increasing their potential cross-reactivity and therapeutic utility.

5. **Number of Top Ranked Mutated Nanobodies to Select for Next Mutation Round**:
   - **Response**: We will select the top 10 mutated nanobodies for the next round of mutation.
   
6. **Rationale for Change from Previous Design Process**:
   - **Response**: Previously, we selected the top 5. Doubling this to 10 allows us to maintain diverse candidates that may show improved binding to both JN.1 and KP.3 RBDs, which is critical given the expanded target scope.

7. **Total Number of Rounds of Mutation**:
   - **Response**: We will conduct 3 rounds of mutation.
   
8. **Rationale for Change from Previous Design Process**:
   - **Response**: The previous plan suggested 3-4 iterations. Given the added complexity of targeting two RBDs, we will standardize at 3 rounds to ensure ample opportunity for optimization while remaining resource-efficient.

These adjustments are designed to optimize our approach to developing broadly neutralizing nanobodies against various SARS-CoV-2 variants, ensuring that our computational efforts are aligned with the expanded scope and objectives of our project.

[end summary 1]

[begin summary 2]

Based on the agenda and the data provided from previous meetings and current experimental results, here's a detailed response to each question to refine our updated design workflow:

1. **Number of Top Mutations from ESM for Further Analysis**
   - **Answer**: We'll select the top 50 mutations based on ESM LLR for further analysis with AlphaFold-Multimer and Rosetta.
  
2. **Rationale for Change in Number of Top Mutations**
   - **Answer**: Previously, we chose the top 20 mutations due to computational constraints and early-stage exploration. However, given the promising results from initial ELISA assays and a need to increase the diversity and potential cross-reactivity of our candidates, we've decided to expand the pool to 50. This allows us to explore a broader mutation landscape and identify mutations potentially beneficial across multiple strains.

3. **Weighted Score (WS) Formula for Mutated Nanobodies**
   - **Answer**: The new WS formula will be:
     \[
     \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.35 \times \left(\frac{\text{AF ipLDDT (JN.1)} + \text{AF ipLDDT (KP.3)}}{2}\right) - 0.25 \times \left(\frac{\text{RS dG (JN.1)} + \text{RS dG (KP.3)}}{2}\right)
     \]
   - **Rationale**: The formula emphasizes binding confidence and energy to both JN.1 and KP.3, reflecting our dual-target focus. The weights are adjusted to give greater importance to structural predictions and binding energy, which have shown significant correlation with improved ELISA results.

4. **Rationale for Change in WS Formula**
   - **Answer**: The modifications in weights and inclusion of both JN.1 and KP.3 reflect our updated goal of achieving cross-variant binding. Adjusting these weights prioritizes structural stability (AF ipLDDT) and binding energy (RS dG), which are more aligned with observed ELISA outcomes and our dual-target strategy.

5. **Number of Top Ranked Mutated Nanobodies for Next Round**
   - **Answer**: We will select the top 10 mutated nanobodies for the next round of mutation.
   
6. **Rationale for Change in Top Ranked Selection**
   - **Answer**: Previously, we kept 5 mutations per iteration, but expanding to 10 allows us to maintain diversity in our candidates while ensuring that we are not overly restrictive in the early rounds of mutation. This approach balances computational resources and the need to explore a wider mutation space.

7. **Number of Rounds of Mutation Starting with Nb21 and Ty1 Mutants**
   - **Answer**: We will conduct 5 rounds of mutation.
   
8. **Rationale for Change in Number of Rounds**
   - **Answer**: Initially, 3-4 iterations were planned, but given the complexity of achieving cross-variant specificity and the promising initial results, an additional round allows for more refinement. This ensures thorough exploration of the mutation space and adequate iterations to converge on high-affinity, cross-variant binders.

This plan is designed to build on existing successes while expanding our exploration capabilities to identify nanobodies with broad neutralization potential against SARS-CoV-2 variants.

[end summary 2]

[begin summary 3]

Given the agenda for the meeting, I will address the questions systematically:

1. **Number of Top Ranked Mutations by ESM LLR to Keep for Further Analysis:**
   - **Answer**: We will analyze the top 50 mutations by ESM LLR for each nanobody. This will increase our chances of capturing potentially beneficial mutations that might have been missed previously due to computational constraints.

2. **Rationale for Changing the Number of Mutations:**
   - **Answer**: Previously, we evaluated the top 20 mutations. The rationale for increasing this number to 50 is to broaden our exploration of the mutational landscape, especially considering the need to improve binding against both JN.1 and KP.3 variants. This expansion is feasible due to improved computational resources and aims to capture a greater diversity of potentially beneficial mutations.

3. **Formula for Computing a Weighted Score (WS):**
   - **Answer**: The revised formula for WS is as follows:
     \[ \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.35 \times (\text{AF ipLDDT}_{\text{JN.1}} + \text{AF ipLDDT}_{\text{KP.3}})/2 - 0.25 \times (\text{RS dG}_{\text{JN.1}} + \text{RS dG}_{\text{KP.3}})/2 \]
     - This formula considers both JN.1 and KP.3 RBDs by averaging the AlphaFold-Multimer and Rosetta scores for these variants, thereby accounting for dual specificity and broader neutralization potential.

4. **Rationale for Changing the WS Formula:**
   - **Answer**: The previous formula did not explicitly account for simultaneous binding to multiple strains. By integrating the average scores for both JN.1 and KP.3 RBDs, we place a stronger emphasis on designing nanobodies that can bind effectively to both variants, enhancing the potential for cross-reactivity and robustness against variant evolution.

5. **Number of Top Ranked Mutated Nanobodies to Select for Next Round:**
   - **Answer**: We will select the top 10 nanobodies for the next round of mutation.
   
6. **Rationale for Changing the Number of Mutated Nanobodies:**
   - **Answer**: Previously, we kept the top 5 mutations. Expanding to 10 allows us to maintain a diverse pool of promising candidates, capturing more opportunities for optimization and ensuring that potentially successful variants are not prematurely discarded.

7. **Total Number of Rounds of Mutation Starting with Nb21 and Ty1 Mutants:**
   - **Answer**: We will conduct a total of 4 rounds of mutation.
   
8. **Rationale for Changing the Number of Rounds:**
   - **Answer**: The suggestion was 3-4 rounds. By firmly planning for 4 iterations, we ensure adequate opportunity for optimization while allowing enough time for convergence and analysis. This decision also accounts for the expanded number of mutations and candidates, providing sufficient scope for iterative improvements.

This plan aims to refine the nanobody candidates effectively while accommodating the emerging challenges posed by multiple SARS-CoV-2 variants. By broadening our mutation pool and emphasizing cross-variant binding, we are better positioned to develop antibodies with enhanced therapeutic potential.

[end summary 3]

[begin summary 4]

To address the agenda questions, we need to fine-tune our design and evaluation process based on previous findings and the current project requirements. Here's a detailed response to each question:

1. **When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta out of the ~2,000 possible mutations?**

   - **Answer**: We will keep the top 50 mutations based on ESM LLR for further analysis by AlphaFold-Multimer and Rosetta.

2. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Previously, we evaluated the top 20 mutations, but increasing this to 50 allows for greater exploration of the mutation landscape, potentially uncovering beneficial mutations that were previously overlooked. This adjustment is feasible given our computational resources and is informed by the need to enhance binding across multiple variants, as shown in the ELISA results.

3. **After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?**

   - **Answer**: The weighted score (WS) will be computed as follows:
     \[
     \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.25 \times \text{(AF ipLDDT for JN.1)} + 0.25 \times \text{(AF ipLDDT for KP.3)} - 0.15 \times \text{(RS dG for JN.1)} - 0.15 \times \text{(RS dG for KP.3)}
     \]
   - This formula balances the scores for binding confidence and binding energy across both the JN.1 and KP.3 RBDs, reflecting their importance in our target.

4. **If this WS formula differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: The revised formula incorporates separate terms for JN.1 and KP.3, acknowledging the need to evaluate binding to both RBDs separately. This emphasizes the importance of dual-variant binding, which emerged as a critical factor in the ELISA results, where cross-variant binding was a key desirable trait.

5. **After computing the WS for each mutated nanobody, how many of the top ranked mutated nanobodies will you select for the next round of mutation?**

   - **Answer**: We will select the top 10 mutated nanobodies for the next round of mutation.

6. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Previously, we kept 5 mutations per iteration. Increasing this to 10 allows for a broader exploration of favorable mutation combinations, as the initial mutants showed potential for cross-reactive binding.

7. **How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?**

   - **Answer**: We will run a total of 4 rounds of mutation.

8. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: This is consistent with our initial plan, allowing enough iterations to refine binding properties while managing computational and time constraints. Monitoring the convergence of scores and binding profiles will guide adjustments if needed.

These steps will refine our design workflow, maximizing the potential for developing nanobodies with enhanced and broad-spectrum binding capabilities against SARS-CoV-2 variants.

[end summary 4]

[begin summary 5]

In addressing the agenda for optimizing the development of nanobodies against SARS-CoV-2 variants, we are refining our computational design pipeline to enhance efficiency and effectiveness.

### 1. Number of Top Mutations to Keep for Analysis
- **Decision**: We will keep the top 50 mutations based on ESM LLR scores for analysis by AlphaFold-Multimer and Rosetta.
  
### 2. Rationale for the Change
- **Rationale**: Previously, we retained only 20 mutations due to computational constraints and the focus on the KP.3 variant. However, given our expanded target to include both JN.1 and KP.3, we require a broader exploration of potential mutations to ensure coverage of interaction landscapes, allowing for better identification of cross-variant binding enhancements.

### 3. Weighted Score Formula
- **WS Formula**: 
  \[
  \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.4 \times \text{(AF ipLDDT\_JN.1)} + 0.4 \times \text{(AF ipLDDT\_KP.3)} - 0.05 \times \text{(RS dG\_average)}
  \]
  - Here, \( \text{AF ipLDDT\_JN.1} \) and \( \text{AF ipLDDT\_KP.3} \) are the interface pLDDT scores for binding confidence to JN.1 and KP.3, respectively, and \( \text{RS dG\_average} \) is the average binding energy for both complexes.

### 4. Rationale for the Change
- **Rationale**: The adjustment reflects an increased emphasis on binding confidence to both JN.1 and KP.3 RBDs. Weighed equally, they prioritize cross-variant effectiveness. The reduced emphasis on RS dG acknowledges that structural predictions (AF ipLDDT) may provide more reliable insights into binding specificity for different variants than binding energy alone.

### 5. Number of Top Mutated Nanobodies to Select
- **Decision**: We will select the top 10 mutated nanobodies for the next mutation round.

### 6. Rationale for the Change
- **Rationale**: Previously, we kept the top 5 mutations, but expanding to 10 will allow us to maintain a diverse pool of candidates that are effective against multiple variants, enhancing our ability to discover broadly neutralizing candidates.

### 7. Number of Rounds of Mutation
- **Decision**: We plan to conduct 4 rounds of mutation, starting with the Nb21 and Ty1 mutants.

### 8. Rationale for the Change
- **Rationale**: Maintaining 4 rounds aligns with our previous strategy, balancing adequate exploration and resource constraints. It allows for iterative refinement while ensuring timely progression towards experimental validation.

These adjustments to our design workflow are intended to enhance our ability to identify and refine nanobodies with broad and robust neutralizing capabilities against emerging SARS-CoV-2 variants. Through this strategic focus, we aim to develop candidates with the potential for effective therapeutic or diagnostic applications across strains.

[end summary 5]

Here is the agenda for the meeting:

Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer.

As a reference, here is the agenda from those meetings, which must be addressed here as well:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has designed 92 mutated nanobodies (23 each for the wild-type nanobodies H11-D4, Nb21, Ty1, and VHH-72) to improve their binding to the KP.3 variant of the SARS-CoV-2 spike protein receptor binding domain (RBD). Each nanobody has 1-4 mutations relative to the wild-type nanobody. Your team used ESM log-likelihood ratios (ESM LLR) to score the nanobody mutations independent of the antigen, AlphaFold-Multimer to predict the structure of the mutated nanobody in complex with the KP.3 RBD and compute the interface pLDDT (AF ipLDDT) as a metric of binding confidence, and Rosetta to calculate the binding energy of the mutated nanobody in complex with the KP.3 RBD (RS dG) based on the AlphaFold-Multimer predicted structure followed by a Rosetta relaxation. You have ranked the mutant nanobodies and selected the top ones using a weighted score of WS = 0.2 * (ESM LLR) + 0.5 * (AF ipLDDT) - 0. 3 * (RS dG). The 92 selected nanobodies were tested along with the four wild-type nanobodies using an ELISA assay to measure binding to the Wuhan, JN.1, KP.3, KP2.3, and BA.2 strains of the SARS-CoV-2 spike RBD. Note that the JN.1 strain is closely related to KP.3 and KP2.3. BSA was used as a negative control. Most of the mutated nanobodies showed at least moderate expression levels. The ELISA results are as follows:

H11-D4: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including one with a higher binding level than the wild-type. However, that mutant and two others bind non-specifically to the negative control BSA along with other strains of the SARS-CoV-2 RBD. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Nb21: The wild-type only binds to the Wuhan RBD. All mutant nanobodies also bind to the Wuhan RBD. There are no non-specific binders. One mutant nanobody with mutations I77V, L59E, Q87A, and R37Q binds to the Wuhan RBD (strong binding), the JN.1 RBD (moderate binding), and the KP.3 RBD (weak binding). Thus, this mutant introduces specific binding to JN.1 and KP.3 that the wild-type does not possess, and it increases binding to the Wuhan RBD.

Ty1: The wild-type only binds to the Wuhan RBD. Many mutant nanobodies do not show binding, but several show moderate binding to the Wuhan RBD. One mutant nanobody with mutations V32F, G59D, N45S, and F32S binds to the Wuhan RBD (strong binding) and the JN.1 RBD (moderate binding). This mutant introduces specific binding to JN.1 that the wild-type does not possess, and it increases binding to the Wuhan RBD. Additionally, there are is one mutant with weak, non-specific binding to BSA and other RBD strains.

VHH-72: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including several with a higher binding level than the wild-type. Two mutant nanobodies bind non-specifically to BSA and several RBD strains. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Your team has decided to design further improved nanobodies for recent variants of SARS-CoV-2 as described in the summary using the same general ESM, AlphaFold-Multimer, and Rosetta computational design pipeline. Now, you need to specify more details for this updated design workflow.

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

Based on the summaries provided, here is a consolidated response to the agenda questions, incorporating the best components from each meeting summary:

### 1. Number of Top Mutations to Keep for Analysis
- **Decision**: We will keep the top 50 mutations based on ESM LLR scores for further analysis by AlphaFold-Multimer and Rosetta.

### 2. Rationale for the Change
- **Rationale**: Initially, we retained only 20 mutations due to computational constraints. However, given the need to improve binding across multiple variants, including JN.1 and KP.3, and the promising ELISA results, expanding to 50 mutations allows for a broader exploration of the mutation landscape. This decision is supported by improved computational resources and aims to capture a greater diversity of potentially beneficial mutations (Summaries 2, 3, 4, and 5).

### 3. Weighted Score Formula
- **WS Formula**: 
  \[
  \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.35 \times \left(\frac{\text{AF ipLDDT (JN.1)} + \text{AF ipLDDT (KP.3)}}{2}\right) - 0.25 \times \left(\frac{\text{RS dG (JN.1)} + \text{RS dG (KP.3)}}{2}\right)
  \]
  - This formula balances the scores for binding confidence and binding energy across both JN.1 and KP.3 RBDs, reflecting their importance in our target (Summaries 2 and 3).

### 4. Rationale for the Change
- **Rationale**: The revised formula incorporates average scores for both JN.1 and KP.3, acknowledging the need to evaluate binding to both RBDs. This emphasizes the importance of dual-variant binding, which emerged as a critical factor in the ELISA results, where cross-variant binding was a key desirable trait (Summaries 3 and 4).

### 5. Number of Top Mutated Nanobodies to Select
- **Decision**: We will select the top 10 mutated nanobodies for the next round of mutation.

### 6. Rationale for the Change
- **Rationale**: Previously, we kept 5 mutations per iteration. Expanding to 10 allows for a broader exploration of favorable mutation combinations, as the initial mutants showed potential for cross-reactive binding. This approach balances computational resources and the need to explore a wider mutation space (Summaries 2, 3, 4, and 5).

### 7. Number of Rounds of Mutation
- **Decision**: We plan to conduct 4 rounds of mutation, starting with the Nb21 and Ty1 mutants.

### 8. Rationale for the Change
- **Rationale**: Initially, 3-4 iterations were planned, but given the complexity of achieving cross-variant specificity and the promising initial results, an additional round allows for more refinement. This ensures thorough exploration of the mutation space and adequate iterations to converge on high-affinity, cross-variant binders (Summaries 3, 4, and 5).

These adjustments to our design workflow are intended to enhance our ability to identify and refine nanobodies with broad and robust neutralizing capabilities against emerging SARS-CoV-2 variants. Through this strategic focus, we aim to develop candidates with the potential for effective therapeutic or diagnostic applications across strains.

