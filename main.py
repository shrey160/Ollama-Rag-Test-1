from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_db import retriever

import re
regex_pattern = r"<think>[\s\S]*?<\/think>\n?\n?"   #to remove the thinking part

import os
from dotenv import load_dotenv,dotenv_values
load_dotenv()

m2 = os.getenv("MODEL_2")
print(m2)

model = OllamaLLM(model=m2)

template = """
You are an expert in recommendation for the restaurant named "Pizza Place" and thus will be asked about various type of restaurants and where the best type of particular food will be available, etc.
You might also be expected to plan some retaurants based on rough iternary and thu, you would be expected to recommend multiple restaurants at a time. 

Example:
User: " We are going to a bar and then would be going to a have dinner after it, 
can you recommend some bar that bar that ha good beer and BBQ restaurant?"
Expected Workflow: First search for the firt type of restaurant and then look for the other and recommend them."

If the user asks for a particular style of pizza/dish, search for the pizza or dish that fits the description and include its name in the result. 
If you cannot find the appropriate result, inform the user about it.

Example: 
User: Do they have any vegan pizza.
Agent-action: 1.) first search for the required pizza, in this case you got a result with name "tropical blast".
If you also obtain the name of the dish/ pizza, be sure to include the name of the pizza/dish in the final result.


You should not be overly formal but at the ame time, keep your answers simple and easy to understand as the users typically prefer short answer with a touch of familiarity,
as if they are having a conversation with friend.
Do not hallucinate and give at-most 3 recomendation with the information such a the place's name .

Here are some relevant reviews: {reviews}

Here is the question to answer: {questions}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

##test
"""
chain.invoke({"reviews":["Lafamilia is the best pizza place in town"],"questions":"What is the best pizza place in town?"})
"""
while True:
    print("\n\n ----------------------")
    question = input("Ask your question (q to quit):")
    if question == "q":
        break
    
    print("\n\n ------    Answer  ---------")
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews":reviews,"questions":question})
    result = re.sub(regex_pattern, '', result)
    print(result)
    print("\n\n------------------------------")
