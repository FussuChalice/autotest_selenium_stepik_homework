from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import math
import time

# Tkinter for put to clipboard
from tkinter import Tk

def calc(x):
    return math.log(abs(12*math.sin(x)))

def main():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://suninjuly.github.io/alert_accept.html")

        btn = driver.find_element(By.CLASS_NAME, "btn")
        btn.click()

        f_alert = driver.switch_to.alert
        f_alert.accept()

        x = driver.find_element(By.ID, "input_value").text
        y = calc(int(x))

        answer = driver.find_element(By.ID, "answer")
        answer.send_keys(str(y))

        btn = driver.find_element(By.CLASS_NAME, "btn")
        btn.click()

    finally:
        pyperclip.copy(driver.switch_to.alert.text)
        pyperclip.paste()


if __name__ == "__main__":
    main()