from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import math
import time

def calc(x):
    return math.log(abs(12*math.sin(x)))

def main():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://suninjuly.github.io/explicit_wait2.html")
        button = driver.find_element(By.ID, "book")

        price = WebDriverWait(driver, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )   
        
        assert price == "$100", price_one(driver, button)

    finally:
        time.sleep(1)
        pyperclip.copy(driver.switch_to.alert.text)
        pyperclip.paste()
        driver.quit()


def price_one(driver, button):
    button.click()
    x = driver.find_element(By.ID, "input_value").text
    print(x)
    y = calc(int(x))

    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(str(y))
    driver.find_element(By.ID, "solve").click()


if __name__ == "__main__":
    main()