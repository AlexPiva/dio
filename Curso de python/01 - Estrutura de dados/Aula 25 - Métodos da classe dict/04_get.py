contatos = {
    'alexandre@gmail.com': {'nome': 'Alexandre', 'telefone': '1111-1111'},
}

#print(contatos['chave']) # keyErros: 'chave'

print(contatos.get('chave'))
print(contatos.get('chave', {}))
print(contatos.get('alexandre@gmail.com', {}))

