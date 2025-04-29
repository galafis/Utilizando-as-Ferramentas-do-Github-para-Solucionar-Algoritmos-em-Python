def validar_email(email):
    return "@" in email and "." in email

print(validar_email("exemplo@dio.me"))
