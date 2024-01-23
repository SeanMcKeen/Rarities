import random

rarities = { # In percent format
    "common" : 50,
    "uncommon" : 35,
    "rare" : 14,
    "legendary" : 1,
    "mythical" : 0.1,
    "blasphemous" : 0.01
}

searchFor = "blasphemous"

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
                    if key == searchFor:
                        print(key)
                        print(numPick)
                    break
                prevTotals += value
    except:
        if plrInput == "stop":
            playing = False
        else:
            print("unhandled response, try again ")