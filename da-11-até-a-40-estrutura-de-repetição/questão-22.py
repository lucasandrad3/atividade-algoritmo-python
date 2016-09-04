num=int(input("-Digite Um Numero--> "))        
contaresto=0
for c in range(1,num+1):
    resto=num%c
    if resto==0:        
        contaresto=contaresto+1    
        print(c)
if contaresto==1 or contaresto==2:
    print("o numero",num," é primo")
else:
    print("o numero",num," nao é primo")
