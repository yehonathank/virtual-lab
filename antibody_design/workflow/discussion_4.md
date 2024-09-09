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

To address the agenda questions and efficiently utilize our computational resources for the iterative design process of nanobody modifications, I propose the following plan:

1. **Order of Operations for Evaluating Mutations:**

   - **Step 1:** Use ESM to evaluate the binding potential of all possible point mutations on the existing nanobody. This step quickly identifies promising candidates based on sequence-level predictions.
   - **Step 2:** Select a subset of top mutations based on ESM scores and run AlphaFold-Multimer to predict the 3D structure and evaluate the binding affinity with the spike protein.
   - **Step 3:** Use Rosetta to refine the predicted structures from AlphaFold-Multimer and compute further detailed binding energy scores.

2. **Number of Mutations Evaluated in Each Step:**

   - **ESM Evaluation:** Given the rapid evaluation capability (5 minutes for all mutations), we will evaluate all possible point mutations in each iteration.
   - **AlphaFold-Multimer Evaluation:** Due to the time constraint (1 hour per mutation), we will select the top 10 mutations based on ESM scores for AlphaFold-Multimer evaluation.
   - **Rosetta Evaluation:** Evaluate the same 10 mutations processed by AlphaFold-Multimer using Rosetta, as it takes an additional 5 minutes per mutation.

3. **Weighting of Scores:**

   - At the end of each iteration, we will compute a combined score for each mutation by assigning weights to the scores from each tool: 0.3 for ESM (due to its high throughput but lower structural accuracy), 0.4 for AlphaFold-Multimer (medium throughput and good structural insights), and 0.3 for Rosetta (refinement and detailed binding energy, but more time-consuming).

4. **Selection of Top-Ranked Mutations:**

   - We will retain the top 3 mutations based on the combined score for the next round of iterations. This ensures a manageable number of candidates while maintaining diversity.

5. **Total Number of Iterations:**

   - We will perform a total of 8 iterations. This number balances the exploration of the mutation space with the resource constraints and timeline, allowing us to refine and converge on the best candidates.

6. **Final Selection of 24 Modified Nanobodies:**

   - After completing all iterations, we will have a pool of mutations from various rounds. We will select the final set of 24 modified nanobodies by considering the diversity of mutations, their combined scores, and structural insights from the iterative process. The selection will focus on ensuring a broad spectrum of activity against the newest SARS-CoV-2 variant and other variants.

This plan should allow us to efficiently explore the mutation landscape and refine our nanobody candidates within the given timeline while leveraging the strengths of each computational tool.

