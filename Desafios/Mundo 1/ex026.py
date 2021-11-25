frase = str(input('\033[1;95;40mDigite uma frase:\033[49m\n')).upper().strip()
frase = frase.replace('Ã', 'A').replace('Â', 'A').replace('À', 'A').replace('Á', 'A').replace('Ä', 'A')
contagem = frase.count('A') + frase.count('Ã') + frase.count('Â')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1
print('\033[49m\n\033[94;40mA letra A aparece \033[31m{}\033[94m vezes.\033[49m\n\033[40mA letra A aparece '
      'primeiramente no \033[31m{}º\033[94m caractere.\033[49m\n\033[40mE aparece pela última vez no '
      '\033[31m{}º\033[94m caractere.\033[49m'.format(contagem, primeira, ultima))
