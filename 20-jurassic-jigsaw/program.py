def main(lines):
    tiles = parse(lines)

    grid = [(0, 0, tiles.pop())] # Start the grid at row 0, col 0

    for position in grid:
        for tile in tiles:
            for orientation in allOrientations(tile[1]):
                if L(orientation) == R(position[2][1]):
                    grid.append((position[0],position[1]+1,(tile[0], orientation)))
                    tiles.remove(tile)
                    break
                if R(orientation) == L(position[2][1]):
                    grid.append((position[0],position[1]-1,(tile[0], orientation)))
                    tiles.remove(tile)
                    break
                if U(orientation) == D(position[2][1]):
                    grid.append((position[0]+1,position[1],(tile[0], orientation)))
                    tiles.remove(tile)
                    break
                if D(orientation) == U(position[2][1]):
                    grid.append((position[0]-1,position[1],(tile[0], orientation)))
                    tiles.remove(tile)
                    break
    top = 0
    bottom = 0
    left = 0
    right = 0
    for place in grid:
        if place[0] > bottom:
            bottom = place[0]
        if place[0] < top:
            top = place[0]
        if place[1] > right:
            right = place[1]
        if place[1] < left:
            left = place[1]

    prod = 1
    for place in grid:
        if place[0] in [bottom, top] and place[1] in [left, right]:
            prod *= place[2][0]
    print(prod)

    imageWidth = (right - left + 1) * (len(grid[0][2][1]) - 2)
    imageHeight = imageWidth  # Assume square
    image = []
    for i in range(imageWidth):
        image.append([])
        for j in range(imageHeight):
            image[-1].append(0)

    for place in grid:
        for i in range(1, 9):
            for j in range(1, 9):
                x = (place[1] - left) * 8 + (j - 1)
                y = (place[0] - top) * 8 + (i - 1)
                image[y][x] = place[2][1][i][j]
    # show(image)

    seaMonsterText = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    seaMonsterText = seaMonsterText.split('\n')
    monsterHeight = len(seaMonsterText)
    monsterWidth = len(seaMonsterText[0])

    seaMonster = []
    for i in range(monsterHeight):
        seaMonster.append([])
        for j in range(monsterWidth):
            if seaMonsterText[i][j] == '#':
                seaMonster[-1].append(1)
            else:
                seaMonster[-1].append(0)
    seaMonster_weight = arraySum(seaMonster)

    for orientation in allOrientations(image):
        seaMonstersMatched = 0
        for i in range(0, imageHeight-monsterHeight+1):
            for j in range(0, imageWidth-monsterWidth+1):
                pixelsMatched = 0
                for y in range(monsterHeight):
                    for x in range(monsterWidth):
                        if seaMonster[y][x] == orientation[i+y][j+x] and seaMonster[y][x] == 1:
                            pixelsMatched += 1
                if pixelsMatched == seaMonster_weight:
                    seaMonstersMatched += 1
        if seaMonstersMatched:
            break
    print(arraySum(image) - seaMonstersMatched * seaMonster_weight)

def arraySum(t):
    s = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            s += t[i][j]
    return s

def D(t):
    return tuple((t[-1]))

def U(t):
    return tuple((t[0]))

def L(t):
    return D(rotate(t))

def R(t):
    return U(rotate(t))

def allOrientations(t):
    yield t
    t = rotate(t)
    yield t
    t = rotate(t)
    yield t
    t = rotate(t)
    yield t
    t = rotate(t)
    t = flip(t)
    yield t
    t = rotate(t)
    yield t
    t = rotate(t)
    yield t
    t = rotate(t)
    yield t

def rotate(t):
    r = []
    for i in range(len(t)-1, -1, -1):
        r.append([])
        for j in range(len(t[i])):
            r[-1].append(t[j][i])
    return r

def flip(t):
    r = []
    for i in range(len(t)):
        r.append([])
        for j in range(len(t[i])):
            r[-1].append(t[j][i])
    return r

def show(t):
    for i in range(len(t)):
        print("".join([str(a) for a in t[i]]))

def parse(lines):
    database = []
    tiles = lines.split('\n\n')
    for tile in tiles:
        tile_lines = tile.split('\n')
        tile_id = int(tile_lines[0][5:-1])
        tile_data = [line for line in tile_lines[1:] if len(line)]
        l = len(tile_data)
        t = []
        for i in range(l):
            t.append([])
            for j in range(l):
                d = tile_data[i][j]
                if d == '#':
                    t[-1].append(1)
                else:
                    t[-1].append(0)
        database.append((tile_id, t))
    return database

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
