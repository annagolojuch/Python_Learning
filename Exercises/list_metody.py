cities = ['Warszawa', 'Łódź', 'Kraków']
cities.append('Gdańsk')
print(cities)


idx = ['001', '002', '001', '003', '001']
i = idx.count('001')
print(f'Liczba wystąpień: {i}')


text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę', 'e')
t = set(text)
t.remove(' ')
t = sorted(t)
print(t[:10])

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.pop(3)
print(filenames)


day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
print(day1 + day2)


techs = ('python', 'java', 'sql', 'aws')
t = sorted(list(techs))
t = tuple(t)
print(t)
# lub
techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)


hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))
