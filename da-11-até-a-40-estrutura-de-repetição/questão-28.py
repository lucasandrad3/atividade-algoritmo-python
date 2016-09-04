quantidade_cd=int(input("-informe a quantidade de CDs adiquiridos: \n "))
somador=0
for c in range(1,quantidade_cd+1):
    preço=float(input("-informe o preço de cada CD--> "))
    somador=somador + preço
    media=somador/quantidade_cd
print("-total investido =",somador,"$")
print("-valor gasto em cada CD =",media,"$")