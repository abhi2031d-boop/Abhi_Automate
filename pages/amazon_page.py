from selenium.webdriver.common.by import By


class AmazonPage:

    def __init__(self, driver):
        self.driver = driver

    search_box = (By.ID, "twotabsearchtextbox")

    search_button = (By.ID, "nav-search-submit-button")

    def open(self):
        self.driver.get("https://www.amazon.in")

    def search_product(self, product):
        self.driver.find_element(*self.search_box).send_keys(product)
        self.driver.find_element(*self.search_button).click()