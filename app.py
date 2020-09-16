import numpy as np
import pandas as pd

import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tricounty.sqlite"
db = SQLAlchemy(app)

# Reflect Database into a new model
Base = automap_base()
# Reflect Tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Geographic = Base.classes.geographic
PE_description = Base.classes.pe_description
Programs = Base.classes.programs
Risk = Base.classes.risk
Violations = Base.classes.violations

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/county_violations")
def countyviolations:
    print("Server received request for 'County Violations' page...")
    return "THIS PAGE IS UNDER CONSTRUCTION!"

@app.route("/county_violations_types")
def countyviolations:
    print("Server received request for 'County Violations Type' page...")
    return "THIS PAGE IS UNDER CONSTRUCTION!"