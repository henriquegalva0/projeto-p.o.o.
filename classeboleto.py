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
  def Fornecedor(self, Fornecedor):
    self.__Fornecedor = Fornecedor

#from classeusuario import Usuario

#def gerarBoleto(status,codigo,vencimento,valor,tipo,descricao,user):
#  b = Boleto(status,codigo,vencimento,valor,tipo,descricao)
#  user.boletos = b
#  return b

#def removerBoleto(boleto, user):
#  user.boletos.remove(boleto)
