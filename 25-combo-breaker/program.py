def main(lines):
    cpk = int(lines[0].strip())
    dpk = int(lines[1].strip())
    cls = 0
    v = 1
    s = 7
    while v != cpk:
        cls += 1
        v = (v * s) % 20201227
    print(transform(dpk, cls))

def transform(s, ls):
    v = 1
    for _ in range(ls):
        v = (v * s) % 20201227
    return v

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
