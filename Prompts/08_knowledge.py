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

big_font = pyfiglet.figlet_format("Gen Knowledge", font="big")
print(big_font)

# Get the model 
print("") 

url = "GET https://atlas.microsoft.com/weather/forecast/hourly/json?api-version=1.1&query={query}"

# Define the prompt 
parameters ="""
name\tlie in\tnecessary\ttype\tDescription
format\tpath\tTrue\tJson Format\tRequired format for the response. Only supported json formats.
api-version\tquery\tTrue\tstring\tThe version number of the Azure Maps Service API.
query\tquery\tTrue\tnumber[]\tApplicable queries specified as a comma-separated string consisting of latitude followed by longitude, for example "47.641268,-122.125679".
    Generally, weather information applies to locations on land, bodies of water enclosed by land, and ocean areas within approximately 50 nautical miles of a coastline.
duration\tquery\tinteger\tThe time range for the returned weather forecast. By default, forecast data for the next hour is returned. Available values are
    1- Returns forecast data for the next hour. The default value.
    12- Returns an hourly forecast for the next 12 hours.
    24- Returns hourly weather forecast for the next 24 hours.
    72- Returns an hourly forecast for the next 72 hours (3 days).
    120- Returns an hourly forecast for the next 120 hours (5). Only available in the S1 SKU.
    240- Returns an hourly forecast for the next 240 hours (10 days). Only available in S1 SKU.
language\tquery\tstring\tThe language in which search results should be returned. This should be one of the supported IETF language tags, case-insensitive. When data in the specified language is not available for a particular field, a default language will be used.
"""

prompt = """here's the documentation for Get Hourly Forecast api endpoint write a python code to call this REST API. """

prompt += url + "\n" + parameters

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
