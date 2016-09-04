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