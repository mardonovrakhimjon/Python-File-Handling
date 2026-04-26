input_file = open('Input/students.txt')

data = input_file.read()
even_names = [name for name in data.split() if len(name) > 5]

output_file = open('Output/output16.txt', 'w')
output_file.write(str(even_names))