'''
MAIN FUNCTION
Function to create a new python file, paste the code that ChatGPT provided and then run it.

Params:
    gpt_python_code - a string of the code provided by ChatGPT.

Returns:
    Output of the chatGPT code
'''
def run_gpt_python_code(gpt_python_code):
    returned_values = exec(gpt_python_code)
    return returned_values

run_gpt_python_code("print('HELLO WORLD')")

