import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.produto import Produto

url = 'https://fakestoreapi.com/products'

try:
    response = requests.get(url)
    if response.status_code == 200:
        produtos = response.json()

        db_path = "database/"
        db_url = f"sqlite:///{db_path}db.sqlite3"

        engine = create_engine(db_url, echo=False)

        Session = sessionmaker(bind=engine)
        session = Session()

        for produto in produtos:
            new_produto = Produto(
                title=produto['title'],
                price=produto['price'],
                description=produto['description'],
                category=produto['category'],
                image=produto['image']
            )
            session.add(new_produto)
        session.commit()
        print('Produtos adicionados ao banco de dados com sucesso!')
        session.close()

    else:
        print(f'Erro ao baixar produtos da API: status {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Erro de requisição: {e}')
