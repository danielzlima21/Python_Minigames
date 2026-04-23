import random
jogadores = []

def adicionar_jogador():
    nome = input('Digite seu nome: ')
    vitorias = 0
    tentativas = 0
    novo_jogador = {'nome': nome, 'vitorias': vitorias, 'tentativas': tentativas}
    jogadores.append(novo_jogador)

def ate_acertar():
    numero_de_jogadores = len(jogadores)
    if len(jogadores) <= 1:
        print('nao há jogadores suficientes')
    else:
        print(f'Os {numero_de_jogadores} jogadores irão jogar até que um deles acerte')
        codigo = random.randint(1, 100)
        alguem_venceu = False
        while not alguem_venceu:
            for jogador in jogadores:
                print(f'Vez de === {jogador["nome"]} ===')
                adivinhe = int(input('Adivinhe o código: '))
                if adivinhe == codigo:
                    print(f'Parabens {jogador["nome"]} voce acertou o codigo era: {codigo}')
                    jogador["vitorias"] += 1
                    alguem_venceu = True
                    break
                elif adivinhe > codigo:
                    print(f'{jogador["nome"]} Chute mais BAIXO')
                elif adivinhe < codigo:
                    print(f'{jogador["nome"]} Chute mais ALTO')

def com_tentativas():
    numero_de_jogadores = len(jogadores)
    if len(jogadores) <= 1:
        print('não há jogadores suficientes')
    else:
        print(f'Quem dos {numero_de_jogadores} jogadores que ganhar com o menor numero de tentativas vence')
        for jogador in jogadores:
            jogador["tentativas"] = 0
            codigo = random.randint(1, 100)
            print(f'vez de {jogador["nome"]}')
            while True:
                print(f'tentativa atual: {jogador["tentativas"]}')
                adivinhe = int(input(f'{jogador["nome"]} adivinhe o código: '))
                jogador["tentativas"] += 1
                if adivinhe == codigo:
                    print(f'Parabens {jogador["nome"]} voce acertou o codigo era: {codigo}')
                    print(f'suas tentativas: {jogador["tentativas"]}')
                    break
                elif adivinhe > codigo:
                    print(f'{jogador["nome"]} Chute mais BAIXO')
                elif adivinhe < codigo:
                    print(f'{jogador["nome"]} Chute mais ALTO')
        vencedor = min(jogadores, key=lambda j: j["tentativas"])
        print((f"Vencedor: {vencedor["nome"]}, Tentativas: {vencedor["tentativas"]}"))
        vencedor["vitorias"] += 1

def jogar():
    while True:
        for jogador in jogadores:#filtrar por quem tem mais vitorias
            print(f'{jogador["nome"]} | Vitorias: {jogador["vitorias"]}🏆')

        print()
        print('=== MENU JOGO DA BOMBA ===')
        print('1 - Adicionar jogador')
        print()
        print('=== MODOS DE JOGO ===')
        print('2 - Até acertar')
        print('3 - Com tentativas')
        print('4 - Sair')

        while True:
            menu = int(input('Digite: '))
            if menu not in(1, 2, 3, 4):
                print('numero invalido')
            else:
                break

        if menu == 1:
            adicionar_jogador()
        elif menu == 2:
            ate_acertar()
        elif menu == 3:
            com_tentativas()
        elif menu == 4:
            print("PROGRAMA FINALIZADO")
            break

jogar()
