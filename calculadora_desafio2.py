import requests
from bs4 import BeautifulSoup

class CalculadoraDeTarifas:

    descontos = {
        'Residencial': {
            1 : .18, #Até 10.000kWh
            2 : .22, #10.000 a 20.000kWh
            3 : .25  #Acima de 20.000kWh
        },
        'Comercial': {
            1 : .16,  #Até 10.000kWh
            2 : .18,  #10.000 a 20.000kWh
            3 : .22 #Acima de 20.000kWh
        },
        'Industrial': {
            1 : .12, #Até 10.000kWh
            2 : .15, #10.000 a 20.000kWh
            3 : .18 #Acima de 20.000kWh
        }
    }

    coberturas = {
        1 : .9, #Até 10.000kWh
        2 : .95, #10.000 a 20.000kWh
        3 : .99 #Acima de 20.000kWh
    }

    tarifas = {}

    @classmethod
    def buscar_tarifa(cls):
        """
        Atualiza as tarifas.
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
        self.buscar_tarifa()

    @classmethod
    def calcular_desconto(cls, consumo: list, classe: str, bandeira: str) -> tuple:
        """
        Retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
        """
        # Caso não seja criado uma instancia.
        if not cls.tarifas:
            cls.buscar_tarifa()

        media = sum(consumo) / len(consumo)

        if media < 10000:
            faixa_consumo = 1
        elif 10000 <= media <= 20000:
            faixa_consumo = 2
        else:
            faixa_consumo = 3

        tarifa = cls.tarifas[classe][bandeira]
        cobertura = cls.coberturas[faixa_consumo]
        desconto_aplicado = cls.descontos[classe][faixa_consumo]
        economia_mensal = ((tarifa * media) * desconto_aplicado) * cobertura
        economia_anual = (economia_mensal * 12)

        # Desenvolva seu código aqui #

        return (
            round(economia_anual, 2),
            round(economia_mensal, 2),
            round(desconto_aplicado, 2),
            round(cobertura, 2),
        )


if __name__ == "__main__":
    print("Testando...")

    Calculadora = CalculadoraDeTarifas()
    
    assert Calculadora.calcular_desconto([1518, 1071, 968], "Industrial", "BANDEIRA VERMELHA 2") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    ) 

    assert Calculadora.calcular_desconto([1000, 1054, 1100], "Residencial", "BANDEIRA VERMELHA 1") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )

    assert Calculadora.calcular_desconto([973, 629, 726], "Comercial", "BANDEIRA AMARELA") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )

    assert Calculadora.calcular_desconto([15000, 14000, 16000], "Industrial", "BANDEIRA VERMELHA 1") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )

    assert Calculadora.calcular_desconto([12000, 11000, 11400], "Residencial", "BANDEIRA VERDE") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )

    assert Calculadora.calcular_desconto([17500, 16000, 16400], "Comercial", "BANDEIRA AMARELA") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )

    assert Calculadora.calcular_desconto([30000, 29000, 29500], "Industrial", "BANDEIRA VERMELHA 1") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )

    assert Calculadora.calcular_desconto([22000, 21000, 21400], "Residencial", "BANDEIRA AMARELA") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )

    assert Calculadora.calcular_desconto([25500, 23000, 21400], "Comercial", "BANDEIRA VERDE") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )

    print("Todos os testes passaram!")
    