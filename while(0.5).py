""""Informar até o último número a imprimir + if (pares e inpares)"""
fim = int(input('Digite o último número a imprimir: '))
x = 0
while (x <= fim):  # variavél <fim> representando o limite da repetição
    if (x % 2 == 0): #Resto de divisão de x por 2 é igual a 0 (famoso par)<modificado> para impar
        print(x)
    x +=1
x = 0
while (x <= fim):
    if (x % 2 == 1):
        print(x)
    x += 1