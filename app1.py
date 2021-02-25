import json
import difflib
from difflib import get_close_matches

word = input("Please enter a word to look up in the Thesaurus.: ")
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data: 
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]}?, Please enter Y if yes, or N if not:  ")      
        if yn == "Y":
            return (data[get_close_matches(w, data.keys())[0]])
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist"



output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)



 

