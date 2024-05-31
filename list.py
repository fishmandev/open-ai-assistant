from openai import OpenAI

client = OpenAI()
assistant_list = client.beta.assistants.list()

for item in assistant_list:
    print(item.name)
