n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
opera = int(input("Inserisci l'operazione da fare: "))
if (opera > 4):
    risultato = n1 + n2
else:
    if(opera == 1):
        risultato = n1 + n2
    if(opera == 2):
        risultato = n1 - n2
    if (opera == 3):
        if (n2 == 0):
            risultato = str("Non si può dividere per zero!")
        else:
            risultato = n1 / n2
    if (opera == 4):
        risultato = n1 * n2
print (risultato)
    