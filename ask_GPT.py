import openai
import key
from openai import *

# UPDATE TO LATEST OPENAI METHOD

'''
MAIN FUNCTION
Function to pass text based instructions to GPT.

Params:
    instructions - string of instructions to give to ChatGPT
    model=4 - use gpt4 or gpt 3.5 model

Returns:
    Output from ChatGPT API
'''
# def ask_GPT(instruction, model=4):


def ask_GPT(instructions, model=3.5):
    # Set the API key for OpenAI
    openai.api_key = key.OpenAIKey()

    client = OpenAI(api_key=key.OpenAIKey())

    # Define the model to use
    if model == 4:
        model_name = "gpt-4-0125-preview"
    elif model == 3.5:
        model_name = "gpt-3.5-turbo-0125"
    else:
        raise ValueError(
            "Invalid model version. Please choose either 4 or 3.5.")

    # Generate the response using ChatGPT API
    response = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        # model="gpt-4-1106-preview",
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant",
            },
            {"role": "user", "content": instructions},
        ],
    )

    # Return the generated response
    return response.choices[0].message.content
