from datetime import date

from usuario import Usuario
from fornecedor import Fornecedor
from boleto import Boleto, gerarBoleto
from nota_fiscal import NotaFiscal, gerarNotaFiscal

class OCR:
    def __init__(self):
        pass

    def extrairDados(self, imagem_documento, tipo_documento, usuario):
        if tipo_documento.lower() == 'boleto':
            dados_extraidos = {
                "codigo": "00190.50095 40144.816069 06809.350314 1 98720000012345",
                "vencimento": date(2025, 10, 20),
                "valor": 123.45,
                "tipo": "Tipo de Boleto Exemplo",
                "descricao": "Descrição de Exemplo para Boleto",
                "cnpj_fornecedor": "XX.XXX.XXX/0001-XX",
                "nome_fornecedor": "Fornecedor Exemplo Ltda"
            }
            novo_boleto = gerarBoleto(
                status=None,
                codigo=dados_extraidos["codigo"],
                vencimento=dados_extraidos["vencimento"],
                valor=dados_extraidos["valor"],
                tipo=dados_extraidos["tipo"],
                descricao=dados_extraidos["descricao"],
                user=usuario
            )
            fornecedor_boleto = Fornecedor(
                nome=dados_extraidos["nome_fornecedor"],
                cnpj=dados_extraidos["cnpj_fornecedor"],
                endereco="Endereço de Exemplo",
                contato="Contato de Exemplo"
            )
            novo_boleto.Fornecedor = fornecedor_boleto
            return novo_boleto

        elif tipo_documento.lower() == 'nota fiscal':
            dados_extraidos = {
                "codigo": "000.000.123-EX",
                "recebimento": date.today(),
                "valor": 987.65,
                "tipo": "Tipo de Serviço Exemplo",
                "descricao": "Descrição de Exemplo para Nota Fiscal",
                "cnpj_fornecedor": "YY.YYY.YYY/0001-YY",
                "nome_fornecedor": "Empresa de Serviços Exemplo S.A."
            }
            nova_nota = gerarNotaFiscal(
                codigo=dados_extraidos["codigo"],
                recebimento=dados_extraidos["recebimento"],
                valor=dados_extraidos["valor"],
                tipo=dados_extraidos["tipo"],
                descricao=dados_extraidos["descricao"],
                user=usuario
            )
            fornecedor_nota = Fornecedor(
                nome=dados_extraidos["nome_fornecedor"],
                cnpj=dados_extraidos["cnpj_fornecedor"],
                endereco="Endereço de Exemplo",
                contato="Contato de Exemplo"
            )
            nova_nota.Fornecedor = fornecedor_nota
            return nova_nota
        else:
            return None
