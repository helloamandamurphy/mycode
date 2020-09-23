#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def easy():
    for animal in farms[0]["agriculture"]:
        print(animal)

def getFarm():
    farm = input("What farm would you like to learn more about? (Enter 1-3)")
    print("1. NE Farm, 2. W Farm, 3. SE Farm")
    return int(farm)-1

def medium():
    i = getFarm()
    print("Plants and animals on this farm include:")
    getAg(i)

def getAg(i):
    for ag in farms[i]['agriculture']:
        print(ag)

def hard():
    i = getFarm()
    print("Animals on this farm include:")
    getAnimals(i)

def getAnimals(i):
    for ag in farms[i]['agriculture']:
        while ag not in ["celery", "carrots"]:
            print(ag)
            break 

#easy()
#medium()
hard()
