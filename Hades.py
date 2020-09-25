#!/usr/bin/python3

# Text Game by Amanda Murphy

import time
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
                                                                                              
                                                                                              
''')
intro = ('''
You've finally escaped your mother and her long list of chores.
You push through the trees, chasing after your friends,
out into a wide field, blanketing the ground in wild flowers.
What do you want to do?
Type `chase your friends` or `slow down`
''')

chaseFriends = ('''
Your friends flop into the grass on the far side of the field to pick flowers.
They start plucking the petals off flowers playing He loves me, He loves me not.
How many letters are in your crush's name?
Enter a number between 1-20.
''')

slowDown = ('''
You slow down and drag you hand along the tops of the flowers and grass.
You look up at the sky and see Helios, then look down back towards the trees.
There are sun spots in your eyes, but you think you see someone in the woods.
Should you confront her or run back to your friends?
Type `confront her` or `run back`
''')

afterLovesMe = ('''
What do you want to do now? Talk with your friends or go explore?
Type `talk` or `explore`
''')

talkToFriends = ('''
The girls exchange gossip. 
    "Want to hear something funny?" one asks.
The girls nod. 
    "I was with Artemis the other day while she was bathing, 
    and this creepy hunter was trying to watch. So she turned
    him into a stag!"
The girls laugh with laughter like tinkling bells.
    "It turns out he had dogs, so that didn't end well for him."
Tinkling bells again.
    "Do you feel that?" another girl asks.
Pretty soon you can all feel it--the ground is shaking.
''')

exploreTheField = ('''
You see an iris away from the girls and walk toward it.
This doesn't seem to be the right place for it, but sure enough it's there.
You reach out and pick the iris. As soon as it's picked, the ground below
you begins to shake violently.
''')

confront = ('''
You walk slowly and quietly towards the trees. You thought you saw a woman,
right behind the big knotted tree, but you can't be sure.
Silently you make your way toward the trees, not blinking, 
but when you get to the tree and sneak around it, 
there's no one there.
You hear a cracking sound as the ground starts to shake and the tree roots break.
''')

run = ('''
You run back quickly to your friends.
    "I think I saw something in the trees," you say.
    "I'm sure it's nothing," says one girl.
    "Besides, says another. Zeus is your father, so you have nothing to be afraid--"
    But just then the ground starts to rumble.
''')

hadesArrives = ('''
The ground shakes more and more violently. Your friends whimper and scream,
trying to hide behind anything they can. A few begin to run, but it doesn't matter,
because if the gods want them, they will find them.
Eventually the center of the field breaks open, and a god emerges.
The girls begin to cry.
He calls your name across the field, but you can hear it like a close whisper.

P E R S E P H O N E

Do you approach him or run?
Type `approach` or `run`
''')

approachHades = ('''
You walk toward Hades.
"Hello, Persie," he says, and you two drop down to the Underworld.
''')

runFromHades = ('''
You take off as fast as you can, but it doesn't matter.

Hades doesn't even have to run after you.
One moment, he's grabbed you by the arms, and then next you've both dropped
down into the underworld.

"You should have known better than that," he says. "No one can escape death."
''')

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

def main(): 
    print(banner)
    time.sleep(1)
    print(intro)
    move = input(">")
    if move == 'chase your friends':
        print(chaseFriends)
        num = int(input(">"))
        time.sleep(1)
        lovesMe(num)
        time.sleep(1)
        print(afterLovesMe)
        move = input(">")
        if move == "talk":
            time.sleep(1)
            print(talkToFriends)
            hades()
        elif move == "explore":
            time.sleep(1)
            print(exploreTheField)
            hades()

    elif move == 'slow down':
        print(slowDown)
        move = input(">")
        if move == "confront her":
            time.sleep(1)
            print(confront)
            hades()
        elif move == "run back":
            time.sleep(1)
            print(run)
            hades()

def lovesMe(num):
    if (num % 2) == 0:
        print("He loves you not!")
    else: 
        print("He loves you!")

def hades():
    time.sleep(3)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(hadesArrives)
    move = input(">")
    if move == "approach":
        print(approachHades)
    elif move == "run":
        print(runFromHades)
    gameOver()

def gameOver():
    time.sleep(3)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(gameOverAscii)

main()

# Hey Chad, I think the logic side of this could be improved--
# the writer half of me was being a little bossy regarding the string output.
# I wanted to drop into another room (with items, etc.) after this, 
# but it took a little longer than I had hoped.
