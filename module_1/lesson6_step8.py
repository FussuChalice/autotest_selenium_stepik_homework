from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def main():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://suninjuly.github.io/find_xpath_form")

        elements = driver.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("SYSTEM OF A DOWN")

        button = driver.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
        button.click()

    finally:
        alert = driver.switch_to.alert
        print(alert.text)

        driver.quit()

if __name__ == "__main__":
    main()