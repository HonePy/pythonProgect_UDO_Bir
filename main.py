from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
import random
import os
from dotenv import load_dotenv, find_dotenv


# Переменная
load_dotenv(find_dotenv())

login = (os.getenv('LOGIN'))
password = (os.getenv('PASSWORD'))

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox()


# Заходим на сайт Одноклассников
driver.get("https://ok.ru")


# Логинимся в Одноклассниках
login_input = driver.find_element('xpath', '(//input[@type="text"])[2]')
login_input.clear()
login_input.send_keys(login)
time.sleep(2)

password_input = driver.find_element('xpath', '//input[@type="password"]')
password_input.clear()
password_input.send_keys(password)
time.sleep(3)

button_tap = driver.find_element('xpath', '//input[@type="submit"]')
button_tap.send_keys(Keys.ENTER)
time.sleep(5)


# Записываем печеньки для входа без авторизации
# cookie = driver.get_cookies()
#
# with open('cookies.json', 'w') as file:
#     json.dump(cookie, file)

# Считываем печеньки для входа без авторизации
# with open('cookies.json', 'r') as file:
#     cookie = json.load(file)
#
# for c in cookie:
#     driver.add_cookie(c)
# driver.refresh()
# time.sleep(4)



# Поиск поля ввода для ввода локации
find_input = driver.find_element('xpath','//input[@class="input__prt1l __size-m__prt1l input__mofy2 input-field__on39s __right-icon__on39s"]')
find_input.clear()
find_input.send_keys('Биробиджан')
find_input.send_keys(Keys.ENTER)
time.sleep(random.randrange(5,7))


# Поиск позиции "Люди" в локации Хабаровск
try:
    button_users = driver.find_element('xpath', '//button[@id="tab-users"]')
    time.sleep(random.randrange(3, 6))
    button_users.send_keys(Keys.ENTER)
    time.sleep(random.randrange(3,6))
    print('Кнопка Люди найдена...')
    time.sleep(4)

except Exception:
   print('Humans not found...')
#
# #Скроллим страницы для сбора ссылок юзеров
for i in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # time.sleep(random.randrange(1,2))
    print(f"Итерация №{i}")

#Поиск и сбор ссылок позиции "Люди" локации

hrefs = driver.find_elements('xpath', '//a[@class="link__91azp title-link__79ad9 __primary__91azp"]')

users_urls = []

for i in hrefs:
    href = i.get_attribute('href')
    users_urls.append(href)
    print(href)
    # time.sleep(random.randrange(1,2))

    for url in users_urls:
        driver.get(url)
        time.sleep(random.randrange(2,3))

    try:
        button_users_offer = driver.find_element('xpath', '(//a[@class="u-menu_a"])[4]')
        button_users_offer.send_keys(Keys.ENTER)
        time.sleep(random.randrange(2,4))
        print('Кнопка добавить в друзья нажата...')


    except Exception:
        time.sleep(random.randrange(3, 5))
        print("Это уже наш друг. Ищем друзей далее...")


        try:
            button_massage = driver.find_element('xpath', '(//a[@class="u-menu_a "])[8]')
            button_massage.send_keys(Keys.ENTER)
            print('Кнопка "написать" нажата...')
            time.sleep(random.randrange(5,7))

        except Exception:
            # time.sleep(random.randrange(3, 5))
            print("Ошибка button_massage обработана...")

        try:
            massage_frands = driver.find_element('xpath', '//div[@class="js-lottie-observer"]')
            print('Поле ввода сообщения готово...')
            time.sleep(random.randrange(2, 5))


            massage_frands.send_keys('Привет. Реальная помощь по вопросам УДО и замене наказания на менее строгое. Актуальная и полезная информация.'
                                 )
            massage_frands.send_keys(Keys.ENTER)
            time.sleep(random.randrange(5, 8))
            print('Message sended...')

        except Exception:
            print("Ошибка ввода ссылки обработана...")



driver.close()
driver.quit()


if __name__ == '__main__':
     main()
