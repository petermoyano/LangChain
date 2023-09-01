from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# import os

# Custom packages (agent and tools for the agent)
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets

name = "Elon Musk"
if __name__ == "__main__":
    # Agent execution: name: str -> str
    # This agent will return a linkedin profile url starting with a name
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    # scarpe linkedin profile page and return information for LLMChain
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=100)

    summary_template = """
        Given the LinkedIn LinkedIn information {linkedin_information} and twitter information {twitter_information} about a person, I want you to create:
        1. a short joke about the person
        1. a short summary of the person
        2. two interesting facts about the person
    """

    # Langchain automatically passes the information variable to the prompt
    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
    )

    # llm inizialization
    llm = ChatOpenAI(temperature=0, model_name="gpt4")

    # Chain execution
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # This function uses the Proxycurl API to scrape information from a LinkedIn profile
    # and returns a cleaned dict of the scraped data.
    # scrape_linkedin_profile: linkedin_profile_url: str -> dict

    print(chain.run(linkedin_information=linkedin_data, twitter_information=tweets))

    scrape_user_tweets(username="@elonmusk")
