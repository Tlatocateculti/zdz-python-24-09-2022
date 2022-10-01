dochod = float(input("Wprowadź swój roczny dochód: "))

"""
if dochod <= 85528:
    podatek = dochod * 0.18 - 556.02
    if podatek <= 0:
        podatek = 0
else:
    podatek = 14839.02 + (dochod-85528) * 0.32


podatek = ((14839.02 + (dochod-85528) * 0.32) , (dochod * 0.18 - 556.02))[dochod<=85528]
if podatek <= 0: podatek = 0
"""

podatek = dochod * 0.18 - 556.02 if dochod<=85528 else 14839.02 + (dochod-85528) * 0.32
if podatek <= 0: podatek = 0

podatek = round(podatek, 0)
print("Podatek wynosi:", podatek)
