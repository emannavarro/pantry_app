from dotenv import dotenv_values, find_dotenv
import openai

if __name__ == "__main__":
    env_path = find_dotenv(".env")
    config   = dotenv_values(env_path)

    openai.api_key = config["API_KEY"]

    prompt   = input("Enter a prompt for chatGPT: ")
    response = openai.Completion.create(
        engine      = "text-davinci-003",
        prompt      = prompt,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print(response.choices[0].text)