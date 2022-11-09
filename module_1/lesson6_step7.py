from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://suninjuly.github.io/huge_form.html")

        elements = driver.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("Something on the way")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        alert = driver.switch_to.alert
        print(alert.text)
        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
    main()