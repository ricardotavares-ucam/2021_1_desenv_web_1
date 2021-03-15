qtvenda = int(input('entre com o numero d vendas '))
comissao = 0
valorVenda = float(input('Entre com o valor total de vendas '))
if (qtvenda >= 20):
    comissao = valorVenda*0.05
    print(comissao)
elif (qtvenda >= 50):
    comissao = valorVenda*0.075
    print(comissao)
elif (qtvenda >= 100):
    comissao = valorVenda*0.1
    print(comissao)
elif (qtvenda >= 500):
    comissao = valorVenda*0.12
    print(comissao)

