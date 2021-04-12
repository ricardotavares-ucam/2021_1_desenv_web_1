##Cálculo de comissão de vendas do produto X
##Regra de negócio:
##Se vendedor vendeu mais de 20 produtos: valor da venda * 5%
##Se vendedor vendeu mais de 50 produtos: valor da venda * 7.5%
##Se vendedor vendeu mais de 100 produtos: valor da venda * 10%
##Se vendedor vendeu mais de 500 produtos: valor da venda * 12.5%

vendas = int(input('Digite o número de vendas: '))
comissao = 0
valor_venda = float(input('Digite o valor total de vendas: '))

if vendas >= 20:
    comissao = valor_venda/05
    print(comissao)
elif vendas >= 50:
    comissao = valor_venda/075
    print(comissao)
elif vendas >= 100:
    comissao = valor_venda/1
    print(comissao)
elif vendas >= 500:
    comissao = valor_venda/12
    print(comissao)
