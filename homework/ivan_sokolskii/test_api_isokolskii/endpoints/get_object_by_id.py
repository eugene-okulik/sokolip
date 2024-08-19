from test_api_isokolskii.endpoints.endpoint import Endpoint
import allure
import requests


class GetObjectById(Endpoint):
    def get_object_by_id(self, post_ids, headers=None):
        headers = headers if headers else self.headers
        query_params = '&'.join([f'id={post_id}' for post_id in post_ids])
        self.response = requests.get(
            url=f'{self.url}?{query_params}'
        )
        response = self.response.json()
        print(response)
        for i, post_id in enumerate(post_ids):
            assert response[i].get('id') == str(post_id), f'Wrong post_id for object {i}'
