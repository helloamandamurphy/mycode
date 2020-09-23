#!/usr/bin/env python3

import requests

# {"number": 3, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}], "message": "success"}

def main():
    r = requests.get("http://api.open-notify.org/astros.json").json()
    numInSpace = r['number']

    print(f"People in space: {numInSpace}")
    peopleInSpace(r)

def peopleInSpace(r):
   ppl =  r['people']
   for person in ppl:
       name = person['name']
       craft = person['craft']
       print(f"{name} on the {craft}")

main()
