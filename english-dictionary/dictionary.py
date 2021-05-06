import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_out(word):
    #make a word with lowercase
    word = word.lower()
    #check completely match like: carrot
    if word in data:
        return data[word]
    #check the word with the capitalized first character like: Carrot
    elif word.title() in data:
        return data[word.title()]
    #check the word with uppercase like: CARROT
    elif word.upper() in data:
        return data[word.upper()]
    #show predictions if its more than 0
    elif len(get_close_matches(word, data.keys())) > 0:
        #print 3 predictions
        guesses = [get_close_matches(word, data.keys())[0],get_close_matches(word, data.keys())[1], get_close_matches(word, data.keys())[2], "Try another way"]
        for index, guess in enumerate(guesses):
            print(str(index) + ". " +guess)

        decision = int(input("Please select index number you want to know: "))

        if decision == 0:
            return get_close_matches(word, data.keys())[0] + " : \n" + str(find_out(get_close_matches(word, data.keys())[0]))
        elif decision == 1:
            return get_close_matches(word, data.keys())[1] + " : \n" + str(find_out(get_close_matches(word, data.keys())[1]))
        elif decision == 2:
            return get_close_matches(word, data.keys())[2] + " : \n" + str(find_out(get_close_matches(word, data.keys())[2]))
        elif decision == 3:
            #find out word again
            user_input = input("Please enter word: ")
            return find_out(user_input)
        else:
            return "You choose the wrong number. Try it again"
    #comletely not match
    else:
        return "Please try another way."

#input in python is always string type
user_input = input("Please enter word: ")
print(find_out(user_input))



