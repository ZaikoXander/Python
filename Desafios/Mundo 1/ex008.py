me = float(input('Digite uma distância em metros: '))
print('\n\033[35mA medida de {}m corresponde a {:.0f}cm e {:.0f}mm.\nCorresponde também a {}dam, {}hm e {}km.'
      .format(me, me*100, me*1000, me/10, me/100, me/1000))
