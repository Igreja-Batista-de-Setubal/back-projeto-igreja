from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Membro(db.Model):
    __tablename__ = 'tb_membro'
    id_membro = db.Column(db.Integer, primary_key=True)
    rg_membro = db.Column(db.String(7))
    cpf_membro = db.Column(db.String(11))
    data_batismo_membro = db.Column(db.Date)
    data_membresia_membro = db.Column(db.Date)
    data_desligamento_membro = db.Column(db.Date)
    igreja_batismo_membro = db.Column(db.String(100))
    id_pessoa_fisica = db.Column(db.Integer, db.ForeignKey('tb_pessoa_fisica.id_pessoa_fisica'), nullable=False)
    id_estado_civil = db.Column(db.Integer, db.ForeignKey('tb_estado_civil.id_estado_civil'), nullable=False)
    membro_departamento = db.relationship('MembroDepartamento', backref='membro', lazy=True)
