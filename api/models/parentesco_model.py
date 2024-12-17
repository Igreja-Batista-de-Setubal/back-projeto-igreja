from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Parentesco(db.Model):
    __tablename__ = 'tb_parentesco'
    id_parentesco = db.Column(db.Integer, primary_key=True)
    nome_parentesco = db.Column(db.String(50), nullable=False)
    
    