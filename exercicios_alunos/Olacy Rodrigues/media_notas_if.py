#https://i.imgur.com/sxB4qwS.jpg

nota1 = float(input("Entre com a nota 1:"))
nota2 = float(input("Entre com a nota 2:"))
media =((nota1+nota2)/2)

if (media>=6):
    print("Aluno aprovado")
elif (media>=5 and media<6):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")

if (media>=9.5):
    print("Média A")
elif (media>=8.5 and media<9.5):
    print("Média B")
elif (media>=7.5 and media<8.5):
    print("Média C")
elif (media>=6 and media<7.5):
    print("Média D")
elif (media>=5 and media<6):
    print("Média E")
else:
    print("Média F")
    

