from copy import deepcopy
EMPTY = 'L'
FILLED = '#'

INF = 2 ** 31 - 1

def main(lines):
    matrix = []
    for line in lines:
        matrix.append([])
        for char in line.strip():
            matrix[-1].append(char)

    print(predictSeats(matrix, 4, 1))
    print(predictSeats(matrix, 5, INF))

def predictSeats(matrix, tolerance, lookDistance):
    lines = deepcopy(matrix)
    changes = 1
    seatsFilled = 0
    while changes:
        nextLines = deepcopy(lines)
        changes = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == EMPTY and adjSeatsFilled(i, j, lines, dist=lookDistance) == 0:
                    nextLines[i][j] = FILLED
                    seatsFilled += 1
                    changes += 1
                if lines[i][j] == FILLED and adjSeatsFilled(i, j, lines, dist=lookDistance) >= tolerance:
                    nextLines[i][j] = EMPTY
                    seatsFilled -= 1
                    changes += 1
        lines = deepcopy(nextLines)
    return seatsFilled

def adjSeatsFilled(i, j, matrix, dist=1):
    dirs = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_i = len(matrix)
    max_j = len(matrix[0])
    adjacentSeatsFilled = 0
    for direction in dirs:
        for d in range(1, dist+1):
            ii = i + d * direction[0]
            jj = j + d * direction[1]
            if 0 <= ii < max_i and 0 <= jj < max_j:
                if matrix[ii][jj] == EMPTY:
                    break
                elif matrix[ii][jj] == FILLED:
                    adjacentSeatsFilled += 1
                    break
            else:
                break
    return adjacentSeatsFilled

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
