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

**1. In each iteration, what is the order of operations for evaluating mutations with ESM, AlphaFold-Multimer, and Rosetta?**

In each iteration, the order of operations will be as follows:
   - **ESM (Evolutionary Scale Modeling):** First, use ESM to quickly evaluate all potential mutations to the nanobody. ESM can rapidly assess the likelihood of each mutation improving binding affinity based on evolutionary conservation and other features.
   - **AlphaFold-Multimer:** After shortlisting mutations with ESM, predict the 3D structures of the nanobody-antigen complexes for the top mutations using AlphaFold-Multimer. This step is crucial to evaluate the structural compatibility of mutations within the binding context.
   - **Rosetta:** Finally, use Rosetta on the AlphaFold-Multimer predicted structures to refine and evaluate the energetic stability and binding affinity of the mutations. Rosetta will provide a more detailed and accurate assessment of the binding interactions.

**2. In each iteration, how many mutations (give a precise number) will you evaluate with ESM, AlphaFold-Multimer, and Rosetta?**

- **ESM:** Evaluate all possible single-point mutations in the nanobody. If we assume 20 possible amino acid substitutions per position and there are around 100 positions that can be mutated, this results in approximately 2,000 mutations.
- **AlphaFold-Multimer:** Select the top 50 mutations from the ESM evaluation for further structural prediction.
- **Rosetta:** Further refine and evaluate these top 50 mutations after structural prediction with AlphaFold-Multimer.

**3. At the end of each iteration, how will you weight the ESM, AlphaFold-Multimer, and/or Rosetta scores to rank the nanobody mutations?**

At the end of each iteration, combine the scores using a weighted approach:
   - **ESM Score:** 20% weight, because it provides an initial filter based on evolutionary insights.
   - **AlphaFold-Multimer Score:** 40% weight, as it provides structural insights into how well each mutation might fit into the antigen binding site.
   - **Rosetta Score:** 40% weight, since it gives detailed energetic and binding affinity information that is crucial for identifying optimal mutations.

**4. At the end of each iteration, how many of the top-ranked mutations (give a precise number) will you keep for the next round?**

Keep the top 10 mutations from the ranked list of 50 mutations for the next round. These mutations will serve as the new starting points for generating further mutations in the next iteration.

**5. How many iterations will you perform in total?**

Perform a total of 5 iterations. This should provide a balance between exploring enough mutation space and the practical constraint of time.

**6. After all of the iterations are complete, how exactly will you select the final set of 24 modified nanobodies for experimental validation?**

After completing all iterations, evaluate the final set of mutations obtained from each iteration. Select a diverse set of 24 nanobodies based on the following criteria:
   - Highest combined scores from ESM, AlphaFold-Multimer, and Rosetta.
   - Diversity in sequence and structure to ensure coverage of different potential binding modes.
   - Prioritize mutations that show potential cross-reactivity with other variants based on structural predictions and sequence conservation.

This strategy maximizes the likelihood of identifying nanobodies with increased binding affinity to the target spike protein variant while also offering potential cross-reactivity to other variants.

