print(30*'-')

item = '001'
items = ['001', '000', '003', '005', '006']
if item in items:
    items.remove(item)
print(items)


print(30*'-')

project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
print(project_ids)

print(30*'-')

project_ids = ['02134', '24253']
if not '02135' in project_ids:
    project_ids.append('02135')
print(project_ids)

print(30*'-')

password = 'cskdnjcasa#!'
if len(password) >= 11 and '!' in password:
    print("Hasło poprawne")
else:
    print('Hasło niepoprawne')

print(30*'-')

password = 'cskdnjcasa#!'
if len(password) >= 11:
    print("Hasło poprawne")
else:
    print('Hasło zbyt krótkie')

print(30*'-')

number = 1.0
if isinstance(number, int):
    print('TAK')
else:
    print(f'{number} NIE jest zamienną typu int')

print(30*'-')

filename = '01012020_sales.xlsx'
if filename.endswith('.xlsx'):
    print('TAK')
else:
    print('NIE')

print(30*'-')

code = 'DSVNDOICSN'
if code.isupper():
    print('TAK')

