info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))
r = tuple(sorted(info, key=lambda tup: tup[1]))
print(r)
m = tuple(sorted(info, key=lambda tup: tup[1], reverse=True))
print(m)


stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
s = stocks[0][1][0]
print(s)    # -> PLW
