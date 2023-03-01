numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None
while start <= end:
    mid = int((start + end) /2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')

print(30*'-')

counter = 0
number = 2
prime = []
while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1
print(','.join(prime))

print(30*'-')

n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)
while fv < 2000:
    fv = fv * 1.04
    n += 1
print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')
