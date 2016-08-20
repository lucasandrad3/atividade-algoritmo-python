populaçãoA=float(input("informe a população da cidade A "))
populaçãoB=float(input("informe a população da cidade B "))
ano=0
taxa_crescimentoA=float(input("informe a taxa de crescimento da população da cidade A "))
taxa_crescimentoB=float(input("informe a taxa de crescimento da população da cidade B "))
while populaçãoA < populaçãoB:
	populaçãoA+=round((populaçãoA*taxa_crescimentoA)/100)
	populaçãoB+=round((populaçãoB*taxa_crescimentoB)/100)
	ano=ano+1

print("levará",ano,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoB-->",populaçãoB,"habitantes")
print("populaçãoA-->", populaçãoA,"habitantes")