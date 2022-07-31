from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper:
    def access_website(self):
        driver = webdriver.Chrome()
        driver.get("http://books.toscrape.com/index.html")

        return driver

    def get_titles(self):
        title_elements = self.access_website().find_elements(
            By.CSS_SELECTOR, "h3 > a"
        )
        title_list = [
            [title.get_attribute("title")] for title in title_elements
        ]

        return title_list

    def get_prices(self):
        return self.access_website().find_elements(
            By.CLASS_NAME, "price_color"
        )

    def generate_information_list(self):
        titles = self.get_titles()
        prices = self.get_prices()
        for index, price in enumerate(prices):
            titles[index].append(price.text)

        return titles
