from open_url import *

'''
MAIN
Function to open a web page from the list of websites provided by ChatGPT

Params:
    relevant_search_arr - An array containing dictionaries of the relevant information from the Google search in {link, snippet, title} format
    number - the element number of the website to open
'''
def open_selected(relevant_search_arr, number):
    open_url(relevant_search_arr[number]["link"])