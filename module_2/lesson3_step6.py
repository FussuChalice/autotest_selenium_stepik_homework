from selenium import webdriver
from selenium.webdriver.common.by import By
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
        driver.get("http://suninjuly.github.io/redirect_accept.html")

        first_window = driver.window_handles[0]

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        x = driver.find_element(By.ID, "input_value").text
        y = calc(int(x))

        answer = driver.find_element(By.ID, "answer")
        answer.send_keys(str(y))

        btn = driver.find_element(By.CLASS_NAME, "btn")
        btn.click()

    finally:
        time.sleep(2)
        pyperclip.copy(driver.switch_to.alert.text)
        pyperclip.paste()
        driver.quit()

if __name__ == "__main__":
    main()