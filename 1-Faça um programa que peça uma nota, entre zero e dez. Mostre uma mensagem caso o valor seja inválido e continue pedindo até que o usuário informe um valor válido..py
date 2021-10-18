
nota=float(input("informe um numero de 0 a 10: "))
while (nota>10) or (nota<0):
	nota=float(input("informe um numero de 0 a 10: "))

#sugestao
nota = int(input('Digite uma nota entre 0 e 10 '))

while (nota > 0) and (nota < 10): 
    nota = int(input('Digite uma nota entre 0 e 10: ')) 
else:
    print('Valor inválido')
    exit()
