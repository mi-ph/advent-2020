def get_colour(line):
    return ' '.join(line.split(' ')[0:2])

def get_other_colours(line):
    colours = []
    words = line.split(' ')
    for i in range(len(words)):
        if words[i].isnumeric():
            colours.append((' '.join(words[i+1:i+3]), int(words[i])))
    return colours

def contains(colours, colour):
    for colour in colours[colour]:
        if colour[0] == "shiny gold" or contains(colours, colour[0]):
            return 1
    return 0

def bagsIn(colours, colourName):
    numBags = 0
    for colour in colours[colourName]:
        numBags += colour[1] * (bagsIn(colours, colour[0]) + 1)
    return numBags

with open("input.txt", "r") as fh:
    lines = fh.readlines()
    colours = {}
    for line in lines:
        colours.update({get_colour(line): get_other_colours(line)})
    containsGold = 0
    for colour in colours:
        containsGold += contains(colours, colour)
    print(containsGold)
    print(bagsIn(colours, "shiny gold"))
