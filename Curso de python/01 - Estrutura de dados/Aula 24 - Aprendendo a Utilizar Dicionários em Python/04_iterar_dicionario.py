contatos = {
    'alexandre@gmail.com': {'nome': 'Alexandre', 'telefone': '1111-1111'},
    'cintia@gmail.com': {'nome': 'Cíntia', 'telefone': '2222-2222'},
    'marcelo@gmail.com': {'nome': 'Marcelo', 'telefone': '3333-3333'},
    'luiza@gmail.com': {'nome': 'Luíza', 'telefone': '4444-4444'},
}

for chave in contatos:
    print(chave, contatos[chave])

print()

for chave, valor in contatos.items():
    print(chave, valor)