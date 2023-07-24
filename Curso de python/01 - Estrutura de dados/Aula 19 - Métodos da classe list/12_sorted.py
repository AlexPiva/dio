linguagens = ['Python', 'JS', 'C', 'Java', 'csharp']

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))