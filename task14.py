input_file = open('Input/students.txt')

data = input_file.read()
a = data[::-1]

output_file = open('Output/output14.txt', 'w')
output_file.write(str(a))