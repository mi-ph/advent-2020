def main(lines):
    programs = []
    for line in lines:
        line = line.strip().split(' ')
        if line[0] == "mask":
            programs.append((line[2], []))
        else:
            programs[-1][1].append((int(line[0][4:-1]),int(line[2])))

    memory = {}
    for program in programs:
        bitmask = program[0]
        for ins in program[1]:
            memory.update({ins[0]: mask(bitmask, ins[1])})

    theSum = 0
    for item in memory:
        theSum += memory[item]

    print(theSum)

def main2(lines):
    programs = []
    for line in lines:
        line = line.strip().split(' ')
        if line[0] == "mask":
            programs.append((line[2], []))
        else:
            programs[-1][1].append((int(line[0][4:-1]),int(line[2])))

    # puzzle 2
    memory = {}
    for program in programs:
        bitmask = program[0]
        for ins in program[1]:
            addresses = mask2(bitmask, ins[0])
            for address in addresses:
                memory.update({address: ins[1]})

    theSum = 0
    for item in memory:
        theSum += memory[item]

    print(theSum)

def mask2(bitmask, num):
    num_string = f"{num:036b}"
    output = [[]]
    for bit, binary in zip(bitmask, num_string):
        for i in range(len(output)):
            if bit == 'X':
                output.append(output[i].copy() + ['0'])
                output[i].append('1')
            elif bit == '0':
                output[i].append(binary)
            else:
                output[i].append('1')

    ints = []
    for o in output:
        output_int = 0
        place = 2 ** 35
        for bit in o:
            output_int += (int(bit) * place)
            place >>= 1
        ints.append(output_int)

    return ints

def mask(bitmask, num):
    num_string = f"{num:036b}"
    output = []
    for bit, binary in zip(bitmask, num_string):
        if bit == 'X':
            output.append(binary)
        else:
            output.append(bit)
    output_int = 0
    place = 1
    output.reverse()
    for bit in output:
        output_int += (int(bit) * place)
        place *= 2

    return output_int

def run(function, input_file):
    try:
        with open(input_file, "r") as fh:
            lines = fh.readlines()
    except:
        print(f"{input_file} not found in current directory. Skipping...")
        return

    function(lines)

print("TEST 1:")
run(main, "test.txt")
print("TEST 2:")
run(main2, "test2.txt")
print("\nMAIN:")
run(main, "input.txt")
run(main2, "input.txt")
