def calcula_a_mais_b(a, b):
    global _primeiro_valor
    _primeiro_valor = a
    _segunda_valor = b
    soma = primeiro_valor + segunda_valor
    return soma

print(_primeiro_valor)