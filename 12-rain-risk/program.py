def main(lines):
    pos_x = 0
    pos_y = 0

    face = 90

    ins = []
    for line in lines:
        line = line.strip()
        ins.append((line[0], int(line[1:])))

    for i, v in ins:
        if i == 'F':
            if face == 90:
                i = 'E'
            if face == 180:
                i = 'S'
            if face == 270:
                i = 'W'
            if face == 0:
                i = 'N'
        if i == 'N':
            pos_y += v
        if i == 'E':
            pos_x += v
        if i == 'W':
            pos_x -= v
        if i == 'S':
            pos_y -= v
        if i == 'L':
            face = (face - v) % 360
        if i == 'R':
            face = (face + v) % 360

    print(f"Puzzle 1: {abs(pos_x) + abs(pos_y)}")

    pos_x = 0
    pos_y = 0
    way_x = 10
    way_y = 1

    for i, v in ins:
        if i == 'F':
            pos_x += (way_x * v)
            pos_y += (way_y * v)
        if i == 'N':
            way_y += v
        if i == 'E':
            way_x += v
        if i == 'W':
            way_x -= v
        if i == 'S':
            way_y -= v
        if i == 'L':
            i = 'R'
            v = -v
        if i == 'R':
            v = v % 360
            if v == 90:
                way_x, way_y = way_y, -way_x
            if v == 180:
                way_x, way_y = -way_x, -way_y
            if v == 270:
                way_x, way_y = -way_y, way_x

    print(f"Puzzle 2: {abs(pos_x) + abs(pos_y)}")

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
