import this
this.precoHamburgao = 5
this.quantHamburgao = 10
this.quantidade = 0
def Preco ():
    print('O preco do Hamburgão é: R$' + str(this.precoHamburgao) + ',00.')

def Quantidade ():
    print('A quantidade disponível desse lanche é: ' + str(this.quantHamburgao) + '.')

def Selecao ():
    print('Digite a quantidade que deseja comprar: ')
    this.quantidade = int(input())
    while (this.quantidade < 0) or (this.quantidade > this.quantHamburgao):
        if (this.quantidade < 0) or (this.quantidade > this.quantHamburgao):
            print('Informe uma quantidade acessível à disponível, por favor!')
            this.quantidade = int(input())
    this.quantHamburgao = this.quantHamburgao - this.quantidade

def Calculo():
    return this.quantidade * this.precoHamburgao

def Compra ():
    Preco()
    Quantidade()
    Selecao()
    print('O valor total da compra é: '+ str(Calculo()) +',00.')