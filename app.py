import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///tricounty.sqlite")

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
tricounty = Base.classes.keys()

# Create a database session object
# session = Session(engine)

# Save references to each table
geographic = Base.classes.geographic
pe_description = Base.classes.pe_description
programs = Base.classes.programs
risk = Base.classes.risk
violations = Base.classes.violations

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# All available routes
@app.route("/")
def welcome():
    """All available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/county<br/>"
        f"/api/v1.0/city<br/>"
        f"/api/v1.0/program_id<br/>"
        f"/api/v1.0/loc_description<br/>"
        f"/api/v1.0/pe_desc<br/>"
        f"/api/v1.0/site_address<br/>"
        f"/api/v1.0/total_violations<br/>"
        f"/api/v1.0/risk_category<br/>"
        f"/api/v1.0/foodborne_illness_violations<br/>"        
        f"/api/v1.0/good_retail_practices_violations<br/>"   
        f"/api/v1.0/inspScore<br/>"   
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )

# Return a JSON representation of a dictionary
@app.route("/api/v1.0/county")
def county():
    session = Session(engine)
    county_results = session.query(geographic.county, geographic.city, geographic.program_id).all()
    session.close()
    
    county_dictionary = list(np.ravel(county_results))
    return jsonify(county_dictionary)

# Return a JSON list of stations
@app.route("/api/v1.0/inspScore")
def inspScore():
    session = Session(engine)
    inspScore_results = session.query(violations.total_violations, violations.inspScore).all()
    session.close()
    
    inspScore_dictionary = list(np.ravel(inspScore_results))
    return jsonify(inspScore_dictionary)

# MORE TO BE CONTINUED