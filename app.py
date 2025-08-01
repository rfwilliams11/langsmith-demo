import os
from dotenv import load_dotenv
from langchain import hub
from langsmith import traceable
from langsmith.client import convert_prompt_to_openai_format
from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam
from typing import List
import nest_asyncio
import retriever

# os.environ["OPENAI_API_KEY"] = ""
# os.environ["LANGCHAIN_API_KEY"] = ""
# os.environ["LANGSMITH_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = "langsmith-demo-4"

load_dotenv(dotenv_path="../../.env", override=True)
nest_asyncio.apply()

MODEL_NAME = "gpt-4o-mini"
MODEL_PROVIDER = "openai"

# RAG_SYSTEM_PROMPT = """You are an assistant for question-answering tasks.
# Use the following pieces of retrieved context to answer the latest question in the conversation.
# If you don't know the answer, just say that you don't know.
# Use one sentence maximum and keep the answer concise.
# """

# Note that we are pulling our prompt from LangChain's Hub
prompt = hub.pull("ls-demo-v1")

openai_client = OpenAI()


@traceable(run_type="chain")
def retrieve_documents(question: str):
    return retriever.retriever.invoke(question)


@traceable(
    run_type="llm",
    metadata={"ls_provider": MODEL_PROVIDER, "ls_model_name": MODEL_NAME},
)
def call_openai(messages: List[ChatCompletionMessageParam]) -> ChatCompletion:
    return openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )


@traceable(run_type="chain")
def generate_response(question: str, documents):
    formatted_docs = "\n\n".join(doc.page_content for doc in documents)
    formatted_prompt = prompt.invoke({"context": formatted_docs, "question": question})
    messages = convert_prompt_to_openai_format(formatted_prompt)["messages"]
    return call_openai(messages)


@traceable(run_type="chain")
def langsmith_rag(question: str):
    documents = retrieve_documents(question)
    response = generate_response(question, documents)
    return response.choices[0].message.content
