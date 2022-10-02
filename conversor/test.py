"""
Programa utilizado para probar la funcion de conversion, no llamada por el bot
"""


import fConversor as Conversor 

cant = float(input("Valor a convertir: "))
MO = input("Moneda de origen: ").strip()
MR = (input("Moneda a convertir: ")).strip()

print(Conversor.convertir(MO,MR,cant))
