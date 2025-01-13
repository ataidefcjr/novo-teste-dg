def calculadora(consumo: list, tarifa: float, classe: str) -> tuple:
    """
    retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """

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

    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura, 2),
    )


if __name__ == "__main__":
    print("Testando...")

    assert calculadora([1518, 1071, 968], 0.878460, "Industrial") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    )  # BANDEIRA VERMELHA 2

    assert calculadora([1000, 1054, 1100], 0.84432, "Residencial") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )  # BANDEIRA VERMELHA 1

    assert calculadora([973, 629, 726], 0.818540, "Comercial") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )  # BANDEIRA AMARELA

    assert calculadora([15000, 14000, 16000], 0.844320, "Industrial") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )  # BANDEIRA VERMELHA 1

    assert calculadora([12000, 11000, 11400], 0.79969, "Residencial") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )  # BANDEIRA VERDE

    assert calculadora([17500, 16000, 16400], 0.818540, "Comercial") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )  # BANDEIRA AMARELA

    assert calculadora([30000, 29000, 29500], 0.844320, "Industrial") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )  # BANDEIRA VERMELHA 1

    assert calculadora([22000, 21000, 21400], 0.81854, "Residencial") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )  # BANDEIRA AMARELA

    assert calculadora([25500, 23000, 21400], 0.799669, "Comercial") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )  # BANDEIRA VERDE

    print("Todos os testes passaram!")
    