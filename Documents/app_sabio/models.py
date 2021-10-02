from sqlalchemy.ext.declarative import declared_attr

from database import COMPET


from datetime import date

class Equip(COMPET.Model):
    __tablename__ = "equip"
    id = COMPET.Column(COMPET.Integer, primary_key=True)
    nom = COMPET.Column(COMPET.String(255))
    password = COMPET.Column(COMPET.String(255))
    temps = COMPET.Column(COMPET.Integer)

    def dict(self):
        return {
            "nom": self.nom,
            "password": self.password,
            "temps": self.temps}
