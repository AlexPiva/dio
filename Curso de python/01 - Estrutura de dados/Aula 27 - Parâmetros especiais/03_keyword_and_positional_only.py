def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(
    "Pálio",
    1999,
    "ABC-1234",
    marca="Fiat",
    motor="1.0",
    combustivel="Gasolina",
)
