# if simples
saldo = 2000.0
saque = float(input('Informe o valor do saque: '))
if saldo >= saque:
    print('Saque realizado com sucesso!')

if saldo < saque:
    print('Saldo insuficiente!')