primeiro_valor = input("Escolha um valor: ")
segundo_valor = input("Escolha outro valor: ")

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f"O primeiro valor: {int_primeiro_valor}, é maior que o segundo valor: {int_segundo_valor}")

elif int_primeiro_valor == int_segundo_valor:
    print(f"O primeiro valor: {int_primeiro_valor}, é igual ao segundo valor: {int_segundo_valor}")

else:
    print(f"O segundo valor: {int_segundo_valor}, é maior que o primeiro valor: {int_primeiro_valor}")