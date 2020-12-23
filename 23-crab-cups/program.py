def main(lines):
    cups = {}
    startingCups = [int(cup) for cup in lines.strip()]

    # puzzle 1
    cups = playCups(startingCups, len(startingCups), 100)
    answer = []
    currCup = 1
    for i in range(len(cups) - 1):
        nextCup = cups[currCup]
        answer.append(str(nextCup))
        currCup = nextCup
    print("".join(answer))

    # puzzle 2
    cups = playCups(startingCups, 1000000, 10000000)
    print(cups[1] * cups[cups[1]])

def playCups(startingCups, numberOfCups, numberOfMoves):
    cups = {}
    firstCup = startingCups[0]
    for i in range(len(startingCups) - 1):
        cups.update({startingCups[i]: startingCups[i+1]})
    currCup = startingCups[-1]
    nextCup = max(cups) + 1
    while len(cups) < numberOfCups - 1:
        cups.update({currCup: nextCup})
        currCup = nextCup
        nextCup += 1
    cups.update({currCup: firstCup})

    currentCup = firstCup
    cupMax = max(cups)

    moves = 0
    while moves < numberOfMoves:
        removed = cups[currentCup]
        removedCups = [removed, cups[removed], cups[cups[removed]]]
        cups.update({currentCup:cups[cups[cups[cups[currentCup]]]]})
        destinationCup = currentCup - 1
        while destinationCup in removedCups or destinationCup not in cups:
            if destinationCup in removedCups:
                destinationCup -= 1
            if destinationCup not in cups:
                destinationCup = cupMax
        cups.update({cups[cups[removed]]:cups[destinationCup]})
        cups.update({destinationCup:removed})
        currentCup = cups[currentCup]
        moves += 1
    return cups

def run(function, input_file):
    try:
        with open(input_file, "r") as fh:
            lines = fh.read()
    except:
        print(f"{input_file} not found in current directory. Skipping...")
        return
    function(lines)

print("TEST:")
run(main, "test.txt")
print("\nMAIN:")
run(main, "input.txt")
