from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Parente(db.Model):
    __tablename__ = 'tb_parente'
    id_parente = db.Column(db.Integer, primary_key=True)
    id_pessoa_fisica = db.Column(db.Integer, db.ForeignKey('tb_pessoa_fisica.id_pessoa_fisica'), nullable=False)
    id_pessoa_fisica_parente = db.Column(db.Integer)
    id_parentesco = db.Column(db.Integer, db.ForeignKey('tb_parentesco.id_parentesco'), nullable=False)
    casamento = db.relationship('Casamento', backref='parente', uselist=False)
    
    