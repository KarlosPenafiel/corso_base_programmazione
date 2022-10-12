maggiore = 0
numero1 = 0
numero2 = 0
numero3 = 0
somma = 0
numero1 = int(input("Inserisci primo numero: "))
numero2 = int(input("Inserisci secondo numero: "))
numero3 = int(input("Inserisci terzo numero: "))
somma = int(numero1+numero2+numero3)

if (numero1 > numero2) and (numero1 > numero3) :
    maggiore = numero1
if (numero2 > numero1) and (numero2 > numero3) :
    maggiore = numero2
if (numero3 > numero1) and (numero3 > numero2) :
    maggiore = numero3
if (somma > 10) :
    print ("Il numero più grande è ", maggiore)
else:
        print("La somma è ", somma)