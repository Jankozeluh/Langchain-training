import configparser
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain.chains import LLMMathChain
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper, SQLDatabase
from langchain_core.runnables import RunnableConfig
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI
from sqlalchemy import create_engine
import sqlite3
from pathlib import Path
import streamlit as st
import asyncio
from callbacks.capturing_callback_handler import playback_callbacks
from callbacks.clear_results import with_clear_container

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# OPENAI API KEY
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['api']['key']

llm = OpenAI(temperature=0, openai_api_key=api_key, streaming=True)
search = DuckDuckGoSearchAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm)

DB_PATH = (Path(__file__).parent / "knowledge.db").absolute()
creator = lambda: sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
db = SQLDatabase(create_engine("sqlite:///", creator=creator))
db_chain = SQLDatabaseChain.from_llm(llm, db)

# Tools setup
tools = [
    # Tool(
    #     name="Search",
    #     func=search.run,
    #     description="useful for when you need to answer questions about current events. You should ask targeted questions",
    # ),
    # Tool(
    #     name="Calculator",
    #     func=llm_math_chain.run,
    #     description="useful for when you need to answer questions about math",
    # ),
    Tool(
        name="FDB",
        func=db_chain.run,
        description="useful for when you need to answer questions about ichthyology, books, taxonomy, fishing science, fish. Input should be in the form of a question containing full context",
    )
]

react_agent = create_react_agent(llm, tools, hub.pull("hwchase17/react"))
mrkl = AgentExecutor(agent=react_agent, tools=tools)

st.set_page_config(page_title="MRKL", page_icon="🦜", layout="wide", initial_sidebar_state="collapsed")
st.write("# 🦜🔗 Fast MRKL")

with st.form(key="form"):
    user_input = st.text_input("Ask your own question")
    submit_clicked = st.form_submit_button("Submit Question")

output_container = st.empty()
if with_clear_container(submit_clicked):
    output_container = output_container.container()
    output_container.chat_message("user").write(user_input)

    answer_container = output_container.chat_message("assistant", avatar="🦜")
    st_callback = StreamlitCallbackHandler(answer_container)
    cfg = RunnableConfig()
    cfg["callbacks"] = [st_callback]

    answer = mrkl.invoke({"input": user_input}, cfg)

    answer_container.write(answer["output"])

