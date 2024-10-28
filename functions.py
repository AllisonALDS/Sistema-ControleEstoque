class funcoes:

    def __init__(self):
        self.produto = produto
        self.qtd_save = qtd_save
        self.qtd = qtd

    def addProduct(self, produto):
        self.produto = input("Qual produto voce quer adicionar: ")
        product_save = produto
        return product_save

    def addQuantity(self, qtd):
        self.qtd = int(input("Digite a quantidade para adicionar ao Estoque: "))
        qtd_save = 0
        qtd_save = qtd_save + qtd
        return qtd_save
    
    def sell(self):
        
        

        while True:
            print(f"Produto: {self.produto}")
            print(f"Quantidade Atual: {self.qtd_save}")

            sell = int(input("Digite a quatidade para ser vendido: "))
            if sell > self.qtd_save:
                qtd_sell = self.qtd_save - sell
                break
            elif self.qtd_save > sell:
                print("Quantidade Indisponivel")
                continue
        return qtd_sell

    def checkstock(self):

        product_save = self.produto

        print(f"Produto 1: {product_save}" )
        print(f"Quantidade: {self.qtd}" )





