def isSymbol(char):
    return (char >= '0' and char <= '9') or char == '+' or char == '*'

def operate(n, op, n2):
    if op == '+':
        return n + n2
    else:
        return n * n2

def evaluate(puzzle):
    i = 0
    LHS = 0
    op = '+'
    while i < len(puzzle):
        if puzzle[i] == '(':
            j = 1
            openedBrackets = 1
            while openedBrackets:
                if puzzle[i+j] == '(':
                    openedBrackets += 1
                elif puzzle[i+j] == ')':
                    openedBrackets -= 1
                j += 1
            LHS = operate(LHS, op, evaluate(puzzle[i+1:i+j-1]))
            i += j
        elif puzzle[i] >= '0' and puzzle[i] <= '9':
            LHS = operate(LHS, op, int(puzzle[i]))
        elif puzzle[i] == '+' or puzzle[i] == '*':
            op = puzzle[i]
        i += 1
    return LHS

def addBrackets(puzzle):
    i = 0
    symbols = 0
    locs = []
    while i < len(puzzle):
        if puzzle[i] == '+':
            locs.append(symbols)
        if isSymbol(puzzle[i]):
            symbols += 1
        i += 1

    for loc in locs:
        symbols = 0
        i = 0
        while i < len(puzzle):
            if isSymbol(puzzle[i]):
                if symbols == loc:
                    # travel right
                    j = 0
                    inserted = False
                    brackets = 0
                    while not inserted:
                        j += 1
                        if not brackets and isSymbol(puzzle[i+j]):
                            puzzle.insert(i+j+1, ')')
                            inserted = True
                        if puzzle[i+j] == '(':
                            brackets += 1
                        if puzzle[i+j] == ')':
                            brackets -= 1
                            if not brackets:
                                puzzle.insert(i+j+1, ')')
                                inserted = True

                    # travel left
                    j = 0
                    inserted = False
                    brackets = 0
                    while not inserted:
                        j -= 1
                        if not brackets and isSymbol(puzzle[i+j]):
                            puzzle.insert(i+j, '(')
                            inserted = True
                        if puzzle[i+j] == ')':
                            brackets += 1
                        if puzzle[i+j] == '(':
                            brackets -= 1
                            if not brackets:
                                puzzle.insert(i+j, '(')
                                inserted = True
                symbols += 1
            i += 1
    return puzzle

def main(lines):
    puzzles = []
    for line in lines:
        puzzles.append([])
        for char in line.strip():
            puzzles[-1].append(char)

    answers = []
    for puzzle in puzzles:
        answers.append(evaluate(puzzle))
    print(sum(answers))

    answers = []
    for puzzle in puzzles:
        answers.append(evaluate(addBrackets(puzzle)))
    print(sum(answers))

def run(function, input_file):
    try:
        with open(input_file, "r") as fh:
            lines = fh.readlines()
    except:
        print(f"{input_file} not found in current directory. Skipping...")
        return
    function(lines)

print("TEST:")
run(main, "test.txt")
print("\nMAIN:")
run(main, "input.txt")
