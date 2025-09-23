from classenotafiscal import NotaFiscal
from classeboleto import Boleto

class Usuario:
    def __init__(self, nome, email, senha, telefone, endereco):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone
        self.__endereco = endereco
        self.__cpf = None
        self.__cnpj = None
        self.__boletos = []
        self.__notas = []

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj
        
    @property
    def boletos(self):
        return self.__boletos
    @boletos.setter
    def boletos(self, boleto):
        self.__boletos.append(boleto)

    @property
    def notas(self):
      return self.__notas
    @notas.setter
    def notas(self, nota):
        self.__notas.append(nota)
