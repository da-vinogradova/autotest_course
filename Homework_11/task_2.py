# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep

url_fix = 'https://fix-online.sbis.ru/auth/'
my_login = 'Oduvanchik2'
my_pass = 'Пароль123'
my_name = 'Одуванчиков Одуванчик'
my_text = 'Привет, Одуванчик'

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.get(url_fix)
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(my_login, Keys.ENTER)
    assert login.get_attribute('value') == my_login

    pass_on_page = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    pass_on_page.send_keys(my_pass, Keys.ENTER)
    sleep(7)
    # my_mac = driver.find_element(By.XPATH, "//*[contains(text(), 'Нет, личное')]")
    # my_mac.click()
    # time.sleep(2)
    # Перейти в реестр Контакты
    page_contacts = driver.find_element(By.CSS_SELECTOR, '[href="/page/dialogs"]')
    page_contacts.click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Контакты')]").click()
    # Отправить сообщение самому себе
    sleep(1)
    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    add_btn.click()
    sleep(1)
    search = driver.find_element(By.CSS_SELECTOR, 'input[tabindex="0"]')
    search.send_keys(my_name)
    driver.find_element(By.CSS_SELECTOR, '[data-qa = "item"]').click()
    sleep(4)
    # Написать сообщение
    text_msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_msg.send_keys(my_text)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]').click()
    sleep(2)
    # Убедиться, что сообщение появилось в реестре
    new_msg_aut = driver.find_elements(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee')
    assert new_msg_aut[0].text == my_name

    first_msg_txt = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')
    assert first_msg_txt[0].text == my_text
    sleep(4)

    # Удалить это сообщение и убедиться, что удалили
    action_chains = ActionChains(driver)
    action_chains.move_to_element(first_msg_txt[0])
    action_chains.context_click(first_msg_txt[0])
    action_chains.perform()
    sleep(1)

    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-target = "menu_item_deleteToArchive"]')
    delete_button.click()
    sleep(2)

    first_msg_txt = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')
    assert first_msg_txt[0].text != my_text, "Сообщение не удалено"

    print("Все ок")
finally:
    driver.quit()
