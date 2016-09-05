codigo = int(input("Informe o código da cidade--> "))
veiculos = int(input("Informe o número de veículos de passeio--> "))
acidente = int(input("Informe o número de acidentes de transito com vitimas--> "))
acidentemaior=acidente
acidentemenor=acidente
contaveiculos=veiculos
contador=0
for c in range(0,4):
    if veiculos>2000:
        contador=contador+1
        veiculosacidente=acidente
        veiculosacidente=acidente+veiculosacidente
    codigo = int(input("Informe o código da cidade--> "))
    veiculos = int(input("Informe o número de veículos de passeio--> "))
    acidente = int(input("Informe o número de acidentes de transito com vitimas--> "))
    contaveiculos=contaveiculos+veiculos
    if acidente > acidentemaior:
        acidentemaior=acidente
        codigomaior=codigo
    elif acidente<acidentemenor:
        acidentemenor=acidente
        codigomenor=codigo
print("")        
print("-o menor indice de acidente está cidade com codigo:",codigomenor,"com",acidentemenor,"acidentes" )
print("")
print("-o maior indice de acidente está cidade com codigo:",codigomaior,"com",acidentemaior,"acidentes")
print("")
print("-as cinco cidades possuem",contaveiculos,"veiculos, com media de",contaveiculos/5,"veiculos por cidade")
print("média de acidentes de trânsito em cidades com mais de 2000 veiculos",veiculosacidente/contador)
