"""
Formatação básica de strings

s - strings
d - int
f - float
.<número de dígitos>f

(Caractere)(><^)(quantidade)
> - Esquerda
> - Direita
^ - Centro
= - Foça o número a aparecer antes do zero
Sinal - + ou -
Exemplo:: 0>-100,.1f

Conversion flags:
!r = __repr__
!s = __str__
!a = __asc__
"""

texto = "ABCD"

print(f"{texto}")
print(f"{texto: >20}")
print(f"{texto: <20}")
print(f"{texto: ^20}")
print(f"{1000.65790326591:0=+10,.1f}")
print(f"O hexadecimal de 1500 é {1500:06X}")

