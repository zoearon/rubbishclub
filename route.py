from urllib2 import urlopen
from json import load
import pprint
import os

APIKEY = os.environ['TOM_TOM_KEY']


def calculate_route(lst_of_coordinates):
    """ Given list of coordinates, returns optimized list of middle points """

    coordinates_str = ':'.join(lst_of_coordinates)

    url = 'https://api.tomtom.com/routing/1/calculateRoute/{}/json?key={}&computeBestOrder=true&routeType=shortest'.format(coordinates_str, APIKEY)

    response = urlopen(url)
    json_obj = load(response)
    # json_obj = pprint.pprint(json_obj)
    optimized_pts_lst = json_obj['optimizedWaypoints']

    #not including start and stop i.e. lst_of_coordinates[0], lst_of_coordinates[-1]
    ordered_pts_dict = {}

    for index_point_dict in optimized_pts_lst:
        optimized_index = index_point_dict['optimizedIndex']
        #since the optimized points lst does not include start and stop,
        #indices given will be one less than the original list of coordinates
        #i.e.      [start, 0, 1, 2, 3, end]
        #original: [(start)0, 1, 2, 3, 4, (end)5]
        original_index = index_point_dict['providedIndex'] + 1
        #getting the coordinates from the original list
        #(since we were only given indices from the request)
        coordinate_value = lst_of_coordinates[original_index]
        ordered_pts_dict[optimized_index] = coordinate_value

    pairs = ordered_pts_dict.items()
    sorted_pairs = sorted(pairs)

    optimized_route = []

    for pair in sorted_pairs:
        #append the coordinates which is pair[1]
        optimized_route.append(pair[1])


    return optimized_route




start = '52.50931,13.42936'
end = '52.50930,13.4456'
lst_of_coordinates = [start, '52.50274,13.43872', '52.50200,13.42900', '52.50274,13.43872', '52.50400,13.43870', end]
print calculate_route(lst_of_coordinates)

