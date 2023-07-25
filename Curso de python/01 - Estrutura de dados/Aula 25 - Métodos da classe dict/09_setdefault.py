contatos = {
    'alexandre@gmail.com': {'nome': 'Alexandre', 'telefone': '1111-1111'},
}

print(contatos)
print(contatos.setdefault('nome', 'Cíntia'))
print(contatos)
print(contatos.setdefault('idade', 51))
print(contatos)