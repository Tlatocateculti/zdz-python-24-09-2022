# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika
slowo_uzytkownika=input("Słowo: ")

for litera in slowo_uzytkownika.upper():
    if litera in ['A','E','I','O','U']:
    #if litera == 'A' or litera == 'E' or litera == 'I' or litera == 'O' or litera == 'U':
        continue
    print(litera)
    # Uzupełnij pętlę for poniżej.
else:
    print('Poza for')
