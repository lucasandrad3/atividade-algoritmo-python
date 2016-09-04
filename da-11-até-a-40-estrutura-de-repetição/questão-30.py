preçopao=float(input("informe o preço do pao---> "))
print("Panificadora Pão de Ontem - Tabela de preços")
for c in range(1,50+1):
    somador=preçopao*c
    print(c,"-",somador,"$")