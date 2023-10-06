"""
Operador lógico "not"
Usado para inverter expessões
not True = False
not False = True
"""

senha = input("Senha: ")

if not senha:
    print("Você não digitou a senha")

print(not True)
print(not "abc")
print(not False)
print(not 0)