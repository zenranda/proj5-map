# README #

###CS322 Project 5: Leaflet Map###
###Author: Marc Leppold###

##Project Notes

### USAGE ###

Execute flask_map.py, then enter 
```
HOST:PORT
```
into an internet browser, where HOST matches the IP address of the host computer and PORT matches the port the server is running on (default 5000). Note that there are various dependancies that will likely require executing pyvenv first, notably Flask and arrow.

Can be executed via automated configure and makefile scripts as well:
```
git clone https://github.com/zenranda/proj5-map InstallDirectory
cd InstallDirectory
make configure
make run
```
where InstallDirectory is the directory you cloned the files to.
