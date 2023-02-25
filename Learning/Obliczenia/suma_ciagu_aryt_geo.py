# Dany jest ciąg arytmetyczny:
# a(n) = 10 +4n
# Oblicz sumę 10-ciu początkowych wyrazów tego ciągu.

x = 0
for i in range(1,11):
    a = 10 + 4*i
    x += a
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {x:.1f}')

#drugi sposób:
a1 = 14
a10 = 50
n = 10
s10 = ((a1 + a10) / 2) * n      #z tego wzoru
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {s10}')

# -------------------------------------------------------------------------------------------------

# Dany jest ciąg geometryczny:
# a(n) = 8 * 2 **(n-1)
# Oblicz sumę 6-ciu pierwszych elementów tego ciągu.

a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'Suma pierwszych {n} wyrazów ciągu wynosi: {s6}')
