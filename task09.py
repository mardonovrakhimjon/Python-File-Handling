input_file = open('Input/numbers.txt')

data = input_file.read().split()
results = []
for num in data:
    clean_num = num.strip().replace('-', '')
    if clean_num.isdigit():
        count = len(clean_num)
        results.append(f"{num}: {count} xonali")
    else:
        results.append(f"{num}: son emas")

output_file = open('Output/output09.txt', 'w')
output_file.write('\n'.join(results))