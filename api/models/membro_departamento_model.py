from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MembroDepartamento(db.Model):
    __tablename__ = 'tb_membro_departamento'
    id_departamento = db.Column(db.Integer, db.ForeignKey('tb_departamento.id_departamento'), primary_key=True)
    id_membro = db.Column(db.Integer, db.ForeignKey('tb_membro.id_membro'), primary_key=True)
    data_inicio_membro_departamento = db.Column(db.Date)
    data_fim_membro_departamento = db.Column(db.Date)
    vinculo_membro_departamento = db.Column(db.Enum('Participante', 'Dirigente'))