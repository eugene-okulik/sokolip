from locust import task, HttpUser
import random


class AllProducts(HttpUser):
    headers = {'Content-Type': 'application/json'}

    @task
    def get_all_product(self):
        self.client.get(
            '/posts'
        )

    @task
    def get_one_product(self):
        self.client.get(
            f'/posts/{random.choice([3, 5, 10])}'
        )

    @task
    def post_product(self):
        self.client.post(
            '/posts',
            json={
                'title': 'foo',
                'body': 'bar',
                'userId': 1,
            },
            headers={
                'Content-type': 'application/json; charset=UTF-8'
            }
        )

    @task
    def put_product(self):
        self.client.put(
            '/posts/1',
            json={
                'id': 1,
                'title': 'foo',
                'body': 'bar',
                'userId': 1,
            },
            headers={
                'Content-type': 'application/json; charset=UTF-8'
            }
        )

    @task
    def patch_product(self):
        self.client.patch(
            '/posts/1',
            json={
                'title': 'foo',
            },
            headers={
                'Content-type': 'application/json; charset=UTF-8'
            }
        )

    @task
    def delete_product(self):
        self.client.delete(
            '/posts/1'
        )

    @task
    def get_comments(self):
        self.client.get(
            '/posts/1/comments'
        )
