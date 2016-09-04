quantidade=int(input("quantidade de temperaturas--> "))
temperaturas=int(input("informe as temperaturas--> "))
menor=temperaturas
maior=temperaturas
somador=temperaturas
for i in range(1,quantidade):
    temperaturas=float(input("informe as temperaturas--> "))
    somador=somador+temperaturas
    if temperaturas>maior:
        maior=temperaturas
    elif temperaturas<menor:
        menor=temperaturas
print("o maior é", maior)
print("o menor é",menor)
print("a media das temperaturas é-->",somador/quantidade)