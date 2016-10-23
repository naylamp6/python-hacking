from random import choice

longitud = (20)
valores = ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/@#$%&")

password = ("")
password = password.join([choice(valores) for i in range(longitud)])
print (password)
