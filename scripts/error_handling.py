def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero."


if __name__ == '__main__':
    print(dividir(10, 0))
