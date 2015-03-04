import urllib2
import simplejson
import sys

url = 'https://api.foursquare.com/v2/venues/explore'
location = '44.3,37.2'

date = '20150304'

full_url = url + '?ll=' + location + '&oauth_token=' + oauth_token + '&v=' + date

req  = urllib2.Request(full_url)
opener = urllib2.build_opener()
f = opener.open(req)

fsdata = simplejson.load(f)
