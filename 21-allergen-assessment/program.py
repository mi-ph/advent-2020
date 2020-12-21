def main(lines):
    ingredients = set()
    allergens = set()
    foods = []
    for food in lines:
        i = food.split(' (contains ')[0].split(' ')
        a = food.split(' (contains ')[1][:-2].split(', ')
        foods.append((set(i), set(a)))
        allergens |= set(a)
        ingredients |= set(i)

    possible = {}
    for allergen in allergens:
        possible_ingredients = ingredients.copy()
        for food in foods:
            if allergen in food[1]:
                possible_ingredients &= food[0]
        possible.update({allergen: possible_ingredients})

    decoded = []
    changes = True
    removed = set()
    while changes:
        changes = False
        for allergen in possible:
            possible[allergen] -= removed
            if len(possible[allergen]) == 1:
                ingredient = possible[allergen].copy()
                decoded.append((allergen, ingredient))
                changes = True
                removed |= ingredient

    allergyFree = ingredients.copy()
    for allergen, ingredient in decoded:
        allergyFree -= ingredient

    count = 0
    for food in foods:
        count += len(food[0] & allergyFree)
    print(count)

    decoded = [(allergen, ingredient.pop()) for allergen, ingredient in decoded]
    decoded.sort()
    print(",".join([ingredient for _, ingredient in decoded]))

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
