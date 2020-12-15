def play(startingNumbers, dinnerTime):
    seen = {}
    for t in range(1, dinnerTime + 1):
        num = startingNumbers[t-1] if t <= len(startingNumbers) else nextNum
        nextNum = 0 if num not in seen else t - seen[num]
        seen.update({num: t})
    return num

def main(lines):
    nums = [int(num) for num in lines[0].split(',')]
    print(play(nums, 2020))
    print(play(nums, 30000000))

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
