import re
from credentials import Creds
from playwright.sync_api import expect, Page
from pages.homepage import HomePage
from pytest_bdd import scenarios, given, when, then, parsers

HOME = None
CREDS = Creds()

scenarios('homepage.feature')

# Given Step Section
# Place all Given steps in this section to make them more findable
@given(parsers.parse('I navigate to {homepage}'))
def navigate(homepage, page: Page):
    global HOME
    HOME = HomePage(page)
    HOME.navigate_to(homepage)

# When Step Section
# Place all When steps in this section to make them more findable
@when(parsers.parse('I fill in my {username} and {password} and hit enter'))
def login(username, password):
    HOME.login(getattr(CREDS, username), getattr(CREDS, password))

# Then Step Section
# Place all Then steps in this section to make them more findable
@then(parsers.parse('I see a {URL}'))
def check(URL, page):
    expect(page).to_have_url(re.compile(f'.*{URL}.*'))

@then(parsers.parse('I am logged in and my {name} appears top right'))
def confirm_name(name):
    expect(HOME.rightmenu).to_contain_text(name)

@then(parsers.parse('I see {Elements} on the page'))
def confirm_element(Elements):
    expect(getattr(HOME, Elements)).to_be_visible()

