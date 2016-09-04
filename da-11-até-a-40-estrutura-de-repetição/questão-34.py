#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo
num=int(input("-Digite Um Numero--> "))        
contaresto=0        
for c in range(1,num+1):        
    resto=num%c    
    if resto==0:        
        contaresto=contaresto+1    
if contaresto==1 or contaresto==2:
    print(num,"é primo")
else:
    print(num,"nao é primo")