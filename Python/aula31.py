"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo não tem fim
"""

while True:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == "sair":
        break

print("você saiu!")