import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w1 = w.lower() #normal cases
    w2 = w.title() #edge cases for words like China, Canada
    w3 = w.upper() #edge cases for words like USA, NATO
    listOfPotentialMatch = get_close_matches(w, data.keys(), cutoff = 0.8)
    if w1 in data in data:
        return data[w1]
    elif w2 in data:
        return data[w2]
    elif w3 in data:
        return data[w3]
    elif len(listOfPotentialMatch) > 0:
        potentailWord = listOfPotentialMatch[0]
        userYesOrNoResponse = input(f"Did you mean {potentailWord}? Enter Y for yes, N otherwise.\n")
        if userYesOrNoResponse.lower() == "y":
            return data[potentailWord]
        elif userYesOrNoResponse.lower() == "n":
            return "This word does not exist. Please try again."
        else:
            return "We did not understand your entry. (Please follow the instructions)"
    else:
        return "This word does not exist. Please double check."

word = input("Enter word: ")

definition = translate(word)

if type(definition) is list:
    index = 0
    print("Definition(s): ")
    for meaning in definition:
        index += 1
        print(f"{index}) {meaning}")
else:
    print(definition)
