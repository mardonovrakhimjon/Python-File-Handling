input_file = open('Input/numbers.txt')

data = input_file.read().split()
numbers = [float(num) for num in data]
even_numbers = [x ** 2 for x in numbers]


output_file = open('Output/output07.txt', 'w')
output_file.write(str(even_numbers))