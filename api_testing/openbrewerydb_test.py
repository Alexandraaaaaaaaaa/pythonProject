import pytest
import requests
from api_testing import URL_OPENBREWERYDB


# positive
def test_get_single_brewery():
    response = requests.get(f'{URL_OPENBREWERYDB}/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')
    assert response.status_code == 200
    brewery_info = response.json(response)
    assert 'name' in brewery_info
    assert 'id' in brewery_info
    assert 'brewery_type' in brewery_info
    assert 'address_1' in brewery_info
    assert 'city' in brewery_info
    assert 'state_province' in brewery_info
    assert 'postal_code' in brewery_info
    assert 'country' in brewery_info
    assert 'longitude' in brewery_info
    assert 'latitude' in brewery_info
    assert 'phone' in brewery_info
    assert 'website_url' in brewery_info
    assert 'state' in brewery_info
    assert 'street' in brewery_info


@pytest.mark.parametrize('page',
                         [
                             '3',
                             '10',
                             '9'
                         ])
def test_list_breweries(page):
    response = requests.get(URL_OPENBREWERYDB + '/breweries?per_page=' + page)
    lists = response.json(response)
    assert len(lists) == int(page)


@pytest.mark.parametrize('city, codeResponse',
                         [
                             ('Norman', 200),
                             ('Austin', 200),
                             ('San Diego', 200),
                             ('Portland', 200),
                             ('Quilcene', 200)

                         ])
def test_breweries_by_city(city, codeResponse):
    response = requests.get(URL_OPENBREWERYDB + '/breweries?by_city=' + city + '&per_page=15')
    breweries = response.json(response)
    assert response.status_code == 200
    for brewery in breweries:
        c = brewery['city']
        assert c == city


@pytest.mark.parametrize('search',
                         [
                             '0759476d-8fed-46cc-abec-1cb02cbca0d6',
                             '189df38b-d6a6-40c0-917e-5b172be8d859',
                             '56dce899-ff23-4f0e-be56-05900ecac53e'
                         ])
def test_search_breweries(search):
    response = requests.get(URL_OPENBREWERYDB + '/breweries/search?query=' + search)
    assert response.status_code == 200
    result = response.json(response)
    assert len(result) == 1
    for brewery in result:
        id = brewery['id']
        assert id == search


def test_meta_request():
    attributes = ['page', 'total', 'per_page']
    response = requests.get(f'{URL_OPENBREWERYDB}/breweries/meta')
    meta = response.json(response)
    for attribute in attributes:
        assert attribute in meta
