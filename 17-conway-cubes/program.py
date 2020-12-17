def neighbours(square):
    neighbours = [tuple()]
    dims = len(square)
    for dim in range(dims):
        for neighbour in neighbours.copy():
            neighbours.remove(neighbour)
            for i in range(square[dim]-1, square[dim]+2):
                neighbours.append(neighbour + (i,))
    neighbours.remove(square)
    return neighbours

def numNeighbours(square, active):
    n = 0
    for neighbour in neighbours(square):
        if neighbour in active:
            n += 1
    return n

def conway(activeSquares, iterations):
    for _ in range(iterations):
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
    return len(activeSquares)

def main(lines):
    activeSquares3D = set()
    activeSquares4D = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                activeSquares3D.add((i, j, 0))
                activeSquares4D.add((i, j, 0, 0))
    print(conway(activeSquares3D, 6))
    print(conway(activeSquares4D, 6))

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
