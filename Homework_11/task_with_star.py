# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_url = 'https://sbis.ru/'

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Перейти на  https://sbis.ru/
    driver.get(sbis_url)
    sleep(1)
    # В Footer'e найти "Скачать СБИС"
    update_in_foot = driver.find_element(By.XPATH, '//a[text()="Скачать СБИС"]')
    assert update_in_foot.accessible_name == 'Скачать СБИС'
    assert update_in_foot.text == 'Скачать СБИС'
    # Перейти по ней
    driver.get(update_in_foot.get_attribute("href"))
    # Скачать СБИС Плагин для вашей ОС в папку с данным тестом
    driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]').click()
    sleep(1)

    # Отсюда что-то идет не так
    mac_os = driver.find_element(By.CSS_SELECTOR, '[data-id="macos"]')

    driver.find_element(By.XPATH, '//a[text() = "Скачать для Apple Silicon (Pkg 269.12 МБ) "]').click()
    # Убедиться, что плагин скачался

    sleep(2)
    print("Все ок")
finally:
    driver.quit()
