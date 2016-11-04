# Autor: hackbier
# https://github.com/hackbier
# Written in Python 3
# Simple Python Script for Generate Secure Password

from random import choice

longitud = (20)
valores = ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/@#$%&")

password = ("")
password = password.join([choice(valores) for i in range(longitud)])
print (password)
