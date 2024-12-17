from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ministerio(db.Model):
    __tablename__ = 'tb_ministerio'
    id_ministerio = db.Column(db.Integer, primary_key=True)
    nome_ministerio = db.Column(db.String(100), nullable=False)
    id_membro_responsavel = db.Column(db.Integer)