def getAdaptersInRange(ad, mx, mn):
    c = []
    for a in ad:
        if mn <= a <= mx:
            c.append(a)
    return c

def countChains(adapters, chain):
    nChains = 0
    nextAdapter = getAdaptersInRange(adapters, chain[-1] + 3, chain[-1] + 1)
    if len(nextAdapter) == 0:
        return 1
    for adapter in nextAdapter:
        nextChain = chain + [adapter]
        nChains += countChains(adapters, nextChain)
    return nChains

def main(lines):
    adapters = []
    for line in lines:
        adapters.append(int(line.strip()))
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    # puzzle 1: distribution of diffs in maximal chain
    chain = [adapters[0]]
    diffs = {}
    while chain[-1] != adapters[-1]:
        nextAdapter = min(getAdaptersInRange(adapters, chain[-1] + 3, chain[-1] + 1))
        diff = nextAdapter - chain[-1]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs.update({diff: 1})
        chain.append(nextAdapter)
    print(f"Puzzle 1: {diffs[1] * diffs[3]}")

    # puzzle 2: number of combinations of functional chains
    adapterLists = [[adapters[0]]]
    prev = adapters[0]

    for adapter in adapters[1:]:
        diff = adapter - prev
        prev = adapter
        if diff == 3:
            adapterLists.append([adapter])
        else:
            adapterLists[-1].append(adapter)

    totalChains = 1
    for adapterList in adapterLists:
        newChains = countChains(adapterList[1:], [adapterList[0]])
        totalChains *= newChains
    print(f"Puzzle 2: {totalChains}")

def run(function, input_file):
    try:
        with open(input_file, "r") as fh:
            function(fh.readlines())
    except:
        print(f"Couldn't read {input_file}. Please ensure it is in the directory and try again.")

print("TEST:")
run(main, "test.txt")
print("\nMAIN:")
run(main, "input.txt")
