num1=float(input("digite o 1º numero--> "))
num2=float(input("digite o 2º numero--> "))
num3=float(input("digite o 3º numero--> "))
num4=float(input("digite o 4º numero--> "))
num5=float(input("digite o 5º numero--> "))
if (num1 >num2 and num1 > num3 and num1 > num4 and num1  >num5):
	print("o maior numero é o 1º-->", num1)
if (num2 >num1 and num2 > num3 and num2 > num4 and num2  >num5):
	print("o maior numero é o 2º-->", num2)
if (num3 >num2 and num3 > num1 and num3 > num4 and num3  >num5):
	print("o maior numero é o 3º-->", num3)	
elif (num4 >num2 and num4 > num3 and num4 > num1 and num4  >num5):
	print("o maior numero é o 4º-->", num4)	
else:
	print("o maior numero é o 5º-->", num5)