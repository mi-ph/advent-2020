def get_colour(line):
    colour = ""
    spaces = 0
    for char in line:
        if char == ' ':
            spaces += 1
        if spaces == 2:
            break
        colour += char
    return colour

def get_other_colours(line):
    colours = []
    numeric = False
    number = ""
    i = 0
    for char in line:
        i += 1
        if char > '0' and char < '9':
            numeric = True
            number += char
        elif numeric == True:
            colours.append((get_colour(line[i:]), int(number)))
            numeric = False
            number = ""
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
