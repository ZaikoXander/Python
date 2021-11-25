real = float(input('\033[1;95;40mDigite quantos reais você tem na carteira: \033[93mR$'))
print('\033[94mCom \033[93mR${:.2f}\033[94m é possível comprar \033[93mUS${:.2f}\033[94m!\033[49m\n\033[94;40mTambém é '
      'possível comprar \033[93m€{:.2f}\033[94m e \033[93m¥{:.2f}\033[94m e \033[93m{:.8f} Bitcoins\033[94m!\033[m'
      .format(real, real / 5.44, real / 6.61, real / 0.052, real / 263147.69))
