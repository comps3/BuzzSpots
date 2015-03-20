import rauth
import time
import json
import keys


def get_search_parameters(name, lat, lng):
  # See the Yelp API for more details
  params = {}
  params["term"] = name
  params['cll'] = str(lat) + "," + str(lng)
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

def get_yelp_resturantData(name, lat, lng):
    print get_results(get_search_parameters(name, lat, lng))
