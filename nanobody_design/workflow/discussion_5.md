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

To address the agenda questions and develop a strategy for using ESM, AlphaFold-Multimer, and Rosetta in our iterative nanobody design process, here's the proposed plan:

1. **Order of Operations in Each Iteration:**
   - **Step 1:** Use ESM to quickly evaluate all potential mutations to the nanobody. This step gives us a preliminary idea of which mutations might be promising.
   - **Step 2:** For a subset of top mutations from the ESM evaluation, run AlphaFold-Multimer. This step will provide detailed structural predictions of the nanobody-antigen complex.
   - **Step 3:** Use Rosetta to refine and score the structures predicted by AlphaFold-Multimer. This will provide a detailed energy-based assessment of binding affinities.

2. **Number of Mutations Evaluated:**
   - **ESM:** Evaluate all possible single-point mutations. Given the computational efficiency, we can screen all possibilities (~20 mutations per amino acid position).
   - **AlphaFold-Multimer and Rosetta:** Select the top 5% of mutations based on ESM scores for further evaluation. Assuming around 1000 positions on average, this results in evaluating approximately 50 mutations per iteration.

3. **Weighting the Scores:**
   - Combine scores using a weighted average approach: 30% weight to ESM (for preliminary filtering), 40% to AlphaFold-Multimer (for structural prediction), and 30% to Rosetta (for final binding affinity refinement). These weights can be adjusted based on empirical validation of their predictive power in early iterations.

4. **Top-Ranked Mutations for Next Round:**
   - Keep the top 10 mutations based on the combined weighted scores for the next round. This balances depth (evaluating different positions) and breadth (evaluating various mutations at preferred positions).

5. **Total Iterations:**
   - Perform 10 iterations in total. This will allow us to thoroughly explore the mutational landscape while adhering to the time constraint of a few days.

6. **Selection of Final 24 Modified Nanobodies:**
   - At the end of all iterations, select the 24 nanobodies that exhibit the highest combined scores across iterations. Ensure diversity in the mutational profiles to account for potential cross-reactivity against minor and past variants. If necessary, include additional criteria such as stability or manufacturability predictions to refine the final selection.

This plan balances computational efficiency and thoroughness in evaluating potential nanobody mutations, ensuring we can identify and validate promising candidates within the given constraints.

