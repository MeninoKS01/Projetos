"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Insira um número: ")


if numero.isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

else:
    print("Seu número não é válido")
   
