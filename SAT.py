'''
IMPORT LIBRARIES
'''
import urllib.request
import random
import json
import colorama
from random import shuffle


'''
OBTAIN DATA
'''
link = "https://raw.githubusercontent.com/lrojas94/SAT-Words/master/MajorTests%20Wordlist/majortests_words.json"
#link = "https://raw.githubusercontent.com/lrojas94/SAT-Words/master/Freevocabulary%20Wordlist/freevocabulary_words.json"
request = urllib.request.urlopen(link)
source = request.read()
request.close()
words = json.loads(source)['results']


'''
SET UP GAME
'''
colorama.init()
class color:
    # Text attributes
    ALL_OFF = '\033[0m'
    BOLD = '\033[1m'
    UNDERSCORE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    CONCEALED = '\033[7m'
    CLEAR_SCREEN = '\033[2J'

    # Foreground colors
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


print(color.CLEAR_SCREEN)
print(f"{color.BOLD}{color.BG_MAGENTA}Welcome to the SAT words game!{color.ALL_OFF}\n")

print(f"Please enter number of {color.BOLD}rounds{color.ALL_OFF}: ", end = '')
rounds = input()

print(f"Please enter number of {color.BOLD}players{color.ALL_OFF}: ", end = '')
players = input()

print()

players_names = {}
for player in range(0,int(players)):
    name = input(f"Player {player+1} Name: ")
    players_names[name] = 0


'''
WORDS
'''
def question(words):
    rand_int = random.randint(0,len(words)+1)
    temp = list(range(0, len(words)+1))
    temp.remove(rand_int)
    options = random.sample(set(temp), 3)  
    
    definition = words[rand_int]['definition']
    
    correct_answer = words[rand_int]['word']
    option1 = words[options[0]]['word']
    option2 = words[options[1]]['word']
    option3 = words[options[2]]['word']

    dic_options = {correct_answer: "Correct",
                   option1: "Wrong", option2: "Wrong", option3: "Wrong"}
    
    return definition, dic_options, correct_answer

'''
GAME LOOP
'''
print()
print(f"{color.BOLD}{color.BG_GREEN}Let's start!{color.ALL_OFF}")
for i in range(int(rounds)):
    print(f"{color.FG_GREEN}ROUND {i+1}{color.ALL_OFF}")
    for player in players_names:
        print(f"{color.FG_MAGENTA}{player}'s turn{color.ALL_OFF}")
        definition, dic_options, correct_answer = question(words)
        values = list(dic_options.keys())
        shuffle(values)
        print(f"Find the correct word for the following definition:")
        print(f"{color.FG_CYAN}{definition}{color.ALL_OFF}")
        print(f" 1) {values[0]}\n 2) {values[1]}\n 3) {values[2]}\n 4) {values[3]}\n 5) I don't know")
        print("Answer: ", end="")
        answer = input()
        if int(answer)==5:
            print(f"The correct answer was {correct_answer}!")
        elif dic_options[values[int(answer)-1]]=="Correct":
            print("That's correct!")
            players_names[player] = players_names[player]+1
        else:
            print(f"Wrong! The correct answer was {correct_answer}!")
            players_names[player] = players_names[player]-1
        print()
    print()
print()
print(f"{color.BG_YELLOW}SCORES!!!{color.ALL_OFF}")
for val in sorted(players_names.items(), key=lambda x: x[1], reverse=True):
    print(f"{val[0]}: {val[1]} points!")


