import pprint

import pytest
import requests
from api_testing import URL_DOG_CEO


# positive
def test_all_dogs():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    pprint.pprint(response.status_code)
    for breed in response.json(response):
        response = requests.get('https://dog.ceo/api/breeds/list/' + breed)
        assert response.status_code == 200


def test_url_images():
    response = requests.get(f'{URL_DOG_CEO}/breeds/list/all')
    lists = response.json(response)
    message = lists['message']
    for breed in message:
        response = requests.get(f'{URL_DOG_CEO}/breed/' + breed + '/images')
        response_json = response.json(response)
        assert 'message' in response_json
        assert len(response_json['message']) > 0
        assert response.status_code == 200
        for image_url in response_json['message']:
            response = requests.get(image_url)
            assert response.status_code == 200
            assert 'image/jpeg' == response.headers.get('content-type')


def test_random_dogs():
    response = requests.get(f'{URL_DOG_CEO}/breeds/list/all')
    lists = response.json(response)
    message = lists['message']
    for breed in message:
        response = requests.get('https://dog.ceo/api/breed/' + breed + '/images/random')
        assert response.status_code == 200


def test_random_three_images():
    response = requests.get(f'{URL_DOG_CEO}/breeds/list/all')
    lists = response.json(response)
    message = lists['message']
    for breed in message:
        response = requests.get('https://dog.ceo/api/breed/' + breed + '/images/random/3')
        assert response.status_code == 200


def test_url_sub_breeds():
    response = requests.get(f'{URL_DOG_CEO}/breeds/list/all')
    lists = response.json(response)
    breeds = lists['message']
    for breed in breeds:
        url = 'https://dog.ceo/api/breed/' + breed + '/list'
        response = requests.get(url)
        subbreed1 = breeds[breed]
        subbreed = response.json(response)['message']
        assert len(subbreed1) == len(subbreed)
        assert response.status_code == 200


# negative

@pytest.mark.parametrize('breed, codeResponse',
                         [
                             ('7689', 404),
                             ('корги', 404),
                             ('*%!&@', 404),
                             ('zuzuzuzuzzzuuu', 404)

                         ])
def test_dogs_negative_type(breed, codeResponse):
    response = requests.get('https://dog.ceo/api/breed/' + breed + '/images')
    assert response.status_code == codeResponse
