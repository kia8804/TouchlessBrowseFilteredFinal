from text_to_speech import *
from record_audio_convert_to_text import *
import openai

'''
Given the results provided by ChatGPT of a list of websites to visit, select 
the number of the website that the user chose to visit.

Params:
    gpt_conversation - the conversation provided by ChatGPT
    model - the model to use for ChatGPT (3.5 by default)

Returns:
    The number of the website to visit from the list
'''
def select_website(gpt_conversation, model = 3.5):

    # Inform the user to select a website
    ask_user = "Here are the websites I found. Which website to you wish to visit."
    text_to_speech(ask_user)
    print("Assistant:", ask_user)

    # Get the response from the user
    user_reply = record_whisper_audio_transcript()
    print("User:", user_reply)

    # Get the number of the website to visit from ChatGPT
    # Set the API key for OpenAI
    openai.api_key = key.OpenAIKey()

    client = OpenAI(api_key=key.OpenAIKey())

    # Define the model to use
    if model == 4:
        model_name = "gpt-4-0125-preview"
    elif model == 3.5:
        model_name = "gpt-3.5-turbo-0125"
    else:
        raise ValueError("Invalid model version. Please choose either 4 or 3.5.")

    # Generate the response using ChatGPT API
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system", "content": "You are a helpful assistant. When responding to all queries only return an integer number. Previously you found the following websites: " + gpt_conversation + "Which website would you like to visit?",
            },
            {"role": "user", "content": user_reply + "\nReturn just the number of the website I selected."},
        ],
        max_tokens=10  # This is an attempt to limit the output; adjust based on trial and error
    )
 
    # Return the generated response
    reply = response.choices[0].message.content.strip()
    print("DEBUG", reply)
    reply_split = reply.split(" ")
    for x in reply_split:
        if x.isdigit():
            website_number_gpt = int(x)
            break
    print("Assistant: Will visit website #"+str(website_number_gpt))

    website_number = website_number_gpt-1
    return website_number

    # Get the response from ChatGPT