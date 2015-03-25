"""
Name: Brian Huynh & Jose Maqueda
Date: 3/25/2015
Title: yelp.py
Abstract: Program creates functions in order to retrieve the information from yelp, using yelps API.
The information it retrieves returns business information from yelp.

"""

import rauth
import time
import keys

def get_search_parameters(name,lat, lng):
  # See the Yelp API for more details
  params = {}
  params["term"] = name
  params['ll'] = "{},{}".format(str(lat), str(lng))
  params["limit"] = "1"
  print params
  return params


def get_results(params):

  # Obtain these from Yelp's manage access page
  # Pulls keys from keys python file
  consumer_key = keys.YELP_CONSUMER_KEY
  consumer_secret = keys.YELP_CONSUMER_SECRET
  token = keys.YELP_TOKEN
  token_secret = keys.YELP_TOKEN_SECRET

    # Obtain these from Yelp's manage access page
  consumer_key =keys.YELP_CONSUMER_KEY
  consumer_secret = keys.YELP_CONSUMER_SECRET
  token = keys.YELP_TOKEN
  token_secret = keys.YELP_TOKEN_SECRET

  session = rauth.OAuth1Session(
    consumer_key=consumer_key
    , consumer_secret=consumer_secret
    , access_token=token
    , access_token_secret=token_secret)

  request = session.get("http://api.yelp.com/v2/search", params=params)

  # Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
  return data

def beginYelpFetch(name,latIn, longIn):
  locations = [(latIn, longIn)]
  api_calls = []
  for lat, lng in locations:
    params = get_search_parameters(name,lat, lng)
    api_calls.append(get_results(params))
    # Be a good internet citizen and rate-limit yourself
    #time.sleep(1.0)

  # #Do other processing
  return api_calls


if __name__ == "__main__":
    main()
