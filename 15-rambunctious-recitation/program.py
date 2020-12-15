def main(lines):
    nums = [int(num) for num in lines[0].split(',')]

    seen = {}
    t = 1
    for num in nums:
        new = num not in seen
        seen.update({num: t})
        t += 1

    while t <= 30000000:
        if new:
            num = 0
        else:
            num = t - lastSeen - 1
        new = num not in seen
        nums.append(num)
        if num in seen:
            lastSeen = seen[num]
        seen.update({num: t})
        t += 1

    print(nums[-1])

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
