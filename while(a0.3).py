""""Poupança"""
# jutos simples = j = c.i.t (juros = capital*taxa*tempo)
x = 1
jurosT = 0
tempo = 24
while (x <= tempo):
    n = float(input(f'({x}),Qual o deposito: '))
    j = float(input(f'({x}),Qual a taxa de juros: '))
    s = float(input('E qual o valor para o mês seguinte: '))
    jn = float(input(f'({x}),Qual a taxa de juros para o mês seguinte: '))
    porcent = (n * j) / 100
    porcent2 = (s * jn) / 100
    print(f'O percentual de juros do mês: ({x}), é de: R${porcent}')
    print(f'No mês seguinte ({x + 1}) o deposito será de: R${s}, com o percentual de juros de {porcent2}')
    form_juro =  (porcent * porcent2) * tempo
    jurosT = (jurosT + form_juro)
    x = (x + 2)
print(f'O ganho de juros por período é: R${jurosT:.2f}')
