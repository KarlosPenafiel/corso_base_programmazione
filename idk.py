risposta = 0
somma = 0
uno = "uno"
due = "due"
tre = "tre"
print("Gay finder ")
risposta= (input("Tette, culo o occhi?: "))
if(risposta == uno ):
    somma = somma + 1
else:
    if(risposta == due):
        somma = somma + 0.5
    else:
        if(risposta == tre):
            somma = somma + 0.5
        else:
            print("eheheheeh furbacchione non puoi scegliere altro...")
risposta= (input("un 10 ma non fa assaggiare, un 6 che fa assaggiare, un 8 ma maranza: "))
if(risposta == uno):
    somma = somma + 1
else:
    if(risposta == due):
        somma = somma + 0.5
    else:
        if(risposta == tre):
            somma = somma + 0.5
        else:
            print("eheheheeh furbacchione non puoi scegliere altro...")
risposta= (input("maranza da riccione o da padove con mia khalifa: "))
if(risposta == uno):
    somma = somma + 1
else:
    if(risposta == due):
        somma = somma + 0.5
    else:
        print("eheheheeh furbacchione non puoi scegliere altro...")
if somma >= 2:
    somma = "sei etero al 110%"
else:
    somma = "sei gay"
print (somma)