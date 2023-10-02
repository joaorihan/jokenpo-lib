import joklib

jogando = True
pontos_player = 0
pontos_bot = 0
num_empates = 0


print("\nVamos jogar jokenpô\n")

while jogando:
    ganhou = 0
    empate = False
    print(f"\n\nPontuação atual: \nVocê: {pontos_player}\nBot: {pontos_bot}\nEmpates: {num_empates}")
    print("\nEscolha entre Pedra, Papel e Tesoura")
    jogada = input()
    print(f"Sua escolha foi {jogada}")
    if jogada == "sair":
        jogando = False
        break
    jogada_bot = joklib.jogada_bot()
    ganhou = joklib.verif_vitoria(jogada, jogada_bot)
    if empate:
        num_empates += 1
    elif ganhou == True:
        pontos_player += 1
    elif ganhou == False: 
        pontos_bot += 1
    else:
        num_empates += 1

print("\n\nFim do Jogo!")