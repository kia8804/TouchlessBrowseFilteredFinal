# This is a file containing all the different functions that ChatGPT will use to run the self instruction code
# These contain just the docstrings and basic idea descriptions. Each function should be its own file to avoid
# overriding each other's work on github pushes.

''' DONE
Function to create a new python file, paste the code that ChatGPT provided and then run it.

Params:
    gpt_python_code - a string of the code provided by ChatGPT.

Returns:
    Output of the chatGPT code
'''
# def run_gpt_python_code(gpt_python_code):


''' DONE
MAIN FUNCTION
Function to organize and return relevant information from the SERPER API request

Params:
    question - a string of the provided question

Returns:
    An array containing dictionaries of the relevant information from the Google search in {link, snippet, title} format
'''
# def ask_google_SERP(question): DONE

'''
MAIN FUNCTION
Function to get all text from a website given a URL and return it as a string.

Params:
    url - the url of the website to get text from

Returns:
    A string of all text from the website
'''
# def get_text_from_website(url): DONE

'''
MAIN FUNCTION
Function to categorize the text from a website into different sections

Params:
    raw_text - the raw text from the website, unfiltered

Returns:
    A dictionary of all text from the website seperated by categories
'''
# def categorized_gpt_text(raw_text):

# def convert_audio_to_text_WHISPER():

# def convert_user_audio_to_text():


''' DONE
MAIN FUNCTION
Given a dictionary of relevant google search responses, get ChatGPT to provide
a summary of each link

Params:
    relevant_search_arr - An array containing dictionaries of the relevant information from the Google search in {link, snippet, title} format
    model=4 - use gpt4 or gpt 3.5 model (4 by default)

Returns:
    Output from ChatGPT API
'''
# def format_google_results_GPT(relevant_search_dict, model=4):

''' DONE
MAIN FUNCTION
Function to pass text based instructions to GPT.

Params:
    instructions - string of instructions to give to ChatGPT
    model=4 - use gpt4 or gpt 3.5 model

Returns:
    Output from ChatGPT API
'''
# def ask_GPT(instruction, model=4):


'''
MAIN FUNCTION
Given the results provided by ChatGPT of a list of websites to visit, select 
the number of the website that the user chose to visit.

Params:
    gpt_conversation - the conversation provided by ChatGPT
    model - the model to use for ChatGPT (3.5 by default)

Returns:
    The number of the website to visit from the list
'''
# def select_website(gpt_conversation, model = 3.5)


'''
MAIN
Function to open a web page in Microsoft Edge

Params:
    url - the url of the website to open
'''
# def open_url(url):

'''
MAIN
Function to open a web page from the list of websites provided by ChatGPT

Params:
    relevant_search_arr - An array containing dictionaries of the relevant information from the Google search in {link, snippet, title} format
    number - the element number of the website to open
'''
# def open_selected(relevant_search_arr, number):