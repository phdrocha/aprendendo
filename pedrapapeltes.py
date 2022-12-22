from random import choice

vitJogador =0
vitMaquina = 0

def escJogador():
    jogador = input('Digite sua escolha entre Pedra, Papel ou Tesoura: ')
    jogador = jogador.lower()
    if jogador == 'pedra':
        return jogador
    elif jogador == 'tesoura':
        return jogador
    elif jogador == 'papel':
        return jogador
    else:
        print('Você digitou uma opção INVÁLIDA! Tente novamente!')
        escJogador()

def escMaquina(): 
    maquina = choice(['pedra', 'papel', 'tesoura'])
    return maquina

while True:
    print('-'*50)
    j = escJogador()
    m = escMaquina()
    print('-'*50)
    if (j == 'pedra') and (m == 'tesoura')\
         or (j == 'papel') and (m == 'pedra')\
            or (j == 'tesoura') and (m == 'papel'):
            print(f'O jogador escolheu {j} e a máquina {m}. Resultado : VITÓRIA!')
            vitJogador += 1
    elif (j == m):
        print(f'O jogador escolheu {j} e a máquina {m}. Resultado : EMPATE!')
    else:
        print(f'O jogador escolheu {j} e a máquina {m}. Resultado : DERROTA!')
        vitMaquina += 1 
    print('-'*50)
    print(f'Vitórias do jogador: {vitJogador}')
    print(f'Vitórias da máquina: {vitMaquina}')
    print('-'*50)
    jogador = input('Deseja jogar novamente?')
    if jogador in ['s', 'S', 'Sim', 'sim']:
        pass
    elif jogador in ['n', 'N', 'Nao', 'nao']:
        break
    else:
        break
    
