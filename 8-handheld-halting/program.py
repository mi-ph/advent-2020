def get_inst(line):
    k = line.split(' ')[0]
    v = int(line.split(' ')[1])
    return (k, v)

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

        (k, v) = instructions[pc]
        visited[pc] = 1

        if k == "acc":
            acc += v
        if k == "jmp":
            pc += v
        else:
            pc += 1

with open("input.txt", "r") as fh:
    lines = fh.readlines()
    instructions = []
    for line in lines:
        instructions.append(get_inst(line))

    run(instructions)

    for i in range(len(instructions)):
        (k, v) = instructions[i]

        if k == "jmp":
            k_fix = "nop"
        elif k == "nop":
            k_fix = "jmp"
        else:
            continue

        instructions[i] = (k_fix, v)
        run(instructions, False)
        instructions[i] = (k, v)
