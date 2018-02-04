from urllib2 import urlopen
from json import load
import pprint
import os

APIKEY = os.environ['TOM_TOM_KEY']


def calculate_route(lst_of_coordinates):
    """ Calculates route given a list of coordinates """

    coordinates_str = ':'.join(lst_of_coordinates)

    url = 'https://api.tomtom.com/routing/1/calculateRoute/{}/json?key={}&computeBestOrder=true&routeType=shortest'.format(coordinates_str, APIKEY)

    response = urlopen(url)
    json_obj = load(response)
    # json_obj = pprint.pprint(json_obj)
    optimized_pts = json_obj['optimizedWaypoints']
    return optimized_pts


lst_of_coordinates = ['52.50931,13.42936', '52.50274,13.43872', '52.50200,13.42900', '52.50274,13.43872', '52.50400,13.43870', '52.50930,13.4456']
print calculate_route(lst_of_coordinates)

