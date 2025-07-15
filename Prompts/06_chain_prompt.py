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

big_font = pyfiglet.figlet_format("Chain of Prompt", font="big")
print(big_font)

# Get the model 
print("") 

# Define the prompt 
prompt ="The problem is: A teacher has 24 candies. She wants to distribute them equally among 6 students. How many candies does each student get?"

prompt = """ 
    1. Imagine you are teaching a school students how to solve a math problem.
    2. The problem is: "A teacher has 24 candies. She wants to distribute them equally among 6 students. How many candies does each student get?" 
    3. Think step by step and provide the answer. 
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
