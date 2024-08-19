from test_api_isokolskii.endpoints.endpoint import Endpoint
import allure
import requests


class GetAllObject(Endpoint):
    @allure.step('Get all object')
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=self.url
        )
        response = self.response.json()
        assert len(response) == 13, 'Wrong amount'
