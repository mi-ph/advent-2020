def get_inst(line):
    i = line.split(' ')[0]
    v = int(line.split(' ')[1])
    return (i, v)

def run(instructions, showResultInError=True):
    acc = 0
    pc = 0
    visited = [0] * len(instructions)
    while True:
        if pc >= len(instructions):
            print(f"Program complete: accumulator {acc}")
            break
        if visited[pc] > 0:
            if showResultInError:
                print(f"Program error: accumulator {acc}")
            break
        i = instructions[pc][0]
        v = instructions[pc][1]

        visited[pc] = 1

        if i == "acc":
            acc += v
        if i == "jmp":
            pc += v
        else:
            pc += 1

with open("input.txt", "r") as fh:
    lines = fh.readlines()
    colours = {}
    instructions = []
    for line in lines:
        instructions.append(get_inst(line))

    run(instructions)

    for i in range(len(instructions)):
        k = instructions[i][0]
        v = instructions[i][1]

        original = (k, v)

        if k == "jmp":
            replace = ("nop", v)
        elif k == "nop":
            replace = ("jmp", v)
        else:
            continue

        instructions[i] = replace
        run(instructions, False)
        instructions[i] = original
