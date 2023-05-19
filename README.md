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

## Como rodar o projeto

- Primeiramente é necessário ter o python instalado no computador. Voce pode fazer o download neste link: https://www.python.org/downloads/ (Lembre-se de habilitar o path das variáveis de ambiente durante a instalação)
- Instalar as dependências abrindo o prompt de comando no diretório raíz do projeto e executar o seguinte comando: pip install -r requirements.txt
- Após a instalação das dependências executar o script python do projeto com o seguinte comando: python app.py
- No próprio terminal deve aparecer a mensagem: Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
- Copie http://127.0.0.1:5000 e cole no navegador ou digite diretamente no navegador http://localhost:5000 e o site deve abrir
