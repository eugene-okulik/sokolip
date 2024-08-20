from endpoints.endpoint import Endpoint
import allure
import requests


class PatchPost(Endpoint):
    @allure.step('Create new object')
    def add_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        post_id = self.response.json()['id']
        return post_id

    @allure.step('Change part of object')
    def change_part_object(self, post_id, headers=None):
        headers = headers if headers else self.headers
        update_name = '"Apple MacBook Pro 19 (Updated Name)"'
        body = {
            "name": update_name
        }
        self.response = requests.patch(
            url=f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        response = self.response.json()
        assert response['name'] == update_name, 'Not updated with PATCH'

    @allure.step('Delete object')
    def delete_object(self, post_id):
        url = f'{self.url}/{post_id}'
        self.response = requests.delete(url)
