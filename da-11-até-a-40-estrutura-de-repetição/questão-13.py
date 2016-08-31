#Faça um programa que peça dois números, base e expoente,
base=int(input("informe o valor da base-->"))
expoente=int(input("informe o valor do expoente-->"))
contador=0
cauculador=base
#calcule e mostre o primeiro número elevado ao segundo número.
while(expoente > contador):
    contador=contador+1
    cauculador=base*cauculador
    print(cauculador)
    contador=contador+1
#Não utilize a função de potência da linguagem.
