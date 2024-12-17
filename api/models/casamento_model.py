from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Casamento(db.Model):
    __tablename__ = 'tb_casamento'
    id_casamento = db.Column(db.Integer, primary_key=True)
    data_casamento = db.Column(db.Date)
    id_parente = db.Column(db.Integer, db.ForeignKey('tb_parente.id_parente'), nullable=False)
    