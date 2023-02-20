# Napisz program, który wyznaczy wartość przyszłą kwoty 1000 PLN przy rocznej stopie procentowej 3%,
# kapitalizacji rocznej oraz 5-letnim okresie inwestycji. Wynik zaokrąglij do pełnych groszy.

a = 1000
p = 1.03
for i in range(1,6):
    a = a*p
print(f'Wartość końcowa inwestycji wynosi: {a:.2f} PLN')

#drugi sposób:
a = 1000
p = 0.03
y = 5
final = a * (1 + p) ** y
print(f'Wartość końcowa inwestycji wynosi: {final:.2f} PLN')
