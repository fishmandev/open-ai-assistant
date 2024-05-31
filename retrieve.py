from openai import OpenAI
import os

client = OpenAI()
assistant_id = os.environ["ASSISTANT_ID"]
assistant = client.beta.assistants.retrieve(assistant_id)
print(assistant)
