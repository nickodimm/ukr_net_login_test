from utils.webdriver import WebDriver


class LOCATORS:
    logo = '//a[@href="//www.ukr.net/"]/img'
    login_input = '//*[contains(@id, "login")]'
    password_input = '//*[contains(@id, "password")]'
    user_email = '//*[contains(@class, "email")]'
    mail_iframe = "mail widget"
    button = '//button[contains(@class, "{}")]'


class UkrNet:

    def __init__(self, driver, url):
        self.driver = WebDriver(driver=driver)
        self.bot_prod_start_url = url

    def go_main_page(self):
        self.driver.go_to_url(self.bot_prod_start_url)
        self.driver.wait_for_visibility_of_web_element(LOCATORS.logo)

    def logging_in(self, email, password):
        self.driver.switch_to_iframe(LOCATORS.mail_iframe)
        self.driver.wait_for_visibility_of_web_element(LOCATORS.login_input)
        self.driver.set_web_element_text(LOCATORS.login_input, email)
        self.driver.wait_for_visibility_of_web_element(LOCATORS.password_input)
        self.driver.set_web_element_text(LOCATORS.password_input, password)
        self.driver.click_web_element(LOCATORS.button.format("submit"))
        self.driver.wait_for_visibility_of_web_element(LOCATORS.user_email)
        email = self.driver.get_web_element_text(LOCATORS.user_email)
        self.driver.click_web_element(LOCATORS.button.format("logout"))
        text = self.driver.get_web_element_text(LOCATORS.button.format("submit"))
        self.driver.switch_to_default()
        return {"email": email, "text": text}

    # def logging_out(self, action):
    #     self.driver.wait_for_web_element_to_be_clickable(self.button.format(action))
    #     self.driver.click_web_element(self.button.format(action))
    #     text = self.driver.get_web_element_text(self.button.format("submit"))
    #     self.driver.switch_to_default()
    #     return text
