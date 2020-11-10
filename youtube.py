# this opens youtube with the typed words

import webbrowser, sys, pyperclip

browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')

if len(sys.argv) > 1:
    typed = ' '.join(sys.argv[1:])
    # this will be like type = 'despacito cover'

else:
    typed = pyperclip.paste()

browser.open('https://www.youtube.com/results?search_query=' + typed)







