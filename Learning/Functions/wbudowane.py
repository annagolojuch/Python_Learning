number = 234
x = 0
y = list(bin(number))
for i in y:
    if i == '1':
        x += 1
print(x)
# drugi sposób:
number = 234
binary = bin(number)
binary = binary[2:]
print(binary.count('1'))

print(30*'-')

items = ('', 0.0, 0, False)     #sprawdzenie czy jakikolwiek element tuple zwraca True
print(any(items))

print(30*'-')

items = (' ', '0', 0.1, True)   #sprawdzenie czy wszystkie elementy tuple zwracają True
print(all(items))

print(30*'-')

ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')
print(list(zip(ticker, full_name)))

print(30*'-')

characters = ['k', 'b', 'c', 'j', 'z', 'w']
print('Pierwsza:', min(characters))
print('Ostatnia:', max(characters))

print(30*'-')

var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}
print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

print(30*'-')

x = -1.5
expression = 'x**2 + x'
print(eval(expression))
