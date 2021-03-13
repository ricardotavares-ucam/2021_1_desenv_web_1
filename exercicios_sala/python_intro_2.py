# a = 10
# b = 5
# c = a * b
# print('O resultado da equação c = a * b é {}'.format(c))



# a = 10
# b = 5
# a %= b
# print('O resultado da equação a = a * b é {}'.format(a))


# Tabelas verdades aplicadas ao Python

# a = True
# b = True
# c = (a or b)
# print('O resultado de c é {}'.format(c))

# a = True
# b = False
# c = (a and b)
# print('O resultado de c é {}'.format(c))

# nome_aluno = input('Por favor, insira o nome do aluno: ')
# nota_1 = input('Por favor, insira a nota da prova 01: ')
# nota_1 = float(nota_1)
# nota_2 = input('Por favor, insira a nota da prova 02: ')
# nota_2 = float(nota_2)
# nota_3 = input('Por favor, insira a nota da prova 03: ')
# nota_3 = float(nota_3)

# media_nota_aluno = (nota_1 + nota_2 + nota_3)/3
# print('A média do aluno: {}, foi igual à: {}'.format(nome_aluno, media_nota_aluno))


# nome_aluno = input('Por favor, insira o nome do aluno: ')
# nota_1 = input('Por favor, insira a nota da prova 01: ')
# nota_1 = float(nota_1)
# nota_2 = input('Por favor, insira a nota da prova 02: ')
# nota_2 = float(nota_2)

# peso_1 = input('Por favor, insira o peso da prova 01: ')
# peso_1 = float(peso_1)
# peso_2 = input('Por favor, insira o peso da prova 02: ')
# peso_2 = float(peso_2)

# media_nota_aluno = ((nota_1 * peso_1)+(nota_2 * peso_2))/(peso_1 + peso_2)
# print('A média do aluno: {}, foi igual à: {:.2f}'.format(nome_aluno, media_nota_aluno))

# # >= 6.0
# # <6.0

# if media_nota_aluno >= 6.0:
#     print('Aluno aprovado!')
# elif (media_nota_aluno >= 5.0) and (media_nota_aluno < 6.0):
#     print('Aluno em recuperação!')
# else:
#     print('Aluno reprovado!')



nome_aluno = input('Por favor, insira o nome do aluno: ')
nota_1 = input('Por favor, insira a nota da prova 01: ')
nota_1 = float(nota_1)
nota_2 = input('Por favor, insira a nota da prova 02: ')
nota_2 = float(nota_2)


media_nota_aluno = (nota_1 + nota_2)/2
print('A média do aluno: {}, foi igual à: {:.2f}'.format(nome_aluno, media_nota_aluno))

# >= 6.0
# <6.0

if media_nota_aluno >= 6.0:
    print('Aluno aprovado!')
elif (media_nota_aluno >= 5.0) and (media_nota_aluno < 6.0):
    print('Aluno em recuperação!')
else:
    print('Aluno reprovado!')