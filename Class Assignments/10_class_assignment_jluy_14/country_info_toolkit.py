from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from dotenv import load_dotenv
import os
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

with open("all_countries.json", "r", encoding="utf-8") as f:
    data = json.load(f)

country_data = data

def get_capital(country: str) -> str:
    return country_data.get(country, {}).get("capital", "Unknown")

def get_language(country: str) -> str:
    return country_data.get(country, {}).get("language", "Unknown")

def get_population(country: str) -> str:
    return country_data.get(country, {}).get("population", "Unknown")

@function_tool
def country_info_agent(country: str = "Name of the country") -> str:
    """
    Get information about a country (capital, language, population).
    """
    capital = get_capital(country)
    language = get_language(country)
    population = get_population(country)

    return (
        f"Country: {country}\n"
        f"Capital: {capital}\n"
        f"Language: {language}\n"
        f"Population: {population}\n"
    )

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.5-flash"
)

# Run Config
config = RunConfig(
    model=model,
    model_provider=client
)

# Agent
Country_info_Agent = Agent(
    name="Country Info Agent",
    instructions="""
    Tum ek helpful country information assistant ho.
    Tumhare paas ek tool hai jo country ke capital, language aur population laa kar de sakta hai.
    Jab user koi country pooche to hamesha tool se info laao
    aur Roman Urdu me jawab do.

    Example:
    User: "Pakistan ke baare me batao"
    Tum: "Pakistan ki capital Islamabad hai, official language Urdu hai, aur population takreeban 220 million hai."
    """,
    tools=[country_info_agent]
)

print("Country Info Agent Started! (type 'exit' to quit)\n")
while True:
    print("-" * 30)
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Good bye!")
        break

    result = Runner.run_sync(Country_info_Agent, user_input, run_config=config)
    print("Agent:", result.final_output)
    print()
