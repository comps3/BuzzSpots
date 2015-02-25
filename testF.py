import foursquare
import json

client_i = "***REMOVED***"
client_s = "***REMOVED***"

# Construct the client object
client = foursquare.Foursquare(client_id=client_i, client_secret=client_s)

print client.venues.stats('40a55d80f964a52020f31ee3')
