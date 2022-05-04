"""Tabuada de divisão"""
n = int(input('numeral : '))
x = int(input("divisor: "))
while(x<=n):
    print(f'{n}/{x} = {n / x}')
    x += 1