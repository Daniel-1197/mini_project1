from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class GuviPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.guvi.in"
        self.signin_url = "https://www.guvi.in/sign-in/"
        self.dashboard_url = "https://www.guvi.in/courses/?current_tab=myCourses"
        self.expected_title = "GUVI | Learn to code in your native language"
        self.login_button = (By.LINK_TEXT, "Login")
        self.signup_button = (By.LINK_TEXT, "Sign up")
        #for login page
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.submit = (By.ID,"login-btn")
        self.profile = (By.ID, "dropdown_title")
        self.signout_button = (By.XPATH, "//*[text()='Sign Out']")

    def open(self):
        self.driver.get(self.url)

    def is_url_valid(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title == self.expected_title

    def is_login_visible(self):
        try:
            return self.driver.find_element(*self.login_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_login_clickable(self):
        try:
            btn = self.driver.find_element(*self.login_button)
            btn.click()
            return True
        except NoSuchElementException:
            return False

    def is_signup_visible(self):
        try:
            return self.driver.find_element(*self.signup_button).is_displayed()
        except NoSuchElementException:
            return False

    def is_signup_clickable(self):
        try:
            btn = self.driver.find_element(*self.signup_button)
            btn.click()
            return True
        except NoSuchElementException:
            return False

    def test_signup_url_validity(self):
        try:
            self.driver.get(self.signin_url)
            if self.driver.title == "GUVI | Login":
                return True
        except TimeoutException:
            return False

    def login(self):
        self.driver.get(self.signin_url)
        try:
            self.driver.find_element(*self.email).send_keys("danielprem1197@gmail.com")
            self.driver.find_element(*self.password).send_keys("DannyShelbyBrother@1197")
            self.driver.find_element(*self.submit).click()
            WebDriverWait(self.driver, 10).until(
                expected_conditions.url_contains("courses")
            )
            return True
        except Exception:
            return False

    def logout(self):
        try:
            self.driver.find_element(*self.profile).click()
            self.driver.find_element(*self.signout_button).click()

            # After signing out, the login button should reappear
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(self.login_button)
            )
            return True
        except Exception:
            return False

    def invalid_login(self):
        self.driver.get(self.signin_url)
        try:
            self.driver.find_element(*self.email).send_keys("freakymanly@gmail.com")
            self.driver.find_element(*self.password).send_keys("password@123")
            self.driver.find_element(*self.submit).click()
            WebDriverWait(self.driver,10).until(
                expected_conditions.visibility_of_element_located(self.login_button)
            )
            return True
        except Exception:
            return False
