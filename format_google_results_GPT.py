from ask_google_SERP import *
from ask_GPT import * 

'''
MAIN FUNCTION
Given a dictionary of relevant google search responses, get ChatGPT to provide
a summary of each link

Params:
    relevant_search_arr - An array containing dictionaries of the relevant information from the Google search in {link, snippet, title} format
    model=4 - use gpt4 or gpt 3.5 model (4 by default)

Returns:
    Output from ChatGPT API
'''
def format_google_results_GPT(relevant_search_arr, model=4):
    # Provide the relevant search array to ChatGPT

    instructions = f"""
        Here is a summary of some google search results: {relevant_search_arr[0:2]}

        List me out the site name and the title along with a summary based on the snippet. Do not include the link. Keep the summary under 20 words for each site.
    """

    # Get the response from ChatGPT
    response = ask_GPT(instructions, model)

    return response