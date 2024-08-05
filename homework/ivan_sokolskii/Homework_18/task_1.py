import requests


def all_posts():
    url = 'https://api.restful-api.dev/objects'
    response = requests.get(url).json()
    assert len(response) == 13, 'Wrong amount'


def post_by_id():
    post_id = '3'
    post_id_2 = '5'
    post_id_3 = '10'
    response = requests.get(f'https://api.restful-api.dev/objects?id={post_id}&id={post_id_2}&id={post_id_3}').json()
    assert response[0]['id'] == post_id, 'Wrong post_id'
    assert response[1]['id'] == post_id_2, 'Wrong post_id_2'
    assert response[2]['id'] == post_id_3, 'Wrong post_id_3'


def one_post():
    post_id = '7'
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}').json()
    assert response['id'] == post_id, 'Wrong post id'


def add_object():
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
    assert response.status_code == 200, 'Wrong status code'


def new_object():
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
    return response.json()['id']


def clear_data(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def put_object():
    post_id = new_object()
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
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}',
                            json=body,
                            headers=headers
                            ).json()
    assert response['updatedAt'] is not None, 'Not updated'
    clear_data(post_id)


def patch_object():
    post_id = new_object()
    update_name = '"Apple MacBook Pro 16 (Updated Name)"'
    body = {
        "name": update_name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}',
                              json=body,
                              headers=headers
                              ).json()
    assert response['name'] == update_name, 'Not updated with PATCH'
    clear_data(post_id)


def delete_post():
    post_id = new_object()
    url = f'https://api.restful-api.dev/objects/{post_id}'
    response = requests.delete(url)
    assert response.status_code == 200


all_posts()
post_by_id()
one_post()
add_object()
put_object()
patch_object()
delete_post()
