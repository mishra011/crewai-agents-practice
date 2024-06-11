from crewai import Agent

from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import AzureChatOpenAI

from crewai_tools.tools import WebsiteSearchTool, FileReadTool
from crewai_tools import SerperDevTool
from langchain_community.tools import DuckDuckGoSearchRun

from crewai import Task
from crewai import Crew, Process


## TOOL 
web_search_tool = WebsiteSearchTool()
#seper_dev_tool = SerperDevTool()
#web_search_tool = SerperDevTool()
search_tool = DuckDuckGoSearchRun()


## AGENT

# from langchain_google_genai import ChatGoogleGenerativeAI

# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_VERSION = os.getenv("AZURE_VERSION")
AZURE_DEP_NAME = os.getenv("AZURE_DEP_NAME")

llm = AzureChatOpenAI(deployment_name=AZURE_DEP_NAME,
                         openai_api_version=AZURE_VERSION,
                          openai_api_key=AZURE_KEY,
                           azure_endpoint=AZURE_ENDPOINT)

upsc_researcher=Agent(
    role="Researcher",
    goal='Uncover ground breaking and latest data and content for the {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "UPSC is one of the toughtest Exams in India."
        "innovation, eager to explore and share knowledge that could change"
        "the prepration of UPSC aspirants."

    ),
    tools=[web_search_tool, search_tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

upsc_writer = Agent(
  role='Writer',
  goal='Narrate the detail with compelling stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner to educate a UPSC aspirant's."
  ),
  tools=[web_search_tool, search_tool],
  llm=llm,
  allow_delegation=False
)

## TASK
# Writing task with language model configuration
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its opportunities, and potential risks."
  ),
  expected_output='A comprehensive 5 paragraphs long report on the latest UPSC trends.',
  tools=[web_search_tool, search_tool],
  agent=upsc_researcher,
)

# Writing task with language model configuration
writer_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the UPSC aspirants."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} formatted as markdown.',
  tools=[web_search_tool, search_tool],
  agent=upsc_writer,
  async_execution=False,
  output_file='upsc-blog.md'  # Example of output customization
)

# EXECUTE

crew=Crew(
    agents=[upsc_researcher, upsc_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    timeout=60
)


import streamlit as st


st.title('UPSC Career Counseler')
input_text=st.text_input("Enter your seach query here..")

if input_text:
    st.write(crew.kickoff(inputs={'topic':input_text}))


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
