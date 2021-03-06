import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0: #gets closest matches by checking its similarity ratio
        yn=input("Did you mean %s instead? Enter y if yes,or n if no :" %get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "This word does not exist. Please check again"
        else:
            return "Sorry. We didn't understand your query"
    else:
        return "This word does not exist. Please check again"

word=input("Enter word:")
output=translate(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)