"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a funsão len retorna a quantidade de 
caracteres da str
"""

texto = "Olá mundo"
print(texto[0:4])
print(texto[4:len(texto)])

print(len(texto))

print(texto[::-1])


