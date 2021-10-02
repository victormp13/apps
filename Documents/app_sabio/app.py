from flask import Flask, render_template
import click
from webmanagement import web_management_bp
from appmanagement import app_management_bp
from config import Config
from database_management import create_database
from database import COMPET

# Create app
app = Flask(__name__)
app.register_blueprint(web_management_bp)
app.register_blueprint(app_management_bp)

settings = Config()
app.config.from_object(settings)
COMPET.init_app(app)
@app.cli.command("createdb")
def initdb_command():
    create_database(COMPET)

if __name__ == '__main__':
    app.run()


