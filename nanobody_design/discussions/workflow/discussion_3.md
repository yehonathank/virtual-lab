## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here is the agenda for the meeting:

You are working on a research project to use machine learning to develop antibodies or nanobodies for the newest variant of the SARS-CoV-2 spike protein that also, ideally, have activity against other circulating minor variants and past variants. Your team previous decided to modify existing nanobodies to improve their binding to the newest variant of the SARS-CoV-2 spike protein. Your team has built three components of a nanobody design pipeline: ESM, AlphaFold-Multimer, and Rosetta. Each of these three tools can be used to score a nanobody mutation based on how the mutation affects binding to an antigen. Your goal is to start with an existing nanobody and iteratively add mutations to it to improve its binding to the newest variant of the SARS-CoV-2 spike protein, resulting in 24 modified nanobodies. Please determine how to use ESM, AlphaFold-Multimer, and Rosetta in this iterative design process. An important constraint is that ESM can evaluate all potential mutations to a nanobody in 5 minutes while AlphaFold-Multimer takes 1 hour per mutation and Rosetta takes five minutes per mutation. The whole iterative process should take no more than a few days to complete. Note that AlphaFold-Multimer must be run before Rosetta on each mutation since Rosetta requires the nanobody-antigen structured predicted by AlphaFold-Multimer.

Here are the agenda questions that must be answered:

1. In each iteration, what is the order of operations for evaluating mutations with ESM, AlphaFold-Multimer, and Rosetta?

2. In each iteration, how many mutations (give a precise number) will you evaluate with ESM, AlphaFold-Multimer, and Rosetta?

3. At the end of each iteration, how will you weight the ESM, AlphaFold-Multimer, and/or Rosetta scores to rank the nanobody mutations?

4. At the end of each iteration, how many of the top-ranked mutations (give a precise number) will you keep for the next round?

5. How many iterations will you perform in total?

6. After all of the iterations are complete, how exactly will you select the final set of 24 modified nanobodies for experimental validation?

Principal Investigator, please provide your response to the agenda.

## Principal Investigator

To address the agenda questions for the research project on developing enhanced nanobodies against the latest SARS-CoV-2 variant, here's the proposed strategy:

### 1. Order of Operations for Evaluating Mutations

In each iteration, the order of operations will be:
1. **ESM**: Evaluate all potential mutations for rapid initial screening.
2. **AlphaFold-Multimer**: Run on a subset of promising mutations identified by ESM to predict the nanobody-antigen structure.
3. **Rosetta**: Apply to the structured outputs from AlphaFold-Multimer to assess the binding affinity and structural stability of the mutations.

### 2. Number of Mutations Evaluated

- **ESM**: Evaluate all possible single-point mutations of the nanobody. If we assume a typical nanobody length of 120 amino acids and each position could mutate to 19 other amino acids, this results in evaluating 2,280 mutations in approximately 5 minutes.
- **AlphaFold-Multimer**: Select the top 50 mutations based on ESM scores for detailed structural prediction. This subset allows for a manageable computational load while providing sufficient diversity of mutations.
- **Rosetta**: Process the same 50 mutations evaluated by AlphaFold-Multimer for detailed energy scoring and ranking.

### 3. Weighting of Scores

At the end of each iteration, mutations will be ranked using a composite score:
- **ESM Score**: Weight of 0.2, since it provides a rapid but less detailed assessment.
- **AlphaFold-Multimer Score**: Weight of 0.4, offering structural insights critical for predicting binding interface changes.
- **Rosetta Score**: Weight of 0.4, as it provides detailed energy calculations and binding affinity estimates.

The weights reflect the balance between computational efficiency and the depth of analysis.

### 4. Number of Top-Ranked Mutations to Keep

At the end of each iteration, retain the top 10 mutations based on the composite score for the next round of iterative mutations. This ensures a focused yet diverse exploration of the sequence space.

### 5. Total Number of Iterations

Perform a total of 5 iterations. This number is chosen to balance computational feasibility within the time constraint and the exploration of sufficient combinatorial mutation space to enhance binding affinity.

### 6. Selection of Final 24 Modified Nanobodies

After completing all iterations:
- Compile a list of top mutations from each iteration.
- Use the final composite scores to rank all unique modified nanobodies.
- Select the top 24 nanobodies with the highest overall scores for experimental validation, ensuring that they represent a diverse set of mutations to maximize the chance of discovering broadly effective binders against the new SARS-CoV-2 variant and other circulating variants.

This plan ensures that within a few days, the project can generate a focused, high-quality set of candidate nanobodies for further experimental analysis.

