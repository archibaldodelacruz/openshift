# SAVITHRUs WEB-BASED LOCATION APP
A simple asynchronous web-application used to fetch your current physical location & display it on Google Maps. Also capable of providing relevant location data such as latitude, longitude, zip code for a given physical address (Also takes keywords, _Eg. Statue of Liberty_). There is also a REST API that users can access & currently provides address-to-coordinate-mapping. 

**PACKAGES REQUIRED**

* [Flask-GoogleMaps](http://flask.pocoo.org)
* [Tornado](http://www.tornadoweb.org/en/stable/)
* [Requests](http://docs.python-requests.org/en/master/)
* [Virtualenv](https://virtualenv.readthedocs.org/en/latest/)
* [Git](https://git-scm.com)

**PROJECT RESOURCES**

* [Screenshots](https://github.com/savithruml/LocationWebApp/tree/master/screenshots)
* [Video-Tutorial](https://www.youtube.com/watch?v=Z1ecUJtr2zU)
* [Project-Site](http://savithruml.github.io/LocationWebApp)

### INSTALLATION<br />

**NOTE:** These steps are for a machine running on Ubuntu 14.04 LTS (or any other Debian flavored OS).

* Install Python 3 or later & update<br /><br />`# sudo apt-get install python3`<br />`# sudo apt-get update`<br />  
* Install git & clone this repository containing the source<br /><br />`# sudo apt-get install git && cd ~`<br />`# git clone https://github.com/savithruml/LocationWebApp.git`<br /><br />
* Create an isolated environment to run our application. We will use python package called Virtualenv. The main purpose of using a virtual environment is to prevent Python3.X dependencies from interfering with those of Python2.X<br /><br />`# sudo apt-get install python-virtualenv`<br />`# virtualenv -p /usr/bin/python3 ~/LocationWebApp`<br />`# cd ~/LocationWebApp && source bin/activate`<br /><br />
* Once in the Virtual-Environment, install Python 3.X dependencies<br /><br />`(virtualEnv)# pip install tornado requests flask-googlemaps`

### RUN
The repository contains **TWO** executables,
* [flaskApp.py](https://github.com/savithruml/LocationWebApp/blob/master/flaskApp.py) contains the code for defining the Application service
* [serve.py](https://github.com/savithruml/LocationWebApp/blob/master/serve.py) contains the code for running the Application service on a server

Run the Application <br /><br />`(virtualenv)# python serve.py <port-number>`<br />_`Eg. python serve.py 8080`_<br /><br />All the log information is present in `locationApp.log`

### ACCESS

#### Access through a Web-Browser
* Open a web-browser & enter<br /><br />`http://<server-ip-address>:<port-number>`<br />_`Eg. http://localhost:8080`_<br /><br />
* Allow/Block the browser to access your location 
* Based on the previous step, you'll either be given the current location information or will be directed to a default page

#### Access through API
* To get the location data of a place (Latitude, Longitude, zip-code), open the web-browser & enter the URL in the following syntax,<br /><br />`http://<server-ip-address>:<port-number>/api/<place-or-address>`<br />_`Eg. http://localhost:8080/api/statue-of-liberty`_<br /><br />**NOTE:** Make sure to separate the address with "-" (_hyphen_)<br /><br />
* Alternatively, install [**_curl_**](https://curl.haxx.se/), an open-source tool for transferring data with URL syntax. You can install curl from the command line<br /><br /> `# sudo apt-get install curl`<br /><br />Get the location data using curl<br /><br />`# curl -i http://server-ip-address:<port-number>/api/<place-or-address>`<br />_`Eg. curl -i http://localhost:8080/api/statue-of-liberty`_<br /><br />**NOTE:** Make sure to separate the address with "-" (_hyphen_)<br /><br />
* The outformat of the location data is currently in **JSON** format

### MEASURE

* Measure the application's performance using [Apache Bench](https://httpd.apache.org/docs/2.2/programs/ab.html). This tool provides vital HTTP information such as requests handled/s, connection times, percentage of requests, etc. Install the tool<br /><br />`# sudo apt-get install apache2-utils`<br /><br />Run a benchmark test to determine the performance characteristics of the application.<br /><br />`# ab -n <requests> -c <concurrency> http://<server-ip-address>:<port-number>`<br />_`Eg. ab -n 50 -c 5 http://localhost:8080/ > ab-test.txt`_<br /><br />The results of my test-run can be found in [ab-test.txt](https://github.com/savithruml/LocationWebApp/blob/master/ab-test.txt) 

### AUTHOR
Savithru Lokanath (@savithruml)<br />
Date: 02/27/2016

### CONTACT
E-Mail: savithru@icloud.com
