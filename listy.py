beatles = []
# Krok 1
print("Krok 1:", beatles)
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
# Krok 2
print("Krok 2:", beatles)
for nazwisko in ['Stu Sutcliffe', 'Pete Best']:
    beatles.append(nazwisko)
# Krok 3
print("Krok 3:", beatles)
del beatles[-1]
del beatles[-1]
# Krok 4
print("Krok 4:", beatles)
beatles.insert(0, 'Ringo Starr')
# Krok 5
print("Krok 5:", beatles)
# Sprawdzanie długości listy.
print("The Fab", len(beatles))
