from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contato(db.Model):
    __tablename__ = 'tb_contato'
    id_contato = db.Column(db.Integer, primary_key=True)
    dado_contato = db.Column(db.String(100), nullable=False)
    tipo_contato = db.Column(db.Enum('Telefone', 'Email', 'Outro'))
    id_pessoa_fisica = db.Column(db.Integer, db.ForeignKey('tb_pessoa_fisica.id_pessoa_fisica'), nullable=False)