turma=int(input("informe a quantidade de turma:\n"))
alunos1=0
for c in range(1,turma+1):
    alunos=int(input("informe a quantidade de alunos em cada turma-->"))
    while alunos>40:
        alunos=int(input("valor incorreto,informe novamente a quantidade de alunos em cada turma-->"))
    alunos1=alunos1+alunos
media_alunos= (alunos1)/turma
print(media_alunos)