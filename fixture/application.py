from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projects import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper

class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.session = SessionHelper(self)
        self.projects = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

 #   def return_to_home_page(self):
 #       wd = self.wd
 #       wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()