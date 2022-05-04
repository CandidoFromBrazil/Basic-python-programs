""""Poupança"""
# jutos simples = j = c.i.t (juros = capital*taxa*tempo)
x = 1
jurosT = 0
tempo = 24
while (x <= tempo):
    n = float(input(f'({x}),Qual o deposito: '))
    j = float(input(f'({x}),Qual a taxa de juros: '))
    porcent = (n * j) / 100
    print(f'O percentual de juros do mês: {x}, é de: R${porcent}')
    form_juro =  (porcent * tempo)
    jurosT = (jurosT + form_juro)
    x = (x + 1)
print(f'O ganho de juros por período é: R${jurosT:.2f}')

