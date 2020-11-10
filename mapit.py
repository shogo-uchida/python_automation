# this is map it

import webbrowser, sys, pyperclip
# sys is for having some arguments from command line argument
# pyperclip, when you use clip (ctr + C)
browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
# making the brorser google chrome

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# check if command line argument were passed

if len(sys.argv) > 1:
    # i wanna do '870', 'Valencia', 'St.' -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    # when you copy sth, you dont even need to paste it, instead pyperclip.paste() will automatically paste it

browser.open('https://www.google.com/maps/place/' + address)
# https://www.google.com/maps/place/<ADDRESS>










