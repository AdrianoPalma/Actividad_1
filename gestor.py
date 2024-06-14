import random

contraseña = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input(ingresa la longitud de tu codigo:))
elemento = ""
for in in range(longitud):
  elemento += random.choice(contraseña)

print("elemento")
