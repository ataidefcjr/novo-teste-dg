import requests
from bs4 import BeautifulSoup

def buscar_tarifa(bandeira: str, classe: str):
    """
    Retorna a tarifa de acordo com a bandeira.
    Parâmetros:
    bandeira (str): Nome da bandeira ('BANDEIRA VERDE', 'BANDEIRA AMARELA', 
                     'BANDEIRA VERMELHA 1', 'BANDEIRA VERMELHA 2')
    classe (str): Nome da classe ('Residencial', 'Comercial', 'Industrial')
    
    Retorno:
    float: O valor da tarifa correspondente à bandeira solicitada.
    """
    try:
        url = 'https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/'
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição para obter os dados da página: {e}")

    classes = {
        'Residencial' : 'B1- RESIDENCIAL NORMAL',
        'Comercial' : 'B3 - DEMAIS CLASSES',
        'Industrial' : 'B3 - DEMAIS CLASSES',
    }
    
    soup = BeautifulSoup(response.content,'html.parser')
    tabelas = soup.find_all('table', attrs={'class':'table table-bordered'})
    tarifas = []
    for tabela in tabelas:
        cabecalhos = tabela.find_all('th')
        for cabecalho in cabecalhos:
            if classes[classe] in cabecalho.text:
                linhas = tabela.find_all('td')
                tarifas = [linha.text.strip().replace('\n', '').replace(',', '.') for linha in linhas][1:]

    bandeiras = {
        'BANDEIRA VERDE': tarifas[0],
        'BANDEIRA AMARELA': tarifas[1],
        'BANDEIRA VERMELHA 1': tarifas[2],
        'BANDEIRA VERMELHA 2': tarifas[3],
    }
    
    return float(bandeiras[bandeira])

def calculadora(consumo: list, classe: str, bandeira: str) -> tuple:
    """
    Retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """
    tarifa = buscar_tarifa(bandeira,classe)

    descontos = {
        'Residencial': {
            '< 10.000 kWh' : .18,
            '>= 10.000 kWh e <= 20.000 kWh' : .22,
            '> 20.000 kWh' : .25
        },
        'Comercial': {
            '< 10.000 kWh' : .16,
            '>= 10.000 kWh e <= 20.000 kWh' : .18,
            '> 20.000 kWh' : .22
        },
        'Industrial': {
            '< 10.000 kWh' : .12,
            '>= 10.000 kWh e <= 20.000 kWh' : .15,
            '> 20.000 kWh' : .18
        }
    }

    coberturas = {
        '< 10.000 kWh' : .9,
        '>= 10.000 kWh e <= 20.000 kWh' : .95,
        '> 20.000 kWh' : .99
    }

    media = sum(consumo) / len(consumo)

    if media < 10000:
        faixa_consumo = '< 10.000 kWh'
    elif 10000 <= media <= 20000:
        faixa_consumo = '>= 10.000 kWh e <= 20.000 kWh'
    else:
        faixa_consumo = '> 20.000 kWh'

    cobertura = coberturas[faixa_consumo]
    desconto_aplicado = descontos[classe][faixa_consumo]
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

    assert calculadora([1518, 1071, 968], "Industrial", "BANDEIRA VERMELHA 2") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    ) 

    assert calculadora([1000, 1054, 1100], "Residencial", "BANDEIRA VERMELHA 1") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )

    assert calculadora([973, 629, 726], "Comercial", "BANDEIRA AMARELA") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )

    assert calculadora([15000, 14000, 16000], "Industrial", "BANDEIRA VERMELHA 1") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )

    assert calculadora([12000, 11000, 11400], "Residencial", "BANDEIRA VERDE") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )

    assert calculadora([17500, 16000, 16400], "Comercial", "BANDEIRA AMARELA") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )

    assert calculadora([30000, 29000, 29500], "Industrial", "BANDEIRA VERMELHA 1") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )

    assert calculadora([22000, 21000, 21400], "Residencial", "BANDEIRA AMARELA") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )

    assert calculadora([25500, 23000, 21400], "Comercial", "BANDEIRA VERDE") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )

    print("Todos os testes passaram!")
    