print('Gerador de senha')
chave = input('Digite a base para gerar sua senha: ')
senha = ''
for letra in chave:
    if letra in 'Aa': senha = senha + '!' 
    elif letra in 'Bb': senha = senha + '0'
    elif letra in 'Cc' : senha = senha + '/'
    elif letra in 'Dd' : senha = senha + '$'
    elif letra in 'Ee' : senha = senha + '#'
    elif letra in 'Ff' : senha = senha + '@'
    elif letra in 'Gg' : senha = senha + '1'
    elif letra in 'Hh' : senha = senha + '5'
    elif letra in 'Ii' : senha = senha + '2'
    elif letra in 'Jj' : senha = senha + '9'
    elif letra in 'Kk' : senha = senha + '7'
    elif letra in 'Ll' : senha = senha + '6'
    elif letra in 'Mm' : senha = senha + '8'
    elif letra in 'Nn' : senha = senha + '4'
    elif letra in 'Oo' : senha = senha + '3'
    elif letra in 'Pp' : senha = senha + '?'
    elif letra in 'Qq' : senha = senha + '*'
    elif letra in 'Rr' : senha = senha + '&'
    elif letra in 'Ss' : senha = senha + '|'
    elif letra in 'Tt' : senha = senha + '<'
    elif letra in 'Uu' : senha = senha + '+'
    elif letra in 'Vv' : senha = senha + '%'
    elif letra in 'Xx' : senha = senha + '}'
    elif letra in 'Ww' : senha = senha + '['
    elif letra in 'Yy' : senha = senha + '-'
    elif letra in 'Zz' : senha = senha + ']'
    else: senha = senha + letra
print(f'Sua senha forte é : {senha}')
