linguagens = ['Python', 'JS', 'C', 'Java', 'csharp']
linguagens.sort()
print(linguagens)

linguagens = ['Python', 'JS', 'C', 'Java', 'csharp']
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ['Python', 'JS', 'C', 'Java', 'csharp']
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ['Python', 'JS', 'C', 'Java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
