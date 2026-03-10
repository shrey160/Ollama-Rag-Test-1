This is a test project for developing local rag agents using ollama.

The python dependecies are added to requirements.txt except ipykernel.
Install all the dependancies using "pip install -r requirements.txt" of  "uv add -r requirements.txt"

First install ollama and then run "ollama pull <model_name>" to install the models. You can check out the official ollama site for more details.

You can first experiment with the models in the test.ipynb notebook where you can first tinker with the prompt and see the full result at the last.
models with 8b parameters like llama3.1:8b are recommended for a good result

Smaller models like lfm2.5-thinking:1.2b also work but might require extensive prompting example: If asked about a particular style of pizza, it would only return with yes or no but with a particular instruction in the prompt like:

"If the user asks for a particular style of pizza/dish, search for the pizza or dish that fits the description and include its name in the result. 
If you cannot find the appropriate result, inform the user about it.

Example: 
User: Do they have any vegan pizza.
Agent-action: 1. first search for the required pizza, in this case you got a result with name "tropical blast".
If you also obtain the name of the dish/ pizza, be sure to include the name of the pizza/dish in the final result."

The thinking models will give desired result.

