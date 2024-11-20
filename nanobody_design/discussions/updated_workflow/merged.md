## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

### Agenda Responses

1. **When using ESM to evaluate all single-point mutations to an input nanobody sequence, how many of the top-ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?**

   - **Answer**: We will keep the top 30 mutations based on ESM LLR for further analysis by AlphaFold-Multimer and Rosetta.

2. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Previously, we selected the top 20 mutations. Increasing this number to 30 allows us to explore a broader mutation landscape, providing additional opportunities for discovering mutations that enhance binding to both JN.1 and KP.3 RBDs. Given the computational efficiency improvements, we can accommodate this increase without significant resource constraints.

3. **After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?**

   - **Answer**: The WS formula for each mutated nanobody will be:
     \[
     \text{WS} = 0.15 \times \text{(ESM LLR)} + 0.4 \times \left(\frac{\text{(AF ipLDDT JN.1)} + \text{(AF ipLDDT KP.3)}}{2}\right) - 0.25 \times \left(\frac{\text{(RS dG JN.1)} + \text{(RS dG KP.3)}}{2}\right) + 0.2 \times \text{(Empirical ELISA Score)}
     \]
   - This formula averages the AlphaFold-Multimer and Rosetta scores for both RBDs to ensure balanced consideration for mutations that improve binding to both variants. The inclusion of an empirical ELISA score component helps validate computational predictions against experimental results.

4. **If this WS formula differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: The changes in the formula include an average of scores for both RBDs, reflecting our objective to enhance cross-variant binding. Additionally, introducing the empirical ELISA score component ensures that computational predictions align with observed experimental binding data, improving the reliability of our selections.

5. **After computing the WS for each mutated nanobody, how many of the top-ranked mutated nanobodies will you select for the next round of mutation?**

   - **Answer**: We will select the top 10 nanobodies for the next round of mutation.

6. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Previously, we selected five top mutations per round. Increasing to ten allows a wider exploration of beneficial mutations while maintaining a focus on candidates that already show promise across both computational and empirical evaluations.

7. **How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?**

   - **Answer**: We will run 5 rounds of mutation in total.

8. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: The increase from 3-4 rounds to 5 rounds is to allow for more extensive refinement of the nanobody candidates. This change is based on the complexity of achieving cross-variant binding and the desire to explore a larger mutational space given the promising results from the initial mutant candidates.

By making these adjustments, we aim to enhance the specificity and affinity of our nanobody designs for multiple SARS-CoV-2 variants, thereby increasing their potential utility in therapeutic applications.

[end summary 1]

[begin summary 2]

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

[end summary 2]

[begin summary 3]

### Agenda Responses:

1. **When using ESM to evaluate all single point mutations to an input nanobody sequence, how many of the top ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?**

   - **Answer**: We will keep the top 30 mutations ranked by ESM LLR for analysis by AlphaFold-Multimer and Rosetta.

2. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: The increase from 20 to 30 mutations allows us to explore a broader mutation landscape. Given that some mutants showed unexpected specificity and binding changes, expanding the pool helps capture more potential candidates that may exhibit desirable binding properties across multiple variants.

3. **After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?**

   - **Answer**: The revised formula for the weighted score will be:
     \[
     \text{WS} = w_1 \times \text{(ESM LLR)} + \frac{w_{2a} \times \text{(AF ipLDDT for JN.1)} + w_{2b} \times \text{(AF ipLDDT for KP.3)}}{2} - \frac{w_{3a} \times \text{(RS dG for JN.1)} + w_{3b} \times \text{(RS dG for KP.3)}}{2}
     \]
     - **Weights**: \( w_1 = 0.2 \), \( w_{2a} = w_{2b} = 0.25 \), \( w_{3a} = w_{3b} = 0.15 \).

4. **If this WS formula differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: This formula gives explicit weights to both the JN.1 and KP.3 interactions, reflecting equal importance to bind across both variants. This adjustment stems from the need to ensure adaptability and cross-reactivity, based on the ELISA findings that some mutants can bind different variants.

5. **After computing the WS for each mutated nanobody, how many of the top ranked mutated nanobodies will you select for the next round of mutation?**

   - **Answer**: We will select the top 10 mutated nanobodies for the next round of mutation.

6. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Reducing the number from 20 to 10 allows us to focus on the most promising mutants, which increases efficiency and allows for a deeper exploration of the selected candidates. This decision reflects the understanding that only a few mutants demonstrated multi-variant binding capability.

7. **How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?**

   - **Answer**: We will run three rounds of mutation in total.

8. **If this number differs from your previous design process, what is the rationale for the change?**

   - **Rationale**: Although the plan initially considered 3-4 iterations, preliminary results show promising leads, suggesting that three rounds are sufficient to refine the top candidates without overextending resources. Additionally, evidence of increased binding to multiple RBD strains in one round suggests that fewer iterations may still yield effective results.

### Overall Strategy

The revised strategy emphasizes flexibility and adaptability in targeting multiple RBD variants, informed by empirical assay results. By adjusting the number of mutations evaluated and refining the scoring system, we aim to enhance the likelihood of identifying nanobodies with broad neutralization potential. The deliberate pace of iteration rounds ensures a balance between innovation and resource management.

[end summary 3]

[begin summary 4]

Sure, let's dive into each of the agenda questions:

1. **Number of Top Ranked Mutations to Keep for Analysis by AlphaFold-Multimer and Rosetta:**
   - We will keep the top 30 mutations based on ESM LLR for further analysis by AlphaFold-Multimer and Rosetta.

2. **Rationale for Keeping 30 Mutations:**
   - This is an increase from the previous 20 mutations. The rationale is based on the need to explore a broader range of mutations given that some mutants showed improvements in binding to JN.1 and KP.3. Expanding the pool allows for capturing more potentially beneficial mutations that might enhance specificity and binding across different variants.

3. **Formula for Weighted Score (WS):**
   - The new WS formula will be:
     \[ \text{WS} = 0.2 \times (\text{ESM LLR}) + 0.35 \times (\text{AF ipLDDT for JN.1}) + 0.35 \times (\text{AF ipLDDT for KP.3}) - 0.3 \times (\text{RS dG for JN.1 and KP.3}) \]
   - This adjustment ensures that an equal emphasis is placed on the structural confidence of binding to both JN.1 and KP.3, reflecting the goal of targeting both variants effectively.

4. **Rationale for the Change in WS Formula:**
   - The previous formula aggregated AlphaFold-Multimer and Rosetta evaluations into a single score, which might have favored one variant over the other. The updated formula provides a balanced evaluation for both JN.1 and KP.3, aligning with our dual-target strategy. The equal weights for AF ipLDDT ensure that structural predictions for both variants contribute equally to the score.

5. **Number of Top Ranked Mutated Nanobodies to Select for Next Round:**
   - We will select the top 10 mutated nanobodies based on the updated WS.

6. **Rationale for Selecting 10 Mutated Nanobodies:**
   - This is a reduction from the previous 5 per iteration. As we have increased the number of initial mutations analyzed, selecting more candidates at this stage allows us to maintain diversity and incorporate a broader range of structural and binding affinities for further refinement.

7. **Number of Rounds of Mutation:**
   - We will conduct 4 rounds of mutation starting with the Nb21 and Ty1 mutants.

8. **Rationale for Conducting 4 Rounds:**
   - This remains consistent with the original plan. The decision stems from observing convergence in previous experiments where improvements plateaued around the third or fourth round, and it allows for sufficient iteration to refine binding without unnecessary resource expenditure. The aim is to achieve a balance between iterative exploration and practical constraints.

These adjustments reflect the experimental insights gleaned from our ELISA assays and computational modeling, optimizing our approach to achieve robust binding across multiple strains of the virus.

[end summary 4]

[begin summary 5]

Based on the prior results and new objectives, here are my responses to the agenda questions:

### 1. How many of the top-ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?

We will keep the top 30 mutations from the ESM LLR step for further analysis by AlphaFold-Multimer and Rosetta.

### 2. Rationale for Change

The previous design process evaluated the top 20 mutations, but given the need to improve binding to both the JN.1 and KP.3 RBDs, we aim for a broader exploration of mutation space. This increase allows for more diverse mutations, potentially capturing those that confer broader or enhanced binding capabilities.

### 3. Formula for Weighted Score (WS)

The new weighted score (WS) formula will be:
\[ \text{WS} = 0.2 \times \text{(ESM LLR)} + 0.25 \times \text{(AF ipLDDT for JN.1)} + 0.25 \times \text{(AF ipLDDT for KP.3)} - 0.3 \times \left( \frac{\text{RS dG for JN.1} + \text{RS dG for KP.3}}{2} \right) \]

### 4. Rationale for Change

The adjusted WS formula equally weights the AlphaFold-Multimer scores for JN.1 and KP.3 to emphasize the need for cross-reactivity. This weighting reflects the importance of stabilizing interactions with both RBDs. The averaging of RS dG scores encourages designs that balance binding affinity across variants.

### 5. How many of the top-ranked mutated nanobodies will you select for the next round of mutation?

We will select the top 10 mutated nanobodies for the next round of mutation.

### 6. Rationale for Change

Previously, we kept 5 top candidates, but expanding to 10 reflects the need for greater exploration given the complexity of achieving cross-reactivity. This allows us to maintain diversity within the candidate pool and maximizes the chances of finding a broadly neutralizing nanobody.

### 7. How many rounds of mutation will you run in total?

We will conduct 4 total rounds of mutation.

### 8. Rationale for Change

While the previous plan contemplated 3-4 iterations, we will fix this at 4 rounds to ensure adequate exploration of the mutation space and to allow for the incorporation of feedback from each iteration. This extended plan reflects the complexity of achieving the desired binding spectrum across multiple strains.

These adjustments aim to refine and broaden our nanobody candidates' binding capabilities, ensuring specific and strong interactions with both JN.1 and KP.3, while maintaining computational feasibility.

[end summary 5]

Here is the agenda for the meeting:

Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer.

As a reference, here is the agenda from those meetings, which must be addressed here as well:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has designed 92 mutated nanobodies (23 each for the wild-type nanobodies H11-D4, Nb21, Ty1, and VHH-72) to improve their binding to the KP.3 variant of the SARS-CoV-2 spike protein receptor binding domain (RBD). Each nanobody has 1-4 mutations relative to the wild-type nanobody. Your team used ESM log-likelihood ratios (ESM LLR) to score the nanobody mutations independent of the antigen, AlphaFold-Multimer to predict the structure of the mutated nanobody in complex with the KP.3 RBD and compute the interface pLDDT (AF ipLDDT) as a metric of binding confidence, and Rosetta to calculate the binding energy of the mutated nanobody in complex with the KP.3 RBD (RS dG) based on the AlphaFold-Multimer predicted structure followed by a Rosetta relaxation. You have ranked the mutant nanobodies and selected the top ones using a weighted score of WS = 0.2 * (ESM LLR) + 0.5 * (AF ipLDDT) - 0. 3 * (RS dG). The 92 selected nanobodies were tested along with the four wild-type nanobodies using an ELISA assay to measure binding to the Wuhan, JN.1, KP.3, KP2.3, and BA.2 strains of the SARS-CoV-2 spike RBD. Note that the JN.1 strain is closely related to KP.3 and KP2.3. BSA was used as a negative control. Most of the mutated nanobodies showed at least moderate expression levels. The ELISA results are as follows:

H11-D4: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including one with a higher binding level than the wild-type. However, that mutant and two others bind non-specifically to the negative control BSA along with other strains of the SARS-CoV-2 RBD. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Nb21: The wild-type only binds to the Wuhan RBD. All mutant nanobodies also bind to the Wuhan RBD. There are no non-specific binders. One mutant nanobody with mutations I77V, L59E, Q87A, and R37Q binds to the Wuhan RBD (strong binding), the JN.1 RBD (moderate binding), and the KP.3 RBD (weak binding). Thus, this mutant introduces specific binding to JN.1 and KP.3 that the wild-type does not possess, and it increases binding to the Wuhan RBD.

Ty1: The wild-type only binds to the Wuhan RBD. Many mutant nanobodies do not show binding, but several show moderate binding to the Wuhan RBD. One mutant nanobody with mutations V32F, G59D, N45S, and F32S binds to the Wuhan RBD (strong binding) and the JN.1 RBD (moderate binding). This mutant introduces specific binding to JN.1 that the wild-type does not possess, and it increases binding to the Wuhan RBD. Additionally, there are is one mutant with weak, non-specific binding to BSA and other RBD strains.

VHH-72: The wild-type only binds to the Wuhan RBD. Most mutants show binding to the Wuhan RBD as well, including several with a higher binding level than the wild-type. Two mutant nanobodies bind non-specifically to BSA and several RBD strains. No mutant nanobody shows specific binding to any strain other than the Wuhan RBD.

Your team has decided to design further improved nanobodies for recent variants of SARS-CoV-2 as described in the summary. Now, you need to specify more details for this updated computational nanobody design workflow.

As a reference, here are the agenda questions from those meetings, which must be answered here as well:

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

### 1. When using ESM to evaluate all single-point mutations to an input nanobody sequence, how many of the top-ranked mutations by ESM LLR will you keep for analysis by AlphaFold-Multimer and Rosetta?

We will keep the top 30 mutations based on ESM LLR for further analysis by AlphaFold-Multimer and Rosetta.

### 2. If this number differs from your previous design process, what is the rationale for the change?

The increase from 20 to 30 mutations allows us to explore a broader mutation landscape. This decision is based on the need to capture more potential candidates that may exhibit desirable binding properties across multiple variants, as indicated by the promising results from certain mutants in the ELISA assays. This rationale was consistently highlighted across all summaries.

### 3. After evaluating those mutated nanobodies with ESM, AlphaFold-Multimer, and Rosetta, what formula will you use to compute a weighted score (WS) for each mutated nanobody, and how will this factor in binding to both the JN.1 and KP.3 RBDs for the AlphaFold-Multimer and Rosetta portions of the score?

The WS formula will be:
\[ 
\text{WS} = 0.2 \times \text{(ESM LLR)} + 0.25 \times \text{(AF ipLDDT for JN.1)} + 0.25 \times \text{(AF ipLDDT for KP.3)} - 0.3 \times \left( \frac{\text{RS dG for JN.1} + \text{RS dG for KP.3}}{2} \right) 
\]

This formula balances the contributions from ESM, AlphaFold-Multimer, and Rosetta, ensuring equal emphasis on binding to both JN.1 and KP.3 variants. This approach was chosen because it reflects the need for cross-reactivity and was a common theme in the summaries.

### 4. If this WS formula differs from your previous design process, what is the rationale for the change?

The rationale for this change is to ensure that both JN.1 and KP.3 interactions are given equal importance, reflecting our goal of achieving cross-variant binding. This adjustment aligns with the empirical findings from the ELISA assays, which showed potential for cross-reactivity in some mutants. The consistent emphasis on balancing the structural metrics across variants was a key point in the summaries.

### 5. After computing the WS for each mutated nanobody, how many of the top-ranked mutated nanobodies will you select for the next round of mutation?

We will select the top 10 mutated nanobodies for the next round of mutation.

### 6. If this number differs from your previous design process, what is the rationale for the change?

Increasing the number from 5 to 10 allows for greater exploration of promising candidates, addressing the need for enhanced cross-reactivity while retaining diversity in our candidate pool. This change was consistently recommended across the summaries to maximize the chances of finding a broadly neutralizing nanobody.

### 7. How many rounds of mutation will you run in total starting with the Nb21 and Ty1 mutants?

We will conduct 4 total rounds of mutation.

### 8. If this number differs from your previous design process, what is the rationale for the change?

While the previous plan contemplated 3-4 iterations, fixing this at 4 rounds ensures adequate exploration of the mutation space and allows for the incorporation of feedback from each iteration. This decision reflects the complexity of achieving the desired binding spectrum across multiple strains and was a common suggestion in the summaries.

### Explanation of Components:

- **Top 30 Mutations**: This was a unanimous decision across all summaries, emphasizing the need to explore a broader mutation landscape.
- **WS Formula**: The chosen formula reflects a balanced approach to evaluating binding across both JN.1 and KP.3, which was a recurring theme in the summaries.
- **Top 10 Mutated Nanobodies**: This number was consistently recommended to ensure a diverse exploration of promising candidates.
- **4 Rounds of Mutation**: This decision balances the need for thorough exploration with practical constraints, as suggested in several summaries.

