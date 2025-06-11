import os
from openai import AzureOpenAI

endpoint = os.getenv("OPENAI_API_ENDPOINT")
deployment = os.getenv("OPENAI_DEPLOYMENT_NAME")
api_key = os.getenv("OPENAI_API_KEY")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2025-01-01-preview"
)

completion = client.chat.completions.create(
    model=deployment,
    messages= [
        {
            "role": "user",
            "content": """
                What is the result of 10 + 10?
            """
        }
    ],
    max_completion_token=4096,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())