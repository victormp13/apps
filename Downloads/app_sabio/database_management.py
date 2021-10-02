"""
Database_management: Creates the database and a default team

"""

from flask import current_app

from models import Equip

def create_database(db):
    db.create_all()
    equip = Equip(nom='equip-A', password='aa', temps=900)
    db.session.add(equip)
    db.session.commit()
