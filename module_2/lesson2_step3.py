from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://suninjuly.github.io/selects2.html")

        num_a = driver.find_element(By.ID, "num1").text
        num_b = driver.find_element(By.ID, "num2").text
        sum = str(int(num_a) + int(num_b))

        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value(sum)

        btn = driver.find_element(By.CLASS_NAME, "btn")
        btn.click()

    finally:
        print(driver.switch_to.alert.text)
        driver.quit()

if __name__ == "__main__":
    main()