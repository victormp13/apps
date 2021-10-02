"""
Blueprint de management de la app
Són rutes a les que s'accedirà des de la app
"""
import json
import datetime
import itertools
from flask import Blueprint, current_app, request, render_template, jsonify
from jinja2 import TemplateNotFound
from database import COMPET
from models import Equip

app_management_bp = Blueprint('app_management', __name__, template_folder='templates')


@app_management_bp.route("/app_admin/obtenir_ranquing", methods=["GET"])
def obtenir_ranquing():
    n = int(request.form["nombre"])
    try:
        llistan = COMPET.session.query(Equip.nom).order_by(Equip.temps.desc()).all()
        llista_novan = list(itertools.chain.from_iterable(llistan))
        for i in range(len(llista_novan), n):
            llista_novan.append('')

        llistap = COMPET.session.query(Equip.temps).order_by(Equip.temps.desc()).all()
        llista_novap = list(itertools.chain.from_iterable(llistap))
        for i in range(len(llista_novap), n):
            llista_novap.append('')

        llista_nova=[llista_novan]+[llista_novap]

        return jsonify({"success":True, "ranquing":llista_nova}), 201
    except:
        return jsonify({"success":False}), 404
@app_management_bp.route("/app_admin/validar_login", methods=["GET"])
def validar_login():
    nom = request.form["nom"]
    password = request.form["password"]
    equip = COMPET.session.query(Equip).filter_by(nom=nom).first()
    if equip == None :
        return jsonify({"success":False, "message":"Equip inexistent"}), 404
    else:
        if equip.password != password:
            return jsonify({"success":False, "message": "Password incorrecte"}), 404
        else:
            return jsonify({"success":True}), 201

@app_management_bp.route("/app_admin/crear_equip", methods=["POST"])
def crear_equip():
    nom = request.form["nom"]
    password = request.form["password"]
    equip = COMPET.session.query(Equip).filter_by(nom=nom).first()
    if equip == None :
        equip = Equip(nom=nom, password=password, temps=0)
        COMPET.session.add(equip)
        COMPET.session.commit()
        return jsonify({"success":True}), 201
    else:
        return jsonify({"success":False}), 404

@app_management_bp.route("/app_admin/modificar_temps", methods=["POST"])
def modificar_temps():
    nom = request.form["nom"]
    equip = COMPET.session.query(Equip).filter_by(nom=nom).first()
    temps = int(request.form["temps"])
    if equip.temps<temps:
        equip.temps = temps
        COMPET.session.commit()
        return jsonify({"success":True, "message":'Has trigat '+str(temps)+' segons'}), 201
    else:
        temps=request.form["temps"]
        return jsonify({"success":False, "message":'Has trigat '+temps+' segons. Millor temps de '+str(equip.temps)+' segons'}), 404




