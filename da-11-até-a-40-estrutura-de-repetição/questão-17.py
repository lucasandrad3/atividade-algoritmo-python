numero=int(input("informe um numero-->"))
contar_multiplicador = numero
while contar_multiplicador>1:
	contar_multiplicador = contar_multiplicador-1
	numero=numero*contar_multiplicador
	print(numero)