print("-calcular médias")
quantidade_notas=int(input("-digite a quantidade de notas---> "))
contadormedia=0
for x in range(1,quantidade_notas+1):
    notas=int(input("-digite sua nota :\n"))
    contadormedia=contadormedia+notas
media=contadormedia/quantidade_notas
print("sua média é-->",media)
