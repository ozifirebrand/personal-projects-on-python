import random

frequency_h = 0
frequency_t = 0

for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T', end=' ')

for i in range(20):
    if random.randrange(2) == 0:
        frequency_h += 1
    else:
        frequency_t += 1
print()
print(frequency_t, frequency_h)