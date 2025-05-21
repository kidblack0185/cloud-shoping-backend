from pydantic import BaseModel

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class ProductCreate(BaseModel):
    nome: str
    preco: float
    descricao: str

class OrderCreate(BaseModel):
    usuario_id: int
    produto_id: int
