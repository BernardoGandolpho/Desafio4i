# Flask
from flask import request

# Inport para tratar datas
from datetime import datetime

from app import create_app, create_db

# Chamo as funções para inicializar o app e o banco de dados
app = create_app()
db = create_db(app)

# Modelo de dados para armazenar fornecedores
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    company = db.Column(db.String(120))
    created_at = db.Column(db.String(30))
    amount_products = db.Column(db.Integer)

    def __repr__(self):
        return f'''id: {self.id},
        name: {self.name},
        company: {self.company},
        created_at: {self.created_at},
        amount_products: {self.amount_products}
        '''


@app.route('/')
def index():
    return {
    'titulo': 'Desafio 4intelligence',
    'autor': 'Bernardo Dalboni Gandolpho',
    'email': 'bernardo.dalboni@gec.inatel.br',
    'url': 'https://github.com/BernardoGandolpho/Desafio4i'
    }


# Rota para listar todos os fornecedores registrados
@app.route('/suppliers')
def get_all_suppliers():
    suppliers = Supplier.query.all()

    output = []

    for supplier in suppliers:
        dados = {'name': supplier.name, 'company': supplier.company, 'created_at': supplier.created_at, 'amount_products': supplier.amount_products}

        output.append(dados)

    return {"Fornecedores": output}


# Rota para buscar um fornecedor pela id
@app.route('/suppliers/<id>')
def get_supplier(id):
    supplier = Supplier.query.get_or_404(id)

    return {'name': supplier.name, 'company': supplier.company, 'created_at': supplier.created_at, 'amount_products': supplier.amount_products}


# Rota para adicionar um novo fornecedor
@app.route('/suppliers', methods=['POST'])
def add_supplier():
    date_now = str(datetime.now())
    supplier = Supplier(name=request.json['name'], company=request.json['company'], created_at=date_now, amount_products=request.json['amount_products'])
    
    db.session.add(supplier)
    db.session.commit()
    
    return {'status': "Registro adicionado com sucesso", 'id': supplier.id}


# Rota para excluir um fornecedor pela id
@app.route('/suppliers/<id>', methods=['DELETE'])
def delete_supplier(id):
    supplier = Supplier.query.get(id)

    # Verifico se o registro existe
    if supplier is None:
        return {"status": "Registro não encontrado"}

    db.session.delete(supplier)
    db.session.commit()

    return {'status': "Registro excluido com sucesso", 'id': supplier.id}


# Rota para atualizar um fornecedos pela id
@app.route('/suppliers/<id>', methods=['PUT'])
def update_supplier(id):
    supplier = Supplier.query.get(id)

    # Verifico se o registro existe
    if supplier is None:
        return {"status": "Registro não encontrado"}

    # Verifico e atualizo os campos existentes na requisição
    if 'name' in request.json:
        supplier.name=request.json['name']
    if 'company' in request.json:
        supplier.company=request.json['company']
    if 'amount_products' in request.json:
        supplier.amount_products=request.json['amount_products']

    db.session.commit()

    return {'status': "Registro atualizado com sucesso", 'id': supplier.id}