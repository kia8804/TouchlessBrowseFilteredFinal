import key
import http.client
import json

'''
MAIN FUNCTION
Function to organize and return relevant information from the SERPER API request

Params:
    question - a string of the provided question

Returns:
    An array containing dictionaries of the relevant information in {link, snippet, title} format
'''
def ask_google_SERP(question):
    response_dict = get_SERP_results(question)
    relevant_responses = {}

    # NEEDS CORRECTING
    # # The quick blurb at the top of the search
    # try:
    #     relevant_responses["quick response"] = response_dict["organic"][0]["snippet"] # THE GOOGLE PROVIDED DESCRIPTION OF THE STUFF
    # except:
    #     relevant_responses["quick response"] = "No quick summary description" # THE GOOGLE PROVIDED DESCRIPTION OF THE STUF

    # Pairs of links and their snippets
        
    relevant_responses = []
    
    # Itterate through all elements of the response_dict and add the {link, snippet, title} to the list from the organic section as a dictionary
    for i in range(len(response_dict["organic"])):
        relevant_responses.append({
            "link": response_dict["organic"][i]["link"],
            "snippet": response_dict["organic"][i]["snippet"],
            "title": response_dict["organic"][i]["title"]
        })
    
    return relevant_responses
'''
Function to run Google searches and return the JSON response a dictionary

Params:
    question - a string of the provided question

Returns:
    A dictonary version of the JSON output
'''
def get_SERP_results(question):
    question = str(question)
    # SERPER API provided code
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
        "q": f"{question}"
    })
    headers = {
        'X-API-KEY': key.Serp(),
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data.decode("utf-8"))

    return json_data

# Test use case on how to query thru
# response = get_SERP_results("What is the capital of Canada?")
# print(response)

# print(response["answerBox"]["answer"])