import requests
from random import randrange


def fetch_otus_json_data(query):
    url = 'http://94.243.167.227/api/courses/'
    params = {
        'fields': 'title,price,img_url',
        'search': query,
    }

    drf_response = requests.get(url=url, params=params)

    return drf_response.json()


def calc_avg_price(courses):
    return sum([course['price'] for course in courses])/len(courses)


def get_rnd_image_url_from_results(courses):
    #random_index = randrange(0, len(courses))
    print(courses[0]['img_url'])
    return courses[0]['img_url'].strip()
    #return 'http://images2.pics4learning.com/catalog/i/img_3436alligator.jpg'
    #return 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png'
    # return 'http://94.243.167.227:8000/media/Javascript.jpg'
    #return [i['img_url'] for i in courses if i['img_url']][0]
