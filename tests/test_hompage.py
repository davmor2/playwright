import re
from playwright.sync_api import expect, Page
from pages.homepage import HomePage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('homepage.feature')

@given(parsers.parse('I navigate to {homepage}'))
def navigate(homepage, page: Page):
    home = HomePage(page)
    home.navigate_to(homepage)

@then(parsers.parse('I see a {URL}'))
def check(URL, page):
    expect(page).to_have_url(re.compile(f'.*{URL}.*'))
