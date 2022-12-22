print('Calculando fatorial de um numero!')
numero = int(input('Digite um número que você deseja saber seu fatorial: '))

fatorial = int(1)
# for x in range(1,numero+1):
#         fatorial = fatorial * x
# print(fatorial)

x=numero
while x != 1:
    fatorial = fatorial * x
    x = x -1
print(fatorial)

# urionlinejudge.com.br
# hackerrank.com
# codechef.com
# codingame.com

