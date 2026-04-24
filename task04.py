input_file = open('Input/numbers.txt')

data = input_file.read().split()
numbers = [float(num) for num in data]
even_numbers = [num for num in numbers if num % 2 == 0]


output_file = open('Output/output04.txt', 'w')
output_file.write(str(even_numbers))