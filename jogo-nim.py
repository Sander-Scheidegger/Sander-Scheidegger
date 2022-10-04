def computador_escolhe_jogada(n, m):
    jogada_pc = 1
    while jogada_pc < m:
        if (n - jogada_pc) % (m+1) == 0:
            return jogada_pc
        else:
            jogada_pc += 1
    return jogada_pc

def usuario_escolhe_jogada(n, m):
    jogada_usuario = int(input('Digite quantas peças deseja retirar: '))
    while jogada_usuario > m or jogada_usuario < 1:
        print(jogada_usuario)
        jogada_usuario = int(input('Digite quantas peças deseja retirar: '))
    else:
        print(jogada_usuario)
        return jogada_usuario
    vez_usuario = False


def partida():
    n = int(input('Digite com quantas peças deseja jogar: '))
    m = int(input('Digite qual limite de peças cada jogador pode retirar: '))
    vez_pc = False
    vez_usuario = False
    if n % (m + 1) == 0:
        print('Você começa!')
        vez_usuario = True
    else:
        print('O computador começa!')
        vez_pc = True

    if n == 0:
        print('O computador ganhou!')


    while n > 0:
        if vez_pc:
            jogada_pc = computador_escolhe_jogada(n, m)
            n = int(n)
            n = (n - jogada_pc)
            print('O computador retirou', jogada_pc, 'peças!')
            if n > 0:
                print('Restam', n, ' peças!')
            else:
                print('O computador ganhou!')
            vez_pc = False

        else:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n = (n - jogada_usuario)
            vez_pc = True
            vez_usuario = False
            print('Você retirou', jogada_usuario, 'peças!')
            print('Restam', n, 'peças')


def campeonato():
    n_partida = 0
    while n_partida < 3:
        n_partida += 1
        print()
        print('Essa é a partida numero ',n_partida, 'de 3!')
        print()
        partida()
    else:
        print('Placar: Você 0 X 3 Computador')

print('Bem-vindo ao jogo do NIM!')
print('O objetivo do jogo é retirar a última peça do tabuleiro.')
print('O jogador tem que retirar 1 ou mais peças por vez.')
print('O jogador deverá escolher quantas peças terão no tabuleiro, e quantas cada jogador poderá tirar.')
print()
print('1 - para jogar uma partida isolada.')
print('2 - para jogar um campeonato.')
tipo_de_partida = int(input('Resposta: '))


if tipo_de_partida == 1:
    partida()
    print('Você escolheu partida!')

if tipo_de_partida == 2:
    print('Você escolheu campeonato!')
    campeonato()