tel = {'jack': 4098, 'sape': 4139}
tel = dict([("jack", 4098), ("sape", 4139)])
tel = dict(sape=4139, guido=4127, jack=4098)

tel['guido'] = 4127
del tel['sape']

#print({x: x**2 for x in (2, 4, 6)})
#print(list(tel))
#print(sorted(tel))