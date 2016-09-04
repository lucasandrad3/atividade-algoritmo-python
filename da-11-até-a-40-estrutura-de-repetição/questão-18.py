#Faça um programa que, dado um conjunto de N números,
#determine o menor valor, o maior valor e a soma dos valores. 
Quantidade=int(input("indique a quantidade de números que deseja  --> "))
valor = int(input("-digite um numero--> "))
maior=valor
menor=valor
soma=valor
contador=0
while contador< Quantidade-1:
    valor = int(input("-digite outro numero--> "))
    soma=valor+soma
    contador=contador+1
    if valor > maior:
        maior=valor
    elif valor < menor:
        menor=valor        
print("o menor valor é--> ",menor)
print("o maior valor é-->",maior)
print("soma =",soma)
