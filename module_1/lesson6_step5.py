from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def main():
    link = "http://suninjuly.github.io/find_link_text_redirect13.html"

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)
        
        first_name_input = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input")
        first_name_input.send_keys("Max")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
        last_name_input.send_keys("Smith")

        city_input = driver.find_element(By.CLASS_NAME, "city")
        city_input.send_keys("London")

        country_input = driver.find_element(By.ID, "country")
        country_input.send_keys("United Kingdom")

        button_submit = driver.find_element(By.ID, "submit_button")
        button_submit.click()

    finally:
        time.sleep(30)





if __name__ == "__main__":
    main()