names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalpha():
        print(f'Hello {name}!')

print(30*'-')

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for code, x in gaming.items():
    if x > 100:
        print(code)

print(30*'-')

indexes = [
    "WIG",
    "WIG-banki",
    "WIG-budownictwo",
    "WIG-CEE",
    "WIG-chemia",
    "WIG-energia",
    "WIG-ESG",
    "WIG-górnictwo",
    "WIG-informatyka",
    "WIG-leki",
    "WIG-media",
    "WIG-motoryzacja",
    "WIG-nieruchomości",
    "WIG-odzież",
    "WIG-paliwa",
    "WIG-Poland",
    "WIG-spożywczy",
    "WIG-telekomunikacja",
    "WIG-Ukraine",
    "WIG.GAMES",
    "WIG.MS-BAS",
    "WIG.MS-FIN",
    "WIG.MS-PET",
    "WIG20",
    "WIG20dvp",
    "WIG20lev",
    "WIG20short",
    "WIG20TR",
    "WIG30",
    "WIG30TR",
    "WIGdiv",
    "WIGtech",
]
for ind in indexes:
    if '20' in ind or '30' in ind:
        print(ind)

print(30*'-')

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)

print(30*'-')

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
d = {}
for i in items:
    if i == 'x':
        d[i] = items.count('x')
    elif i == 'y':
        d[i] = items.count('y')
    else:
        d[i] = items.count('z')
print(d)

print(30*'-')

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
new_p = []
for p in probabilities:
    if p >= 0.5:
        new_p.append(1)
    else:
        new_p.append(0)
print(new_p)

print(30*'-')

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
new_p = []
for p in probabilities:
    if p > 0.5:
        new_p.append(p)
print(new_p)

print(30*'-')

text = 'Python jest bardzo popularnym językiem programowania'
words = text.split(' ')
x = []
for idx, word in enumerate(words):
    if idx < 4:
        x.append(word.lower())
print(x)

print(30*'-')

items = [1, 5, 3, 2, 2, 4, 2, 4]
x = []
for i in items:
    if not i in x:
        x.append(i)
print(x)

print(30*'-')

x_list = []
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
for i in items:
    if i % 2 != 1:
        x_list.append(i)
print(x_list)

print(30*'-')

x_list = []
for i in range(100):
    if i % 11 == 0 and i != 0 and i % 3 != 0:
        i = str(i)
        x_list.append(i)
print(','.join(x_list))
