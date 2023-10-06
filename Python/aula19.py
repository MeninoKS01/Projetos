"""
Operador Lógico

and = e
or = ou
not = não

"and" - Todas as condições precisam ser verdadeiras

Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor

São considerados falsy:
0
0.0
""
False

Também existe  o tipo None que é usado para 
representar um não valor
"""

entrada = input("[E]ntrar ou [S]air? ")
senha = input("Insira a senha: ")

senha_valida = "123"

if (entrada == "E" or entrada == "e") and senha == senha_valida:
    print("Entrou")
elif entrada == "S" or entrada == "s":
    print("Saiu")
else:
    print("Resposta inválida")

# Avaliação de curto circuito

print(True and False and True)
print(bool(0))

print(0 or False or "" or "abc" or True)