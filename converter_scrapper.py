import requests, re
from requests import get
from bs4 import BeautifulSoup
from tkinter import messagebox


try:
    #-------------------------Connecting page------------------------

    url = "https://www.x-rates.com/table"

    results = requests.get(url)

    soup = BeautifulSoup(results.text, "html.parser")

    # print(soup.prettify)


    #------------------------Variables to store data------------------------

    name_currency = []
    exchange_rate = []

    #------------------Obtaining data and adding to variables-----------------

    currencys_table = soup.find_all('tr')

    for currency in currencys_table:

        name = currency.find('td')
        name_str = str(name)
        name_strip = name_str.lstrip('<td>').rstrip('</td>') 
        if name_strip == "" or name_strip == 'None':  # Cleans empty entrys
            pass
        else:
            name_currency.append(name_strip)
        

        rate_find = currency.find('a')
        rate_str = str(rate_find)
        compiler = re.compile('>.*<')
        result = str(compiler.findall(rate_str)).lstrip('[\'>').rstrip('<\']')
        if result == "" or result == 'None':   # Cleans empty entrys
            pass
        else:
            result = float(result)   # Transform str elements to float
            exchange_rate.append(result)
    name_currency.insert(0, "US Dollar")
    exchange_rate.insert(0,1.0)

except:
    messagebox.showinfo("","Verify internet connection")