quantidade=int(input("quantidade de produtos comprados--> "))
soma=0
for produtos in range (1,quantidade+1):
    preço=float(input("informe o preço dos produtos--> "))
    soma=soma+preço
    
print("total = R$",soma)
dinheiro=float(input("dinheiro total--> "))
troco=dinheiro-soma
print("troco: R$",troco)