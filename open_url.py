import os

'''
Function to open a web page in Microsoft Edge

Params:
    url - the url of the website to open
'''
def open_url(url):
    os.system(f"""\"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe\" {url}""")