import urllib2
import simplejson
import sys

# Stores each locations name, location and all time checkin count
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


search_url = 'https://api.foursquare.com/v2/venues/search'
categories_url = 'https://api.foursquare.com/v2/venues/categories'
location = '40.7,-74'

results = 50
categoriesC = 20
subCategories = 5
date = '20150307'
businesses = []
categoriesStore = {} # Dictionary
query = ""

full_search_url = search_url + '?ll=' + location + '&limit=' + `results` + '&client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date
full_categories_url = categories_url + '?client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date
"""
req  = urllib2.Request(full_search_url)
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
"""
# Pull foursquare categories API to allow users to search
# for business within certain categories

req  = urllib2.Request(full_categories_url)
opener = urllib2.build_opener()
f = opener.open(req)
fsdata = simplejson.load(f)

for categories in fsdata['response']['categories']:
    categoriesStore[categories['name']] = categories['id']
    #print "Name: " + categories['name']
    #print "ID: " + categories['id']
    for subCategories in categories['categories']:
        categoriesStore[subCategories['name']] = subCategories['id']
        #print "Subname: " + subCategories['name']
        #print "SubID: " + subCategories['id']
