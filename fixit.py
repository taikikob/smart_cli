import subprocess
import sys
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Takes the command, error, and sends an api request to grok, returns groq's completion
def get_groq_fix(command, error):
    prompt = f"The user ran this command: {command}\nIt failed with this error: {error}\nExplain why it failed in one sentence and provide the corrected command."

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user", "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return completion.choices[0].message.content

def run_command(command_list):
    
    # Joins the list back into a string command
    full_command = " ".join(command_list)

    # Run the command
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"\nCommand failed. Asking Groq for help...")
        fix = get_groq_fix(full_command, result.stderr)
        print(f"\nGroq's Suggestion:\n{fix}")
    else:
        print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_command(sys.argv[1:])
    else:
        print("Usage: python fixit.py [your command]")
