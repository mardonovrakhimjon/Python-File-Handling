input_file = open('Input/students.txt')

data = input_file.read().lower()

nums = data.split()
s = sorted(nums)

output_file = open('Output/output13.txt', 'w')
output_file.write(str(s))