from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello World!")
    print(os.environ["OPENAI_API_KEY"])

summary_template = """
    Given the LinkedIn information {information} about the person from I want you to create:
    1. a short summary of the person
    2. two interesting facts about the person

"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template,
)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

# Notice how langchain makes the information variable available to the prompt
linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url="https://www.linkedin.com/in/pedro-moyano/"
)
print(chain.run(information=linkedin_data))
