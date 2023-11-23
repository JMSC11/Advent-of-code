def subroutine(len_preview_characters, array):
    preview_characters = []

    preview_characters = [character for character in array[:len_preview_characters-1]]
    
    for index, character  in enumerate(array[len_preview_characters-1:], start=len_preview_characters-1):
        preview_characters.append(character)
        #print(f'Ultimos elementos: {preview_characters}')
        unique_elements = set(preview_characters)

        if len(unique_elements) == len_preview_characters:
            position = index +1
            return position
        
        preview_characters.pop(0)

def start_package(array):
    len_preview_characters = 4
    return subroutine(len_preview_characters, array)

def start_message(array):
    len_preview_characters = 14
    return subroutine(len_preview_characters, array)
    
with open('entradas.txt', 'r') as file:
    array = file.read().strip()

print(f'Start package in position: {start_package(array)}')
print(f'Start message in position: {start_message(array)}')