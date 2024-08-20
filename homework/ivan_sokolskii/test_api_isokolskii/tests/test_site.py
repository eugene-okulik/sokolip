import pytest

TEST_DATA = (
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

NEW_BODY = (
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

POST_IDS = [3, 5, 10]


@pytest.mark.parametrize('body', TEST_DATA)
def test_add_object(create_post_endpoint, body):
    create_post_endpoint.new_object(body=body)
    create_post_endpoint.check_than_status_is_200()


def test_put_a_post(update_post_endpoint):
    post_id = update_post_endpoint.add_object(body=TEST_DATA[1])
    update_post_endpoint.make_changes_in_object(post_id, body=NEW_BODY)
    update_post_endpoint.delete_object(post_id)
    update_post_endpoint.check_than_status_is_200()


def test_patch_a_post(patch_object_endpoint):
    post_id = patch_object_endpoint.add_object(body=TEST_DATA[1])
    patch_object_endpoint.change_part_object(post_id)
    patch_object_endpoint.delete_object(post_id)
    patch_object_endpoint.check_than_status_is_200()


def test_get_all_object(get_all_object_endpoint):
    get_all_object_endpoint.get_all_objects()
    get_all_object_endpoint.check_than_status_is_200()


def test_get_object_by_id(get_object_by_id_endpoint):
    get_object_by_id_endpoint.get_object_by_id(post_ids=POST_IDS)
