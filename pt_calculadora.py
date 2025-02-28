line ="________________________________________"
def operacao():
    print(line)
    print("Escolha uma operação:")
    print("'1' para ADIÇÃO")
    print("'2' para SUBTRAÇÃO")
    print("'3' para MULTIPLICAÇÃO")
    print("'4' para DIVISÃO")

    print(line)

    escolha=input()
    print("Qual o primeiro valor?")
    n1=float(input())
    print(line)

    print("Qual o segundo valor?")
    n2=float(input())
    print(line)
    if escolha=='1':
        resultado = (n1+n2)
        print(f"{n1} + {n2} =")
        print(resultado)
        print(f"O resultado da soma de {int(n1)} e {int(n2)} é {int(resultado)} .")
        input()


    elif escolha=='2':
        resultado = (n1-n2)
        print(f"{n1}-{n2} =")
        print(resultado)
        print(f"O resultado da subtração de {int(n1)}  por {int(n2)} é {int(resultado)} .")
        input()

    elif escolha=='3':
        resultado = (n1*n2)
        print(n1, "*", n2, "=")
        print (resultado)
        print(f"O resultado de {int(n1)} multiplicado por {int(n2)} é {int(resultado)}.")
        input()

    elif escolha=='4':
        if n2 == 0:
            print("Erro! Não é possível dividir por 0.")
        else:
            resultado = (n1 / n2)
            print(n1, "/", n2, "=")
            print(resultado)
            print(f"O resultado de {int(n1)} dividido por {int(n2)} é {int(resultado)}.")
            input()


operacao()
