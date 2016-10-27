import flask
from flask import render_template
from flask import request
from flask import url_for

import json
import logging

# Date handling 
import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times

# Our own module
import pre  # Preprocess schedule file


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

