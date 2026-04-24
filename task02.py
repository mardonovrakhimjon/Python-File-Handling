input_file = open('Input/numbers.txt')

data = input_file.read()

nums = data.split()
s = 0
for num in nums:
    s += int(num)

output_file = open('Output/output02.txt', 'w')
output_file.write(str(s))