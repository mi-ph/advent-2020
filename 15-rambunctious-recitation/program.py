def play(startingNumbers, dinnerTime):
    seen = {}
    t = 1
    startingNumbers = startingNumbers.copy()
    startingNumbers.reverse()
    while t <= dinnerTime:
        num = startingNumbers.pop() if startingNumbers else nextNum
        nextNum = 0 if num not in seen else t - seen[num]
        seen.update({num: t})
        t += 1
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
