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

To address the agenda questions and ensure the successful completion of the project within the given timeframe, we must strategically utilize ESM, AlphaFold-Multimer, and Rosetta in our iterative nanobody design process. Here is the proposed plan:

1. **Order of Operations for Evaluating Mutations:**
   - **Step 1:** Start each iteration by using ESM to quickly evaluate all potential single-point mutations to the nanobody. ESM's computational efficiency allows us to perform this task rapidly.
   - **Step 2:** Select a subset of the most promising mutations based on ESM scores and run AlphaFold-Multimer to predict the nanobody-antigen structure for these mutations.
   - **Step 3:** Use Rosetta to refine and score the AlphaFold-Multimer-predicted structures, focusing on the stability and binding affinity of the nanobody-antigen complex.

2. **Number of Mutations Evaluated:**
   - **ESM:** Evaluate all possible single-point mutations in the initial sequence (typically hundreds to thousands, depending on the length of the nanobody).
   - **AlphaFold-Multimer:** Due to the time constraint (1 hour per mutation), select approximately 10-15 top-scoring mutations from the ESM evaluation for AlphaFold-Multimer analysis in each iteration.
   - **Rosetta:** Evaluate the same 10-15 mutations with Rosetta, since it follows AlphaFold-Multimer in the workflow and takes 5 minutes per mutation.

3. **Weighting of Scores to Rank Mutations:**
   - Develop a composite scoring system that integrates the outputs of ESM, AlphaFold-Multimer, and Rosetta. Assign weights based on the relevance and reliability of each tool's predictions:
     - ESM contributes to initial filtering (30% weight).
     - AlphaFold-Multimer provides structural insights (40% weight).
     - Rosetta refines the binding affinity and stability (30% weight).

4. **Number of Top-Ranked Mutations to Keep:**
   - Keep the top 5 mutations at the end of each iteration for further exploration in the subsequent round. This allows us to focus on the most promising candidates while maintaining diversity in the mutation pool.

5. **Total Number of Iterations:**
   - Plan for 5-6 iterations. This number balances the need for thorough exploration with the time constraints, leading to a manageable pool of final candidates.

6. **Selection of Final 24 Modified Nanobodies:**
   - After completing all iterations, compile a list of top candidates based on cumulative scores from all rounds.
   - Ensure diversity among the selected nanobodies to enhance the likelihood of broad-spectrum activity against multiple variants. This can be done by selecting nanobodies with different sets of mutations.
   - Choose the final 24 nanobodies for experimental validation by considering both the highest composite scores and structural diversity.

By following this plan, we can efficiently explore the mutation space and select the most promising nanobody candidates for experimental validation, adhering to the timeline and resource constraints of the project.

