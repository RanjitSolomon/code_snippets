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

big_font = pyfiglet.figlet_format("Few - shot", font="big")
print(big_font)

# Get the model 
print("") 
system_message ="""
    classify the sentiment of the following text as positive or negative or neural. 
    Example 1: 'I love this place' -> Positive 
    Example 2: 'I hate the weather today.' -> Negative 
    Example 3: 'I hate the food here, it's amazing!' -> Neutral
"""
user_message = system_message +  "What is the sentiment of the text: I love this place! but I hate the food here" 
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role':'system',
            'content': "You are helpful assistant"
        },
        {
            'role': 'user',
            'content': user_message
        }
    ]
)

print("AI : " , response.choices[0].message.content)
