contatos = {
    'alexandre@gmail.com': {'nome': 'Alexandre', 'telefone': '1111-1111'},
}

print(contatos)

copia = contatos.copy()
print(copia)
copia['alexandre@gmail.com'] = {'nome': 'Alex'}
print(copia)