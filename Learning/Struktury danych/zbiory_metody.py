przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski') #dodanie elementu do zbioru
print(przedmioty)
# .discard() - usuwa elemant zbioru
# .remove() - usuwa element zbioru; NIE STOSOWAĆ GDY NIE MAMY PEWNOŚCI CZY ELEMENT JEST W ZBIORZE
# .pop() - zwraca i usuwa pierwszy element zbioru


# Zamień wszystkie litery na małe.
# Usuń spacje i kropkę.
# Utwórz zbiór składający się z wszystkich liter w tak przetworzonym tekście.
# Odpowiednią metodą dla zbiorów usuń z tego zbioru wszystkie samogłoski (zbiór vowels)
# Wydrukuj liczbę elementów w tak przetworzonym zbiorze (inaczej liczba spółgłosek)
text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
text = set(text)
text = text.difference(vowels)
print(f'Liczba elementów: {len(text)}')


# Różnica symetryczna
A = {2, 4, 6, 8}
B = {4, 10}
A ^= B                                  # to samo: sym_diff = A.symmetric_difference(B)
print(f'Różnieca symetryczna: {A}')     # -> {2, 6, 8, 10}


is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
print(f'ID klientów: {is_clicked.intersection(is_bought)}')  # wyrzuca elemnty wspólne zbiorów
