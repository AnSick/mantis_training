from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
import string
import random

class Application():
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.session = SessionHelper(self)
        self.baseUrl = baseUrl
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        # Open homepage
        if not wd.current_url.endswith("mantisbt-2.1.0/my_view_page.php"):
            wd.get(self.baseUrl)


    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def destroy(self):
        self.wd.quit()
