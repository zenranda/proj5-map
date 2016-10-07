# README #

###CS322 Project 2: Flask Syllabus###
###Author: Marc Leppold###

##Project Notes

The second project of CS322. A syllabus that's date-aware, built with Flask. Reads a text file to get the term's schedule, then formats it into a html file. Pipes in the date the schedule provides as a starting time and changes it to match each week with the arrow framework. The current week will be highlighted. Acts as a server, accepts incoming connections and serves them the syllabus.

Scalable, can adapt to any positive number of weeks. Please note that the schedule file requires a certain formatting to be read accurately, consult schedule.txt to get an idea of the syntax.

Utilizes Flask, Jinja2, arrow, gunicorn, itsdangerous, MarkupSafe, python-dateutil, six, Werkzeug and wheel. All of the above are supplied with pyvenv.

### USAGE ###

Execute flask_syllabus.py, then enter 
```
HOST:PORT
```
into an internet browser, where HOST matches the IP address of the host computer and PORT matches the port the server is running on (default 5000). Note that there are various dependancies that will likely require executing pyvenv first, notably Flask and arrow.

Can be executed via automated configure and makefile scripts as well:
```
git clone https://github.com/zenranda/proj2-flask InstallDirectory
cd InstallDirectory
make configure
make run
```
where InstallDirectory is the directory you cloned the files to.