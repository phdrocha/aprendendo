print('Jogo do acerto!')
acerto = 9
palpite = int(input('Digite um número de 0 a 10: '))
while True:
    if palpite == acerto:
        print(bool(palpite))
        print('Acertou miseravi')
        break
    else: 
        print(bool(palpite))
        print('Você ERROU')  
        palpite = int(input('Digite um número de 1 a 10:'))
       
