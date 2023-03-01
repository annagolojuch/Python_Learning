number = 5
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - nie jest pierwsza')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} - nie jest pierwsza')

print(30*'-')

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
for h in hashtags:
    if h is str:
        print(True)
    else:
        print(False)
    break

print(30*'-')

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break
print(result)
