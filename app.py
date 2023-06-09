from flask import Flask, render_template, request
import requests
import matplotlib.pyplot as plt
import os
import datetime

app = Flask(__name__)

# Rota da função para obter os dados do request na página inicial
@app.route("/")
def index():

    # Dados para o gráfico
    listavalores = []
    listadatas = []
    responsehistory = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
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
            valorbase = '1,00'
            askvalue = data['USDBRL']['ask']
            valormoeda = askvalue.replace(".",",") 
            
            return render_template("index.html", valormoeda=valormoeda, valorbase=valorbase, cifra=cifra, cifrabase=cifrabase, labels=listadatas, data=listavalores)


# Rota da função para obter os dados do request quando o usuário selecionar outra moeda
@app.route('/buscarcotacao', methods=['POST'])
def buscarcotacao():
    listavalores = []
    listadatas = []

    # Dados da conversão do câmbio
    moeda1 = str(request.form.get('moeda1'))
    moeda2 = str(request.form.get('moeda2'))
    periodo = str(request.form.get('periodo'))
    valorraw = str(request.form.get('valorbase'))
    if valorraw == '':
        return index()
    valorbase = valorraw.split(' ')[1].replace(',','.')
    if valorbase == '' or valorbase == '0':
        mensagem = 'Valor base inválido'
        return render_template("index.html", moeda1=moeda1, moeda2=moeda2, mensagem=mensagem, labels=listadatas, data=listavalores)
    if moeda1 == moeda2:
        valorbase = '1,00'
        mensagem = 'Selecione moedas diferentes'
        return render_template("index.html", valorbase=valorbase, moeda1=moeda1, moeda2=moeda2, mensagem=mensagem, labels=listadatas, data=listavalores)
    response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda1}-{moeda2}")
    if response.status_code != 200:
        return render_template("serverdown.html")
    else:
        valor = response.json()
        for item, value in valor.items():
            if 'ask' in value:
                valormoeda = value['ask']
        valorconvertido = float(valorbase) * float(valormoeda)
        valorconvertido = str(valorconvertido).replace('.',',')
        valorbase = valorbase.replace('.',',')
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
            cifrabase = 'R$'


        # Dados para o gráfico
        responsehistory = requests.get(f"https://economia.awesomeapi.com.br/json/daily/{moeda1}-{moeda2}/{periodo}")
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

            return render_template("index.html", valormoeda=valorconvertido, valorbase=valorbase, cifra=cifra, cifrabase=cifrabase, moeda1=moeda1, moeda2=moeda2, labels=listadatas, data=listavalores, periodo=periodo)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
