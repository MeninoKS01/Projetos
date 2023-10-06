"""
Interpolação básica de strings

s - sring
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Nathan"
preco = 1000.898453
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)
print("O hexadecimal de %d é %04X" % (758917590182, 758917590182))