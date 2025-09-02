class Fornecedor():
    def __init__(self,nome,cnpj,endereco,contato):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__endereco = endereco
        self.__contato = contato
    
    @property             
    def nome(self):
        return self.__nome

    @nome.setter     
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cpnj(self, cnpj):
        self.__cnpj = cnpj
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        self.__contato = contato
