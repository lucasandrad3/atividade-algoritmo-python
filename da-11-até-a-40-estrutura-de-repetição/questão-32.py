fatorial=int(input("informe o fatorial--> "))
print("Fatorial de:",fatorial)
somador=1
for c in range(1,fatorial+1):
    somador=somador*c
    print(c,"*")
print("=",somador)