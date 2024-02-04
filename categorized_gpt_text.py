import openai
from get_text_from_website import *
import key

'''
MAIN FUNCTION
Function to categorize the text from a website into different sections

Params:
    raw_text - the raw text from the website, unfiltered

Returns:
    A dictionary of all text from the website seperated by categories
'''

import openai
import re

# Set your OpenAI API key
openai.api_key = key.OpenAIKey()


def clean_text(raw_text, topic):
    if topic is None:
        return "No relevant information found."

    # Use regular expressions to extract content related to the topic
    pattern = re.compile(
        rf'\b{re.escape(topic)}\b(.+?)(?=\b\w+\b|$)', re.DOTALL | re.IGNORECASE)
    match = pattern.search(raw_text)

    if match:
        return match.group(1).strip()
    else:
        return "No relevant information found."


def categorize_gpt_text(raw_text):
    # Truncate the raw text to fit within the model's token limit
    truncated_text = raw_text[:4096]

    # Specify the prompt for the GPT model
    prompt = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Please categorize the following text:\n{truncated_text}\nTopic:"},
    ]

    # Use OpenAI GPT model to generate categories
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the specified model
        messages=prompt,
        max_tokens=1000,  # Adjust as needed
    )

    # Extract the generated topic from the GPT response
    generated_response = response['choices'][0]['message']['content']

    # Split the generated response into lines
    lines = [line.strip() for line in generated_response.split('\n')]

    # Identify the topic based on the generated response
    topic = None

    for line in lines:
        if line.startswith("Topic:"):
            topic = line[len("Topic:"):].strip()
            break

    # Extract content related to the topic using regular expressions
    content = clean_text(raw_text, topic)

    # Return the result as a dictionary
    result = {'topic': topic, 'content': content}
    return result


# Example usage
text_to_categorize = get_text_from_website(
    "https://en.wikipedia.org/wiki/Introspection")
result = categorize_gpt_text(text_to_categorize)
print(result)
