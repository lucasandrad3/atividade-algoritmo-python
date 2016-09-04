Quantidade=int(input("indique a quantidade de números --> "))
valor = int(input("-digite um numero--> "))
while valor < 0 or valor > 1000:
    valor = int(input("-valor não aceito, digite um numero--> "))
else:    
    maior=valor
    menor=valor
    soma=valor
    contador=0
    while contador< Quantidade-1:
        valor = int(input("-digite outro numero--> "))
        while valor < 0 or valor > 1000:
            valor = int(input("-valor não aceito, digite outro  numero--> "))
        else:
            soma=valor+soma
            contador=contador+1
            if valor > maior:
                maior=valor
            elif valor < menor:
                menor=valor        
print("o menor valor é--> ",menor)
print("o maior valor é-->",maior)
print("soma =",soma)
