import json
import urllib2
import simplejson
import sys
from flask import Flask
from flask import request

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

# Please remove API keys before pushing to Github

app = Flask(__name__)

results = 50
date = '20150311'
query = ""

# Pull foursquare categories API to allow users to search
# for business within certain categories


# Flask section
# Program should make an API once visit the site
@app.route("/")
def test():
    if 'q' in request.args:
        return "We are all good " + request.args['q']
    else:
        return "We are all good!"

@app.route('/businesses')
def foursquare_stats():

    businesses = []
    search_url = 'https://api.foursquare.com/v2/venues/search'
    category = ""
    #Location will be set by the user
    if 'location' in request.args:
        location = request.args['location']
        if 'c' in request.args:
            category = request.args['c']
            categoryId = foursquareCategoriesLookup(category)
            full_search_url = search_url + '?ll=' + location + '&limit=' + `results` + '&client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date + '&categoryId=' + categoryId
        else:
            full_search_url = search_url + '?ll=' + location + '&limit=' + `results` + '&client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date
    else:
        return "Location has not been set."

    req = urllib2.Request(full_search_url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    fsdata = simplejson.load(f)

    for location in fsdata['response']['venues']:
        businesses.append(FoursquareStats(location['name'],
        location['location']['lat'],
        location['location']['lng'],
        location['stats']['checkinsCount']))

    return json.dumps([p.__dict__ for p in businesses])

def foursquareCategoriesLookup(category):
    categoriesStore = {}
    categories_url = 'https://api.foursquare.com/v2/venues/categories'
    full_categories_url = categories_url + '?client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date

    req  = urllib2.Request(full_categories_url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    fsdata = simplejson.load(f)

    for categories in fsdata['response']['categories']:
        categoriesStore[categories['name']] = categories['id']
        for subCategories in categories['categories']:
            categoriesStore[subCategories['name']] = subCategories['id']

    return categoriesStore[category]

@app.route('/categories')
def foursquare_categories():

    categoriesStore = {}
    categories_url = 'https://api.foursquare.com/v2/venues/categories'
    full_categories_url = categories_url + '?client_id=' + client_id + '&client_secret=' + client_secret + '&v=' + date

    req  = urllib2.Request(full_categories_url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    fsdata = simplejson.load(f)

    for categories in fsdata['response']['categories']:
        categoriesStore[categories['name']] = categories['id']
        for subCategories in categories['categories']:
            categoriesStore[subCategories['name']] = subCategories['id']

    return json.dumps(categoriesStore)

if __name__ == '__main__':
    app.run(debug=True)
