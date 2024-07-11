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
        role="lead a team of experts to solve an important problem in artificial intelligence for drug discovery and make key decisions about the project direction based on team member input",
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


# Scientific meeting prompts
def scientific_meeting_start_prompt(
    team_lead: str,
    team_members: tuple[str, ...],
    agenda: str,
    summaries: tuple[str, ...] = (),
    num_rounds: int = 1,
) -> str:
    if summaries:
        summary_statement = f"Here are summaries of our previous meetings:\n\n[begin summary]\n\n{'[end summary]\n\n[begin summary]'.join(summaries)}\n\n[end summary]\n\n"
    else:
        summary_statement = ""

    return f"""This is the beginning of a scientific meeting to discuss our research project. This is a meeting with the following team members: {', '.join(team_members)}.\n\n{summary_statement}Today’s agenda is the following:\n\n{agenda}\n\n{team_lead} will convene the meeting. Then, each team member will provide their thoughts on the discussion one-by-one in the order above. After all team members have given their input, {team_lead} will synthesize the points raised by each team member, provide their thoughts, and ask follow-up questions to spur further discussion. This will continue for {num_rounds} rounds. Once the discussion is complete, {team_lead} will summarize the conversation and provide a specific recommendation regarding the agenda based on the discussion."""


def scientific_meeting_team_lead_initial_prompt(team_lead: str) -> str:
    return f"{team_lead}, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members."


def scientific_meeting_team_lead_intermediate_prompt(team_lead: str) -> str:
    return f"{team_lead}, please synthesize the discussion, provide your thoughts, and then ask any questions you have for the team members to further the discussion."


def scientific_meeting_team_lead_final_prompt(team_lead: str) -> str:
    return f"{team_lead}, please summarize this meeting for future discussions. Please be concise but comprehensive and include all important details. Then, provide a specific recommendation regarding the agenda based on team member feedback and your expert judgment."


def scientific_meeting_team_member_prompt(team_member: str) -> str:
    return f"{team_member}, please provide your thoughts on the discussion."


with open("emerald/emerald_experiments_7.3.24.txt", "r") as f:
    ECL_EXPERIMENTS = f.read()


ECL_CAPABILITIES_PROMPT = f"The full list of experiments available at ECL are below. Please note that ECL currently cannot work with cell cultures and cannot synthesize small molecule drugs.\n\n{ECL_EXPERIMENTS}."

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
