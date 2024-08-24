import pprint

import openai

from config import GPT_API_KEY

# Replace with your actual OpenAI API key
openai.api_key = GPT_API_KEY


def chat_with_gpt(prompt):
    response_gpt = openai.ChatCompletion.create(
        model="gpt-4",  # Updated to use the correct model name
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500  # You can adjust this value based on your needs
    )
    pprint.pp(response_gpt)
    return response_gpt['choices'][0]['message']['content']


# Example usage
user_input = "Provide all Internet information and business network links about Artel Uzbekistan"
response = chat_with_gpt(user_input)
# print(response)
