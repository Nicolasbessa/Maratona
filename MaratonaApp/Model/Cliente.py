from model.Pessoa import Pessoa

class Cliente(Pessoa):
    def_init_(self,nome):
    super(Cliente,self)._init_(nome)

    def Pagar(self):
        print("Pagando como cliente")


