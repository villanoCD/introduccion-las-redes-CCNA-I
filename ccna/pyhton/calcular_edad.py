# aun no has nacido
# bebe
# niño/a
# adolescente
# joven
# adulto/a joven
# adulto/a mayor
# adulto/a peliado
# viejo/a
# viviendo tiempo extra
# jablador

# le damos la bienvenida al programa
print('Bienvenido/a al programa de estados de un ser humano!')
print('Desarrollado por: Vladimir')
print('------------------------------------------')

# pedimos la edad al usuario
edad = int(input('Por favor, ingrese su edad en años: '))
print("<---------------------------------------->")
if (edad < 0):
    print('aun no has nacido')
elif (edad >= 0 and edad <= 1):
    print('usted es un bebe')
elif (edad >= 2 and edad <= 10):
    print('usted es un niño/a')
elif (edad >= 12 and edad <= 14):
    print('usted es un/a adolescente')
elif (edad >= 15 and edad <= 17):
    print('usted es un/a joven')
elif (edad >= 18 and edad <= 25):
    print('usted es un adulto/a joven')
elif (edad >= 26 and edad <= 39):
    print('usted es un adulto/a mayor')
elif (edad >= 40 and edad <= 59):
    print('usted es un adulto/a peliado')
elif (edad >= 60 and edad <= 84):
    print('usted es un/a viejo/a')
elif (edad >= 85 and edad <= 99):
    print('usted es un/a viviendo tiempo extra, felicidades!')
else:
    print('usted es un/a jablador, que vida tan larga! acaba de batir un record mundial! acaso eres inmortal?')

# despedida del programa
print("<---------------------------------------->")
print("Muchas gracias por utilizar este sofware con mucho cariño, esperamos verte pronto de nuevo! ,vladimir cornelio") 
