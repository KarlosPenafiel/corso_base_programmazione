#Crea una semplice calcolatrice. Chiedi all'utente che operazione vuole eseguire e i due numeri. 
#Le operazioni sono la somma, la differenza, la moltiplicazione e la divisione.
#Una volta eseguito il calcolo chiedi se vuole proseguire (Y/N) e so vuole eseguire un altro calcolo. Usa le funzioni.
#Presta attenzione che l'utente non divida per 0
x = 0
y = 0
def somma(a,b):
    return a+b
def sottrazione(a,b):
    return a-b
def moltiplicazione(a,b):
    return a*b
def divisione(a,b):
    return a/b
while(True):
    calcolo = str(input("inserisci il calcolo che vuoi fare: "))
    x= int(input("inserisci primo numero: "))
    y= int(input("inserisci secondo numero: "))
    if (calcolo == "somma"):
        print(somma(x,y))
    if (calcolo == "sottrazione"):
        print(sottrazione(x,y))
    if (calcolo == "moltiplicazione"):
        print(moltiplicazione(x,y))
    if (calcolo == "divisione"):
    if
