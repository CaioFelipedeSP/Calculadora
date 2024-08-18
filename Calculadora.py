#Calculadora
while True:
    Conta = str("Esta é uma calculadora, escolha seus números. ")
    print(Conta)
    #Números
    primeiro_numero = int(input("Primeiro número: "))
    segundo_numero = int(input("Segundo número: "))

    #Sexo
    Genero = "F, M"
    Sexo = input("Qual o seu sexo? ")

    #Operação

    Operacao = input("Escolha uma operação para sua conta: ")

    if Operacao == "+":
        print("Resultado:", primeiro_numero + segundo_numero)
    elif Operacao == "*":
        print("Resultado:", primeiro_numero * segundo_numero)
    elif Operacao == "-":
        print("Resultado:", primeiro_numero - segundo_numero)
    elif Operacao == "/":
        print("Resultado:", primeiro_numero / segundo_numero)

    #Loop

    Repetir = input("Deseja fazer outra conta? ")
    if Repetir.lower() != "sim":
        break

