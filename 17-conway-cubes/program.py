def neighbours(square):
    neighbours = []
    i, j, k, l = square
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                for w in range(l - 1, l + 2):
                    if (i, j, k, l) != (x, y, z, w):
                        neighbours.append((x, y, z, w))
    return neighbours

def numNeighbours(square, active):
    n = 0
    for neighbour in neighbours(square):
        if neighbour in active:
            n += 1
    return n

def main(lines):
    activeSquares = set()
    z = 0
    w = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                activeSquares.add((i, j, z, w))

    for _ in range(6):
        nextActiveSquares = set()
        for square in activeSquares:
            n = numNeighbours(square, activeSquares)
            if n == 2 or n == 3:
                nextActiveSquares.add(square)
            for neighbour in neighbours(square):
                n = numNeighbours(neighbour, activeSquares)
                if n == 3:
                    nextActiveSquares.add(neighbour)
        activeSquares = nextActiveSquares.copy()

    print(len(activeSquares))

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
