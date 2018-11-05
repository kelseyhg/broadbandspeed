# Who Gets the Internet?

This site visualizes inequality of broadband internet access in the US.
Visit the prototype at: (https://broadband-speed.herokuapp.com/)

## Technologies and Tools

The site is built on a Django framework.

Python scripts gather speed information from the [National Broadband Map](https://www.broadbandmap.gov) and write to a database and a geoJSON file.

Leaflet maps, overlaid with a modified version of [this](http://eric.clst.org/tech/usgeojson/) geoJSON file containing US county polygons, created by Eric Celeste.

CSS animations illustrate the problems with slow internet connections.
	
## Stills

![stats](/cap-1.png "Learn about broadband access")

![map](/cap-2.png "Visualize broadband speed across the country")

![comparison](/cap-3.png "Compare two counties' speeds")


## Issues
* Broadband speeds are outdated; API should be replaced in 2019
* Several Indiana counties are missing from the database
* Median broadband speed is missing from over 200 counties on the map; some of this is due to incomplete data from the API



















