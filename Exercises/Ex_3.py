a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#pierwsza część
x = []
for i in a:
    if i < 5:
        x.append(i)
        x.sort()
print(x)
print()

#druga część
y = []
num = int(input("Wprowadź liczbę >>"))
for j in a:
    if j < num:
        y.append(j)
        y.sort()
print(y)




