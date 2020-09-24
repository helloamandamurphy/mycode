#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    
    all = input("Do you want to print all facts? Enter y or n: ")
    if all == "y":
        printAll(r)
    random = input("Do you want a random fact?")
    if random == "y":
        getRandom(r)

def printAll(r):
    for catfact in r.json()["all"]:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found

def getRandom(r):
    print(random.choice(r.json()).get("text"))

main()
