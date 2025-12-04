from typing import List
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama
from ollama import Tool, chat


@tool
def convert_temperature(from_unit: str,temperature: float,  to_unit: str) -> float:
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        temperature: The temperature value to convert., this must be a float type
        from_unit: 'C' for Celsius, 'F' for Fahrenheit. this must be a str 
        to_unit: 'C' for Celsius, 'F' for Fahrenheit. this must be a str 

    Returns:
        Converted temperature value.
    """
    print("Ollama called convert temprature tool!!!!")
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return temperature

    if from_unit == "C" and to_unit == "F":
        return (temperature * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (temperature - 32) * 5/9
    else:
        raise ValueError("Units must be 'C' or 'F'")


llm = ChatOllama(model="llama3.1:8b", temperature=0)

agent = create_agent(llm, tools=[convert_temperature])
m = HumanMessage(content="covert 32 Fahrenheit to Celsius")
m2 = HumanMessage(content="what is 100 degree Celcius in Fahrenheit")

response = agent.invoke({
    "messages":[m]
    
})

for msg in reversed(response['messages']):
    if msg.__class__.__name__ == "AIMessage" and msg.content:
        print(msg.content)
        break

response = agent.invoke({
    "messages":[m2]
})

for msg in reversed(response['messages']):
    if msg.__class__.__name__ == "AIMessage" and msg.content:
        print(msg.content)
        break