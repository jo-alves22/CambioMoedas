# CambioMoedas

## Site para conversão do câmbio das principais moedas
- O projeto foi desenvolvido utilizando HTML, CSS e Javascript na interface e Python para processamento das informações no backend.

- O projeto é estruturado da seguinte forma:
meu_projeto/
    |- static/
    |   |- css/
    |   |   |- index.css
    |   |- images/
    |   |   |exchange.png
    |- templates/
    |   |- index.html
    |   |- serverdown.html
    |- app.py
    |- README.md
    |- requirements.txt

- As seguintes bibliotecas foram utilizadas no desenvolvimento do projeto: **flask, requests, matplotlib, datetime, chart.js**
- O arquivo app.py na contém a inicialização do projeto, bem como as rotas para os requests que efetuarão as solicitações da API para obter as informações relacionadas aos valores do câmbio. Neste mesmo arquivo são efetuadas as tratativas para conversão e envio dos dados no formato correto para display na página HTML.
- O arquivo README.md contém as instruções sobre o projeto para configuração e execução.
- O requirements.txt contém as dependências que precisam ser instaladas no ambiente para o funcionamento do projeto.
- Dentro da pasta templates/ ficam armazenadas as páginas HTML que serão exibidas no navegador.
- No diretório static/ ficam os arquivos .css de estilização e as imagens, cada um sua respectiva subpasta.

