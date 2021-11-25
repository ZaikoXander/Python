# Cores no Terminal

#     ANSI
# escape sequence
# \033[(style);(text);(back)m
# print('\033[0;33;44m Bom dia!')

# style
#
# 0 - Reset_All
# 1 - Bold
# 2 - Thin
# 3 - Italic
# 4 - Underline
# 7 - Negative
# 9 - Strikethrough
# 22 - None

# text
#
# 30 - Preto
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Magenta
# 36 - Ciano
# 37 - Cinza
# 39 - None
# 90 - Cinza escuro
# 91 - Vermelho claro
# 92 - Verde claro
# 93 - Amarelo claro
# 94 - Azul claro
# 95 - Magenta claro
# 96 - Ciano claro
# 97 - Branco

# back
#
# 40 - Preto
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Magenta
# 46 - Ciano
# 47 - Cinza
# 49 - None
# 100 - Cinza escuro
# 101 - Vermelho claro
# 102 - Verde claro
# 103 - Amarelo claro
# 104 - Azul claro
# 105 - Magenta claro
# 106 - Ciano claro
# 107 - Branco

print('\033[97;41mTeste')
print('\033[0;4;33;44mTeste')
print('\033[0;1;35;43mTeste')
print('\033[0;97;42mTeste')
print('\033[0;97;40mTeste')
print('\033[7mTeste')
