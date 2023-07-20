inicio = """
     Bem vindo(a) ao Banco Piva!!!
    É sempre uma honra atende-lo(a).
"""
menu = """
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

erro = """
     Valor inválido!!!
    Reinicie a operação.
"""

fim = """

    Obrigado por ser nosso cliente!!!
            Volte sempre!

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(inicio)

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))

        if valor_deposito <= 0:
            print(erro)
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f} - Saldo: R$ {saldo:.2f}\n"

    elif opcao.lower() == "s":
        valor_saque = float(input("Digite o valor do saque: R$ "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print("Limite de saque diário excedido.")

        elif excedeu_limite:
            print(f"Valor máximo de R$ {limite:.2f} por saque excedido.")

        elif excedeu_saldo:
            print('Não há saldo sificiente na conta para este valor!')

        elif valor_saque > 0:
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f} - Saldo: R$ {saldo:.2f}\n"

        else:
            print(erro)

    elif opcao.lower() == "e":
        print(' EXTRATO '.center(40, '$') + '\n')
        print('Não foram realizadas movimentações.\n'.center(40) if not extrato else extrato)
        print(''.center(40, '$') + '\n')

    elif opcao.lower() == "q":
        break

    else:
        print("Opção inválida!")

print(fim)
