from dotenv import dotenv_values, find_dotenv
import openai

if __name__ == "__main__":
    env_path = find_dotenv(".env")
    config   = dotenv_values(env_path)

    openai.api_key = config["API_KEY"]

    prompt   = input("Enter a prompt for chatGPT: ")
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens = 60,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    print(response.choices[0].text)