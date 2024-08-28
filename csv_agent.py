#from langchain_community.chat_models import ChatOpenAI #from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
import os

# os.environ['OPENAI_API_KEY'] = ""

def csv_ai_chatbot(user_query):
    LLM = ChatOpenAI(temperature=1, openai_api_key=os.environ['OPENAI_API_KEY'], model='gpt-4')

    file_path = "Property Details.csv"
    
    # Initialize memory
    memory = ConversationBufferMemory()
    conversation_history = memory.load_memory_variables({})['history']

    prompt_template = f"""
    You are a real estate agent with access to detailed property information.
    The data includes Link, Price, Address (use it for location), Broker name, broker phone number, 
    Brokerage company, brokerage address, brokerage phone number, brokerage website, MLS Number, Property description, 
    Property type, building type, community name, annual property taxes, parking space, bedrooms above grade, 
    bedrooms below grade, bathrooms, features, cooling, heating, Storeys, land size, Parking type, 
    appliances included, Flooring, Basement features, Basement type, Building Amenities, Pool type, 
    Land frontage, Land depth, etc.

    Respond to the Query: {user_query}

    **Important Instruction**: You need to provide the complete link each time whenever you think the user is asking for the website.

    Here is the History of the conversation. This history will also help you to answer user queries:
    {conversation_history}
    """

    agent = create_csv_agent(
        llm=LLM,
        path=file_path,
        verbose=True,
        allow_dangerous_code=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        # handle_parsing_errors=True
    )

    response = agent.invoke(prompt_template)
    memory.save_context({"input": user_query}, {"output": response})
    
    return response
