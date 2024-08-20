import pytest
from endpoints.create_post import CreatePost
from endpoints.update_object import UpdatePost
from endpoints.patch_post import PatchPost
from endpoints.get_all_object import GetAllObject
from endpoints.get_object_by_id import GetObjectById


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_object_endpoint():
    return PatchPost()


@pytest.fixture()
def get_all_object_endpoint():
    return GetAllObject()


@pytest.fixture()
def get_object_by_id_endpoint():
    return GetObjectById()
