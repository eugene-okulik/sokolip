import requests
import pytest


@pytest.fixture(scope='session')
def start_end():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.mark.critical
def test_all_posts(start_end):
    print('before test')
    url = 'https://api.restful-api.dev/objects'
    response = requests.get(url).json()
    assert len(response) == 13, 'Wrong amount'
    print('after test')


def test_post_by_id():
    print('before test')
    post_id = '3'
    post_id_2 = '5'
    post_id_3 = '10'
    response = requests.get(f'https://api.restful-api.dev/objects?id={post_id}&id={post_id_2}&id={post_id_3}').json()
    assert response[0]['id'] == post_id, 'Wrong post_id'
    assert response[1]['id'] == post_id_2, 'Wrong post_id_2'
    assert response[2]['id'] == post_id_3, 'Wrong post_id_3'
    print('after test')


@pytest.mark.medium
def test_one_post():
    print('Start testing')
    post_id = '7'
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}').json()
    assert response['id'] == post_id, 'Wrong post id'
    print('after test')


@pytest.mark.parametrize("body", (
                {
                    "name": "Apple MacBook Pro 16",
                    "data": {
                        "year": 2019,
                        "price": 1849.99,
                        "CPU model": "Intel Core i9",
                        "Hard disk size": "1 TB"
                    }
                },
                {
                    "name": "Apple MacBook Pro 17",
                    "data": {
                        "year": 2019,
                        "price": 1849.99,
                        "CPU model": "Intel Core i9",
                        "Hard disk size": "1 TB"
                    }
                },
                {
                    "name": "Apple MacBook Pro 19",
                    "data": {
                        "year": 2019,
                        "price": 1849.99,
                        "CPU model": "Intel Core i9",
                        "Hard disk size": "1 TB"
                    }
                }

                                )
                        )
def test_add_object(body):
    print('before test')
    url = 'https://api.restful-api.dev/objects'
    body = body
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url,
                             json=body,
                             headers=headers
                             )
    assert response.status_code == 200, 'Wrong status code'
    print('after test')


@pytest.fixture()
def new_post_id():
    url = 'https://api.restful-api.dev/objects'
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url,
                             json=body,
                             headers=headers
                             )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('Deleting the post id')
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def test_put_object(new_post_id):
    print('before test')
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{new_post_id}',
                            json=body,
                            headers=headers
                            ).json()
    assert response['updatedAt'] is not None, 'Not updated'
    print('after test')


def test_patch_object(new_post_id):
    print('before test')
    update_name = '"Apple MacBook Pro 16 (Updated Name)"'
    body = {
        "name": update_name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{new_post_id}',
                              json=body,
                              headers=headers
                              ).json()
    assert response['name'] == update_name, 'Not updated with PATCH'
    print('after test')


def test_delete_post(new_post_id):
    print('before test')
    url = f'https://api.restful-api.dev/objects/{new_post_id}'
    response = requests.delete(url)
    assert response.status_code == 200
    print('after test')


print('Testing completed')
