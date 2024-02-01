"""
Open a web browser and search for a user-provided query on Bing AI.

The user can enter the query either as an input or directly in the code.
The function uses pyperclip to copy and paste the query, and pyautogui
to simulate keyboard actions.

"""
import time
import webbrowser
import pyperclip
import pyautogui

def brows():

    # Method 1: get the query from the user input
    query = input("Enter your query: ")
    pyperclip.copy(query)

    # Method 2: get the query from the code
    # query = "Ram"
    # pyperclip.copy(query)

    # Method 3: copy the text to the clipboard using pyperclip
    #pyperclip.copy('Enter the query you wish to copy to the clipboard')

    # To use a different method, add # before the method you are not using and remove # from the method you wish to use

    # Open the web browser with the Bing AI URL
    url = "https://www.bing.com/search?form=NTPCHB&q=Bing+AI&showconv=1"
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open(url)

    # Wait for the browser to load
    time.sleep(5)

    # Paste the query and press enter
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('Enter')

# Call the function
brows()
