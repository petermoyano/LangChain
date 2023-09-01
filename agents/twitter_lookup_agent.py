from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    """
    Searches for twitter Profile Page by inizializing an agent. Starts with a name and returns that person's twitter username.
    """

    llm = ChatOpenAI(temperature=0, model_name="gpt4")
    template = """given the full name {name_of_person} I want you to findt me a link to their  twitter profile page. Only include in your answer the URL to the person's twitter profile page."""

    tools_for_agent = [Tool(
        name="Crawl Google for twitter profile page", func=get_profile_url,
        description="useful for when you need to get the twitter page URL"
    )]

    agent = initialize_agent(tools=tools_for_agent, llm=llm,
                             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    twitter_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name)
    )

    return twitter_profile_url
