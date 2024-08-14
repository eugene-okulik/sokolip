import pytest
import requests


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
