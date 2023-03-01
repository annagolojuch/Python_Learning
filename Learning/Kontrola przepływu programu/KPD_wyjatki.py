suma = 3000
counter = 0
try:
    result = suma / counter
print(result)
except ZeroDivisionError:
    print('Dzielenie przez zero.')

print(30*'-')

try:
    with open('file.txt', 'r') as file:
        content = file.read()

except FileNotFoundError:
    print('Nie zanleziono pliku.')

print(30*'-')

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'
try:
    print(users[user_id])
except:
    print(f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...')
    users['004'] = None
    print(users)
