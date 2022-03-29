# Desafio4i

Passos para executar a aplicação:

$ virtualenv venv
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate

$ pip3 install -r requirements.txt

$ export FLASK_APP=application.py
$ export FLASK_ENV=development
$ flask run


Em um navegador, acesse o domínio "localhost:5000" para acessar a aplicação

Para interagir com o banco de dados, utilize a rota "localhost:5000/suppliers". Nessa página, será feita a requisição de todos os registros.

Para buscar registros individualmente, acesse "localhost:5000/suppliers/<id>". A partir dessa URL é possível fazer operações GET, POST, DELETE e PUT.
    Para as operações GET e PUT, é necessário enviar um json contendo as informações que serão adicionadas ou alteradas.
