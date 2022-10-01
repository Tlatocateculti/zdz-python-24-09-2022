blokow = int(input("Wprowadź liczbę bloków: "))
wysokosc=0
#for i in range(1,blokow+1):
#    if (blokow-i>=0):
#        wysokosc+=1
#        blokow-=i
#    else:
#        break

#while True:
#    if (blokow-(wysokosc+1)>=0):
#        wysokosc+=1
#        blokow-=wysokosc
#    else:
#        break
while blokow-(wysokosc+1)>=0:
    wysokosc+=1
    blokow-=wysokosc



print("Wysokość piramidy wynosi:", wysokosc)
