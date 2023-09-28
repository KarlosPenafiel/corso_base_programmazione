numero_inserito = 0
numero_precedente = 0
numeri_maggiori = 0
i = 0
while i <= 9:
    numero_inserito = int(input("inserisci un numero: "))
    if (i == 0):
        numero_precedente = numero_inserito
        i = i + 1
        continue
    if (numero_inserito > numero_precedente):
        numeri_maggiori = numeri_maggiori + 1
    numero_precedente = numero_inserito
    i = i + 1
    print (numeri_maggiori)








