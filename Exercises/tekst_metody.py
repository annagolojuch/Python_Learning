text = 'python jest popularnym językiem programowania.'
t = text.count('p')
print(f'Liczba wystąpień: {t}')


text = 'python jest popularnym językiem programowania.'
print(text.capitalize())    #zmiana pierwszej dużej litery w tekście


code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print(f'code1: {code1.endswith("2020")}')
print(f'code2: {code2.endswith("2020")}')


path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print(f'path1: {path1.startswith("youtube")}')
print(f'path2: {path2.startswith("youtube")}')


path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
print(f'path1: {path1.index("scientist")}')
print(f'path2: {path2.find("scientist")}')
print(f'path3: {path3.find("scientist")}') #zwraca -1 jesli nie ma tego wyrazu w stringu


code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')
# .isalpha() - sprawdza czy tylko znaki
# .isdigit() - sprawdza czy tylko numery
# .isspace() - sprawdza czy tylko białe znaki są w stringu


text = 'Google Colab'
print(text.lower())


text = 'Google Colab'
print(text.upper())


text = '  Google Colab   '
print(text.strip())     #usuwa białe znaki dookoła stringa


code = 'FVNISJND-XX'
print(code.replace('-',' '))

text = '340-23-245-235'
print(text.replace('-', ''))


text = 'Open,High,Low,Close'
print(text.split(','))      #tworzy listę stringów podzieloną przecinkiem i spacją


text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""
print(text.split('\n'))

num = 34
print(str(num).zfill(6))    #wyściela zerami od lewej strony strin aby miał 6 znaków


url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
u = url.split('/')[-1]
print(u.replace('-', ' '))  #wycinamy wszystko po ostatnim / i zamieniamy - na spacje
