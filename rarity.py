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

        option1Occured = 0
        option2Occured = 0
        option3Occured = 0
        option4Occured = 0
        option5Occured = 0

        for i in range(numToRoll):
            prevTotals = 0
            numPick = random.uniform(1, totalNum)
            for key, value in rarities.items():
                if numPick <= value + prevTotals:
                    if key == "common":
                        prize = random.choice(common)
                        option1Occured += 1
                    elif key == "uncommon":
                        prize = random.choice(uncommon)
                        option2Occured += 1
                    elif key == "rare":
                        prize = random.choice(rare)
                        option3Occured += 1
                    elif key == "legendary":
                        prize = random.choice(legendary)
                        option4Occured += 1
                    elif key == "mythical":
                        prize = random.choice(mythical)
                        option5Occured += 1
                    break
                prevTotals += value
        print("Option 1 Occured:", option1Occured, "| Real Percentage:", (option1Occured/numToRoll)*100, "%")
        print("Option 2 Occured:", option2Occured, "| Real Percentage:", (option2Occured/numToRoll)*100, "%")
        print("Option 3 Occured:", option3Occured, "| Real Percentage:", (option3Occured/numToRoll)*100, "%")
        print("Option 4 Occured:", option4Occured, "| Real Percentage:", (option4Occured/numToRoll)*100, "%")
        print("Option 5 Occured:", option5Occured, "| Real Percentage:", (option5Occured/numToRoll)*100, "%")
            
    except:
        if plrInput == "stop":
            playing = False
        else:
            print("unhandled response, try again ")