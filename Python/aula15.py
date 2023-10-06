"""
Docstring
if = se
elif = se não se
else = se não
"""

entrada = input('Você quer "entrar" ou "sair" do sistema? ')

if entrada == "entrar":
    print("Você entrou no sistema!")
elif entrada == "sair":
    print("Você saiu do sistema!")
else:
    print("Você não digitou uma resposta válida")