from database.sessao import db


class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    etiqueta = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(20), nullable=False)
    valor = db.Column(db.Float(), nullable=False)
    codigoBarras = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(), nullable=True)