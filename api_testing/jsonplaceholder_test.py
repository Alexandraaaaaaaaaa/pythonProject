import pytest
import requests
from api_testing import URL_JSONPLACEHOLDER


@pytest.mark.parametrize('id',
                         [
                             '1',
                             '3',
                             '99',
                             '100'
                         ],
                         ids=["bottom_line", "middle", "near_border", "upper_bound"]
                         )
def test_resources_posts(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/posts/' + id)
    assert response.status_code == 200
    post = response.json(response)
    assert 'userId' in post
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post
    assert len(post) == 4


@pytest.mark.parametrize('id',
                         [
                             '50',
                             '3',
                             '1',
                             '499',
                             '500'
                         ])
def test_resources_comments(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/comments/' + id)
    assert response.status_code == 200
    comments = response.json(response)
    assert 'postId' in comments
    assert 'id' in comments
    assert 'name' in comments
    assert 'email' in comments
    assert 'body' in comments


@pytest.mark.parametrize('id',
                         [
                             '40',
                             '9',
                             '1',
                             '99',
                             '100'
                         ])
def test_resources_albums(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/albums/' + id)
    assert response.status_code == 200
    album = response.json(response)
    assert 'userId' in album
    assert 'id' in album
    assert 'title' in album


@pytest.mark.parametrize('id',
                         [
                             '30',
                             '8',
                             '1',
                             '4999',
                             '5000'
                         ])
def test_resources_photos(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/photos/' + id)
    assert response.status_code == 200
    photo = response.json(response)
    assert 'albumId' in photo
    assert 'id' in photo
    assert 'title' in photo
    assert 'url' in photo
    assert 'thumbnailUrl' in photo



@pytest.mark.parametrize('id',
                         [
                             '18',
                             '5',
                             '1',
                             '199',
                             '200'
                         ])
def test_resources_todos(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/todos/' + id)
    assert response.status_code == 200
    do = response.json(response)
    assert 'userId' in do
    assert 'id' in do
    assert 'title' in do
    assert 'completed' in do


@pytest.mark.parametrize('id',
                         [
                             '4',
                             '8',
                             '1',
                             '9',
                             '10'
                         ])
def test_resources_users(id):
    response = requests.get(URL_JSONPLACEHOLDER + '/users/' + id)
    assert response.status_code == 200
    user = response.json(response)
    assert 'id' in user
    assert 'name' in user
    assert 'username' in user
    assert 'email' in user
    assert 'address' in user
    assert 'phone' in user
    assert 'website' in user
    location = user['address']
    assert 'street' in location
    assert 'suite' in location
    assert 'city' in location
    assert 'zipcode' in location
    assert 'geo' in location
    geo = location['geo']
    assert 'lat' in geo
    assert 'lng' in geo
    assert 'company' in user
    company = user['company']
    assert 'name' in company
    assert 'catchPhrase' in company
    assert 'bs' in company