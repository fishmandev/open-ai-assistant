from openai import OpenAI

client = OpenAI()
assistant = client.beta.assistants.create(
    name="Fishman", description="Fishman's assistant", tools=[], model="gpt-3.5-turbo"
)
print(assistant)
