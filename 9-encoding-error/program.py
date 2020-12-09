def last25(array, i):
    return array[i-25:i]

def find(num, array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == num:
                return False
    return True

with open("input.txt", "r") as fh:
    lines = fh.readlines()
    array = []
    for line in lines:
        array.append(int(line))

    error = 0
    for trial in range(25,len(array)):
        if find(array[trial], last25(array, trial)):
            error = array[trial]
            print(f"Puzzle 1: {error}")

    begin = 0
    end = 0
    while True:
        theSlice = array[begin:end+1]
        theSum = sum(theSlice)
        if theSum == error:
            print(f"Puzzle 2: {min(theSlice) + max(theSlice)}")
            break
        if theSum > error:
            begin += 1
        if theSum < error:
            end += 1
