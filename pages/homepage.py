from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = self.page.locator('#username')
        self.password = self.page.locator('#password')
        self.CXP_image = self.page.locator(".loginImage").first
        self.signin_text = self.page.get_by_text("Sign in", exact=True)
        self.username_text = self.page.get_by_text("Username", exact=True)
        self.password_text = self.page.get_by_text("Password", exact=True)
        self.forgot_password = self.page.get_by_role("link", name="Forgot password?")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.single_sign_on_button = self.page.get_by_role("link", name="Use Single Sign On")
        self.privacy_policy_link = self.page.get_by_role("link", name="Privacy Policy")
        self.rightmenu = page.locator('xpath=//*[@id="rightMenuItems"]/li[1]/b/span')

    def navigate_to(self, URL):
        self.page.goto(URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
