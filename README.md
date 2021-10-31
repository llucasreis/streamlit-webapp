# Lung Cancer Prediction

## Descrição

Este é um Data App para Diagnóstico preditivo de Câncer de Pulmão

Desenvolvido pelos alunos: Andrea Monicque, Francisco Marcelo, Lucas Pereira e Marcos Wenneton para a discplina de Infraestrutura em Nuvem para Projetos com Ciência dos Dados do curso de Pós-Graduação em Ciência de Dados da Universidade do Estado do Amazonas - UEA.

### Dataset e Modelo Preditivo
O dataset utilizado está disponível gratuitamente na plataforma Kaggle por este [link](https://www.kaggle.com/mysarahmadbhat/lung-cancer). Desenvolvemos uma solução preditiva com [Microsoft Machine Learning Studio (classic)](https://studio.azureml.net/) e publicamos online para ser consumido pela aplicação.

## Requerimentos
Para executar localmente, é necessário você ter instalado as seguintes ferramentas:
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://docs.python.org/3/installing/index.html)

Após isso você pode clonar o repositório com o comando:
```
git clone https://github.com/llucasreis/streamlit-webapp
```

## Iniciando a aplicação

Antes de iniciar é recomendável você utilizar um ambiente virtual, e para isto, execute os seguintes comandos:
```shell
# instalando a biblioteca de ambiente virtual
pip install virtualenv

# criando o ambiente virtual
python3 -m virtualenv .venv

# ativando o ambiente virtual
source .venv/bin/activate
```

Após ativar seu ambiente virtual, basta executar o comando para instalar as bibliotecas:
```shell
pip install -r requirements.txt
```

E por fim, execute o comando para rodar a aplicação com `streamlit`:
```shell
streamlit run src/app.py
```

### Azure

Os passos acima habilitam o ambiente e executa localmente, mas não será possível realizar a predição
pois a aplicação utiliza a Azure como dependência externa para hospedar o modelo preditivo. Acima, é recomendável utilizar o sistema diretamente do [Heroku](https://streamlit-webapp-uea-pos2.herokuapp.com/), pois já está conectado com a Azure.

Caso você já tenha um modelo preditivo na Azure com este dataset, basta criar um arquivo de ambiente com:
```shell
make dotenv

# caso não funcione esse comando, pode usar:
cp .env.example .env
```

E inserir as credenciais da sua aplicação.

---

Made by [Andrea Monicque](https://github.com/DevNicque), [Francisco Marcelo](https://github.com/fmmdamasceno), [Lucas Pereira](https://github.com/llucasreis) and [Marcos Wenneton](https://github.com/wenneton)