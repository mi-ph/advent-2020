def main(lines):
    directions = []
    for line in lines:
        directions.append([])
        line = line.strip()
        i = 0
        while i < len(line):
            if line[i] == 'e':
                directions[-1].append((2, 0))
            elif line[i] == 'w':
                directions[-1].append((-2, 0))
            elif line[i] == 'n':
                i += 1
                if line[i] == 'e':
                    directions[-1].append((1, 1))
                elif line[i] == 'w':
                    directions[-1].append((-1, 1))
            elif line[i] == 's':
                i += 1
                if line[i] == 'e':
                    directions[-1].append((1, -1))
                elif line[i] == 'w':
                    directions[-1].append((-1, -1))
            i += 1
    flipped_tiles = set()
    for direction_list in directions:
        pos = (0, 0)
        for direction in direction_list:
            pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos in flipped_tiles:
            flipped_tiles.remove(pos)
        else:
            flipped_tiles.add(pos)
    print(len(flipped_tiles))

    day = 1
    while day <= 100:
        new_tiles = flipped_tiles.copy()
        seen = set()
        for tile in flipped_tiles:
            if numAdjacent(tile, flipped_tiles) not in [1, 2]:
                new_tiles.remove(tile)
            for neighbour in neighbours(tile):
                if neighbour not in seen and neighbour not in flipped_tiles:
                    seen.add(neighbour)
                    if numAdjacent(neighbour, flipped_tiles) == 2:
                        new_tiles.add(neighbour)
        flipped_tiles = new_tiles
        day += 1
    print(len(flipped_tiles))

def numAdjacent(tile, tiles):
    n = 0
    for t in neighbours(tile):
        if t in tiles:
            n += 1
    return n

def neighbours(tile):
    i, j = tile
    yield (i + 1, j + 1)
    yield (i + 1, j - 1)
    yield (i - 1, j + 1)
    yield (i - 1, j - 1)
    yield (i + 2, j)
    yield (i - 2, j)


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
