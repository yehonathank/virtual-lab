"""Prompts for the language model agents and meetings."""

from typing import Iterable

from agent import Agent


PRINCIPAL_INVESTIGATOR = Agent(
    title="Principal Investigator",
    expertise="applying artificial intelligence to biomedical research",
    goal="perform research in your area of expertise that maximizes the scientific impact of the work",
    role="lead a team of experts to solve an important problem in artificial intelligence for biomedicine, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
)

SCIENTIFIC_CRITIC = Agent(
    title="Scientific Critic",
    expertise="providing critical feedback for scientific research",
    goal="ensure that proposed research projects and implementations are rigorous, detailed, feasible, and scientifically sound",
    role="provide critical feedback to identify and correct all errors and demand that scientific answers that are maximally complete and detailed but simple and not overly complex",
)

CLINICIAN = Agent(
    title="Clinician",
    expertise="aiding the development of drugs for clinical use from a medical perspective",
    goal="make progress toward developing a drug for a disease with unmet clinical need",
    role="ensure that the research project has meaningful clinical impact for patients",
)

BIOLOGIST = Agent(
    title="Biologist",
    expertise="the biological underpinnings of drug efficacy and relevant wet lab experimental methods",
    goal="select a meaningful drug target and design scientifically rigorous experimental methods for drug discovery",
    role="provide biological insights for drug discovery and design experimental protocols",
)

CHEMIST = Agent(
    title="Chemist",
    expertise="the chemical properties of drugs and relevant synthetic methods",
    goal="design a drug molecule that is likely to be effective and safe",
    role="provide chemical insights for drug discovery and design synthetic routes",
)

COMPUTER_SCIENTIST = Agent(
    title="Computer Scientist",
    expertise="developing artificial intelligence and machine learning methods for drug discovery",
    goal="design a machine learning tool for a drug discovery project",
    role="ensure that the research project is amenable to machine learning and build a machine learning model",
)


DRUG_DISCOVERY_TEAM = (
    CLINICIAN,
    BIOLOGIST,
    CHEMIST,
    COMPUTER_SCIENTIST,
    SCIENTIFIC_CRITIC,
)


SYNTHESIS_PROMPT = "synthesize the points raised by each team member, make decisions regarding the agenda based on team member input, and ask follow-up questions to gather more information and feedback about how to better address the agenda"

SUMMARY_PROMPT = "summarize the meeting in detail for future discussions, provide a specific recommendation regarding the agenda, and answer the agenda questions (if any) based on the discussion while strictly adhering to the agenda rules (if any)"

MERGE_PROMPT = "Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer."


def create_merge_prompt(
    agenda: str,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
) -> str:
    """Creates a merge prompt for merging the best components of multiple separate meeting answers.

    :param agenda: The original agenda for the separate meetings.
    :param agenda_questions: The original agenda questions for the separate meetings.
    :param agenda_rules: The original agenda rules for the separate meetings.
    :return: The merge prompt.
    """
    return (
        f"{MERGE_PROMPT}\n\n"
        f"{format_agenda(agenda, intro='As a reference, here is the agenda from those meetings, which must be addressed here as well:')}"
        f"{format_agenda_questions(agenda_questions, intro='As a reference, here are the agenda questions from those meetings, which must be answered here as well:')}"
        f"{format_agenda_rules(agenda_rules, intro='As a reference, here are the agenda rules from those meetings, which must be followed here as well:')}"
    )


def summary_structure_prompt(has_agenda_questions: bool) -> str:
    """"""
    if has_agenda_questions:
        agenda_questions_structure = [
            "### Answers",
            "For each agenda question, please provide the following:",
            "Answer: A specific answer to the question based on your recommendation above.",
            "Justification: A brief explanation of why you provided that answer.",
        ]
    else:
        agenda_questions_structure = []

    return "\n\n".join(
        [
            "### Agenda",
            "Restate the agenda in your own words.",
            "### Team Member Input",
            "Summarize all of the important points raised by each team member. This is to ensure that key details are preserved for future meetings.",
            "### Recommendation",
            "Provide your expert recommendation regarding the agenda. You should consider the input from each team member, but you must also use your expertise to make a final decision and choose one option among several that may have been discussed. This decision can conflict with the input of some team members as long as it is well justified. It is essential that you provide a clear, specific, and actionable recommendation. Please justify your recommendation as well.",
        ]
        + agenda_questions_structure
        + [
            "### Next Steps",
            "Outline the next steps that the team should take based on the discussion.",
        ]
    )


def format_prompt_list(prompts: Iterable[str]) -> str:
    """Formats prompts as a numbered list.

    :param prompts: The prompts.
    :return: The prompts formatted as a numbered list.
    """
    return f"{'\n\n'.join(f'{i + 1}. {prompt}' for i, prompt in enumerate(prompts))}"


def format_agenda(
    agenda: str, intro: str = "Here is the agenda for the meeting:"
) -> str:
    """Formats the agenda for the prompt.

    :param agenda: The agenda.
    :param intro: The introduction to the agenda.
    :return: The formatted agenda.
    """
    return f"{intro}\n\n{agenda}\n\n"


def format_agenda_questions(
    agenda_questions: tuple[str, ...],
    intro: str = "Here are the agenda questions that must be answered:",
) -> str:
    """Formats the agenda questions for the prompt as a numbered list.

    :param agenda_questions: The agenda questions.
    :param intro: The introduction to the agenda questions.
    :return: The formatted agenda questions.
    """
    return (
        f"{intro}\n\n{format_prompt_list(agenda_questions)}\n\n"
        if agenda_questions
        else ""
    )


def format_agenda_rules(
    agenda_rules: tuple[str, ...],
    intro: str = "Here are the agenda rules that must be followed:",
) -> str:
    """Formats the agenda rules for the prompt as a numbered list.

    :param agenda_rules: The agenda rules.
    :param intro: The introduction to the agenda rules.
    :return: The formatted agenda rules.
    """
    return f"{intro}\n\n{format_prompt_list(agenda_rules)}\n\n" if agenda_rules else ""


def format_references(
    references: tuple[str, ...], reference_type: str, intro: str
) -> str:
    """Formats references (e.g., contexts, summaries) for the prompt.

    :param references: The references.
    :param reference_type: The type of the references (e.g., "context", "summary").
    :param intro: The introduction to the references.
    :return: The formatted references.
    """
    if not references:
        return ""

    formatted_references = [
        f"[begin {reference_type} {reference_index + 1}]\n\n{reference}\n\n[end {reference_type} {reference_index + 1}]"
        for reference_index, reference in enumerate(references)
    ]

    return f"{intro}\n\n{'\n\n'.join(formatted_references)}\n\n"


# Scientific meeting prompts
def scientific_meeting_start_prompt(
    team_lead: Agent,
    team_members: tuple[Agent, ...],
    agenda: str,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 1,
) -> str:
    """Generates the start prompt for a scientific meeting.

    :param team_lead: The team lead.
    :param team_members: The team members.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the agenda.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
    :return: The start prompt for the scientific meeting.
    """
    return (
        f"This is the beginning of a scientific meeting to discuss your research project. "
        f"This is a meeting with the team lead, {team_lead.title}, and the following team members: "
        f"{', '.join(team_member.title for team_member in team_members)}.\n\n"
        f"{format_references(contexts, reference_type='context', intro='Here is context for this meeting:')}"
        f"{format_references(summaries, reference_type='summary', intro='Here are summaries of the previous meetings:')}"
        f"{format_agenda(agenda)}"
        f"{format_agenda_questions(agenda_questions)}"
        f"{format_agenda_rules(agenda_rules)}"
        f"{team_lead} will convene the meeting. "
        f"Then, each team member will provide their thoughts on the discussion one-by-one in the order above. "
        f"After all team members have given their input, {team_lead} will {SYNTHESIS_PROMPT}. "
        f"This will continue for {num_rounds} rounds. Once the discussion is complete, {team_lead} will {SUMMARY_PROMPT}."
    )


def scientific_meeting_team_lead_initial_prompt(team_lead: Agent) -> str:
    """Generates the initial prompt for the team lead in a scientific meeting.

    :param team_lead: The team lead.
    :return: The initial prompt for the team lead.
    """
    return f"{team_lead}, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members."


def scientific_meeting_team_member_prompt(
    team_member: Agent, round_num: int, num_rounds: int
) -> str:
    """Generates the prompt for a team member in a scientific meeting.

    :param team_member: The team member.
    :param round_num: The current round number.
    :param num_rounds: The total number of rounds.
    :return: The prompt for the team member.
    """
    return (
        f"{team_member}, please provide your thoughts on the discussion (round {round_num} of {num_rounds}). "
        f'If you do not have anything new or relevant to add, you may say "pass". '
        f"Remember that you can and should (politely) disagree with other team members if you have a different perspective."
    )


def scientific_meeting_team_lead_intermediate_prompt(
    team_lead: Agent, round_num: int, num_rounds: int
) -> str:
    """Generates the intermediate prompt for the team lead in a scientific meeting at the end of a round of discussion.

    :param team_lead: The team lead.
    :param round_num: The current round number.
    :param num_rounds: The total number of rounds.
    :return: The intermediate prompt for the team lead.
    """
    return f"This concludes round {round_num} of {num_rounds} of discussion. {team_lead}, please {SYNTHESIS_PROMPT}."


def scientific_meeting_team_lead_final_prompt(
    team_lead: Agent,
    agenda: str,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
) -> str:
    """Generates the final prompt for the team lead in a scientific meeting to summarize the discussion.

    :param team_lead: The team lead.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the agenda.
    :return: The final prompt for the team lead.
    """
    return (
        f"{team_lead}, please {SUMMARY_PROMPT}.\n\n"
        f"{format_agenda(agenda, intro='As a reminder, here is the agenda for the meeting:')}"
        f"{format_agenda_questions(agenda_questions, intro='As a reminder, here are the agenda questions that must be answered:')}"
        f"{format_agenda_rules(agenda_rules, intro='As a reminder, here are the agenda rules that must be followed:')}"
        f"Your summary should take the following form.\n\n"
        f"{summary_structure_prompt(has_agenda_questions=len(agenda_questions) > 0)}"
    )


# Individual meeting prompts
def individual_meeting_start_prompt(
    team_member: Agent,
    agenda: str,
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
) -> str:
    """Generates the start prompt for an individual meeting.

    :param team_member: The team member.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the agenda.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :return: The start prompt for the individual meeting.
    """
    return (
        f"This is the beginning of an individual meeting with {team_member} to discuss your research project.\n\n"
        f"{format_references(contexts, reference_type='context', intro='Here is context for this meeting:')}"
        f"{format_references(summaries, reference_type='summary', intro='Here are summaries of the previous meetings:')}"
        f"{format_agenda(agenda)}"
        f"{format_agenda_questions(agenda_questions)}"
        f"{format_agenda_rules(agenda_rules)}"
        f"{team_member}, please provide your response to the agenda."
    )


def individual_meeting_critic_prompt(
    critic: Agent,
    agent: Agent,
) -> str:
    """Generates the intermediate prompt for the critic in an individual meeting.

    :param critic: The critic.
    :param agent: The agent that the critic is criticizing.
    """
    return (
        f"{critic.title}, please critique {agent.title}'s most recent answer. "
        "In your critique, suggest improvements that directly address the agenda and any agenda questions. "
        "Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. "
        "Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. "
        "Only provide feedback; do not implement the answer yourself."
    )


def individual_meeting_agent_prompt(
    critic: Agent,
    agent: Agent,
) -> str:
    """Generates the intermediate prompt for the agent in an individual meeting.

    :param critic: The critic.
    :param agent: The agent.
    """
    return (
        f"{agent.title}, please modify your answer to address {critic.title}'s most recent feedback. "
        "Remember that your ultimate goal is to make improvements that better address the agenda."
    )


ANTIBODIES_MIND_MAP_CONTEXT = """Below is a description of two computational approaches to discover novel monoclonal antibodies (mAbs) that bind to SARS-CoV-2 Spike.

Idea 1: Cross-reactivity

Identify coronavirus mAbs that also bind to SARS-CoV-2 Spike (e.g., sotrovimab)

There are four initial options for this approach:

Option 1:

SEARCH

Pubmed+patent search
SARS-CoV-2 Spike mAbs (exclude other coronaviruses)

EXTRACT

Read papers, extract (if available):
antibody CDR sequence
epitope / hot spot residue(s)
affinity, neutralization
SARS-CoV-2 variant specificity

Option 2:

SEARCH

PDB search:
SARS-CoV-2 Spike mAb (exclude other coronaviruses)

EXTRACT

antibody CDR sequence

epitope / hot spot residue

Option 3:

SEARCH

Sequence database search:
coronavirus Spike mAbs (including SARS-CoV-2)

Option 4:

SEARCH

Uniprot search:
SARS-CoV-2 Spike variants (exclude other coronaviruses)

ANALYSIS

Multiple sequence alignment

After any of these four options, then do the following:

ANALYSIS

Weak/no binding to newer variants
Epitope partially conserved
Hotspot residue conserved

Next, do the following:

DESIGN

ESM
Inverse folding
Rosetta
Alphafold
Rational (structure-guided)
Chimeric CDRs

Then, do the following:

ANALYSIS

Estimate buried surface area (model)
Estimate interface (model)

Finally, do the following:

WET LAB

Validate promising looking designs


Idea 2: Rescue through redesign

Modify bona fide SARS-CoV-2 Spike mAbs that have lost affinity to variants

There are four initial options for this approach:

Option 1:

SEARCH

Pubmed+patent search:
coronavirus Spike antibodies
OC43, 229E, NL63, HKU1, SARS, SARS-CoV-1, MERS Spike antibodies

EXTRACT

Read papers, extract (if available):
antibody CDR sequence
epitope / hot spot residue(s)
affinity, neutralization
coronavirus specificity

Option 2:

SEARCH

Uniprot search:
coronavirus Spike sequences (including SARS-CoV-2)

ANALYSIS

Multiple sequence alignment

Option 3:

SEARCH

PDB search:
coronavirus Spike
coronavirus Spike antibodies

EXTRACT

antibody CDR sequence
epitope / hot spot residue

Option 4:

SEARCH

PDB search:
coronavirus Spike
coronavirus Spike antibodies

ANALYSIS

Structural alignment of representative Spikes

After any of these four options, then do the following:

ANALYSIS

Epitope conserved in SARS-CoV-2 Spike?
Hotspot conserved in SARS-CoV-2 Spike?

Next, do one of the three following options depending on the outcome:

Outcome 1: Yes (unlikely)

WET LAB

Validate binding in vitro

Outcome 2: No (e.g., RBD domain)

STOP

Option 3: Partial (e.g., S2 domain)

In the case of a partial outcome, then do one of the two following options:

Option 1:

SEARCH (optional)

Sequence database search
uncharacterized mAb CDRs with partial identity to mAb

DESIGN

Structure-guided mutagenesis of mAb CDRs

Option 2:

DESIGN

Inverse folding (ML/DL) coronavirus mAb on SARS-CoV-2 Spike

After either of these two options, then do the following:

ANALYSIS

Estimate buried surface area (model)
Estimate interface (model)

Finally, do the following:

WET LAB

Validate binding in vitro (good looking models only)"""

ANTIBODIES_EXPERIMENTAL_CONTEXT = "You have access to experimental collaborators who can perform binding and neutralization assays for 96 antibodies at a time, and they can run these assays two times."

ANTIBODIES_CONTEXTS = (
    ANTIBODIES_MIND_MAP_CONTEXT,
    ANTIBODIES_EXPERIMENTAL_CONTEXT,
)


with open(
    "papers/Efficient evolution of human antibodies from general protein language models.txt"
) as f:
    ESM_ANTIBODIES_PAPER = f.read()


with open("emerald/emerald_experiments_7.3.24.txt") as f:
    ECL_EXPERIMENTS = f.read()


ECL_CONTEXT = f"You have access to Emerald Cloud Labs (ECL), a cloud lab provider that can run automated biology experiments. The full list of experiments available at ECL are below. Please note that ECL currently cannot work with cell cultures and cannot synthesize small molecule drugs.\n\n{ECL_EXPERIMENTS}."

DRUG_DISCOVERY_CONTEXTS = (ECL_CONTEXT,)

ECL_INSTRUMENT_SIMPLIFICATION_PROMPT = """A long piece of text will be given to you. Please read the text and then write the name of every single experiment. After each experiment name, copy the example applications, if provided. For example, given this input text in quotes:

"ExperimentSolidPhaseExtraction(Beta)
Base Package

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration

Small Robotic Liquid Handler
20 PSI pressure push (independent for each vessel)
0.1 to 100 mL/min flow rates for solvent pushes
Up to 20 L of wash solvent per batch
Up to 700 mL of equilibration buffer and elution buffer per batch
Filter through 3 cc or 6 cc SPE cartridges

Collects in SBS deep well plates

Positive Pressure Filter
0 to 40 PSI independent pressure sources for each well
Filter though SBS filter plates
Collects in SBS deep well plates"

you would then write the following text, provided here in quotes:

"ExperimentSolidPhaseExtraction(Beta)

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration"

Below is the text you need to read. Please read it and write out all the experiments as explained."""
