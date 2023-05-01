import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


while True:
    prompt = input()
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0.1,
        max_tokens = 1000
    )

    response = completion.choices[0].message.content
    print(f"{response}\n\n")
