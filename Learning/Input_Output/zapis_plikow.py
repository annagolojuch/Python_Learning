headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv', 'w') as file3:
    file3.write(','.join(headers) + '\n')
    for user in users:
        file3.write(','.join(user) + '\n')

print(30*'-')

import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
with open('stocks.json', 'w') as file2:
    json.dump(stocks, file2, indent=4)

print(30*'-')

with open("num.txt", "w") as file1:
    for i in range(20):
        if i % 2 == 0 and i != 0:
            file1.write(str(i) + '\n')
