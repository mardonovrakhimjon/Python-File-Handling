input_file = open('Input/students.txt')

data = input_file.read().split()
names = filter(
    lambda name: name.startswith("A"), data
)
n = list(names)
output_file = open('Output/output17.txt', 'w')
output_file.write(str(n))