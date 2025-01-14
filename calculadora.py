import requests
from bs4 import BeautifulSoup

class CalculadoraDeTarifas:
    """
    Uma calculadora para calcular descontos na conta de luz.
    """
    
    # Faixa de Consumo : Porcentagem
    # 1 = até 10.000kWh
    # 2 = 10.000 a 20.000kWh
    # 3 = Acima de 20.000kWh
    descontos = {
        'Residencial': {
            1 : .18, 
            2 : .22, 
            3 : .25  
        },
        'Comercial': {
            1 : .16,  
            2 : .18,  
            3 : .22 
        },
        'Industrial': {
            1 : .12, 
            2 : .15, 
            3 : .18 
        }
    }

    coberturas = {
        1 : .9, 
        2 : .95, 
        3 : .99 
    }

    tarifas = {}

    @classmethod
    def atualizar_tarifas(cls):
        """
        Atualiza o dicionário tarifas com as tarifas mais recentes buscadas no site da Cemig.
        """
        try:
            url = 'https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/'
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição para obter os dados da página: {e}")

        soup = BeautifulSoup(response.content,'html.parser')
        tabela_residencial = soup.find('table', attrs={'class':'table table-bordered'})
        linhas_residencial = tabela_residencial.find_all('td')
        tarifas_residencial = [linha.text.strip().replace('\n', '').replace(',', '.') for linha in linhas_residencial][1:]

        tabela_outros = soup.find_all('table', attrs={'class':'table table-bordered'})
        for tabela in tabela_outros:
            if "B3 - DEMAIS CLASSES" in tabela.text:
                tabela_outros = tabela
                break
        linha_outros = tabela_outros.find_all('td')
        tarifas_outros = [linha.text.strip().replace('\n', '').replace(',', '.') for linha in linha_outros][1:]

        cls.tarifas = {
            'Residencial' : {
                'BANDEIRA VERDE':float(tarifas_residencial[0]),
                'BANDEIRA AMARELA':float(tarifas_residencial[1]),
                'BANDEIRA VERMELHA 1':float(tarifas_residencial[2]),
                'BANDEIRA VERMELHA 2':float(tarifas_residencial[3])
            },
            'Comercial' : {
                'BANDEIRA VERDE':float(tarifas_outros[0]),
                'BANDEIRA AMARELA':float(tarifas_outros[1]),
                'BANDEIRA VERMELHA 1':float(tarifas_outros[2]),
                'BANDEIRA VERMELHA 2':float(tarifas_outros[3])
            },
            'Industrial' : {
                'BANDEIRA VERDE':float(tarifas_outros[0]),
                'BANDEIRA AMARELA':float(tarifas_outros[1]),
                'BANDEIRA VERMELHA 1':float(tarifas_outros[2]),
                'BANDEIRA VERMELHA 2':float(tarifas_outros[3])
            }
        } 

    def __init__(self):
        self.atualizar_tarifas()

    @classmethod
    def calcular_desconto(cls, consumo: list, classe: str, bandeira: str) -> tuple:
        """
        Retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
        """
        
        # Verifica as tarifas foram criadas
        if not cls.tarifas:
            cls.atualizar_tarifas()

        media = sum(consumo) / len(consumo)

        # Definição da Faixa de Consumo
        if media < 10000:
            faixa_consumo = 1
        elif 10000 <= media <= 20000:
            faixa_consumo = 2
        else:
            faixa_consumo = 3

        tarifa = cls.tarifas[classe][bandeira]
        cobertura = cls.coberturas[faixa_consumo]
        desconto_aplicado = cls.descontos[classe][faixa_consumo]
        economia_mensal = tarifa * media * desconto_aplicado * cobertura
        economia_anual = (economia_mensal * 12)

        # print(f"Economial Mensal Estimada: R${economia_mensal:.2f}")
        # print(f"Economial Anual Estimada: R${economia_anual:.2f}")
        # print()

        return (
            round(economia_anual, 2),
            round(economia_mensal, 2),
            round(desconto_aplicado, 2),
            round(cobertura, 2),
        )
