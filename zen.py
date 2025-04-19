zen=["Bonito é melhor do que feio.", #Criando uma lista de strings com o nome zen da lista zen of Python
     "Explícito é melhor do que implícito.",
     "Simples é melhor do que complexo.",
     "Complexo é melhor do que complicado.",
     "Plano é melhor do que amontoado.",
     "Legibilidade conta.",
     "Casos especiais não são especiais o bastante para quebrar as regras.",
     "Embora a Praticidade vence a Pureza.",
     "Erros nunca devem passar silenciosamente.",
     "A menos que sejam explicitamente silenciados.",
     "Diante da ambiguidade recuse a tentação de adivinhar.",
     "Deveria haver um e referencialmente só um modo óbvio de fazer isso.",
     "Embora esse modo possa não ser óbvio a primeira vista, a menos que você seja holandês.",
     "Agora é melhor do que nunca.",
     "Embora nunca frequentemente seja melhor do que *extamente* agora.",
     "Se a implementação é dificil de explicar, é uma má idéia.",
     "Se a implementação é facil de explicar, pode ser uma boa idéia.",
     "Namespaces são uma grande idéia- Vamos fazer mais dessas!"
     ]
nome = input("Qual o seu nome? ") # pedi o nome do usuario 

print("Escolha sua frase favorita do Zen of Python: ")
for i, frase in enumerate(zen,1): #Transformando a lista em uma sequência enumerada para o usuario escolher mais facilmente 
    print(f"{i}. {frase}")

while True:
    try: #convertendo a entrada em um número    
        escolha=int(input("\nDigite o número da frase que você mais gostou: "))
        if 1 <= escolha <= len(zen): # garantindo que o número digitado esteja na lista 
            break
        else:
            print("por favor escolha um número válido da lista.")
    except ValueError: # indentificando se houver erro 
        print("Digite um valor válido.")
motivo=(input("Porque essa frase chamou sua atenção? "))

print("\n--- ZEN DO USUÁRIO PYTHON---")
print(f"Olá {nome}!!")
print(f"Sua frase favorita:{zen[escolha-1]}") # pegando a frase escolhida de dentro da lista 
print(f" Motivo: {motivo}")
print("Seja bem vindo ao universo Python! ")