#Note: The openai-python library support for Azure OpenAI is in preview.
import os  
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_GPT4"),
api_version="2023-05-15",
api_key=os.getenv("AZURE_OPENAI_KEY_GPT4"))  
import logging  
  
# Set up Azure OpenAI API credentials  
  
try:  
    response = client.chat.completions.create(model="gpr4model1", # engine = "deployment_name".  
    messages=[  
        {"role": "system", "content": "You are a helpful assistant."},  
        {"role": "user", "content": "What do you kmnow about Sinergija events happen every year in Serbia?"},  
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},  
        {"role": "user", "content": "Which Senergija event was the best one?"}  
    ])  
      
    print(response)  
    print(response['choices'][0]['message']['content'])  
      
except Exception as e:  
    logging.error(f'Unsuccessful connection to Azure OpenAI: {str(e)}')  
