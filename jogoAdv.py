from random import randint
from time import sleep

def jogar_novamente():
    while True:
        rsp = input('\nDeseja jogar novamente? (s/n)> ').lower()
        if rsp == 'n':
            print(f'\nFoi um prazer jogar com você, {nome.capitalize()}! Até breve! 😉')
            return False
        elif rsp == 's':
            print('\nOBA! Vamos mais uma! 🤩')
            return True
        else:
            print("\nResposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

def placar():
    print('\n------ PLACAR -------')
    print(f'Máquina: {pts_pc} ponto(s)')
    print(f'{nome.capitalize()}: {pts_player} ponto(s)')
    print('---------------------')

def validacao_entrada(menor, maior):
    while True:
        try:
            player = int(input(f'\nDigite um número entre {menor} e {maior}: '))
            if menor <= player <= maior:
                return player
            else:
                print(f"\nDigite um número válido entre {menor} e {maior}.")
        except ValueError:
            print("\nPor favor, digite um número válido.")

def dicas(pc, player):
    if abs(pc - player) <= 2:
        print('🔥 Você está muito próximo!')
    elif abs(pc - player) <= 5:
        print('🌟 Você está perto!')
    else:
        print('❄️ Você está longe...')

# Início do jogo
pts_pc = 0
pts_player = 0
rodadas = 0
executando = True

print('Seja bem-vindo(a) ao Jogo de Adivinhação! Vamos brincar? 😄\n')
nome = input('Diga-me qual o seu nome > ')
print(f'\nOlá, {nome.capitalize()}! Seja bem-vindo(a)! 🫡')

while True:
    print('\nEscolha um nível de dificuldade:')
    print('1 - Fácil (0 a 10, tentativas ilimitadas)')
    print('2 - Médio (0 a 20, 5 tentativas)')
    print('3 - Difícil (0 a 50, 3 tentativas)')
    try:
        nivel = int(input('Escolha o nível (1/2/3): '))
        if nivel == 1:
            menor, maior, tentativas = 0, 10, None
        elif nivel == 2:
            menor, maior, tentativas = 0, 20, 5
        elif nivel == 3:
            menor, maior, tentativas = 0, 50, 3
        else:
            print('Por favor, escolha um nível válido.')
            continue
        break
    except ValueError:
        print('Por favor, digite um número válido.')

print('-='*40)
print(f'\nEscolhi um número entre {menor} e {maior}. Será que você consegue adivinhar? 😜')
print('-='*40)

while executando:
    rodadas += 1
    print(f'\n--- RODADA {rodadas} ---')
    pc = randint(menor, maior)
    tentativas_restantes = tentativas

    while True:
        if tentativas_restantes is not None:
            print(f'Tentativas restantes: {tentativas_restantes}')

        player = validacao_entrada(menor, maior)

        print(f'\nVocê acha que o número é {player}? 🤔')
        sleep(1)

        print('\nVamos ver... ⏳')
        sleep(2)

        if player == pc:
            print(f'\n🎉 PARABÉNS! Você acertou! 🥳')
            pts_player += 1
            break
        else:
            print(f'\n❌ ERRADO! O número escolhido não foi {player}.')
            dicas(pc, player)

            if tentativas_restantes is not None:
                tentativas_restantes -= 1
                if tentativas_restantes == 0:
                    print(f'\n🤖 GAME OVER! O número que escolhi foi {pc}.')
                    pts_pc += 1
                    break

    placar()
    executando = jogar_novamente()

print('\nObrigado por jogar! 🎮')
