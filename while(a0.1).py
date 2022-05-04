""""Média de cinco números em while"""
x = 1 # contador
soma = 0 # acumulador
while (x <= 5): #condição while
    n = int(input(f'{x}, Digite o número: '))
    soma = (soma + n) # acumulador
    x =(x + 1) # contador
print(f'Média: {soma / 5:5.2f}')