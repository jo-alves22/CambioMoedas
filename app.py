from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    data = response.json()
    print(data)
    print(data['USDBRL']['ask'])
    cifra = 'R$'
    cifrabase = 'US$'
    askvalue = data['USDBRL']['ask']
    valormoeda = askvalue.replace(".",",")
    return render_template("index.html", valormoeda=valormoeda, cifra=cifra, cifrabase=cifrabase)

#USD-BRL,EUR-BRL,BTC-BRL,EUR-USD,BTC-USD,AUD-BRL,CAD-BRL,ARS-BRL,BRL-ARS,CHF-BRL,GBP-BRL

@app.route('/buscarcotacao', methods=['POST'])
def buscarcotacao():
    moeda1 = str(request.form.get('moeda1'))
    moeda2 = str(request.form.get('moeda2'))
    if moeda1 == moeda2:
        mensagem = 'Selecione moedas diferentes'
        return render_template("index.html", moeda1=moeda1, moeda2=moeda2, mensagem=mensagem)
    response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda1}-{moeda2}")
    valor = response.json()
    for item, value in valor.items():
        if 'ask' in value:
            print(value['ask'])
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
    return render_template("index.html", valormoeda=valormoeda, cifra=cifra, cifrabase=cifrabase, moeda1=moeda1, moeda2=moeda2)


if __name__ == "__main__":
    app.run(debug=True)
