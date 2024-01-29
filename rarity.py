import random

rarities = { # In percent format
    "common" : 50,
    "uncommon" : 35,
    "rare" : 14,
    "legendary" : 1,
    "mythical" : 0.1
}

common = ["dog", "cat"]
uncommon = ["bird", "turtle"]
rare = ["fox", "owl"]
legendary = ["bear", "moose"]
mythical = ["polar bear", "dragon"]

searchFor = "mythical"

totalNum = 0
for x in rarities.values():
    totalNum += x
print(totalNum)

playing = True
while playing:
    plrInput = input("Enter amount of times to roll, or type 'stop': ")
    try:
        plrInput = int(plrInput)
        numToRoll = plrInput
        for i in range(numToRoll):
            prevTotals = 0
            numPick = random.uniform(1, totalNum)
            for key, value in rarities.items():
                if numPick <= value + prevTotals:
                    if key == "common":
                        prize = random.choice(common)
                    elif key == "uncommon":
                        prize = random.choice(uncommon)
                    elif key == "rare":
                        prize = random.choice(rare)
                    elif key == "legendary":
                        prize = random.choice(legendary)
                    elif key == "mythical":
                        prize = random.choice(mythical)
                    print(prize)
                prevTotals += value
    except:
        if plrInput == "stop":
            playing = False
        else:
            print("unhandled response, try again ")