import os
from openai import OpenAI


client = OpenAI()


def main():
    assistant_id = os.environ["ASSISTANT_ID"]
    assistant = client.beta.assistants.retrieve(assistant_id)
    print(assistant)


if __name__ == "__main__":
    main()
