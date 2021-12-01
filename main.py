with open('input.txt') as input_file:
    input = [int(reading.strip()) for reading in input_file.readlines()]
    print(input)

running_total = 0
compare_value = input[0] + input[1] + input[2]

for index in range(1, len(input) - 2):
    current_reading = input[index] + input[index + 1] + input[index + 2]
    if current_reading > compare_value:
        running_total += 1
    print(f'{compare_value} - {current_reading}')
    compare_value = current_reading

print(running_total)