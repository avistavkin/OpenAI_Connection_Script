#Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import AzureOpenAI

client = AzureOpenAI(azure_endpoint="https://andvis-openai.openai.azure.com/",
api_version="2023-05-15",
api_key="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")


response = client.chat.completions.create(model="Model1", # engine = "deployment_name".
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
    {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
    {"role": "user", "content": "Do other Azure AI services support this too?"}
])
print(response)
print(response['choices'][0]['message']['content'])