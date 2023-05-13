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
    valormoeda = data['USDBRL']['ask']
    return render_template("index.html", valormoeda=valormoeda, cifra=cifra)

#USD-BRL,EUR-BRL,BTC-BRL,EUR-USD,BTC-USD,AUD-BRL,CAD-BRL,ARS-BRL,BRL-ARS,CHF-BRL,GBP-BRL
#https://docs.awesomeapi.com.br/api-de-moedas

#response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
#print(response.text)


#response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
#print(response.text)


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
            valormoeda = value['ask']
    #print(valor['EURBRL']['ask'])
    cifra = 'R$'
    return render_template("index.html", valormoeda=valormoeda, cifra=cifra, moeda1=moeda1, moeda2=moeda2)


if __name__ == "__main__":
    app.run(debug=True)
