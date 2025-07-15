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

big_font = pyfiglet.figlet_format("Meta Prompt", font="big")
print(big_font)

# Get the model 
print("") 

delimiter = "####"

# Define the prompt 
prompt = """ 
    Imagine you are teaching a school students how to solve a math problem.
    "A teacher has 24 candies. She wants to distribute them equally among 6 students. How many candies does each student get?" 

    Step 1: Explain the strategy for solving the problem 
    Step 2: Sove the problem step-by-step based on the stratgy 
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
