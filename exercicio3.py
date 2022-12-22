print(50 * '-' )
print(f'Descobrindo maior e menor numero!! Digite 5 números quaisquer:')
a = int(input('Digite o primeiro número :'))
b = int(input('Digite o segundo número :'))
c = int(input('Digite o terceiro número :'))
d = int(input('Digite o quarto número :'))
e = int(input('Digite o quinto número :'))
if a > b and a > c and a > d and a > e:
    maior = a
if a < b and b > c and b > d and b > e:
    maior = b
if a < c and b < c and c > d and c > e:
    maior = c
if a < d and b < d and c < d and d > e:
    maior = d
if a < e and b < e and c < e and d < e:
    maior = e

if a < b and a < c and a < d and a < e:
    menor = a
if a > b and b < c and b < d and b < e:
    menor = b
if a > c and b > c and c < d and c < e:
    menor = c
if a > d and b > d and c > d and d < e:
    menor = d
if a > e and b > e and c > e and d > e:
    menor = e
print(f'O menor número digitado foi : {menor}')
print(f'O maior número digitado foi : {maior}')
print(50 * '-' )

#soma 1
# a = 3/40
# b =340
# num = 32
# den = 39
# soma = 0
# for i in range(1,4):
#     soma = soma + num/den
#     num = num + 1
#     den = den -1
# soma = soma + a + b
# print(round(soma,2))

#soma 2
# num = 480
# den = 2
# soma = 0
# for i in range(1,1):
#     soma = soma + num/den
#     num = num - 5
#     den = den + 20
# for x in range (1,20):
#     soma = soma + num/den
#     num = num + 5
#     den = den + 1
# print(soma)




    


