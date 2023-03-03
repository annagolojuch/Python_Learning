with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
data = [(line.split(',')[0], line.split(',')[5]) for line in content]
data = [(val[0], int(val[1])) for val in data[1:]]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Data: {max_date}')

print('--------------')

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
result = []
data = [(line.split(',')[5]) for line in content][1:]
for i in data:
    result.append(int(i))
print(f'Max Vol: {max(result)}')

print('--------------')

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)],
}
print(result)

print('--------------')

with open("playway.txt", "r") as file:
    f = file.readlines()
for i in range(len(f)):
    f[i] = f[i].split(',')

total = 0
for i in range(1, len(f)):
    total += int(f[i][4])
average = total / (len(f)-1)
print(f'3-dniowa średnia cena zamknięcia: {average:.2f}')

print('--------------')

x = []
with open('indeksy.txt', 'r') as file1:
    f1 = file1.read().splitlines()
print(f1)
print('--------------')
for i in f1:
    if i.startswith("WIG"):
        x.append(i)
print(x)
