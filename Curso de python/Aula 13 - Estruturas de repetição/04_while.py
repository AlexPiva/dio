opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \nDigite sua opção: '))
    if opcao == 1:
        print('Sacando ...')
    elif opcao == 2:
        print('Exibindo extrato ...')
    elif opcao == 0:
        print('Encerrando programa!!!')
    else:
        print('Opção inválida!!!')