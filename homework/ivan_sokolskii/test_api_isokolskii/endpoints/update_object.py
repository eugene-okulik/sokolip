from endpoints.endpoint import Endpoint
import allure
import requests


class UpdatePost(Endpoint):
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

    @allure.step('Update an object')
    def make_changes_in_object(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        json = self.response.json()
        assert json['updatedAt'] is not None, 'Not updated'

    @allure.step('Delete object')
    def delete_object(self, post_id):
        url = f'{self.url}/{post_id}'
        self.response = requests.delete(url)
