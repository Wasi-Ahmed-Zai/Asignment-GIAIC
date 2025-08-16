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

# Mood Analyzer Agent
mood_analyzer_agent = Agent(
        name = "Mood Analyzer",
        instructions = "Listen to the user's message and identify their mood. Reply with ONLY ONE WORD in lowercase English (e.g., happy, sad, stressed, excited, angry, tired, bored, nervous, calm, confused). No extra words, punctuation, or emojis."
)

# Mood Analyzer Agent
activity_suggester_agent = Agent(
    name = "Activity Suggester",
    instructions =  "Diya gaya mood aur user ka message dekh kar chhota, practical mashwara ya activity suggest karo. Jawab sirf Roman Urdu me do. 1–2 jumlay, seedha mashwara; emojis, headings ya extra tafseel na ho."
)


print("Mood Analyzer started! (type 'exit' to quit)\n")

while True:
    # User ka message input
    print("-"*30)
    user_message = input("You: ")

    # Program exit karne ka option
    if user_message.lower() == "exit":
        print("Goodbye! 👋")
        break

    # Step 1: Detect mood
    mood_result = Runner.run_sync(mood_analyzer_agent, user_message, run_config=config)
    normalized_mood = mood_result.final_output

    print("Detected Mood:", normalized_mood)

    # Step 2: Mood ke hisab se Roman Urdu me suggestion do
    prompt = f"Mood: {normalized_mood}. User said: {user_message}. Is mood ke hisaab se Roman Urdu me ek behtareen activity suggest karo."
    suggestion = Runner.run_sync(activity_suggester_agent, prompt, run_config=config)
    
    print("Suggested Activity:", suggestion.final_output)
    print()
