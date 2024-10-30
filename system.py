qtd_atual = 0
    
while True:
    print("Bem vindo ao Sistema de Estoque!")
    print(" \n [1] - Adicionar \n [2] - Vender \n [3] - Verificar estoque \n [4] - Sair \n ")
    op = int(input("Escolha sua opção: "))

    if op == 1:
        qtd = int(input("Quantas unidades adicionar: "))
        qtd_atual = qtd_atual + qtd
        print(f"Quantidade atual: {qtd_atual}")
    elif op == 2:
        print(f"Quantidade Atual: {qtd_atual}")
        qtd_sell = int(input("Quantas unidades voce quer vender: "))
        if qtd_atual >= qtd_sell:
            qtd_atual = qtd_atual - qtd_sell
            print(f"Vendido! Quantidade atual: {qtd_atual}")
        else:
            print(f"Quantidade Indisponivel")
            continue
    elif op == 3:
        print(f"Quantidade do Estoque atual: {qtd_atual}")
    elif op == 4:
        print("Voce saiu do Sistema de Estoque !")
        break