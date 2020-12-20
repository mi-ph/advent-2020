def main(lines):
    rules, messages = parse(lines)
    puzzle(rules, messages)
    rules.update({8: [[42], [42, 8]]})
    rules.update({11: [[42, 31], [42, 11, 31]]})
    puzzle(rules, messages)

def puzzle(rules, messages):
    nValid = 0
    for message in messages:
        output = solveRule(message, rules, {0}, 0)
        if len(message) in output:
            nValid += 1
    print(nValid)

def solveRule(message, rules, indices, rule):
    # print(f"{rule}:{rules[rule]} with {indices}")
    if not indices:
        return set()
    passingIndices = set()
    for branch in rules[rule]:
        inputIndices = indices.copy()
        outputIndices = inputIndices
        for nextRule in branch:
            inputIndices = outputIndices
            outputIndices = set()
            if not inputIndices:
                break
            if isinstance(nextRule, str):
                for index in inputIndices:
                    if index < len(message) and message[index] == nextRule:
                        outputIndices.add(index + 1)
            else:
                outputIndices = solveRule(message, rules, inputIndices, nextRule)
        passingIndices |= outputIndices
    return passingIndices

def parse(lines):
    sections = lines.split('\n\n')
    rules_block = sections[0].split('\n')
    messages = sections[1].split('\n')[:-1]
    rules = {}
    for rule_line in rules_block:
        parts = rule_line.split(': ')
        rule = int(parts[0])
        subrules = [list(int(n) if n.isnumeric() else n.strip('"') for n in i.split(' ')) for i in parts[1].split(' | ')]
        rules.update({rule: subrules})
    return rules, messages

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
print("\nTEST2:")
run(main, "test2.txt")
print("\nMAIN:")
run(main, "input.txt")
