# -*- coding: utf-8 -*-

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import forecastio
from geopy.geocoders import Nominatim
import os
from random import randint

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

address="12345"


# def get_weather(address):
# 	FORECASTIO_API_KEY =os.environ['FORECASTIO_API_KEY']
# 	geolocator = Nominatim()
# 	location = geolocator.geocode(address)
# 	forecast = forecastio.load_forecast(FORECASTIO_API_KEY, location.latitude, location.longitude).currently()
# 	summary = forecast.summary
# 	temperature = forecast.temperature
# 		# return "{} and {} degrees".format(forecast.summary, forecast.temperature)


def search_food(address):
	auth = Oauth1Authenticator(
    	consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ['TOKEN'],
    	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	FORECASTIO_API_KEY =os.environ['FORECASTIO_API_KEY']

	# print("What term are you looking for?")

	# term_input=raw_input()

	# print("And around what address are you looking at?")

	# area=raw_input()

	# print("Looking for {} in {}".format(term_input, area))

	params = {
    	'term': 'bar',
    	'radius_filter': 1200,
    	'lang': 'en'
		}

	response = client.search(address, **params)
	

	businesses_list = []


	for business in response.businesses:
		if business.rating>=3.5:
			businesses_list.append({"name": business.name, 
			"rating": business.rating, 
			"phone": business.phone
		})

	# Select a random number from the list of businesses
	

	rannum = randint(0,len(businesses_list)-1)
	# print("Cool! Beep boop beep beep boop....")
	# print("calculating...")
	# print("calculating...")
	# print("calculating...")
	# print("Out of {} businesses I am choosing number {}".format(len(businesses_list),rannum))
	

	# Caclulate weather at random selected resturant
	# def get_address(buisnessname):
	# 	location = geolocator.geocode(buisnessname)
	# 	print(location)



	# Select a random business from the business list, using the random int generated above
	return "Check out {}! \n Phone number is {}".format(businesses_list[rannum].get('name'),businesses_list[rannum].get('phone'))



search_food(address)
