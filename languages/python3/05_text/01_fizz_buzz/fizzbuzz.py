
for i in range(1, 100):
    if i % 15 == 0:
        line = 'FizzBuzz'
    elif i % 3 == 0:
        line = 'Fizz'
    elif i % 5 == 0:
        line = 'Buzz'
    else:
        line = i
    print(line)
