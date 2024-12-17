from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Departamento(db.Model):
    __tablename__ = 'tb_departamento'
    id_departamento = db.Column(db.Integer, primary_key=True)
    nome_departamento = db.Column(db.String(100), nullable=False)
    id_ministerio = db.Column(db.Integer, db.ForeignKey('tb_ministerio.id_ministerio'), nullable=False)
    id_membro_responsavel = db.Column(db.Integer)
    membro_departamento = db.relationship('MembroDepartamento', backref='departamento', lazy=True)