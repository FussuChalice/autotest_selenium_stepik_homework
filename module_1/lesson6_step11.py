from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from webdriver_manager.chrome import ChromeDriverManager

_DEFAULT_FIRSTNAME_ = "Rick"
_DEFAULT_LASTNAME_  = "Sanchez"
_DEFAULT_EMAIL_     = "r.sanchez@gmail.com"

def main():
    try: 
        link = "http://suninjuly.github.io/registration2.html"

        # Создаем драйвер и передаем ссылку на регистрацию
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)

        # Заполняем обязательные поля
        first_input = driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_input.send_keys(_DEFAULT_FIRSTNAME_)

        second_input = driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        second_input.send_keys(_DEFAULT_LASTNAME_)

        third_input = driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        third_input.send_keys(_DEFAULT_EMAIL_)

        # Отправляем заполненную форму
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        driver.quit()


if __name__ == "__main__":
    main()