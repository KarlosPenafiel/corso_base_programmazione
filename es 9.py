tax1 = 22/100
tax2 = 33/100
totale = 0
reddito = int(input("Inserisci il tuo reddito: "))
if (reddito < 10000):
    totale = 0
else:
    if(10000 <= reddito <= 30000):
            totale = (reddito * tax1)
    else:
        if(reddito > 30000):
            tax1 = tax1 * 20000
            tax2 = tax2 * (reddito-30000)
            totale = tax1 + tax2 
print("la tassa totale da pagare è:€",totale)