tempo = int(input('Digite o tempo em HORAS gasto na viagem: '))
vel = int(input('Digite a velociade média em km/h gasto na viagem: '))
consumo = (vel * tempo)/12
print(f'Você vai gastar {round(consumo,3)} litros de combustível')