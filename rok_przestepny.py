rok = int(input("Wprowadź rok: "))

if rok<1582:
    print('Nie w kalendarzu gregoriańskim')
elif rok % 4 != 0 and rok % 400 != 0:
    print('Rok zwykły')
else:
    print('Rok przestępny')
