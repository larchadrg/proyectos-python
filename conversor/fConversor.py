"""
Conversor de monedas a tiempo real utilizando la pagina https://themoneyconverter.com/
Ultima actualización: 2/10/22
"""

import requests 
from bs4 import BeautifulSoup

def convertir(monedaOriginal, monedaConversion, cantidad: float):
    html = requests.get('https://themoneyconverter.com/es/{}/{}'.format(monedaOriginal,monedaConversion)).text
    soup = BeautifulSoup(html, "lxml")

    #Obtiene el valor de la moneda a convertir en base a que la origen valga 1 
    valorConversionCadena = soup('span')[0].contents[0][10:]
    valorConversionFloat = float(valorConversionCadena.replace(',','.'))

    total = round(cantidad * valorConversionFloat, 2)
    return total 

         
