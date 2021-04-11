#https://i.imgur.com/jto1dKb.jpg

produto = float(input("Entre com o valor do produto:"))
qnt_Vendas = float(input("Quantos produtos foram vendidos?:"))
total = (produto*qnt_Vendas)

if(qnt_Vendas >=20 and qnt_Vendas<=49):
    total*=0.05
    print("A sua comissão é:{}.".format(total))

elif(qnt_Vendas >=50 and qnt_Vendas <=99):
    total*=0.075
    print("A sua comissão é:{}.".format(total))

elif(qnt_Vendas >=100 and qnt_Vendas <=499):
    total*=0.1
    print("A sua comissão é:{}.".format(total))

elif(qnt_Vendas >=500):
    total*=0.125
    print("A sua comissão é:{}.".format(total))
    
else:
    print("Não há comissão:")