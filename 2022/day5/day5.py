def read_lines(file_path):
    lines = []

    with open(file_path) as f:
        lines = f.readlines()

    return lines

def extract_movements_and_stacks(lines):
    movements = []
    movements_start = False
    stacks = []

    for crates in lines:
        if not crates.replace(" ", "").strip():
            movements_start = True
            continue
        if not movements_start:
            stacks.append(crates)
        else:
            movements.append(crates)

    return movements, stacks

def format_columns(stacks):
    columns = [[line[x] for line in stacks] for x in range(len(stacks[0]))]
    formatted_columns = []

    for i in columns:
        if i and i[-1].strip():
            i = [x for x in i if x.strip()]
            i.reverse()
            i.pop(0)
            formatted_columns.append(i)

    return formatted_columns

def perform_movements(formatted_columns, movements, is_part_two=False):
    for move in movements:
        move_nums = [int(i) for i in move.split() if i.isdigit()]
        num_to_move = move_nums[0]
        num_move_from = move_nums[1]
        num_move_to = move_nums[2]

        if is_part_two and num_to_move > 1 and num_move_to <= len(formatted_columns):
            move_multi_columns = formatted_columns[num_move_from - 1][-num_to_move:]
            formatted_columns[num_move_from - 1] = formatted_columns[num_move_from - 1][:-num_to_move]
            formatted_columns[num_move_to - 1] += move_multi_columns
        elif 1 <= num_move_to <= len(formatted_columns) and formatted_columns[num_move_from - 1]:
            formatted_columns[num_move_to - 1].append(formatted_columns[num_move_from - 1].pop())

    return formatted_columns

def get_final_result(formatted_columns):
    result = "".join([x[-1] if x else '' for x in formatted_columns])
    return result

def process_part_one(file_path):
    lines = read_lines(file_path)
    movements, stacks = extract_movements_and_stacks(lines)
    columns = [[line[x] for line in stacks] for x in range(len(stacks[0]))]
    formatted_columns = []

    for i in columns:
        if i and i[-1].strip():
            i = [x for x in i if x.strip()]
            i.reverse()
            i.pop(0)
            formatted_columns.append(i)

    for move in movements:
        move_nums = [int(i) for i in move.split() if i.isdigit()]
        num_to_move = move_nums[0]
        num_move_from = move_nums[1]
        num_move_to = move_nums[2]

        for _ in range(num_to_move):
            formatted_columns[num_move_to - 1].append(formatted_columns[num_move_from - 1].pop())

    result = "".join([x[-1] if x else '' for x in formatted_columns])
    return result


def process_part_two(file_path):
    lines = read_lines(file_path)
    movements, stacks = extract_movements_and_stacks(lines)
    formatted_columns = format_columns(stacks)
    formatted_columns = perform_movements(formatted_columns, movements, is_part_two=True)
    result = get_final_result(formatted_columns)
    return result


file_path = "entradas.txt"


print("Parte Uno Resultado:", process_part_one(file_path))

#print("Parte Dos Resultado:", process_part_two(file_path))
