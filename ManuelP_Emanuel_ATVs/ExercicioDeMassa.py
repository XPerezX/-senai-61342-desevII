from abc import ABC, abstractmethod


class MassaAbstract(ABC):

    @abstractmethod
    def criar_massa(self):
        pass


class FabricaMacarronada(MassaAbstract):

    def criar_massa(self):
        return "Massa fina e suave "



class FabricaAbelha(MassaAbstract):

    def criar_massa(self):
        return "Massa Grossa "




class ingredienteAbstract(ABC):

    @abstractmethod
    def nome_ingrediente(self):
        pass



class Queijo(ingredienteAbstract):
    def nome_ingrediente(self):
        return "Queijo "


class Tomate(ingredienteAbstract):
    def nome_ingrediente(self):
        return "Tomate "


class Calabresa(ingredienteAbstract):
    def nome_ingrediente(self):
        return "calabresa "


class Frango(ingredienteAbstract):
    def nome_ingrediente(self):
        return "Frango "



class PizzasAbstract(ABC):

    @abstractmethod
    def ingredientes(self):
        pass


class PizzaFrango(PizzasAbstract):


    def ingredientes(self):
        return FabricaMacarronada().criar_massa(), Frango().nome_ingrediente(), Queijo().nome_ingrediente() ,Tomate().nome_ingrediente()


class PizzaCalabresa(PizzasAbstract):

    def ingredientes(self):
        return FabricaAbelha().criar_massa(), Calabresa().nome_ingrediente(), Queijo().nome_ingrediente() ,Tomate().nome_ingrediente()




def codigo_cliente(Pizza):
    Pizza1 = Pizza.ingredientes()
    print(Pizza1)


if __name__ == "__main__":
    print("Por favor, Me veja uma pizza de Calabresa!!!")
    codigo_cliente(PizzaCalabresa())

    print("Por favor, Me veja uma pizza de Frango!!!")
    codigo_cliente(PizzaFrango())

