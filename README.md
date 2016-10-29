# README #

###CS322 Project 5: Leaflet Map###
###Author: Marc Leppold###

##Project Notes

The fifth project in CS322. An interactive map using an outside API, in this case Leaflet. Functionality is very basic; it centers on the Eugene, Oregon area and populates it with pins on 4 locations of interest. The locations are read from an external POI.txt file, for modularity and ease of modification. It's easy to add new locations of interest to be added if you modify POI.txt - though be wary of the syntax; it's NAME|LATITUDE|LONGITUDE.

Requires an access token from MapBox in order to get map data - this program is currently configured to read one from a file called SECRETS.txt in its directory. If you don't have a SECRETS.txt file in your directory, or if it doesn't contain a valid MapBox access token, this program will not work. If you wish to add your own SECRETS.txt, the syntax is just the access token, no extra characters or spaces.

### USAGE ###

Execute the following commands
```
git clone https://github.com/zenranda/proj5-map InstallDirectory
cd InstallDirectory
make configure
make run
```
where InstallDirectory is the directory you cloned the files to.

After you've ran it, enter
```
HOST:PORT
```
into an internet browser, where HOST is the host IP of the computer the program is running on and PORT is the port it's configured to (default 5000).
Please note that this program requires a constant internet connection in order to fetch map information.
