def main():
    with open("entradas.txt", "r") as file:
        rucksacks = file.read().splitlines()
    total = 0
    #first_part(rucksacks, total)
    total_second_part = second_part(rucksacks, total)

def first_part(rucksacks, total):
    for item in rucksacks:
        part1, part2 = get_compartments(item)
        type_duplicated = list(find_duplicated(part1, part2))
        type = type_duplicated[0]
        priority = get_priority(type)
        total += priority
    print(f"El total de todos los items es: {total}")

def second_part(rucksacks, total):
    group = []
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        badge =  find_badge_in_group(group)
        total += get_priority(badge[0])
    print(f"El total de la segunda parte es: {total}")

def get_priority(type):
    type = str(type) 
    if 'a' <= type <= 'z':
        return ord(type) - ord('a') + 1
    elif 'A' <= type <= 'Z':
        return ord(type) - ord('A') + 27

def get_compartments(rucksack):
    middle = int(len(rucksack) / 2)  
    part1 = rucksack[:middle]
    part2 = rucksack[middle:]
    return part1, part2

def find_duplicated(part1, part2):
    first_compartment = set(part1)
    second_compartment = set(part2)
    type_duplicated = first_compartment.intersection(second_compartment)
    return type_duplicated

def find_badge_in_group(group):
    elve1 = set(group[0])
    elve2 = set(group[1])
    elve3 = set(group[2])
    badge = list(elve1.intersection(elve2.intersection(elve3)))
    return badge

main()