def reverse_number(number):
    return [int(x) for x in str(number)[::-1]]


def return_number(reverse_number):
    for y in reverse_number:
        number = ''.join([str(y)])
    return number

reverse_number1 = reverse_number(154875987)
print(reverse_number1)
return_number1 = return_number(reverse_number1)
print(return_number1)

