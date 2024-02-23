from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate_to(self, URL):
        self.page.goto(URL)

