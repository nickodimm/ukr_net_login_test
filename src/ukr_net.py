import os
from utils.webdriver import WebDriver


class LOCATORS:
    logo = '//a[@href="//www.ukr.net/"]/img'
    login_input = '//*[contains(@id, "login")]'
    password_input = '//*[contains(@id, "password")]'
    user_email = '//*[contains(@class, "email")]'
    mail_iframe = "mail widget"
    button = '//button[contains(@class, "{}")]'


class UkrNet(WebDriver):

    def go_main_page(self):
        self.go_to_url(os.getenv("url"))
        self.wait_for_visibility_of_web_element(LOCATORS.logo)

    def logging_in(self, email, password):
        self.switch_to_iframe(LOCATORS.mail_iframe)
        self.wait_for_visibility_of_web_element(LOCATORS.login_input)
        self.set_web_element_text(LOCATORS.login_input, email)
        self.wait_for_visibility_of_web_element(LOCATORS.password_input)
        self.set_web_element_text(LOCATORS.password_input, password)
        self.click_web_element(LOCATORS.button.format("submit"))
        self.wait_for_visibility_of_web_element(LOCATORS.user_email)
        email = self.get_web_element_text(LOCATORS.user_email)
        return {"email": email}

    def logging_out(self):
        self.click_web_element(LOCATORS.button.format("logout"))
        text = self.get_web_element_text(LOCATORS.button.format("submit"))
        self.switch_to_default()
        return text
