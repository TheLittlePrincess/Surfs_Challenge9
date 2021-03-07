#%%
import datetime as dt
import numpy as np
import pandas as pd
# %%
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
# %%
engine = create_engine("sqlite:///hawaii.sqlite")
# %%
#reflect the database into our classes.
Base = automap_base()
# %%
#reflect the database
Base.prepare(engine, reflect=True)
# %%
#create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station
# %%
#create a session link from Python to our database
session = Session(engine)
# %%
#from flask import Flask
#create a Flask application called "app."
app = Flask(__name__)
# %%
# define the welcome route (9.5.2)
# create a function welcome() with a return statement
# and then add the routes that we'll need into the return statement. 
# will use f-strings to display them 
@app.route('/')

#def welcome():
 #   return(
  #  '''
   # Welcome to the Climate Analysis API!
    #Available Routes:
    #/api/v1.0/precipitation
    #/api/v1.0/stations
    #/api/v1.0/tobs
    #/api/v1.0/temp/start/end
    #''')
#%%
def welcome():
    test = (f"Welcome to the Hawaii Climate Analysis API!<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/temp/start/end"
            )
    return (test)

# %%
#build a route for the precipitation analysis
@app.route("/api/v1.0/precipitation")
# if I run it here it gives me this :
# %%
#create the precipitation() function.
def precipitation():
    return
# %%
#add a line of code that calculates the date one year ago 
# from the most recent date in the database
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   return
# %%
# get the date and precipitation for the previous year. Add this query to your existing code.

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return
# %%
#jsonify
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
# %%
# define the route and route name for a list of all the stations
@app.route("/api/v1.0/stations")
# %%
#create a new function called stations()
def stations():
    return
# %%
#create a query that will allow us to get all of the stations in the database
def stations():
    results = session.query(Station.station).all()
    return
# %%
#unraveling the results into a one-dimensional array.
#use thefunction np.ravel(), with results as our parameter
# Next convert unraveled results into a list and jsonify
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# %%
#defining the route for Temperature observations
@app.route("/api/v1.0/tobs")
# %%
#create a function called temp_monthly()
def temp_monthly():
    return
# %%
#calculate the date one year ago from the last date in the database
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return
# %%
#query the primary station for all the temperature observations from the previous year
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    return
# %%
# unravel the results into a one-dimensional array
# convert that array into a list
# jsonify the list and return the results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# %%
# to see the minimum, maximum, and average temperatures.
# provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# %%
#create a function called stats()
def stats():
     return
# %%
# add parameters to the stats()function: a start parameter and an end parameter. 
# For now, set them both to None
def stats(start=None, end=None):
     return
# %%
# create a query to select the minimum, average, and maximum temperatures from teh SQLite db
# start by just creating a list called sel
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
# %%
# need to determine the starting and ending date, add an if-not statement
# unravel the results into a one-dimensional array and convert them to a list
# jsonify our results and return them
#  the asterisk is used to indicate there will be multiple results for the query
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
# %%
# calculate the temperature minimum, average, and maximum with the start and end dates
# use the sel list, which is simply the data points we need to collect
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# %%
# After running this code, we'll be able to copy and paste the web address provided by Flask into a web browser. 
# Open /api/v1.0/temp/start/end route and check to make sure you get the correct result, which is:
# [null,null,null]
# This code tells us that we have not specified a start and end date for our range. 
# fix this by entering any date in the dataset as a start and end date. 
# The code will output the minimum, maximum, and average temperatures. i.e find the minimum, maximum, and average temperatures for June 2017. 
# add         /api/v1.0/temp/2017-06-01/2017-06-30             to the address in the web browser
# When you run the code, it should return the following result: ["temps":[71.0,77.21989528795811,83.0]]

