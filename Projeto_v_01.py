from abc import ABCMeta, abstractclassmethod
import copy

#Factory Method
class Veiculo(metaclass=ABCMeta):
  @abstractclassmethod
  def reservar():
    pass

class Carro(Veiculo):
  def __init__(self):
    self.tipo = "Carro"

  def reservar(self):
    print(f"Sua reserva de {self.tipo} foi efetuada com sucesso!!")

class Moto(Veiculo):
  def __init__(self):
    self.tipo = "Moto"

  def reservar(self):
    print(f"Sua reserva de {self.tipo} foi efetuada com sucesso!!")

class Caminhao(Veiculo):
  def __init__(self):
    self.tipo = "Caminhão"

  def reservar(self):
    print(f"Sua reserva de {self.tipo} foi efetuada com sucesso!!")

#Abstract Method
class Cliente():
  @staticmethod
  def GetReserva(tipo):
    if tipo == "Carro":
      return Carro().reservar()
    elif tipo == "Moto":
      return Moto().reservar()
    elif tipo == "Caminhão":
      return Caminhao().reservar()


#Builder
class BuilderLocacao():
    def __init__(self):
        pass

    def SetMarca(self):
        pass

    def SetModelo(self):
        pass

    def SetCliente(self):
        pass

class Locacao(BuilderLocacao):
    def __init__(self):
        self.veiculo = DirectorLocacao()
    
    def SetMarca(self, marca):
        self.veiculo.marca = marca

    def SetModelo(self, modelo):
        self.veiculo.modelo = modelo

    def SetCliente(self, cliente):
        self.veiculo.cliente = cliente

    def PegaTudo(self):
        return self.veiculo.__str__()

class DirectorLocacao():
    def __init__(self, marca = "", modelo = "", cliente = ""):
        self.marca = marca
        self.modelo = modelo
        self.cliente = cliente
    
    def __str__(self):
        print(f'Sr. {self.cliente} o agendamento para o carro de marca {self.marca}, modelo {self.modelo} foi efetuado com sucesso.')

#Singleton
class Reservar():
    def __init__ (self, tipo, pessoa):
        self.tipo = tipo
        self.pessoa = pessoa

    def PegaReserva(self):
        print(f'Sr. {self.pessoa} sua reserva para {self.tipo}, foi efetuada com sucesso.')

    def PegaTipo(self):
        print(f'O veiculo é {self.tipo}')

    def PegarPessoa(self):
        print(f'Sr. {self.nome}')

    def SetNovaReserva(self, novotipo, novapessoa):
        self.tipo = novotipo
        self.pessoa = novapessoa


#Prototype
class Veiculo(metaclass=ABCMeta):
    @abstractclassmethod
    def clonar():
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, cliente):
        self.marca = marca
        self.modelo = modelo
        self.cliente = cliente

    def clonar(self):
        return type(self)(
            self.marca,
            self.modelo,
            self.cliente,
            copy.deepcopy(self.marca),
            copy.deepcopy(self.modelo),
            copy.deepcopy(self.cliente)
        )
    
    def __str__(self):
        return f"Reserva do carro {self.marca} {self.modelo} para o cliente {self.cliente}"

#Observer
class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def Notificar():
        pass

    def NotificarSemana():
        pass

    def NotificarAmanha():
        pass

class Agendamento():
    def __init__(self, tipo_veiculo, pessoa, modelo, marca):
        self.tipo = tipo_veiculo
        self.pessoa = pessoa
        self.modelo = modelo
        self.marca = marca

    def Retornar(self):
        return f"Sr. {self.pessoa}, sua reserva para {self.tipo} de marca {self.marca} e modelo {self.modelo}"

class Notificacao(Observer):
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def Notificar(self):
        print(f"{self.pessoa.Retornar()} deverá ser retirado em breve, fique atento a data")

    def NotificarSemana(self):
        print(f"{self.pessoa.Retornar()} deverá ser retirado na proxima semana.")

    def NotificarAmanha(self):
        print(f"{self.pessoa.Retornar()} deverá ser retirado amanha, estamos te aguardando.")

    def Remover(self):
        print(f'{self.pessoa.Retornar()} foi removido das notificações.')

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome


class Caixa(Funcionario):
    def __init__(self, nome, salario, outro_parametro=None):
        super(Caixa, self).__init__(nome, salario)
        self.__outro_parametro = outro_parametro

    @property
    def outro_parametro(self):
        return self.__outro_parametro


class Manobrista(Funcionario):
    def __init__(self, nome, salario, mais_um_parametro=None):
        super(Manobrista, self).__init__(nome, salario)
        self.__mais_um_parametro = mais_um_parametro

    @property
    def mais_um_parametro(self):
        return self.__mais_um_parametro


class Locadora:
    def __init__(self):
        self.__locacadora = list()

    def add_funcionario(self, Funcionario):
        self.__locacadora.append(Funcionario)

    def total_salarios(self):
        salarios = 0
        for funcionario in self.__locacadora:
            salarios += funcionario.salario
        return salarios


#Builder
a = Locacao()
a.SetMarca("Fiat")
a.SetModelo("Uno")
a.SetCliente("Jorge")
print(a.PegaTudo())

#Singleton
a = Reservar("Carro", "Jorge")
a.PegaReserva()
a.PegaTipo()
a.SetNovaReserva("Caminhao", "Paulo")
a.PegaTipo()
a.PegaReserva()

#Prototype
a = Carro("Fiat", "Uno", "Cleiton")
print(a.__str__())

#Observer
a = Agendamento("Moto", "Jorge", "POP100", "Honda")
b = Notificacao(a)
b.Notificar()
b.NotificarSemana()
b.NotificarAmanha()

#Composite
joao = Manobrista('Joao', 1800)
carla = Caixa('Carla', 1900)

a = Locadora()
a.add_funcionario(joao)
a.add_funcionario(carla)

print(f'Total salários: {a.total_salarios()}')