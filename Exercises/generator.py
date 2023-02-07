#generowanie liczb parzystych z jakiegos zakresu

def liczby():
    for x in range(11):
        yield x*2

for i in liczby():
    print(i)
