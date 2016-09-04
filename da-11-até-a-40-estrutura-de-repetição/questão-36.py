tabuada=int(input("informe a tabuada que voce deseja ver--> "))
primeiro=int(input("a partir de  que numero voce deseja ver ?--> "))
ultimo=int(input("até qual numero ? --> "))
while primeiro>ultimo:
	print("-ERRO 404; tente novamente")
	tabuada=int(input("informe a tabuada que voce deseja ver--> "))
	primeiro=int(input("a partir de  que numero voce deseja ver ?--> "))
	ultimo=int(input("até qual numero ? --> "))
for c in range(primeiro,ultimo+1,):
    conta=c*tabuada
    print(c,"*",tabuada,"=",conta)
      
