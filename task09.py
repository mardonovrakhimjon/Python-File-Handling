input_file = open('Input/numbers.txt')

data = input_file.read().split()
for line in data:
    numbers = line.split()
    for num in numbers:
        digits = len(num.replace('-', ''))
        output_file = open('Output/output09.txt', 'w')
        output_file.write(f"{num}: {digits} xonali\n")

# output_file.write(str(even_numbers))