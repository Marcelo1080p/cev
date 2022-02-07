medida = float(input('Coloque uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida /1000
he = medida / 100
de = medida / 10
deci = medida * 10
print('A medida de {} M corresponde a {}Cm \n e {}Mm, {}Km, \n {} Hectômetro, {} Decâmetros \n {} Decímetro'. format(medida, cm, mm, km, he, de, deci))