print('Simple calculator!')
first_number = input('First number?  ')
if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation?  ')

second_number = input('Second number?  ')
if second_number.isnumeric() == False:
    print('Please input a number.')

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == '+':
    result = first_number + second_number
    label = 'Sum'

elif operation == '-':
    result = first_number - second_number
    label = 'Difference'

elif operation == '*':
    result = first_number * second_number
    label = 'Product'

elif operation == '/':
    result = first_number / second_number
    label = 'Quotient'

elif operation == '^':
    result = first_number ^ second_number
    label = 'Exponent'

elif operation == '%':
    result = first_number % second_number
    label = 'Modulus'

else:
    print('Operation not recognized.')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation +
      ' ' + str(second_number) + ' equals ' + str(result))
