import flask
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG


###
# Pages
###

@app.route("/")
@app.route("/index")
@app.route("/map")
def index():
  app.logger.debug("Main page entry")
  if 'map' not in flask.session:
      app.logger.debug("Sending map file")
      
      
  app.logger.debug("Sending keys...")
  with open('SECRETS.txt') as key:      #sends access token to the page
    ent = ""                            #in theory, sensitive information
    for line in key:
        while ent == "":
            ent = line
    flask.session['confidental'] = ent
  
  
  app.logger.debug("Sending loc data...")
  with open('POI.txt') as points:
    data = []                       #reads the list of points
    for line in points:             
        item = []
        line = line.strip()
        k = line.split("|")
        item.append(k[0])        #puts each part of the point (name, lat, long) into a list
        item.append(k[1])
        item.append(k[2])
        data.append(item)        #adds the list with the data to another list
    flask.session['points'] = data  #sends that list to jinja
  return flask.render_template('map.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404


#############
#    
# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#
app.secret_key = CONFIG.secret_key
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)
if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

