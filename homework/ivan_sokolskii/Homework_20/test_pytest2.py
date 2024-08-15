import requests
import pytest
import allure


@pytest.fixture(scope='session')
def start_end():
    print('Start testing')
    yield
    print('Testing completed')


@allure.feature('Post')
@pytest.mark.critical
def test_all_posts(start_end):
    print('before test')
    url = 'https://api.restful-api.dev/objects'
    with allure.step('Run get request for all posts'):
        response = requests.get(url).json()
    assert len(response) == 13, 'Wrong amount'
    print('after test')


@allure.feature('Post by ID')
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


@allure.feature('Post generator')
@allure.story('Create post')
@pytest.mark.medium
def test_one_post():
    print('Start testing')
    post_id = '7'
    with allure.step('Create new post with id'):
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
    with allure.step('Check that status code is correct'):
        assert response.status_code == 200, 'Wrong status code'
    print('after test')


@allure.feature('Post')
@allure.story('Put post')
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


@allure.feature('Post changed')
@allure.story('Patch post')
@allure.title('Изменение объекта')
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


@allure.feature('Post changed')
@allure.story('Delete post')
@allure.title('Удаление поста')
def test_delete_post(new_post_id):
    print('before test')
    url = f'https://api.restful-api.dev/objects/{new_post_id}'
    response = requests.delete(url)
    assert response.status_code == 200
    print('after test')


print('Testing completed')
