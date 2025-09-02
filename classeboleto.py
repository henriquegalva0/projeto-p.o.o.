from datetime import datetime,date
from random import randint
from classefornecedor import Fornecedor

class Boleto():

  def __init__(self,status,codigo,vencimento,valor,tipo,descricao):
    self.__status=status
    self.__codigo=codigo
    self.__vencimento=vencimento
    self.__valor=valor
    self.__tipo=tipo
    self.__descricao=descricao
    self.__Fornecedor=None

  def bloquear_modificacao(self, nome):
      raise ValueError(f"Não é possível modificar o {nome} do boleto.")

  @property
  def status(self):
    return self.__status
  @status.setter
  def status(self, alteracao):
    raise ValueError(self.bloquear_modificacao("status"))

  @property
  def codigo(self):
    return self.__codigo
  @codigo.setter
  def codigo(self, alteracao):
    raise ValueError(self.bloquear_modificacao("código"))

  @property
  def vencimento(self):
    return self.__vencimento
  @vencimento.setter
  def vencimento(self, alteracao):
    raise ValueError(self.bloquear_modificacao("vencimento"))

  @property
  def valor(self):
    return self.__valor
  @valor.setter
  def valor(self, alteracao):
    raise ValueError(self.bloquear_modificacao("valor"))

  @property
  def tipo(self):
    return self.__tipo
  @tipo.setter
  def tipo(self, alteracao):
    raise ValueError(self.bloquear_modificacao("tipo"))

  @property
  def descricao(self):
    return self.__descricao
  @descricao.setter
  def descricao(self, alteracao):
    raise ValueError(self.bloquear_modificacao("descricao"))

  @property
  def Fornecedor(self):
    return self.__Fornecedor
  @Fornecedor.setter
  def Fornecedor(self, autor):
    self.__Fornecedor = Fornecedor
    
  def atualizarStatus(self):
    if datetime.combine(self.__vencimento, datetime.min.time()) >= datetime.now():
      self.__status="A vencer"
    else:
      self.__status="Vencido"

  def calcularDataVencimento(self):
    distanciaData=str(datetime.now()-datetime.combine(self.vencimento, datetime.min.time()))
    if len(distanciaData.split(","))>1:
      distanciaData=distanciaData.split(",")[0]
      distanciaData=distanciaData.replace(' ','').replace('days','').replace('day','')
      inteiroDias=int(distanciaData)
      if inteiroDias<0:
        return f"{inteiroDias*(-1)} dia(s) até que o boleto expire."
      else:
        return f"{inteiroDias} dia(s) desde que o boleto expirou."
    else:
      return "O boleto expirou hoje."

  def exibirBoleto(self):
    self.atualizarStatus()
    return print(f"""
      Status: {self.__status}
      Código: {self.__codigo}
      Vencimento: {str(self.__vencimento),self.calcularDataVencimento()}
      Valor: R${self.__valor:.2f}
      Tipo: {self.__tipo}
      Descricao: {self.__descricao}
      Fornecedor: {self.Fornecedor.nome}
      """)

BoletoTeste = Boleto(
    None,
    1234567890,
    datetime.now(),
    1234.56,
    "tipo",
    "descricao"
    )
BoletoTeste.Fornecedor=Fornecedor("nome","cnpj","endereco","contato")

BoletoTeste.exibirBoleto()
