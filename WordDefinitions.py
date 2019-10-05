import json
import difflib as db
data=json.load(open("076 data.json"))

def translate(word):

    if word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif word not in data:
        inputs=input("your Mean is {} Y for yes OR N for No: ".format(db.get_close_matches(word,data.keys())[0]))
        if inputs=="Y":
            return data[db.get_close_matches(word,data.keys())[0]]
        elif inputs=="N":
            return "Word does not exist"
        else:
            return "We didn't understand your entry."
    else:
        return "Word does not exist"

if __name__=='__main__':
    output=translate(input("Type Word: ",))
    if type(output) is list:
        for i in output:
            print(i)
    else:
        print(output)
