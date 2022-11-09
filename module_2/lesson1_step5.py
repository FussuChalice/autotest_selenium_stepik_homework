import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def main():
    link = "http://suninjuly.github.io/get_attribute.html"

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)

        treasure = driver.find_element(By.ID, "treasure")
        x = treasure.get_attribute("valuex")
        y = str(math.log(abs(12*math.sin(int(x)))))

        answer = driver.find_element(By.ID, "answer")
        answer.send_keys(y)

        robotCheckBox = driver.find_element(By.ID, "robotCheckbox").click()
        robotsRule = driver.find_element(By.ID, "robotsRule").click()

        defBtn = driver.find_element(By.CLASS_NAME, "btn").click()

    finally:
        time.sleep(1)
        alert = driver.switch_to.alert
        print(alert.text)
        
        driver.quit()


if __name__ == "__main__":
    main()