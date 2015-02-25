import foursquare
import json

client_i = "2KRQZ4TFG2QFUKHZ453PQBF4ZIYORQ2KDE0SY40INKYB0PJP"
client_s = "1EPZ1OFADQFWVKT41QE10G5C1C03QPM0BPLPXM0DOZLHS3FL"

# Construct the client object
client = foursquare.Foursquare(client_id=client_i, client_secret=client_s)

print client.venues.stats('40a55d80f964a52020f31ee3')
