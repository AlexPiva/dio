import textwrap


def inicio():
    print(
        """
     Bem vindo(a) ao Banco Piva!!!
    É sempre uma honra atendê-lo(a).
    """
    )


def erro():
    print(
        """
            Valor inválido!!!
           Reinicie a operação.
        """
    )


def fim():
    print(
        """
                Obrigado por ser nosso cliente!!!
                          Volte sempre!
        """
    )


def menu():
    menu = """
        Digite a opção desejada:

        [1]\tNovo cliente
        [2]\tNova conta
        [3]\tListar contas
        [4]\tSacar
        [5]\tDepositar
        [6]\tExtrato
        [7]\tSair

        => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("$$$ Depósito realizado com sucesso! $$$")
    else:
        print("!!! Operação falhou. Valor inválido !!!")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Não há saldo suficiente na conta para este valor!")

    elif excedeu_limite:
        print(f"Valor máximo de R$ {limite:.2f} por saque excedido.")

    elif excedeu_saques:
        print("Limite de saque diário excedido.")

    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque:\tR$\t{valor:.2f}\n"
        print("$$$ Saque realizado com sucesso $$$")

    else:
        erro()

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(40, "$") + "\n")
    print(
        "Não foram realizadas movimentações.\n".center(40) if not extrato else extrato
    )
    print(f"Saldo:\tR$\t{saldo:.2f}\n")
    print("".center(40, "$") + "\n")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números):")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("!!! Já existe um cliente com este CPF !!!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade:")
    estado = input("Estado: ")
    endereco = ""
    endereco += f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    clientes.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("=== Cliente criado com sucesso ===")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("+++ Conta driada com sucesso +++")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("!!! Cliente não foi encontrado, fluxo de criação de conta encerrado !!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    inicio()

    while True:
        opcao = menu()

        if opcao == "1":
            criar_cliente(clientes)

        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

        if conta:
            contas.append(conta)

        elif opcao == "3":
            listar_contas(contas)

        elif opcao == "4":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "5":
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "7":
            break

        else:
            erro()

    fim()


main()
