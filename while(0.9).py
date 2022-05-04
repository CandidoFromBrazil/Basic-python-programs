"""Tabuada de multiplicação"""
n = int(input('numeral : '))
x = int(input("multiplicador: "))
while(x<=n):
    print(f'{n}x{x} = {n * x}')
    x += 1