from utils.webdriver import WebDriver


class UkrNet:

    def __init__(self, driver, url):
        self.driver = WebDriver(driver=driver)
        self.bot_prod_start_url = url
        self.logo = '//a[@href="//www.ukr.net/"]/img'
        self.login_input = '//*[contains(@id, "login")]'
        self.password_input = '//*[contains(@id, "password")]'
        self.user_email = '//*[contains(@class, "email")]'
        self.mail_iframe = "mail widget"
        self.button = '//button[contains(@class, "{}")]'

    def go_main_page(self):
        self.driver.go_to_url(self.bot_prod_start_url)
        self.driver.wait_for_visibility_of_web_element(self.logo)

    def logging_in(self, email, password):
        self.driver.switch_to_iframe(self.mail_iframe)
        self.driver.wait_for_visibility_of_web_element(self.login_input)
        self.driver.set_web_element_text(self.login_input, email)
        self.driver.wait_for_visibility_of_web_element(self.password_input)
        self.driver.set_web_element_text(self.password_input, password)
        self.driver.click_web_element(self.button.format("submit"))
        self.driver.wait_for_visibility_of_web_element(self.user_email)
        email = self.driver.get_web_element_text(self.user_email)
        self.driver.wait_for_web_element_to_be_clickable(self.button.format("logout"))
        self.driver.click_web_element(self.button.format("logout"))
        text = self.driver.get_web_element_text(self.button.format("submit"))
        self.driver.switch_to_default()
        return {"email": email, "text": text}

    # def logging_out(self, action):
    #     self.driver.wait_for_web_element_to_be_clickable(self.button.format(action))
    #     self.driver.click_web_element(self.button.format(action))
    #     text = self.driver.get_web_element_text(self.button.format("submit"))
    #     self.driver.switch_to_default()
    #     return text
