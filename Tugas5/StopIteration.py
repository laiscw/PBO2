print('Lais Cakrawati\n210511002\nT121A(R1)\n')
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
        if number == 3:
            raise StopIteration
    except StopIteration:
        break