from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    image = Column(String, nullable=False)

    def __repr__(self):
        return f"<ID='{self.id}', titulo='{self.title}', preco='{self.price}', descrição='{self.description}', categoria='{self.category}', imagem='{self.image}'>"
