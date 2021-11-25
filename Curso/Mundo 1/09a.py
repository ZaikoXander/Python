# 'Curso em Vídeo Python' = cadeia de texto, cadeia de caractere, string
frase1 = 'Curso em Vídeo Python'
#         012345678912345678912
# fatiamento -- frase[9]
print('FATIAMENTO')
print(frase1[9])
print(frase1[9:13])
print(frase1[9:21])
print(frase1[9:21:2])
print(frase1[:5])
print(frase1[15:])
print(frase1[9::3])
print()
# análise
print('ANÁLISE')
print(len(frase1))
print(frase1.count('o'))
print(frase1.count('o', 0, 13))
print(frase1.find('deo'))
print(frase1.find('Android'))
print('Curso' in frase1)
print()
# transformação
print('TRANSFORMAÇÃO')
print(frase1.replace('Python', 'Android'))
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize())
print(frase1.title())
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print()
# divisão
print('DIVISÃO')
print(frase1.split())
print(frase1.split('o'))
print()
# junção
print('JUNÇÃO')
print('-'.join(frase1.split()))
