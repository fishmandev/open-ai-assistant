from openai import OpenAI

client = OpenAI()


def main():
    assistant_list = client.beta.assistants.list()

    for item in assistant_list:
        print(item.name, item.id)


if __name__ == "__main__":
    main()
