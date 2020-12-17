def main(lines):
    lines = lines.split('\n\n')
    ruleLines = lines[0].split('\n')
    ticketLine = lines[1].split('\n')[1]
    otherTickets = lines[2].split('\n')[1:-1]

    rules = []
    nums = []
    anyValid = set()
    for line in ruleLines:
        sect = line.strip().split(': ')
        category = sect[0]
        ranges = sect[1].split(' or ')
        valid = set()
        for r in ranges:
            low = int(r.split('-')[0])
            high = int(r.split('-')[1])
            for num in range(low, high+1):
                valid.add(num)
                anyValid.add(num)
        rules.append((category, valid))

    errorRate = 0
    validTickets = []
    for ticket in otherTickets:
        isValid = True
        nums = ticket.split(',')
        ticketInt = []
        for num in nums:
            ticketInt.append(int(num))
            if int(num) not in anyValid:
                errorRate += int(num)
                isValid = False
        if isValid:
            validTickets.append(ticketInt)
    print(errorRate)

    numFields = len(rules)
    possibilities = []
    for i in range(numFields):
        possibilities.append([])
        for j in range(numFields):
            possibilities[-1].append(j)

    for place in range(numFields):
        for field in range(numFields):
            for ticket in validTickets:
                if ticket[place] not in rules[field][1]:
                    possibilities[place].remove(field)
                    break

    fields = []
    i = 0
    while i < numFields:
        if len(possibilities[i]) == 1:
            field = possibilities[i][0]
            fields.append((field, i))
            for place in range(numFields):
                if field in possibilities[place]:
                    possibilities[place].remove(field)
            i = -1
        i += 1

    yourTicket = [int(a) for a in ticketLine.split(',')]
    product = 1
    for field, position in fields:
        if rules[field][0].startswith("departure"):
            product *= yourTicket[position]
    print(product)

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
print("\nMAIN:")
run(main, "input.txt")
