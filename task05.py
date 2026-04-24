input_file = open('Input/numbers.txt')

data = input_file.read().split()
numbers = [float(num) for num in data]
average = sum(numbers) / len(numbers)

output_file = open('Output/output05.txt', 'w')
output_file.write(str(average))