i = 0
n_mag = 0
n_min = 0
while i < 10:
    numero= int(input("Inserisci un valore: "))
    if(numero > 50):
        n_mag = n_mag + 1
    if(numero < 15):
        n_min = n_min + 1
    i = i + 1
    output = "*" * n_mag + "#" * n_min
print (output)
