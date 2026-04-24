input_file = open('Input/numbers.txt')

data = input_file.read().split()
numbers = [float(num) for num in data]

num = max(numbers)

output_file = open('Output/output03.txt', 'w')
output_file.write(str(num))