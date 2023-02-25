capitals = {'Poland' : 'Warsaw', 'Germany' : 'Berlin', 'Austria' : 'Vienna'}
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get('Austria'))

print(30*'-')

stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks.get('PLW'))
print(stocks['TEN']['Ten Square Games'])
stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR'])
stocks['BTS'] = {'Boombit': 23}
print(stocks.values())

print(30*'-')

ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]
print(list(enumerate(ticker)))  # -> drukuje listę tupli z numeracją każdego elementu listy ticker
print(30*'-')
print(dict(enumerate(ticker)))

print(30*'-')

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
result = list(set(project_ids.values()))
result.sort()
print(result)
