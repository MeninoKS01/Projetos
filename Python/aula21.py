"""
Operadores in e not in

Strings são iteráveis
0 1 2 3 4 5
N a t h a n
6 5 4 3 2 1
"""

nome = "Nathan"

print(nome[3])
print(nome[-4])

print("Na" in nome)
print("ta" in nome)

print("Na" not in nome)
print("ta" not in nome)

nome = input("Qual o seu nome? ")
encontrar = input("O que deseja encontrar? ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")