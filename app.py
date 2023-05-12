from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    data = response.json()
    print(data)
    print(data['USDBRL']['high'])
    cifra = 'R$'
    dolarvalor = data['USDBRL']['high']
    return render_template("index.html", dolar=dolarvalor, cifra=cifra)

#https://docs.awesomeapi.com.br/api-de-moedas

#response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
#print(response.text)


#response = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/15')
#print(response.text)

if __name__ == "__main__":
    app.run(debug=True)
