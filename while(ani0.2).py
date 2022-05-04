""""Gerador de tabuadas, com: multi, div, soma e sub"""
menu = input('Escolha: multiplicar, dividir, somar, subtrair e (0) - para sair do gerador de tabuadas: ')
if menu == '0':
    print('Exit')
elif menu == 'multiplicar':
    tabuada_multi = 1
    while tabuada_multi <= 10:
        numeromulti = 1
        while numeromulti <= 10:
            print(f'{tabuada_multi} X {numeromulti} = {tabuada_multi * numeromulti}')
            numeromulti += 1
        tabuada_multi += 1
elif menu == 'dividir':
    tabuada_div = 1
    while tabuada_div <= 10:
        numerodiv = 1
        while numerodiv <= 10:
            print(f'{tabuada_div} // {numerodiv} = {tabuada_div // numerodiv}')
            numerodiv += 1
        tabuada_div += 1
elif menu == 'somar':
    tabuada_soma = 1
    while tabuada_soma <= 10:
        numerosoma = 1
        while numerosoma <= 10:
            print(f'{tabuada_soma} + {numerosoma} = {tabuada_soma + numerosoma}')
            numerosoma += 1
        tabuada_soma += 1
elif menu == 'subtrair':
    tabuada_sub = 1
    while tabuada_sub <= 10:
        numerosub = 1
        while numerosub <= 10:
            print(f'{tabuada_sub} - {numerosub} = {tabuada_sub - numerosub}')
            numerosub += 1
        tabuada_sub += 1