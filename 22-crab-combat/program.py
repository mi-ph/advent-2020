def main(lines):
    lines = lines.split('\n\n')
    playerOneDeck = [int(a) for a in lines[0].split('\n')[1:]]
    playerTwoDeck = [int(a) for a in lines[1].split('\n')[1:-1]]

    playerOne = playerOneDeck.copy()
    playerTwo = playerTwoDeck.copy()
    combat(playerOne, playerTwo)
    determineWinnerScore(playerOne, playerTwo)

    playerOne = playerOneDeck.copy()
    playerTwo = playerTwoDeck.copy()
    recursiveCombat(playerOne, playerTwo)
    determineWinnerScore(playerOne, playerTwo)

def combat(playerOne, playerTwo):
    while len(playerOne) and len(playerTwo):
        one = playerOne[0]
        two = playerTwo[0]
        playerOne.remove(one)
        playerTwo.remove(two)
        if one > two:
            playerOne += [one, two]
        else:
            playerTwo += [two, one]

def determineWinnerScore(playerOne, playerTwo):
    winner = playerOne if playerOne else playerTwo
    multiplier = 1
    score = 0
    while winner:
        score += (winner.pop() * multiplier)
        multiplier += 1
    print(score)

def recursiveCombat(playerOne, playerTwo):
    seen = set()
    while len(playerOne) and len(playerTwo):
        record = (tuple(playerOne), tuple(playerTwo))
        if record in seen:
            return 1
        else:
            seen.add(record)
        one = playerOne[0]
        two = playerTwo[0]
        playerOne.remove(one)
        playerTwo.remove(two)
        if len(playerOne) >= one and len(playerTwo) >= two:
            result = recursiveCombat(playerOne.copy()[:one], playerTwo.copy()[:two])
            if result == 1:
                playerOne += [one, two]
            else:
                playerTwo += [two, one]
        elif one > two:
            playerOne += [one, two]
        else:
            playerTwo += [two, one]
    if playerOne:
        return 1
    else:
        return 2

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
