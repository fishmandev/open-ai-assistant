import os
from openai import OpenAI

client = OpenAI()


def main():
    assistant_id = os.environ["ASSISTANT_ID"]
    client.beta.assistants.delete(assistant_id)
    print(f"Deleted: {assistant_id}")


if __name__ == "__main__":
    main()
