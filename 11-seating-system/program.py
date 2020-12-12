
def seatsFree(i, j, m):
    seatsEmpty = 0
    for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
            if not(ii == i and jj == j):
                if m[ii][jj] <= 1:
                    seatsEmpty += 1
    return seatsEmpty

def seatsFree2(i, j, m):
    seatsEmpty = 8
    width = len(m[0])
    height = len(m)
    # right
    ii = i+1
    jj = j
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += 1
    # left
    ii = i-1
    jj = j
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += -1
    # down
    ii = i
    jj = j+1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        jj += 1
    # up
    ii = i
    jj = j-1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        jj += -1
    # up-right
    ii = i+1
    jj = j+1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += 1
        jj += 1

    # up-left
    ii = i-1
    jj = j+1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += -1
        jj += 1
    # up-right
    ii = i+1
    jj = j-1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += 1
        jj += -1
    # up-right
    ii = i-1
    jj = j-1
    while 0 < ii < height and 0 < jj < width:
        if m[ii][jj] == 1:
            break
        if m[ii][jj] == 2:
            seatsEmpty -= 1
            break
        ii += -1
        jj += -1
    return seatsEmpty

def show(m):
    width = len(m[0])
    height = len(m)
    for i in range(1, height-1):
        print(m[i][1:width-1])

def main(lines):
    m = []
    for line in lines:
        m.append([0])
        for char in line:
            if char == 'L':
                m[-1].append(1)
            if char == '.':
                m[-1].append(0)
        m[-1].append(0)
    width = len(m[0])
    height = len(m)
    m2 = [[0] * width] + m + [[0] * width]
    width = len(m2[0])
    height = len(m2)
    count = 0
    while True:
        nextM = copy(m2)
        changes = 0
        for i in range(1, height-1):
            for j in range(1, width-1):
                if m2[i][j] == 1:
                    if seatsFree(i, j, m2) == 8:
                        nextM[i][j] = 2
                        changes += 1
                elif m2[i][j] == 2:
                    if seatsFree(i, j, m2) < 5:
                        nextM[i][j] = 1
                        changes += 1
        m2 = copy(nextM)
        if changes == 0:
            break
    #show(m2)
    count = 0
    for line in m2:
        for seat in line:
            if seat == 2:
                count += 1
    print(count)

def copy(m):
    n = []
    for mm in m:
        n.append([])
        for i in mm:
            n[-1].append(i)
    return n

def main2(lines):
    m = []
    for line in lines:
        m.append([0])
        for char in line:
            if char == 'L':
                m[-1].append(1)
            if char == '.':
                m[-1].append(0)
        m[-1].append(0)
    width = len(m[0])
    height = len(m)
    m2 = [[0] * width] + m + [[0] * width]
    width = len(m2[0])
    height = len(m2)
    count = 0
    while True:
        nextM = copy(m2)
        changes = 0
        count += 1
        for i in range(1, height-1):
            for j in range(1, width-1):
                if m2[i][j] == 1:
                    if seatsFree2(i, j, m2) == 8:
                        nextM[i][j] = 2
                        changes += 1
                elif m2[i][j] == 2:
                    if seatsFree2(i, j, m2) < 4:
                        nextM[i][j] = 1
                        changes += 1
        m2 = copy(nextM)
        if changes == 0 or count == -1:
            break
    #show(m2)
    count = 0
    for line in m2:
        for seat in line:
            if seat == 2:
                count += 1
    print(count)

def run(function, input_file):
    with open(input_file, "r") as fh:
        function(fh.readlines())

print("TEST:")
run(main, "test.txt")
run(main2, "test.txt")
print("\nMAIN:")
run(main, "input.txt")
run(main2, "input.txt")
