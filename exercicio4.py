# maior e menor
# def maior(x, y):
#     if x > y:
#         print(f'O número da variável x = {x} é maior quer o número da variável y = {y}')
#     elif x == y:
#         print('Números iguais!')
#     else:
#         print(f'O número da variável y = {y} é maior quer o número da variável x = {x}')

# while True:
#     x = float(input('Digite um número para variável x :'))
#     y = float(input('Digite um número para variável y :'))
#     print('-'*50) 
#     maior(x, y)
#     print('-'*50)
#     aux = input('Deseja inserir novos números?')
#     if aux in ['s', 'S', 'Sim', 'sim']:
#         print('-'*50)
#         pass
#     elif aux in ['n', 'N', 'Nao', 'nao']:
#         break
#     else:
#         break


#média aritimetica
# def media(x, y):
#     aux = (x + y)/2
#     print(f'A média aritimética de x e y é : {aux}')

# while True:
#     x = float(input('Digite um número para variável x : '))
#     y = float(input('Digite um número para variável y : '))
#     print('-'*50) 
#     media(x, y)
#     print('-'*50)
#     aux = input('Deseja inserir novos números?')
#     if aux in ['s', 'S', 'Sim', 'sim']:
#         print('-'*50)
#         pass
#     elif aux in ['n', 'N', 'Nao', 'nao']:
#         break
#     else:
#         break


# exponenciação
def exp(x, y):
    e = x**y
    print(f'O valor de x elevado a y é : {e}')

while True:
    print('EXPONENCIAÇÃO')
    print('-'*50)
    x = int(input('Digite um número para variável x : '))
    y = int(input('Digite um número para variável y : '))
    print('-'*50) 
    exp(x, y)
    print('-'*50)
    aux = input('Deseja inserir novos números?')
    if aux in ['s', 'S', 'Sim', 'sim']:
        print('-'*50)
        pass
    elif aux in ['n', 'N', 'Nao', 'nao']:
        break
    else:
        break


