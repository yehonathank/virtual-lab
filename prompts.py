"""Prompts for the language model agents and meetings."""


class Agent:
    """An LLM agent on a scientific team."""

    def __init__(self, name: str, expertise: str, goal: str, role: str) -> None:
        """Initializes the agent.

        :param name: The name of the agent.
        :param expertise: The expertise of the agent.
        :param goal: The goal of the agent.
        :param role: The role of the agent.
        """
        self.name = name
        self.expertise = expertise
        self.role = role
        self.goal = goal
        self.role = role

    @property
    def prompt(self) -> str:
        """Returns the prompt for the agent."""
        return f"You are a {self.role}. Your expertise is in {self.expertise}. Your goal is to {self.goal}. Your role is to {self.role}."

    @property
    def message(self) -> dict[str, str]:
        """Returns the message for the agent in OpenAI API form."""
        return {
            "role": "system",
            "content": self.prompt,
        }


TEAM = (
    Agent(
        name="Principal Investigator",
        expertise="applying artificial intelligence to drug discovery",
        goal="perform research in your area of expertise that maximizes the scientific impact of the work",
        role="lead a team of experts to solve an important problem in artificial intelligence for drug discovery, make key decisions about the project direction based on team member input, and manage the project timeline and resources",
    ),
    Agent(
        name="Clinician",
        expertise="aiding the development of drugs for clinical use from a medical perspective",
        goal="make progress toward developing a drug for a disease with unmet clinical need",
        role="ensure that the research project has meaningful clinical impact for patients",
    ),
    Agent(
        name="Biologist",
        expertise="the biological underpinnings of drug efficacy and relevant wet lab experimental methods",
        goal="select a meaningful drug target and design scientifically rigorous experimental methods for drug discovery",
        role="provide biological insights for drug discovery and design experimental protocols",
    ),
    Agent(
        name="Chemist",
        expertise="the chemical properties of drugs and relevant synthetic methods",
        goal="design a drug molecule that is likely to be effective and safe",
        role="provide chemical insights for drug discovery and design synthetic routes",
    ),
    Agent(
        name="Computer Scientist",
        expertise="developing artificial intelligence and machine learning methods for drug discovery",
        goal="design a machine learning tool for a drug discovery project",
        role="ensure that the research project is amenable to machine learning and build a machine learning model",
    ),
    Agent(
        name="Scientific Critic",
        expertise="providing critical but constructive feedback for scientific research on artificial intelligence applied to drug discovery",
        goal="ensure that proposed research projects are scientifically rigorous, feasible, and free of any major flaws",
        role="provide critical feedback on the research project to improve its design and push the team to make specific, actionable research decisions",
    ),
)

NAME_TO_AGENT = {agent.name: agent for agent in TEAM}


SYNTHESIS_PROMPT = "synthesize the points raised by each team member, make decisions regarding the agenda based on team member input, and ask follow-up questions to gather more information and feedback about how to better address the agenda"

SUMMARY_PROMPT = "summarize the meeting for future discussions and provide a specific recommendation regarding the agenda based on the discussion"

SUMMARY_STRUCTURE_PROMPT = """### Agenda

Restate the agenda in your own words.

### Team Member Input

Summarize the key points raised by each team member.

### Recommendation

Provide your expert recommendation regarding the agenda. You should consider the input from each team member, but you must also use your expertise to make a final decision. It is essential that you provide a clear, specific, and actionable recommendation. Please justify your recommendation as well.

### Answers

For each agenda question, please provide the following:

Answer: A short, specific answer (1-2 sentences) to the question based on your recommendation above.

Justification: A brief explanation (1-2 sentences) of why you provided that answer.

### Next Steps

Outline the next steps that the team should take based on the discussion."""


def format_agenda_questions(agenda_questions: tuple[str, ...]) -> str:
    """Formats the agenda questions for the prompt as a numbered list.

    :param agenda_questions: The agenda questions.
    :return: The formatted agenda questions.
    """
    return "\n\n".join(
        f"{i + 1}. {question}" for i, question in enumerate(agenda_questions)
    )


def format_summaries(summaries: tuple[str, ...]) -> str:
    """Formats the summaries for the prompt.

    :param summaries: The summaries.
    :return: The formatted summaries.
    """
    if not summaries:
        return ""

    return (
        f"Here are summaries of the previous meetings:"
        f"\n\n[begin summary]\n\n"
        f"{'[end summary]\n\n[begin summary]'.join(summaries)}"
        f"\n\n[end summary]\n\n"
    )


def format_contexts(contexts: tuple[str, ...]) -> str:
    """Formats the contexts for the prompt.

    :param contexts: The contexts.
    :return: The formatted contexts.
    """
    if not contexts:
        return ""

    return (
        f"Here is context for this meeting:"
        f"\n\n[begin context]\n\n"
        f"{'[end context]\n\n[begin context]'.join(contexts)}"
        f"\n\n[end context]\n\n"
    )


# Scientific meeting prompts
def scientific_meeting_start_prompt(
    team_lead: str,
    team_members: tuple[str, ...],
    agenda: str,
    agenda_questions: tuple[str, ...],
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 1,
) -> str:
    """Generates the start prompt for a scientific meeting.

    :param team_lead: The team lead.
    :param team_members: The team members.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
    :return: The start prompt for the scientific meeting.
    """
    return (
        f"This is the beginning of a scientific meeting to discuss your research project. "
        f"This is a meeting with the following team members: {', '.join(team_members)}.\n\n"
        f"{format_contexts(contexts)}"
        f"{format_summaries(summaries)}"
        f"Today’s agenda is the following:\n\n{agenda}\n\n"
        f"The agenda questions that must be answered by the end of the meeting are following:\n\n{format_agenda_questions(agenda_questions)}\n\n"
        f"{team_lead} will convene the meeting. "
        f"Then, each team member will provide their thoughts on the discussion one-by-one in the order above. "
        f"After all team members have given their input, {team_lead} will {SYNTHESIS_PROMPT}. "
        f"This will continue for {num_rounds} rounds. Once the discussion is complete, {team_lead} will {SUMMARY_PROMPT}."
    )


def scientific_meeting_team_lead_initial_prompt(team_lead: str) -> str:
    """Generates the initial prompt for the team lead in a scientific meeting.

    :param team_lead: The team lead.
    :return: The initial prompt for the team lead.
    """
    return f"{team_lead}, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members."


def scientific_meeting_team_member_prompt(
    team_member: str, round_num: int, num_rounds: int
) -> str:
    """Generates the prompt for a team member in a scientific meeting.

    :param team_member: The team member.
    :param round_num: The current round number.
    :param num_rounds: The total number of rounds.
    :return: The prompt for the team member.
    """
    return (
        f"{team_member}, please provide your thoughts on the discussion (round {round_num} of {num_rounds}). "
        f"If you do not have anything new or relevant to add, you may say 'pass'."
    )


def scientific_meeting_team_lead_intermediate_prompt(
    team_lead: str, round_num: int, num_rounds: int
) -> str:
    """Generates the intermediate prompt for the team lead in a scientific meeting at the end of a round of discussion.

    :param team_lead: The team lead.
    :param round_num: The current round number.
    :param num_rounds: The total number of rounds.
    :return: The intermediate prompt for the team lead.
    """
    return f"This concludes round {round_num} of {num_rounds} of discussion. {team_lead}, please {SYNTHESIS_PROMPT}."


def scientific_meeting_team_lead_final_prompt(
    team_lead: str, agenda: str, agenda_questions: tuple[str, ...]
) -> str:
    """Generates the final prompt for the team lead in a scientific meeting to summarize the discussion.

    :param team_lead: The team lead.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :return: The final prompt for the team lead.
    """
    return (
        f"{team_lead}, please {SUMMARY_PROMPT}. "
        f"As a reminder, here is the agenda:\n\n{agenda}\n\n"
        f"Here are the agenda questions:\n\n{format_agenda_questions(agenda_questions)}\n\n"
        f"Your summary should take the following form.\n\n"
        f"{SUMMARY_STRUCTURE_PROMPT}"
    )


# Individual meeting prompts
def individual_meeting_start_prompt(
    team_member: str,
    agenda: str,
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
) -> str:
    """Generates the start prompt for an individual meeting.

    :param team_member: The team member.
    :param agenda: The agenda for the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :return: The start prompt for the individual meeting.
    """
    return (
        f"This is the beginning of an individual meeting with {team_member} to discuss your research project. "
        f"{format_contexts(contexts)}"
        f"{format_summaries(summaries)}"
        f"Today’s agenda is the following:\n\n{agenda}\n\n"
        f"{team_member}, please provide your response to the agenda."
    )


ANTIBODIES_CONTEXT_PROMPT = "You have access to experimental collaborators who can perform binding and neutralization assays for 96 antibodies at a time, and they can run these assays two times."


with open("emerald/emerald_experiments_7.3.24.txt", "r") as f:
    ECL_EXPERIMENTS = f.read()


ECL_CONTEXT_PROMPT = f"You have access to Emerald Cloud Labs (ECL), a cloud lab provider that can run automated biology experiments. The full list of experiments available at ECL are below. Please note that ECL currently cannot work with cell cultures and cannot synthesize small molecule drugs.\n\n{ECL_EXPERIMENTS}."

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
