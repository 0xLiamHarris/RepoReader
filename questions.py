# questions.py
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
import os
from config import model_name

# Initialize ChatOpenAI with the model name from config.py
chat_model = ChatOpenAI(model_name=model_name, temperature=0.2, openai_api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(question, repo_name, github_url):
    # Define the system message with repository context
    system_message = SystemMessage(content=f"You are a helpful assistant analyzing the GitHub repository named '{repo_name}' located at {github_url}. Provide detailed answers based on the repository's code and documentation.")

    # Define the human message with the user's question
    human_message = HumanMessage(content=question)

    # Construct the chat prompt using the system and human messages
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

    # Generate a response from ChatOpenAI
    response = chat_model.chat(chat_prompt.format_prompt().to_messages())

    # Assuming the response object contains a 'content' attribute with the answer
    answer = response.content  # Adjust based on actual structure of the response object

    return answer
