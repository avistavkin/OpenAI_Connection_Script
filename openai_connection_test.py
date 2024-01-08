from openai import OpenAI

client = OpenAI(api_key=api_key)  
import logging  
import sys  
import os  
  
# Get API key from environment variable  
api_key = os.getenv("OPENAI_API_KEY")  
  
if not api_key:  
    logging.error("Please set your OPENAI_API_KEY environment variable")  
    sys.exit(1)  
  
# Set the OpenAI API key  
  
try:  
    # Make a request to the API  
    client.completions.create(engine="text-davinci-002", prompt="Test", max_tokens=5)  
except Exception as e:  
    logging.error("Failed to connect to OpenAI: %s", e)  
    sys.exit(1)  
  
logging.info("Successfully connected to OpenAI")  
