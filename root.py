from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'http://localhost/about'


def get_location_name(span):
    try:
        span = span[0]
        print(span.get_text())
        return span.get_text().replace('\n','')
    except:
        return ''


def get_location_address(span):
    try:
        span = span[0]
        return span.get_text().replace('\n','')
    except:
        return ''


def get_coordinates(span):
    try:
        span = span[0]
        url = str(span['href']).split('=')
        lat, lng = url[2].split(',')
        print(lat,lng)
        return {
            "Latitude"  : lat,
            "Longitude" : lng
        }
    except:
        return {
            "Latitude": 0.0,
            "Longitude": 0.0
        }


def get_price(span):
    try:
        price_list = []
        capacity = span[0].get_text()
        capacity =capacity.replace('\n',"-").split('-')
        for val in capacity:
            val = val.replace(' ','')
            if val.isnumeric():
                price_list.append(val)

        print(price_list)
        price_dict = {}
        price_dict['Car'] = price_list[0]
        if len(price_list) == 2:
            price_dict['Bike'] = price_list[1]
        return price_dict
    except:
        return {}



try:
    location_dict = {}
    locations = []
    resp = urlopen(URL)
    soup = BeautifulSoup(resp, features="html.parser")
    for val in soup.find_all("li", class_="list-group-item"):
        print("------------------------------")
        location_dict['Name'] = get_location_name(val.find_all("span", class_="name"))
        location_dict['Address'] = get_location_address(val.find_all("p"))
        location_dict["Price"] = get_price(val.find_all("div", class_="col-md-3"))
        location_dict['"Coordinates'] = get_coordinates(val.find_all("a"))
        locations.append(location_dict)
        print("------------------------------")

    print(locations)

except Exception as ex:
    print(ex)
