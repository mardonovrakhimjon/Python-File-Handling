input_file = open('Input/students.txt')

data = input_file.read().split()
name = input(">>> ")
for line in data:
    if name in data:
            result = "FOUND"
    else:
        result = "NOT FOUND"

output_file = open('Output/output18.txt', 'w')
output_file.write(str(name))