import urllib2
import simplejson
import sys

class FoursquareStats:
    def __init__(self, name, lat, lng, checkins):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.checkins = checkins
    def __str__(self):
        return 'Location Name: ' + self.name + "\n" + "Latitude: " + `self.lat` + "\n" + "Longitude: " + `self.lng` + "\n" + "Checkins: " + `self.checkins` + "\n"
    def businessName(self):
        return self.name
    def businessLocation(self):
        return (self.lat, self.lng)
    def businessCheckins(self):
        return self.checkins


url = 'https://api.foursquare.com/v2/venues/search'
location = '40.7,-74'
client_id = '***REMOVED***'
client_secret = '***REMOVED***'
results = 50
date = '20150306'
businesses = []

full_url = url + '?ll=' + location + '&limit=' + `results` + '&client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date

req  = urllib2.Request(full_url)
opener = urllib2.build_opener()
f = opener.open(req)

fsdata = simplejson.load(f)

for i in range(0,results):
    businesses.append(FoursquareStats(fsdata['response']['venues'][i]['name'],
    fsdata['response']['venues'][i]['location']['lat'],
    fsdata['response']['venues'][i]['location']['lng'],
    fsdata['response']['venues'][i]['stats']['checkinsCount']))

businesses.sort(key= lambda x: x.checkins, reverse=True)

for j in range(0, len(businesses)):
    print businesses[j]
