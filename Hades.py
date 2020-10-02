#!/usr/bin/python3

# Text Game by Amanda Murphy

# To do: 
## Add input check

import time
import sys

banner = ('''

                         ___                                                ___               
                        (   )                                              (   )              
 ___  ___  ___   .--.    | |    .--.      .--.    ___ .-. .-.     .--.      | |_       .--.   
(   )(   )(   ) /    \   | |   /    \    /    \  (   )   '   \   /    \    (   __)    /    \  
 | |  | |  | | |  .-. ;  | |  |  .-. ;  |  .-. ;  |  .-.  .-. ; |  .-. ;    | |      |  .-. ; 
 | |  | |  | | |  | | |  | |  |  |(___) | |  | |  | |  | |  | | |  | | |    | | ___  | |  | | 
 | |  | |  | | |  |/  |  | |  |  |      | |  | |  | |  | |  | | |  |/  |    | |(   ) | |  | | 
 | |  | |  | | |  ' _.'  | |  |  | ___  | |  | |  | |  | |  | | |  ' _.'    | | | |  | |  | | 
 | |  ; '  | | |  .'.-.  | |  |  '(   ) | '  | |  | |  | |  | | |  .'.-.    | ' | |  | '  | | 
 ' `-'   `-' ' '  `-' /  | |  '  `-' |  '  `-' /  | |  | |  | | '  `-' /    ' `-' ;  '  `-' / 
  '.__.'.__.'   `.__.'  (___)  `.__,'    `.__.'  (___)(___)(___) `.__.'      `.__.    `.__.'  
                                                                                              
                                                                                              
 ___                     ___                                                                  
(   )                   (   )                                                                 
 | | .-.     .---.    .-.| |    .--.       .--.                                               
 | |/   \   / .-, \  /   \ |   /    \    /  _  \                                              
 |  .-. .  (__) ; | |  .-. |  |  .-. ;  . .' `. ;                                             
 | |  | |    .'`  | | |  | |  |  | | |  | '   | |                                             
 | |  | |   / .'| | | |  | |  |  |/  |  _\_`.(___)                                            
 | |  | |  | /  | | | |  | |  |  ' _.' (   ). '.                                              
 | |  | |  ; |  ; | | '  | |  |  .'.-.  | |  `\ |                                             
 | |  | |  ' `-'  | ' `-'  /  '  `-' /  ; '._,' '                                             
(___)(___) `.__.'_.  `.__,'    `.__.'    '.___.'                                              
                                                                                              

Text Game by Amanda Murphy                                                                                            
''')

def instructions():
    print('''
    Thanks for playing Welcome to Hades.
    To view the INSTRUCTIONS, please enter `i`.
    To continue without instructions, press any key.
    ''')
    resp = input(">")
    if resp == "i":
        print('''
        "Welcome to Hades" is a story game. Press any key to continue
        the story, and enter type your move when prompted.
        Press any key to start the game.
        ''')
    input()


def intro():
    input()
    print('''
    You've finally escaped your mother and her long list of chores.
    You push through the trees, chasing after your friends,
    out into a wide field, blanketing the ground in wild flowers. ''')
    input()
    print('''
        What do you want to do?
        Type `chase your friends` or `slow down`
    ''')

def chaseFriends():
    print('''
    Your friends flop into the grass on the far side of the field to pick flowers.
    They start plucking the petals off flowers playing He loves me, He loves me not.
        ''')
    input()
    print('''
        How many letters are in your crush's name?
        Enter a number between 1-20.
    ''')

def slowDown():
    print('''
    You slow down and drag you hand along the tops of the flowers and grass.
    You look up at the sky and see Helios, then look down back towards the trees.
    There are sun spots in your eyes, but you think you see someone in the woods.
    ''')
    input()
    print('''
        Should you confront her or run back to your friends?
        Type `confront her` or `run back`
    ''')

def afterLovesMe():
    print('''
        What do you want to do now? Talk with your friends or go explore?
        Type `talk` or `explore`
    ''')

def talkToFriends():
    print("The girls exchange gossip.")
    input()
    print('       "Want to hear something funny?" one asks.')
    input()
    print("The girls nod.")
    input()
    print(''' 
        "I was with Artemis the other day while she was bathing, 
        and this creepy hunter was trying to watch. So she turned
        him into a stag!"
    ''')
    input()
    print("The girls laugh with laughter like tinkling bells.")
    input()
    print('       "It turns out he had dogs, so that did not end well for him."')
    input()
    print("Tinkling bells again.")
    input()
    print('       "Do you feel that?" another girl asks. ')
    input()
    print("Pretty soon you can all feel it--the ground is shaking.")

def exploreTheField(): 
    print('''
        You see an iris away from the girls and walk toward it.
        This doesn't seem to be the right place for it, but sure enough it's there.
    ''')
    input()
    print('''
        You reach out and pick the iris. As soon as it's picked, the ground below
        you begins to shake violently.
    ''')

def confront():
    print('''
        You walk slowly and quietly towards the trees. You thought you saw a woman,
        right behind the big knotted tree, but you can't be sure.
        ''')
    input()
    print(''' 
        Silently you make your way toward the trees, not blinking, 
        but when you get to the tree and sneak around it, 
        there's no one there.
    ''')
    input()
    print("You hear a cracking sound as the ground starts to shake and the tree roots break.")

def run(): 
    print("You run back quickly to your friends.")
    input()
    print('       "I think I saw something in the trees," you say.')
    input()
    print('       "It is probably nothing," says one girl lazily.')
    input()
    print('       "Besides," says another. "Zeus is your father, so you have nothing to be afraid--"')
    input()
    print("       But just then, the ground starts to rumble.")

def hadesArrives(): 
    print('''
        The ground shakes more and more violently. Your friends whimper and scream,
        trying to hide behind anything they can. A few begin to run, but it doesn't matter,
        because if the gods want them, they will find them.
        ''')
    input()
    print('''
        Eventually the center of the field breaks open, and a god emerges.
        The girls begin to cry.
        ''')
    input()
    print("He calls your name across the field, but you can hear it like a close whisper.")
    
    printName()

    print('''
        Do you approach him or run?
        Type `approach` or `run`
    ''')

def printName():
    name = "Persephone".upper()
    name_list = list()
    name_list[:0]=name
    
    for letter in name_list:
        print(letter, end=' ', flush=True) 
        time.sleep(.75)

def approachHades(): 
    print("You walk toward Hades.")
    input()
    print('       "Hello, Persie," he says, and you two drop down to the Underworld.')

def runFromHades():
    print("You take off as fast as you can, but it doesn't matter.")
    input()
    print("Hades doesn't even have to run after you.")
    input()
    print('''
        One moment, he's grabbed you by the arms, and then next you've both dropped
        down into the Underworld.
        ''')
    input()
    print('       "You should have known better than that," he says. "No one can escape death."')

gameOverAscii = ('''

  .-_"""-.      ____    ,---.    ,---.    .-''-.              ,-----.    ,---.  ,---.   .-''-.  .-------.     
 '_( )_   \   .'  __ `. |    \  /    |  .'_ _   \           .'  .-,  '.  |   /  |   | .'_ _   \ |  _ _   \    
|(_ o _)|  ' /   '  \  \|  ,  \/  ,  | / ( ` )   '         / ,-.|  \ _ \ |  |   |  .'/ ( ` )   '| ( ' )  |    
. (_,_)/___| |___|  /  ||  |\_   /|  |. (_ o _)  |        ;  \  '_ /  | :|  | _ |  |. (_ o _)  ||(_ o _) /    
|  |  .-----.   _.-`   ||  _( )_/ |  ||  (_,_)___|        |  _`,/ \ _/  ||  _( )_  ||  (_,_)___|| (_,_).' __  
'  \  '-   .'.'   _    || (_ o _) |  |'  \   .---.        : (  '\_/ \   ;\ (_ o._) /'  \   .---.|  |\ \  |  | 
 \  `-'`   | |  _( )_  ||  (_,_)  |  | \  `-'    /         \ `"/  \  ) /  \ (_,_) /  \  `-'    /|  | \ `'   / 
  \        / \ (_ o _) /|  |      |  |  \       /           '. \_/``".'    \     /    \       / |  |  \    /  
   `'-...-'   '.(_,_).' '--'      '--'   `'-..-'              '-----'       `---`      `'-..-'  ''-'   `'-'   
                                                                                                              

''')

# def validInput(input):
#     if input in turns.keys():
#         return turns[input]
#     else: print("Sorry, I don't understand. Try again.")

# turns = {
#         {"chase your friends": chaseFriends()},
#         "talk": talkToFriends(),
#         "explore": exploreTheField(), 
#         "slow down": slowDown(), 
#         "confront her": confront(),
#         "run back": run()
#         }

def main(): 
    instructions()
    print(banner)
    intro()
    move = input(">")
    if move == 'chase your friends':
        chaseFriends()
        num = int(input(">"))
        lovesMe(num)
        afterLovesMe()
        move = input(">")
        if move == "talk":
            talkToFriends()
            hades()
        elif move == "explore":
            exploreTheField()
            hades()

    elif move == 'slow down':
        slowDown()
        move = input(">")
        if move == "confront her":
            confront()
            hades()
        elif move == "run back":
            run()
            hades()

def lovesMe(num):
    if (num % 2) == 0:
        print("He loves you not!")
    else: 
        print("He loves you!")

def hades():
    input()
    print(".")
    input()
    print(".")
    input()
    print(".")
    input()
    hadesArrives()
    move = input(">")
    if move == "approach":
        approachHades()
    elif move == "run":
        runFromHades()
    gameOver()

def gameOver():
    input()
    print(".")
    input()
    print(".")
    input()
    print(".")
    input()
    print(gameOverAscii)

main()

# Hey Chad, I worked on a few things this week:

# I messed around with an API from one of the labs (on Monday, I think)
# because I thought I needed more practice with that.

# I added a lot more time.sleep()'s in the code to get the text to print out
# slower--this involved changing my variables that contained the text to print
# into functions, but I ultimately was unhappy with it, so I switched those to
# `input()` so the player can move at their own pace.

# Next I was trying to get Persephone's name to spell out one letter at a time
# horizontally (I tried a couple things that printed each letter on a new line)
# I tried importing sys, as per some Stack Overflow, but found out the solution
# was simpler.

# I started working on input validation, but wasn't able to get it to work.
# I wanted to use a switch case that would execute a function if the input matched,
# and found that Python uses dictionaries for this. When I implemented it,
# it would print out one string just fine, but it ended up executing all of the functions
# in the dictionary rather than just one that matched the input. So I just commented
# my code out for the moment, and reverted everything else back to its working state.
