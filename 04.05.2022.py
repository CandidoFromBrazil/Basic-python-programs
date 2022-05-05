"""Alunos x Monitores X Bondinho"""

x = 1
v = 3
total_passageiros = 0
print("Alunos, O bondinho só suporta dez pessoas por viagem")
while x <= 3:
    print(f"O bondinho só irá realizar mais {v} viagens hoje")
    alunos = int(input(f"Quantos Alunos pretendem subir no bondinho na {x}° viagem? "))
    total_passageiros += alunos
    monitor = (input("Um (1) monitor irá acompanhar? "))
    if alunos <= 9 and monitor == "sim":
        total_passageiros += 1
        print("Podem subir a borto!")
    elif alunos > 9:
        print("O bondinho só suporta dez pessoas!")
        print("Tente reorganizar o grupo...")
        break
    elif monitor != "sim":
        print("O bondinho só irá partir se houver um monitor")
        print("Tente reorganizar o grupo...")
        break
    else:
        print("Tente novamente...")
    print(f"Faltam {v-1} viagens para encerrarmos o bondinho por hoje")
    x += 1
    v -= 1
print(f"A soma de pessoas ao término do bondinho foi de: {total_passageiros}")
#programa inspirado em um exemplo de exercício;