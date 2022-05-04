""""Controle de máquina registradora"""
preco = 0
total_compras = 0
while True:
    produto = int(input('Qual o código do produto (1),(2),(3),(5),(9) ou (0) para finalizar a compra: '))
    if produto == 0:
        break
    quantidade = int(input(f'Qual a quantidade do produto({produto}), comprada: '))
    if produto == 1:
        preco = quantidade * 0.50
    elif produto == 2:
        preco = quantidade * 1.00
    elif produto == 3:
        preco = quantidade * 4.00
    elif produto == 5:
        preco = quantidade * 7.00
    elif produto == 9:
        preco = quantidade * 8.00
    total_compras += preco
print(total_compras)
