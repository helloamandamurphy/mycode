#!/usr/bin/python3

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
Should you confront them or run back to your friends?
Type `confront them` or `run back`
''')

whatToDo = ("What do you want to do now?")


def main(): 
    print(intro)
    move = input(">")
    if move == 'chase your friends':
        print(chaseFriends)
        num = input(">")
        lovesMe(num)

    elif move == 'slow down':
        print(slowDown)
        move = input(">")


validMoves = {
    {
        {'chase your friends' : chaseFriends},
        {'slow down': slowDown},
        # {'look around' : lookAround}
    },
}

def lovesMe(num):
    if (num % 2) == 0:
        print("He loves you not!")
    else: 
        print("He loves you!")

# What do you want to do now?
# >Stay and talk.
# >Go pick a bouquet in the field. 
