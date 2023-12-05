""" import re

with open('entradas.txt', 'r') as entradas:
    lineas = entradas.read().splitlines()
numbers = {
    "one": 1, "1": 1,
    "two": 2, "2": 2,
    "three": 3, "3": 3,
    "four": 4, "4": 4,
    "five": 5, "5": 5,
    "six": 6, "6": 6,
    "seven": 7, "7": 7,
    "eight": 8, "8": 8,
    "nine": 9, "9": 9,
}

patron = '|'.join(numbers.keys()) + r'|\d+'

def getDigitLetter(lineas, patron):
    suma = 0
    for linea in lineas:
        numeros = []    
        ocurrencias = re.findall(patron, linea)
        print(f'Las ocurrencias son: {ocurrencias}')
        for ocurrencia in ocurrencias:
            numeros.append(numbers[ocurrencia])
        if numeros:
            number_in_line = str(numeros[0]) + str(numeros[-1])

            suma = getSum(int(number_in_line), suma)
    #print(f'La suma total es: {suma}')

def getSum(number_in_line, total):
    total += number_in_line
    print(f'Sumando {number_in_line} = {total}')
    return total

#getSum(lineas)
getDigitLetter(lineas, patron)
 """

with open('entradas.txt', 'r') as entradas:
    lineas = entradas.read().splitlines()

p1 = 0
p2 = 0
for line in lineas:
  p1_digits = []
  p2_digits = []
  for i,c in enumerate(line):
    if c.isdigit():
      p1_digits.append(c)
      p2_digits.append(c)
    for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[i:].startswith(val):
        p2_digits.append(str(d+1))
  p1 += int(p1_digits[0]+p1_digits[-1])
  p2 += int(p2_digits[0]+p2_digits[-1])
print(p1)
print(p2)