def calcula_soma(valor, *args):
    soma = valor
    for arg in args:
        soma += arg
    return soma


def print_dict(**kwargs):
    print(kwargs)


print(calcula_soma(1, 2, 3, 4, 5))  # 15

print_dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
