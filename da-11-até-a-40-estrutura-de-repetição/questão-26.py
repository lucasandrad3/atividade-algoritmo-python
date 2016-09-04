print("-calcular votos de cada candidato")
quantidade_eleitores=int(input("-digite a quantidade de eleitores---> "))
contador=0
for x in range(1,quantidade_eleitores+1):
    candidato=str(input("-informe o candidato que irá votar, 1, 2 ou 3:\n"))
if candidato=="1":
    contador1=contador1+1
elif candidato=="2":
    contador2=contador2+1
else:
    contador3=contador3+1
print(contador1)
print(contador2)
print(contador3)   
