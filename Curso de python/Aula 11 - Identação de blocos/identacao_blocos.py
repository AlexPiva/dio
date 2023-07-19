
def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print(f"Foram sacados R${valor:.2f}")
        saldo -= valor
    else:
        print('Saldo insuficiente para este valor')
    
    print(f'Seu saldo atual é de R${saldo:.2f}')


sacar(100)
sacar(600)