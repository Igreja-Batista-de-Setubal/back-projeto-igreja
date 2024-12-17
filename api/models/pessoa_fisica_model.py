from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PessoaFisica(db.Model):
    __tablename__ = 'tb_pessoa_fisica'
    id_pessoa_fisica = db.Column(db.Integer, primary_key=True)
    nome_pessoa_fisica = db.Column(db.String(100), nullable=False)
    data_nascimento_pessoa_fisica = db.Column(db.Date)
    convertido_pessoa_fisica = db.Column(db.Enum('Sim', 'Não'))
    vinculo_pessoa_fisica = db.Column(db.Enum('Membro', 'Visitante', 'Frequentador'))
    contatos = db.relationship('Contato', backref='pessoa_fisica', lazy=True)
    parentes = db.relationship('Parente', backref='pessoa_fisica', lazy=True)
    membro = db.relationship('Membro', backref='pessoa_fisica', uselist=False)