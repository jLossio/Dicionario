cadastro = {}
while True:
    nome = input("Digite o nome completo: ")
    if nome == '':
        break

    idade = int(input('Digite a idade: '))
    cidade = input('Digite a cidade: ')

    #adiciona os dados ao dicionáio 
    cadastro[nome] = {"idade": idade, "cidade": cidade}

    #imprime o cadastro completo
    print('Cadatro:')
    print(cadastro)
    for nome, dados in cadastro.items():
        print("- Nome:", nome)
        print(" Idade:", dados["idade"])
        print(" Cidade:", dados["cidade"])