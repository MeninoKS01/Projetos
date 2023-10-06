# O método format é responsável por também formatar o seu código

a = "A"
b = "B"
c = 1.1

string = f"{a} {b} {c:.2f}"
formato = string.format(a, b, c) 
print(formato)

string2 = "a={nome1} b={nome2} c={nome3:.2f}"
formato2 = string2.format(
    nome1=a, nome2=b, nome3=c
    ) 
print(formato2)