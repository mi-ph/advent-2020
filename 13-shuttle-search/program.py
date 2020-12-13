def main(lines):
    timestamp = int(lines[0].strip())
    bus_ids = lines[1].strip().split(',')
    timetable = []
    for t, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            timetable.append((t, int(bus_id)))

    min_wait_time = 2147000000
    for _, bus in timetable:
        wait_time = -timestamp % bus
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_wait_bus = bus
    print(f"{min_wait_bus} is leaving next! Wait time {min_wait_time} mins.")
    print(f"Puzzle 1: {min_wait_bus * min_wait_time}\n")

    t = 0
    jump_distance = 1
    consec = 0
    searching = False
    while True:
        times = [abs((t + i) % b) for (i, b) in timetable]
        # print(f"{t}: {times}")
        if times[consec] == 0 and not searching:
            searching = True
            start = t
            print(f"Found {consec} at {t}")
        elif times[consec] == 0 and searching:
            searching = False
            jump_distance = t - start
            print(f"Found {consec} at {t}, jumping by {jump_distance}")
            consec += 1
        if (sum(times) == 0):
            break
        else:
            t += jump_distance
    print(f"\nPuzzle 2: {t}")

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
