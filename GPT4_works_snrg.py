#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

# Set up Azure OpenAI API credentials
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT_GPT4")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY_GPT4")

response = openai.ChatCompletion.create(
    engine="gpr4model1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What do you kmnow about Sinergija events happen every year in Serbia?"},
        {"role": "assistant", "content": "Yes, this event happens every year and is very popular."},
        {"role": "user", "content": "Which Senergija event was the best one?"}
    ]
)

print(response)
#print(response['choices'][0]['message']['content'])