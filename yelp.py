import rauth
import time
import keys

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

def beginYelpFetch(latIn, longIn):    
  locations = [(latIn, longIn)]
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
