from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import math

def calc(x):
    y = math.log(abs(12*math.sin(x)))
    return y

def main():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://SunInJuly.github.io/execute_script.html")

        driver.execute_script("let bdFooter = document.querySelector('.bd-footer'); bdFooter.style.height = '0px';")

        iV = driver.find_element(By.ID, "input_value").text
        y = calc(int(iV))

        answer = driver.find_element(By.ID, "answer")
        driver.execute_script('return arguments[0].scrollIntoView(true);', answer)
        answer.send_keys(str(y))

        robotCheckBox = driver.find_element(By.ID, "robotCheckbox")
        driver.execute_script('return arguments[0].scrollIntoView(true);', robotCheckBox)
        robotCheckBox.click()

        robotsRule = driver.find_element(By.ID, "robotsRule")
        driver.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
        robotsRule.click()

        btn = driver.find_element(By.CLASS_NAME, "btn")
        driver.execute_script('return arguments[0].scrollIntoView(true);', btn)
        btn.click()


    finally:
        print(driver.switch_to.alert.text)
        driver.quit()

if __name__ == "__main__":
    main()