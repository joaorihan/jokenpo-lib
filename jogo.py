import joklib

escolha = ""
jogando = "sim"
pontos_player = 0
pontos_bot = 0
num_empates = 0


print("\nVamos jogar jokenpô\n")

while jogando == "sim":
    ganhou = 0
    empate = False
    sair = False    
    print(f"\n\nPontuação atual: \nVocê: {pontos_player}\nBot: {pontos_bot}\nEmpates: {num_empates}")
    print("\nEscolha entre Pedra, Papel e Tesoura")
    jogada = input()
    print(f"Sua escolha foi {jogada}")
    jogada_bot = joklib.jogada_bot()
    ganhou = joklib.verif_vitoria(jogada, jogada_bot)
    if sair:
        break
    if empate:
        num_empates += 1
    elif ganhou == True:
        pontos_player += 1
    elif ganhou == False: 
        pontos_bot += 1
    else:
        num_empates +=1