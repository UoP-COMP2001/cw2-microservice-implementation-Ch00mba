import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.engine import URL

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

#database connection details
connection_url = URL.create(
    "mssql+pyodbc",
    username="EGove",
    password="ZecA894",
    host="dist-6-505.uopnet.plymouth.ac.uk",
    database="COMP2001_EGove",
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "Encrypt": "yes",
        "TrustServerCertificate": "yes",
    },

)

app = connex_app.app

#SQLAlchemy Connection URL
app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)