def validar_email(email):
    return "@" in email and "." in email


if __name__ == '__main__':
    print(validar_email("exemplo@dio.me"))
