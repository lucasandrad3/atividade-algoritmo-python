#Altere o programa de cálculo do fatorial, permitindo ao usuário
#calcular o fatorial várias vezes
#e limitando o fatorial a números inteiros positivos e menores que 16.
while 1==1:
    numero=int(input("informe um numero-->"))
    while numero>16 or numero<0:
        numero=int(input("numero incorreto,informe outro numero-->"))
    else:             
        contar_multiplicador = numero 
        while contar_multiplicador>1:
                contar_multiplicador = contar_multiplicador-1
                numero=numero*contar_multiplicador
                print(numero)
