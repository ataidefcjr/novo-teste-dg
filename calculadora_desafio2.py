from calculadora import Calculadora

if __name__ == "__main__":
    print("Testando...")

    calc = Calculadora()
    
    assert calc.calcular_desconto([1518, 1071, 968], "Industrial", "BANDEIRA VERMELHA 2") == (
        1349.86,
        112.49,
        0.12,
        0.90,
    ) 

    assert calc.calcular_desconto([1000, 1054, 1100], "Residencial", "BANDEIRA VERMELHA 1") == (
        1725.61,
        143.8,
        0.18,
        0.90
    )

    assert calc.calcular_desconto([973, 629, 726], "Comercial", "BANDEIRA AMARELA") == (
        1097.6,
        91.47,
        0.16,
        0.90
    )

    assert calc.calcular_desconto([15000, 14000, 16000], "Industrial", "BANDEIRA VERMELHA 1") == (
        21656.81,
        1804.73,
        0.15,
        0.95
    )

    assert calc.calcular_desconto([12000, 11000, 11400], "Residencial", "BANDEIRA VERDE") == (
        22997.8,
        1916.48,
        0.22,
        0.95
    )

    assert calc.calcular_desconto([17500, 16000, 16400], "Comercial", "BANDEIRA AMARELA") == (
        27938.08,
        2328.17,
        0.18,
        0.95
    )

    assert calc.calcular_desconto([30000, 29000, 29500], "Industrial", "BANDEIRA VERMELHA 1") == (
        53262.07,
        4438.51,
        0.18,
        0.99
    )

    assert calc.calcular_desconto([22000, 21000, 21400], "Residencial", "BANDEIRA AMARELA") == (
        52186.84,
        4348.9,
        0.25,
        0.99
    )

    assert calc.calcular_desconto([25500, 23000, 21400], "Comercial", "BANDEIRA VERDE") == (
        48697.35,
        4058.11,
        0.22,
        0.99
    )

    print("Todos os testes passaram!")
    