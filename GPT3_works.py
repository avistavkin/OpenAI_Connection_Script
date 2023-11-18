#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai


openai.api_type = "azure"
openai.api_base = "https://andvis-openai.openai.azure.com/"

#os.environ['HG_USER']
#"https://andvis-openai.openai.azure.com/"
#os.getenv("AZURE_OPENAI_ENDPOINT") 
openai.api_version = "2023-05-15"
openai.api_key = "999dfa8e15214b08b2ed2c0c637c21f8"
openai_api_key = "999dfa8e15214b08b2ed2c0c637c21f8"
npm_access_token = "999dfa8e15214b08b2ed2c0c637c21f8"
"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"
#os.getenv("AZURE_OPENAI_KEY")

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
