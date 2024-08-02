# Entrada de dados
nome = str(input("Informe o seu nome: "))
idade = int(input("Informe a sua idade: "))

while True:
    print(f"{"="*30}LISTA DE FILMES{"="*30}")
    print("Sala 1 - Divertidamente. Classificação Livre.") 
    print("Sala 2 - Bad boys. Classificação 16.")
    print("Sala 3 - Velozes e furiosos. Classificação 14.")
    print("Sala 4 - O contador. Classificação 16.")
    print("Sala 5 - O amanhã. Classificação 10")

    # Usuário informa a sala que deseja
    opcao = int(input(f"\n{nome} informe o número da sala: "))
    
    match opcao:
        case 1:
            idade_minima = 0
            filme = "Divertidamente"
        case 2:
            idade_minima = 16
            filme = "Bad boys"
        case 3:
            idade_minima = 14
            filme = "Velozes e furiosos"
        case 4:
            idade_minima = 16
            filme = "O contador"
        case 5:
            idade_minima = 10
            filme =  "O amanhã"
    
    if idade >= idade_minima:
        print(f"{nome} tenha um bom filme!")
        break
    else:
        print(f"{nome} não tem idade suficiente para escolher {filme}.")
        print("Escolha outro filme, por favor!")
        continue