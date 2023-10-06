nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if " " in nome:
        print("Seu nome contém espaço")
    else:
         print("Seu nome não contém espaço")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0:1]}")
    print(f"A última letra do seu nome é {nome[5:6]}")  
        
else:
    print("Desculpe, você deixou os campom vazios.")