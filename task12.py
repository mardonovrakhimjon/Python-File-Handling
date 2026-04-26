input_file = open('Input/students.txt')

data = input_file.read()

nums = data.split()
s = ""
for num in nums:
    s += str(num) + " "

output_file = open('Output/output12.txt', 'w')
output_file.write(str(s))