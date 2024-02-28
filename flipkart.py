from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Flipkart:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 40)

    def open_page_search_data(self, search, search1):
        self.driver.get(self.url)
        self.driver.maximize_window()

        search_box = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,'//div[@class="_2SmNnR"]/input[@type="text"]')))
        search_box.send_keys(search)
        search_box.send_keys(Keys.RETURN)

        search_box1 = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,'//div[@class="_3OO5Xc"]/input[@class="_3704LK"]')))

        search_box1.clear()   # clear the already existed content using clear() method
        search_box1.send_keys(search1)
        search_box1.send_keys(Keys.RETURN) 

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@title="BELCO SPORTS PU Baseball"]'))).click()

    def page_source(self):
        all_windows = self.driver.window_handles
        new_window = all_windows[-1] #switch to latest window
        self.driver.switch_to.window(new_window)
        page_data = self.driver.page_source  # get the Page source data of the last active tab or window
        with open("flipkart.txt",mode ="w") as file:
                file.write(page_data)
                print("The Page_source data is written on flipkart.txt file")
          
url = 'https://www.flipkart.com'
call = Flipkart(url)
search = "q"
search1 = "baseball"
call.open_page_search_data(search, search1)
call.page_source()
