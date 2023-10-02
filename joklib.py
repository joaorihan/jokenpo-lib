
def jogada_bot():
    import random
    joken = ("pedra" , "papel", "tesoura")
    bot = 0
    bot = random.choice(joken)
    print(f"\nA escolha do Bot foi {bot}")
    return bot

def verif_vitoria(escolha, bot):
    empate = 0
    ganhou = 0
    if escolha== "papel" and bot == "pedra":
        print("\nVocê Ganhou!")
        ganhou = True
    elif escolha== "pedra" and bot == "tesoura":
        print("\nVocê Ganhou!")
        ganhou = True
    elif escolha== "tesoura" and bot == "papel":
        print("\nVocê Ganhou!")
        ganhou = True
    elif escolha== "pedra" and bot == "papel":
        print("\nVocê Perdeu")  
        ganhou = False
    elif escolha== "papel" and bot == "tesoura":
        print("\nVocê Perdeu")
        ganhou = False
    elif escolha== "tesoura" and bot == "pedra":
        print("\nVocê Perdeu")
        ganhou = False
    elif escolha == bot:
        print("\nEmpate")
        empate = True
        ganhou = 0
        return empate, ganhou
    elif escolha == "sair" or escolha == "exit":
        sair = True
        return sair
    return ganhou
    


