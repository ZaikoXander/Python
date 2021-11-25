from time import sleep
data = input('\033[1;30;107mDigite algo:\033[m ')
print('\033[1;35;107mIDENTIFICANDO PROPRIEDADES...\033[m')
sleep(3)
print('\n\033[1;30;107mÉ string.\033[m')
if data.isnumeric():
    print('\033[1;30;107mÉ numérico.\033[m')
if data.isalpha():
    print('\033[1;30;107mÉ alfabético.\033[m')
if data.isalnum():
    print('\033[1;30;107mÉ alfanumérico.\033[m')
if data.isdigit():
    print('\033[1;30;107mÉ dígito.\033[m')
if data.isdecimal():
    print('\033[1;30;107mÉ decimal.\033[m')
if data.islower():
    print('\033[1;30;107mÉ minúsculo.\033[m')
if data.isspace():
    print('\033[1;30;107mSó tem espaços.\033[m')
if data.isupper():
    print('\033[1;30;107mÉ maiúsculo.\033[m')
if data.istitle():
    print('\033[1;30;107mÉ capitalizado.\033[m')
