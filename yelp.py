import rauth
import time
import json
<<<<<<< HEAD
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

=======

def get_search_parameters(lat, long):
  # See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat), str(long))
  params["radius_filter"] = "2000"
  params["limit"] = "10"
 
  return params 

def get_results(params):
 
  # Obtain these from Yelp's manage access page
  consumer_key = "YOUR_KEY"
  consumer_secret = "YOUR_SECRET"
  token = "YOUR_TOKEN"
  token_secret = "YOUR_TOKEN_SECRET"
   
>>>>>>> origin/master
  session = rauth.OAuth1Session(
    consumer_key=consumer_key
    , consumer_secret=consumer_secret
    , access_token=token
    , access_token_secret=token_secret)
<<<<<<< HEAD

  request = session.get("http://api.yelp.com/v2/search", params=params)

  # Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
  return data

def get_yelp_resturantData(name, lat, lng):
    print get_results(get_search_parameters(name, lat, lng))
=======
     
  request = session.get("http://api.yelp.com/v2/search", params=params)
   
  # Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
   
  return data

def main():
  locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
  api_calls = []
  for lat, long in locations:
    params = get_search_parameters(lat, long)
    api_calls.append(get_results(params))
    # Be a good internet citizen and rate-limit yourself
    time.sleep(1.0)
     
  # #Do other processing
  print api_calls


if __name__ == "__main__":
    main()
>>>>>>> origin/master
