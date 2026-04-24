input_file = open('Input/numbers.txt')

data = input_file.read()

output_file = open('Output/output01.txt', 'w')
output_file.write(data)