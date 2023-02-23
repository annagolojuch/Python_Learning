capitals = {'Poland' : 'Warsaw', 'Germany' : 'Berlin', 'Austria' : 'Vienna'}
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get('Austria'))


stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks.get('PLW'))
print(stocks['TEN']['Ten Square Games'])
stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR'])
