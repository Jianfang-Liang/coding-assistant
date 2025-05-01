#Step 1: Set up imports and load API key
import os
from openai import OpenAI
from dotenv import load_dotenv

client= OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
load_dotenv()

#Step 2: Create a function to talk to OpenAI
def ask_openai(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
        ],
        max_tokens = 400, #This controls the maximum length of the reply
        temperature = 0.5
    )
    return response.choices[0].message.content.strip() 

#Step 3: Create a function to run the assistant 
def run_assistant():
    print("\n👋 Welcome to CodeBuddy – your friendly coding assistant!")
    print("💡 Type 'exit' to quit or 'annotate:' followed by code for line-by-line explanations.\n")

    while True:
        user_input = input("You> ").strip()
        if user_input.lower() in ("exit","quit"):
            print("👋 Goodbye! Happy coding!\n")
            break
        else:
            if user_input.startswith("annotate: "):
                code = user_input[len("annotate: "):].strip() 
                prompt = f"Explain the following code for a beginner, line by line:\n\n{code}"
            else:
                prompt =  (
                    "You are a helpful and friendly coding tutor for beginners. "
                    "Explain clearly and include simple code examples when helpful.\n\n"
                    f"Question: {user_input}"
                )
            reply = ask_openai(prompt)
            print("\nAssistant>\n" + reply + "\n")

#Step 4: add the program entry point
if __name__ == "__main__":
    run_assistant()



