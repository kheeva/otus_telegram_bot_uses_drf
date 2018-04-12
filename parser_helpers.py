import requests


def fetch_otus_json_data(query):
    url = 'http://94.243.167.227:8000/api/courses/'
    params = {
        'fields': 'title,price,img_url',
        'search': query,
    }

    drf_response = requests.get(url=url, params=params)

    return drf_response.json()


def calc_avg_price(courses):
    return sum([course['price'] for course in courses])/len(courses)


def get_first_image_url_from_results(courses):
    return courses[0]['img_url'].strip()
