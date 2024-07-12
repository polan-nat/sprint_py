from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Produto, get_session

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API de Produtos'})

@app.route('/produtos', methods=['GET'])
def get_produtos():
    session = get_session()
    produtos = session.query(Produto).all()
    result = []
    for produto in produtos:
         produto_data = {
             'id': produto.id,
             'title': produto.title,
             'price': produto.price,
             'description': produto.description,
             'category': produto.category,
             'image': produto.image,
         }
         result.append(produto_data)
    session.close()
    return jsonify(result)

@app.route('/produto/<int:id>', methods=['GET'])
def get_produto(id):
    session = get_session()
    produto = session.query(Produto).filter_by(id=id).first()
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    
    produto_data = {
        'id': produto.id,
        'title': produto.title,
        'price': produto.price,
        'description': produto.description,
        'category': produto.category, 
        'image': produto.image,
    }
    session.close()
    return jsonify(produto_data)

@app.route('/produto', methods=['POST'])
def add_produto():
    data = request.get_json()
    session = get_session()
    new_produto = Produto(
        title=data['title'],
        price=data['price'],
        description=data['description'],
        category=data['category'],
        image=data['image']
    )
    session.add(new_produto)
    session.commit()
    session.close()
    return jsonify({'message': 'Produto adicionado com sucesso'}), 201

@app.route('/produto/<int:id>', methods=['PUT'])
def update_produto(id):
    data = request.get_json()
    session = get_session()
    produto = session.query(Produto).filter_by(id=id).first()
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    
    produto.title = data.get('title', produto.title)
    produto.price = data.get('price', produto.price)
    produto.description = data.get('description', produto.description)
    produto.category = data.get('category', produto.category)
    produto.image = data.get('image', produto.image)

    session.commit()
    session.close()
    return jsonify({'message': 'Produto atualizado com sucesso'}), 200

@app.route('/produto/<int:id>', methods=['DELETE'])
def delete_produto(id):
    session = get_session()
    produto = session.query(Produto).filter_by(id=id).first()
    if not produto:
        return jsonify({'message': 'Produto não encontrado'})
    
    session.delete(produto)
    session.commit()
    session.close()
    return jsonify({'message': 'Produto deletado com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)