#!/usr/bin/env python3

import statistics 
from statistics import mode 

# Iron Man, Captain America, Hulk, Thor, Black Widow, and Hawkeye (6)

welcome = "Hello hero, which Avenger are you?"

#Questions
question1 = "What would you risk your life for?"
answers1 = ["Hope", "Justice", "Freedom", "Peace", "Duty", "Honor", "Family", "Purpose", "Redemption"]

question2 = "Who would you bring home to meet your parents?"
answers2 = ["Captain Marvel", "Hulk", "Iron Man", "Captain America", "Ant-Man", "Okoye", "Thor", "Black Widow", "Nebula"]

question3 = "If you could wield one Infinity stone, which would it be?"
answers3 = ["Power", "Soul", "Reality", "Space", "Time", "Mind"]

question4 = "What's your biggest flaw?"
answers4 = ["I live in the past", "I bite off more than I can chew", "I'm flaky", "I'm insecure", "I leap before I look", "I'm stubborn", "I lie", "I don't pay attention to what's around me", "I'm narrow-minded", "I don't take time for myself", "I overreact"]

question5 = "If you were alone when the snap happened, who would you call first?"
answers5 = ["Your parents", "Your significant other", "Your pets", "Your siblings", "Your kids", "Your best friend", "Your coworkers", "Your favorite celebrity", "Someone not listed"]

results = list()

def answersToString(answers):
    for num, answer in enumerate(answers, start=1):
        print(f"{num}. {answer}")

def checkAndAppend(response):
    if 1 <= int(response) <= 6:
        results.append(int(response) -1)
    else:
        print("Please enter a number between 1 and 6")

def most_common(results):
    char = mode(results)

    if char == 0:
        print("Iron Man")
    if char == 1:
        print ("Captain America")
    if char == 2:
        print("Hulk")
    if char == 3:
        print("Thor")
    if char == 4:
        print("Black Widow")
    if char == 5:
        print("Hawkeye")


#Starts program
print(welcome)

#This could be cut down later using a dictionary to contain all questions/answers and then iterating through to print all questions/answers

print(question1)
resp = input(answersToString(answers1)) 
checkAndAppend(resp)
print(f"Results: {results}")
print(" ")

print(question2)
resp = input(answersToString(answers2))
checkAndAppend(resp)
print(f"Results: {results}")
print(" ")

print(question3)
resp = input(answersToString(answers3))
checkAndAppend(resp)
print(f"Results: {results}")
print(" ")

print(question4)
resp = input(answersToString(answers4))
checkAndAppend(resp)
print(f"Results: {results}")
print(" ")

print(question5)
resp = input(answersToString(answers5))
checkAndAppend(resp)
print(f"Results: {results}")
print(" ")

print("The results are in!")
print(" ")

print("You are...")
print(" ")
most_common(results)
