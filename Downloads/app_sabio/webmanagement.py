"""
Blueprint de management de la web
"""
import json

from flask import Blueprint, current_app, request, render_template, jsonify
from jinja2 import TemplateNotFound
from database import COMPET
import database as d
from models import Equip

web_management_bp = Blueprint('web_management', __name__, template_folder='templates')
error=True

@web_management_bp.route('/')
def show_main():
    d.error=True
    return render_template('index.html',m=d.text)

@web_management_bp.route('/menu')
def index():
    tempstotal=0
    llista=COMPET.session.query(Equip).order_by(Equip.temps.desc())
    for k in llista:
        tempstotal+=k.temps
    part=llista.count()
    tempsmitja=int(round(tempstotal/llista.count(), 0))
    if d.error==False:
        return render_template('inicio.html',equips=llista,t=tempsmitja,p=part)
    else:
        return render_template('redirect1.html',m=d.text)

@web_management_bp.route('/comprova', methods=['POST'])
def validar_login():
    nom = request.form["nom"]
    password = request.form["contrasenya"]
    equip = COMPET.session.query(Equip).filter_by(nom=nom).first()
    if equip == '' and password=='':
        d.text='Introdueix un equip i contrasenya vàl·lids'
        return render_template('redirect1.html',title='Home',)
    if equip == None :
        d.text='Usuari no existent'
        return render_template('redirect1.html',title='Home',)
    else:
        if equip.password != password:
            d.text='Contrasenya incorrecta'
            return render_template('redirect1.html',title='Home',)
        else:
            d.text=''
            d.error=False
            return render_template('redirect2.html',title='Home',)

@web_management_bp.route('/ranking')
def index1():
    return render_template('ranking.html',title='Home',)



