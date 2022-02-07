import math
angulo = float(input('Digit p ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O Angulo {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O Angulo de {} te a TANGENTE de {:.2f}'.format(angulo,tangente))