larg = float(input('\033[95;40mDigite a largura de sua parede em metros: '))
alt = float(input('Digite a altura de sua parede em metros: '))
print('\033[91mSua parede tem uma dimensão de {}x{} e sua área é {:.2f}m².\033[49m\n\033[40mÉ necessário {:.4f}l de '
      'tinta para pintá-la.\033[m'.format(larg, alt, larg * alt, larg * alt / 2))
