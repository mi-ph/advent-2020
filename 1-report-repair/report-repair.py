FILENAME = "input.txt"
TARGET = 2020
import random

def main():
    with open(FILENAME, 'r') as fh:
        array = [int(line) for line in fh.readlines()]
        array.sort()

    search = [0, 0, 0]
    maxI = len(array) - 1
    success = False
    count = 0
    while not success:
        count += 1
        values = [array[s] for s in search]
        total = sum(values)
        bestError = abs(total - TARGET)
        bestSearch = search
        bestValues = values
        print(f"{bestSearch}: {total - TARGET}")
        if total == TARGET:
            success = True
            break
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    stepSearch = [max(0,min(maxI,search[0] + i - 1)),
                                  max(0,min(maxI,search[1] + j - 1)),
                                  max(0,min(maxI,search[2] + k - 1))]
                    stepValues = [array[s] for s in stepSearch]
                    stepError = abs(TARGET - sum(stepValues))
                    if stepError < bestError:
                        bestError = stepError
                        bestSearch = stepSearch
                        bestValues = stepValues
        if sum(values) == sum(bestValues):
            print("re-search")
            bestSearch = [random.randint(0,maxI) for i in range(3)]
        search = bestSearch

    chosen_product = 1
    chosen_sum = 0
    for c in bestValues:
        chosen_product *= c
        chosen_sum += c
    print(f"Values: {bestValues}")
    print(f"Sum: {chosen_sum}")
    print(f"Product: {chosen_product}")

def main2():
    with open(FILENAME, 'r') as fh:
        array = [int(line) for line in fh.readlines()]
        array.sort()

    head = 0
    tail = len(array) - 1

    success = False

    while head < tail and not success:
        total = array[head] + array[tail]
        if total == TARGET:
            success = True
        elif total > TARGET:
            tail -= 1
        elif total < TARGET:
            head += 1

    if success:
        print(f"{array[head]} * {array[tail]} = {array[head] * array[tail]}")
    else:
        print("failed")


    print(array)

    search = [0, 1, 2]
    incrementIndex = 0
    success = False
    while not success:
        total = array[search[0]] + array[search[1]] + array[search[2]]
        if total == TARGET:
            success = True
        elif total > TARGET:
            search[incrementIndex] -= 1
            incrementIndex = (incrementIndex + 1) % 3
        elif total < TARGET:
            search[incrementIndex] += 1

    print(search)
    chosen = [array[s] for s in search]
    chosen_product = 1
    chosen_sum = 0
    for c in chosen:
        chosen_product *= c
        chosen_sum += c
    print(chosen)
    print(chosen_sum)
    print(chosen_product)

main()
