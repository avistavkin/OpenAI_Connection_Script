
#Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import AzureOpenAI

# Set up Azure OpenAI API credentials
client = AzureOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_GPT4"),
api_version="2023-05-15",
api_key=os.getenv("AZURE_OPENAI_KEY_GPT4"))



response = client.chat.completions.create(model="gpr4model1",
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What do you kmnow about Sinergija events happen every year in Serbia?"},
    {"role": "assistant", "content": "Yes, this event happens every year and is very popular."},
    {"role": "user", "content": "Which Senergija event was the best one?"}
])

#print(response)
# Print the assistant's response
print("Assistant's response:", response.choices[0].message.content)

