import random

tajny_numer = random.randrange(0,5000)

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

while True:
    liczba=int(input("Podaj liczbę:"))
    if (liczba==tajny_numer):
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
        break
    else:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")

