import json
import re
from playwright.sync_api import Page, Route
from time import sleep


def test_listen(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = "Яблокофон 16"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
    page.route(re.compile('/step0_iphone/digitalmat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    sleep(2)
    iphone_16 = page.locator("//button[@data-index='1']")
    iphone_16.click()
    sleep(10)
