from openai import OpenAI 
import os 
from dotenv import load_dotenv 
import pyfiglet 

# Load the environment variables 
load_dotenv() 

# Get the API key from the environment variables 
api_key = os.getenv("OPENAI_API_KEY") 

# Create an Instance of OpenAI 
client = OpenAI(api_key=api_key)

big_font = pyfiglet.figlet_format("Self Prompt", font="big")
print(big_font)

# Get the model 
print("") 

delimiter = "####"

# Define the prompt 
prompt = """ 
    Generate multiple ways to solve the problem: "What is 15 x 23?"

    returns: 
        list: A list of solutions.
    
    Task: 
        - Find the most consistent answer from the list. 
        - If there are differences, explain why and give the most likely correct answer.
"""

print(" ")
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role':'system',
            'content': "You are helpful assistant"
        },
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

print("AI : " , response.choices[0].message.content)
