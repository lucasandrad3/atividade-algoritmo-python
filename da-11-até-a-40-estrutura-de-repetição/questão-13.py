base = int(input('informe a base \n'))
expoente = int(input('informe o expoente \n'))
acumulador = 1
for c in range (0,expoente):
  acumulador = base*acumulador
print('resultado =',acumulador)
