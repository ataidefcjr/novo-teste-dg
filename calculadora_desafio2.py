def calculadora(consumo: list, classe: str) -> tuple:
    """
    retorna uma tupla de floats contendo economia anual, economia mensal, desconto aplicado e cobertura.
    """
    economia_anual = 0
    economia_mensal = 0
    desconto_aplicado = 0
    cobertura = 0

    # Desenvolva seu código aqui #

    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura, 2),
    )


if __name__ == "__main__":
    print("Testando...")

    assert calculadora([1518, 1071, 968], "Industrial") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    )  # BANDEIRA VERMELHA 2

    assert calculadora([1000, 1054, 1100], "Residencial") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )  # BANDEIRA VERMELHA 1

    assert calculadora([973, 629, 726], "Comercial") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )  # BANDEIRA AMARELA

    assert calculadora([15000, 14000, 16000], "Industrial") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )  # BANDEIRA VERMELHA 1

    assert calculadora([12000, 11000, 11400], "Residencial") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )  # BANDEIRA VERDE

    assert calculadora([17500, 16000, 16400], "Comercial") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )  # BANDEIRA AMARELA

    assert calculadora([30000, 29000, 29500], "Industrial") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )  # BANDEIRA VERMELHA 1

    assert calculadora([22000, 21000, 21400], "Residencial") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )  # BANDEIRA AMARELA

    assert calculadora([25500, 23000, 21400], "Comercial") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )  # BANDEIRA VERDE

    print("Todos os testes passaram!")
    