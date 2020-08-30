import random
import string
#Digitos + Letras Mayusculas + letras Minusculas
def op_1(longitud):
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres)
                   for _ in range(longitud))
#Letras Mayusculas + Letras Minusculas
def op_2(longitud):
    caracteres = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(caracteres)
                   for _ in range(longitud))
#Solo Digitos
def op_3(longitud):
    caracteres = string.digits
    return ''.join(random.choice(caracteres)
                   for _ in range(longitud))
#Letras mayusculas + Digitos
def op_4(longitud):
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres)
                   for _ in range(longitud))
#Letras Minuscculas + Digitos
def op_5(longitud):
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres)
                   for _ in range(longitud))
longitud = int(input("longitud de la contraseña, ejemplo = 10: "))
op = int(input("Que tipo de contraseña deseas: \n"
               ".............................\n"
               "1- Digitos + Letras Mayusculas + letras Minusculas \n"
               "2- Letras Mayusculas + Letras Minusculas \n"
               "3- Solo Digitos \n"
               "4- Letras mayusculas + Digitos \n"
               "5- Letras Minuscculas + Digitos \n"
               "= "))


if op == 1:
    resultado = op_1(longitud)
    print("tu contraseña es: {}".format(resultado))
elif op == 2:
    resultado = op_2(longitud)
    print("tu contraseña es: {}".format(resultado))
elif op == 3:
    resultado = op_3(longitud)
    print("tu contraseña es: {}".format(resultado))
elif op == 4:
    resultado = op_4(longitud)
    print("tu contraseña es: {}".format(resultado))
elif op == 5:
    resultado = op_5(longitud)
    print("tu contraseña es: {}".format(resultado))
else:
    print("opcion incorrecta, solo escoge entre 1, 2, 3, 4, 5")








