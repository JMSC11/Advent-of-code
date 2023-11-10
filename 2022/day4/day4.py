def main():
    count = 0
    with open("entradas.txt", 'r') as file:
        for line in file:
            sections = []
            parts = line.strip().split(',')
            for part in parts:
                begin, end = part.split('-')
                sections.extend([int(begin), int(end)])
            
            range1, range2 = get_ranges(sections)
            #count += find_sub_set(range1, range2)
            count += find_overlap(range1, range2)
    print(f"Hay:  {count} empalmes")

def get_ranges(sections):
    range_elve1 = [i for i in range(sections[0], sections[1] + 1)]
    range_elve2 = [i for i in range(sections[2], sections[3] + 1)]
    return set(range_elve1), set(range_elve2) 

def find_sub_set(range1, range2):
    if range1.issubset(range2) or range2.issubset(range1):
        return 1 
    else:
        return 0
def find_overlap(range1, range2):
    if range1.intersection(range2):
        return 1
    else:
        return 0
        
main()
