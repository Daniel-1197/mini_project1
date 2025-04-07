import pytest
from guvi_page import GuviPage

@pytest.mark.usefixtures("invoke_browser")
class TestGuvi:
    def setup_method(self):
        self.page = GuviPage(self.driver)
        self.page.open()

    def test_url(self):
        assert "https://www.guvi.in" in self.driver.current_url,"URL not valid"

    def test_title(self):
        assert self.page.get_title() == True, "Title does not match"

    def test_login_button(self):
        assert self.page.is_login_visible(), "Login button is not visible"
        assert self.page.is_login_clickable(), "Login button is not clickable"

    def test_signup_button(self):
        assert self.page.is_signup_visible(), "Sign-up button is not visible"
        assert self.page.is_signup_clickable(), "Sign-up button is not clickable"

    def test_signup_page_exists(self):
        assert self.page.test_signup_url_validity(), "Sign-in page not accessible"

    def test_login_and_logout(self):
            assert self.page.login(), "Login with user credentials failed"
            assert self.page.logout(), "Logout failed"

    def test_invalid_login(self):
            assert self.page.invalid_login(),"Login failed with Invalid credentials"
