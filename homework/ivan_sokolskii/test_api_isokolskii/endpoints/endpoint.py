import allure
import requests
import pytest


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_than_status_is_200(self):
        assert self.response.status_code == 200
