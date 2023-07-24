opcao = int(input('Informe uma opção:\n[1] Sacar \n[2] Extrato\nOpção: '))

if opcao == 1:
    valor = float(input('Digite a quantia para o saque: '))
    # ...
elif opcao == 2:
    print('Exibindo o extrato ... ')
else:
    print('Opção inválida')
