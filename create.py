from openai import OpenAI

client = OpenAI()


def main():
    assistant = client.beta.assistants.create(
        name="Fishman",
        description="Fishman's assistant",
        tools=[],
        model="gpt-3.5-turbo",
    )
    print(assistant)


if __name__ == "__main__":
    main()
