# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_site_about = 'https://tensor.ru/about'
contacts_text = 'Контакты'

# Открываем браузер (создаем экземпляр браузера)
driver = webdriver.Chrome()
try:
    # Переходим на страницу
    driver.get(sbis_site)
    # Проверяем, что открылся именно нужный нам сайт
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    # Перейти в раздел "Контакты"
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1 [href = "/contacts"]')
    assert contacts.text == contacts_text, "Не верная вкладка или название вкладки"
    assert contacts.accessible_name == contacts_text, "Не верная вкладка или название вкладки"
    # На отображение проверять обязательно
    assert contacts.is_displayed()

    # Перейти в раздел "Контакты"
    contacts.click()
    time.sleep(1)
    # Найти баннер Тензор, кликнуть по нему
    tensor_banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8')
    tensor_banner.click()
    # При клике на баннер Тензора открывается новое окно (строчка ниже переходит в это окно)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # Ищем силу в людях
    time.sleep(1)
    # Проверить, что есть блок новости "Сила в людях"
    strength_in_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card>p')
    assert strength_in_people.text == 'Сила в людях'
    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    time.sleep(1)
    more_info = driver.find_element(By.CSS_SELECTOR,'[href="/about"]')
    time.sleep(1)
    more_info.click()
    time.sleep(1)
    assert driver.current_url == tensor_site_about, f"Не сайт {tensor_site_about}"
    print("Тест прошел")
finally:
    # Чтобы браузер всегда закрывался
    driver.quit()
