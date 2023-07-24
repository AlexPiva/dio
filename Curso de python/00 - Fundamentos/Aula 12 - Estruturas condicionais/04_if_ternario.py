saldo, saque = 1000, 1500
status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} ao realizar o saque!')