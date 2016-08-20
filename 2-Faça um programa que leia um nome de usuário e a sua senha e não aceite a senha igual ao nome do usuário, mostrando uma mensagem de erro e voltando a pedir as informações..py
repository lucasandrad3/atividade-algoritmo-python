2)
print("faça já seu cadastro:")
usuario=str(input("usuário--> "))
senha=str(input("senha-->"))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")
