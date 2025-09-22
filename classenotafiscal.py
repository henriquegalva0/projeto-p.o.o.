from classefornecedor import Fornecedor

class NotaFiscal():

  def __init__(self,codigo,recebimento,valor,tipo,descricao):
    self.__codigo=codigo
    self.__recebimento=recebimento
    self.__valor=valor
    self.__tipo=tipo
    self.__descricao=descricao
    self.__Fornecedor=None

  def bloquear_modificacao(self, nome):
      raise ValueError(f"Não é possível modificar o {nome} do boleto.")

  @property
  def codigo(self):
    return self.__codigo
  @codigo.setter
  def codigo(self, alteracao):
    raise ValueError(self.bloquear_modificacao("código"))

  @property
  def recebimento(self):
    return self.__vencimento
  @recebimento.setter
  def recebimento(self, alteracao):
    raise ValueError(self.bloquear_modificacao("recebimento"))

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

def gerarNotaFiscal(codigo,recebimento,valor,tipo,descricao,user):
  n = NotaFiscal(codigo,recebimento,valor,tipo,descricao)
  user.notas = n
  return n

def removerNota(nota, user):
  user.notas.remove(nota)
