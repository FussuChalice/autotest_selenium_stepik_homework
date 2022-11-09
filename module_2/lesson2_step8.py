from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def_firstname = "Rick"
def_lastname = "Lermont"
def_email = "lermont@gmail.com"

def main():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://suninjuly.github.io/file_input.html")

        current_dir = os.path.abspath(os.path.dirname(__file__))

        firstNameInput = driver.find_element(By.NAME, "firstname")
        lastNameInput = driver.find_element(By.NAME, "lastname")
        emailInput = driver.find_element(By.NAME, "email")

        firstNameInput.send_keys(def_firstname)
        lastNameInput.send_keys(def_lastname)
        emailInput.send_keys(def_email)

        fileInput = driver.find_element(By.ID, "file")
        file_path = os.path.join(current_dir, 'file.txt')  

        fileInput.send_keys(file_path)

        button = driver.find_element(By.CLASS_NAME, "btn")
        button.click()

    finally:
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.quit()

if __name__ == "__main__":
    main()