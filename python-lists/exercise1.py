# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

# sundry = ['John', 3.14, 7, False]
# print(sundry)
# print(type(sundry))

# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# # print(colors)
# # print(type(colors))

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')

# colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')

# print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
# print(colors[2:5])
# print(type(colors[2:5]))

# print('\nPrint a slice, starting at index 0 to index 3:')
# print(colors[:3])

# print('\nPrint a slice, starting a index 4 to the end of the list:')
# print(colors[4:])

# print('\nPrint a slice, from the 4th from the end (but not the last item):')
# print(colors[-4:-1])

# numbers = [1, 3, 5]

# print(5 in numbers)
# print(8 in numbers)

# print(5 not in numbers)
# print(8 not in numbers)

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()

# for number in numbers:
#     if number > 42:
#         break
#     print(number)

# import random
# numbers = []

# while len(numbers) < 6:
#     numbers.append(random.randint(1, 100))

# for number in numbers:
#     print(number)
#     if number >= 90:
#         print('Found at least one number greater than 90')
#         break
# else:
#     print('No numbers greater than 90')

# print('Complete')

values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
    if isinstance(value, str) == False:
        continue
    equipment.append(value)

print(equipment)
