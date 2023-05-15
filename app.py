from flask import Flask, render_template, request
import requests
import matplotlib.pyplot as plt
import os
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Dados para o gráfico
    listavalores = []
    listadatas = []
    responsehistory = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/60")
    print(responsehistory.status_code)
    if responsehistory.status_code != 200:
        return render_template("serverdown.html")
    else:
        history = responsehistory.json()
        for item in history:
            askvaluehistory = item['ask']
            timestamp = int(item['timestamp'])
            listavalores.append(float(askvaluehistory))
            datahora = datetime.datetime.fromtimestamp(timestamp)
            date = datahora.strftime('%d-%m')
            listadatas.append(date)
        
        #Dados da conversão do câmbio
        response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        if response.status_code != 200:
            return render_template("serverdown.html")
        else:
            data = response.json()
            cifra = 'R$'
            cifrabase = 'US$'
            askvalue = data['USDBRL']['ask']
            valormoeda = askvalue.replace(".",",") 
            
            return render_template("index.html", valormoeda=valormoeda, cifra=cifra, cifrabase=cifrabase, labels=listadatas, data=listavalores)

#USD-BRL,EUR-BRL,BTC-BRL,EUR-USD,BTC-USD,AUD-BRL,CAD-BRL,ARS-BRL,BRL-ARS,CHF-BRL,GBP-BRL



@app.route('/buscarcotacao', methods=['POST'])
def buscarcotacao():
    
    moeda1 = str(request.form.get('moeda1'))
    moeda2 = str(request.form.get('moeda2'))
    if moeda1 == moeda2:
        mensagem = 'Selecione moedas diferentes'
        return render_template("index.html", moeda1=moeda1, moeda2=moeda2, mensagem=mensagem, labels=labels, data=data)
    response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda1}-{moeda2}")
    if response.status_code != 200:
        return render_template("serverdown.html")
    else:
        valor = response.json()
        for item, value in valor.items():
            if 'ask' in value:
                askvalue = value['ask']
        valormoeda = askvalue.replace(".",",")
        if moeda2 == 'BRL':
            cifra = 'R$'
        elif moeda2 == 'USD':
            cifra = 'US$'
        else:
            cifra = '€'

        if moeda1 == 'USD':
            cifrabase = 'US$'
        elif moeda1 == 'CAD':
            cifrabase = 'CAD'
        elif moeda1 == 'AUD':
            cifrabase = 'AUD'
        elif moeda1 == 'EUR':
            cifrabase = '€'
        elif moeda1 == 'GBP':
            cifrabase = '£'
        elif moeda1 == 'ARS':
            cifrabase = 'ARS'
        elif moeda1 == 'CHF':
            cifrabase = 'CHF'
        else:
            cifrabase = 'BRL'


        # Dados para o gráfico
        listavalores = []
        listadatas = []
        responsehistory = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/60")
        if responsehistory.status_code != 200:
            return render_template("serverdown.html")
        else:
            history = responsehistory.json()
            for item in history:
                askvaluehistory = item['ask']
                timestamp = int(item['timestamp'])
                listavalores.append(float(askvaluehistory))
                datahora = datetime.datetime.fromtimestamp(timestamp)
                date = datahora.strftime('%d-%m')
                listadatas.append(date)

            return render_template("index.html", valormoeda=valormoeda, cifra=cifra, cifrabase=cifrabase, moeda1=moeda1, moeda2=moeda2, labels=listadatas, data=listavalores)


if __name__ == "__main__":
    app.run(debug=True)
