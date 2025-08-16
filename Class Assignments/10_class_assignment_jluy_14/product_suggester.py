from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel 
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
     api_key=GEMINI_API_KEY,   
     base_url="https://generativelanguage.googleapis.com/v1beta"
) 

model = OpenAIChatCompletionsModel(
        openai_client=client,         
        model="gemini-2.5-flash"     
)

config = RunConfig(
        model_provider=client,  
        model=model               
)

Product_Suggester_Agent = Agent(
        name="Product Suggester Agent",
        instructions="You are a helpful store assistant. Suggest a suitable product based on the user's problem or need, and explain why it is useful. Always reply in Roman Urdu."
)

print("Product Suggestion started! (type 'exit' to quit)\n")
while  True:

    print("-"*30)
    user_input = input("you :")

    if user_input.lower() == "exit":
        print("Good bye!.")
        break

    result = Runner.run_sync(Product_Suggester_Agent, user_input, run_config = config  )

    print("Suggestion:", result.final_output)
    print()
