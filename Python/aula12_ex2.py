# Exercício cálculo IMC

# ... = Ellipsis
print(...)
      
# f-strings são strings com formatação, onde podem ser 
# colocadas variáveis dentro de uma string
# Exemplo: f" texto {variável} "

nome = "Niceía"
altura = 1.6
peso = 80
imc = peso / (altura * altura)

linha1 = f"{nome} tem {altura:.2f} de altura"
linha2 = f"e pesa {peso} quilos e seu IMC é:"
linha3 = f"{imc:.2f}"

print(linha1)
print(linha2)
print(linha3)