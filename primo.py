print(50*'-')
print('Números Primos!')
num = int(input('Digite um número para saber se ele é um número primo: '))
if num > 1:    
    for x in range(2, num ):
        if num % x == 0:
            print('Este não é um numero primo!')
            break
    else:
        print('Este é um número primo')
          
else:
    print('Você digitou um número inválido!')       
print(50*'-') 