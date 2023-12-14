#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

openai.api_type = "azure"
openai.api_base = "https://andvis-openai.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "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"

response = openai.ChatCompletion.create(
    engine="Model1", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)
print(response)
print(response['choices'][0]['message']['content'])