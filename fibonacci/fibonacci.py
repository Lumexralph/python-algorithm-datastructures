"""Using generator to produce the value of the
next fibonacci value by computing the value when
required"""

def fibonacci_series():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

# create an iterator from the generator
print('The Sequence begins..')
for value in fibonacci_series():
    print(value)
    if value > 100:
        break