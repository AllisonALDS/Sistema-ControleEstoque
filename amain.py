from functions import funcoes as fc

class SistemaControle:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print('\n'
                '[1] - Adicionar  \n'
                '[2] - Vender  \n'
                '[3] - Verificar estoque \n'
                '[4] - Sair  \n'
                '\n')
            op = int(input("Escolha uma opção: "))
            if op == 1:
                fc.addProduct(self)
                fc.addQuantity(self)
            elif op == 2:
                fc.sell(self)
            elif op == 3:
                fc.checkstock(self, )
                

SistemaControle()