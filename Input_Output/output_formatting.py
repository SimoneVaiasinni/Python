import math

day = 1
year = 2020
mounth = "April"

a = f'Today is {day} {mounth} {year}'
a = "Today is {} {} {}".format(day,mounth, year)
a = "Today is {0} {1} {2}".format(day,mounth, year)

b = 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
c = f'The value of pi is approximately {math.pi:.3f}.'

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

t = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)
t = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))