from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EstadoCivil(db.Model):
    __tablename__ = 'tb_estado_civil'
    id_estado_civil = db.Column(db.Integer, primary_key=True)
    nome_estado_civil = db.Column(db.String(20), nullable=False)
