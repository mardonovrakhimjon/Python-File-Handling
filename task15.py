input_file = open('Input/students.txt')

data = input_file.read()


output_file = open('Output/output15.txt', 'w')
output_file.write(str(data))