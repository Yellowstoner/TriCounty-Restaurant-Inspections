import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
tricounty = Base.classes.keys()

# Create a database session object
# session = Session(engine)

# Save references to each table
geographic = Base.classes.geographic
risk = Base.classes.risk
scores = Base.classes.scores

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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )

# Return a JSON representation of a dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    precip_results = session.query(measurement.date, measurement.prcp).all()
    session.close()
    
    precip_dictionary = list(np.ravel(precip_results))
    return jsonify(precip_dictionary)
