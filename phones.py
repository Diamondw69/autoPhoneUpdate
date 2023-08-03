from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
# Скрипт для автоматического обновления телефонов грандстрим
# Устанавливается поддержка 802.1.х, а также обновление прошивки через tftp 
# Перед любыми изменениями рекомендую изучить selenium через сайт https://selenium-python.readthedocs.io/ 

# Тут вводить айпи адреса
phone_ip_address = ["10.6.3.8","10.6.3.143","10.6.3.141","10.6.3.128","10.6.3.136","10.6.3.142",
                    "10.6.3.6","10.6.3.17","10.6.3.11","10.6.3.12","10.6.3.13","10.6.3.139","10.6.3.148",
                    "10.6.3.149","10.6.3.126","10.6.3.131","10.6.3.9","10.6.3.134","10.6.3.5","10.6.3.7",
                    "10.6.3.130","10.6.3.124","10.6.3.10"]

# Логин пароль для входа
login = "admin"
passwd = "3nf85S!"
identity = "phone"
MD5passwd= "Grand2023"

def automate_phone_settings():
    # Тут не трогать, настройка дров для браузера
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    
    # Цикл по айпи адресам 
    for ip in phone_ip_address:

     try:
        # Переход по адресу
        driver.get(f"http://{ip}")

        # В данном этапе происходит поиск HTML элементов для взаимодействия  
        # Элементы страницы по классу 
        loginTextBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-TextBox")))
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-PasswordTextBox")))
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-Button")))

        # С элемента убираются данные, и вставляются другие (Логин и пароль)
        loginTextBox.clear()
        loginTextBox.send_keys(login)
        password.clear()
        password.send_keys(passwd)

        # Пауза между этапами для загрузки страниц

        time.sleep(1)

        submitButton.click()

        time.sleep(3)

        # Переход на страницу для настройки 802.1.х

        driver.get(f"http://{ip}/#page:network_advance")

        time.sleep(3)

        select = Select(driver.find_element(By.NAME,"P7901"))
        select.select_by_value('3')

        time.sleep(3)

        identityTextBox =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "P7902")))
        
        identityTextBox.clear()
        identityTextBox.send_keys(identity)

        time.sleep(1)

        MD5Password =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "P7903")))
        
        MD5Password.clear()
        MD5Password.send_keys(MD5passwd)
        
        time.sleep(1)

        elementUpload = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Upload"]')))

        elementUpload.click()
        time.sleep(1)

        elementButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'gwt-FileUpload')))

        # Здесь нужно ввести путь к файлу pem 

        elementButton.send_keys(r'C:\Users\almaz\Downloads\radius.pem')

        time.sleep(5)
  

        elementUps = driver.find_elements(By.CLASS_NAME,"gwt-Button")
        elementUps[7].click()

        time.sleep(10)
        x=driver.find_elements(By.CLASS_NAME,"closebtn")
        x[1].click()
        time.sleep(3)

        SaveAndApply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save and Apply"]')))

        SaveAndApply.click()

        time.sleep(1)

        # Переход на страницу для настройки обновы

        driver.get(f"http://{ip}/#page:maintenance_upgrade")

        time.sleep(2)

        UpgradeEveryDay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[text()="Yes, check for upgrade every day"]')))

        UpgradeEveryDay.click()

        time.sleep(1)

        tftp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'P6767')))

        tftp.click()

        time.sleep(1)

        #Адрес tftp с которого телефон будет брать обновления

        tftpAddress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'P192')))

        tftpAddress.clear()
        tftpAddress.send_keys("10.1.0.36")

        time.sleep(2)

        SaveApply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save and Apply"]')))

        SaveApply.click()

        time.sleep(4)

        rebootButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'reboot')))

        rebootButton.click()
        time.sleep(3)

        okButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="OK"]')))
        okButton.click()
        time.sleep(3)

        # Победа, для проверки нужно проверить терминал

        print("Phone settings at"+ip +"updated successfully!")

     except Exception as e:
        print(ip+"An error occurred:", str(e))
    # Закрываем окно браузера
    driver.close()


# Функция для обновления телефона моментально
def automate_phone_update():
    # Тут не трогать, настройка дров для браузера
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    
    # Цикл по айпи адресам 
    for ip in phone_ip_address:

     try:
        # Переход по адресу
        driver.get(f"http://{ip}")

        
        # В данном этапе происходит поиск HTML элементов для взаимодействия  
        # Элементы страницы по классу 
        loginTextBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-TextBox")))
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-PasswordTextBox")))
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-Button")))

        # С элемента убираются данные, и вставляются другие (Логин и пароль)
        loginTextBox.clear()
        loginTextBox.send_keys(login)
        password.clear()
        password.send_keys(passwd)

        # Пауза между этапами для загрузки страниц

        time.sleep(1)

        submitButton.click()

        time.sleep(3)

        # Переход на страницу для настройки обновы

        driver.get(f"http://{ip}/#page:maintenance_upgrade")

        time.sleep(2)

        tftp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'P6767')))

        tftp.click()

        time.sleep(1)

        #Адрес tftp с которого телефон будет брать обновления

        tftpAddress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'P192')))

        tftpAddress.clear()
        tftpAddress.send_keys("10.1.0.36")

        time.sleep(2)

        saveButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Save and Apply"]')))

        saveButton.click()

        time.sleep(4)

        startButton =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Start"]')))
        startButton.click()

        time.sleep(2)

        # Победа, для проверки нужно проверить терминал

        print("Phone updated at"+ip)

     except Exception as e:
        print(ip+"An error occurred:", str(e))
    # Закрываем окно браузера
    driver.close()

# Функция для перезагрузки телефона моментально
def automate_phone_reboot():
    # Тут не трогать, настройка дров для браузера
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    
    # Цикл по айпи адресам 
    for ip in phone_ip_address:

     try:
        # Переход по адресу
        driver.get(f"http://{ip}")

        
        # В данном этапе происходит поиск HTML элементов для взаимодействия  
        # Элементы страницы по классу 
        loginTextBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-TextBox")))
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-PasswordTextBox")))
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gwt-Button")))

        # С элемента убираются данные, и вставляются другие (Логин и пароль)
        loginTextBox.clear()
        loginTextBox.send_keys(login)
        password.clear()
        password.send_keys(passwd)

        # Пауза между этапами для загрузки страниц

        time.sleep(1)

        submitButton.click()

        time.sleep(3)

        rebootButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'reboot')))

        rebootButton.click()

        time.sleep(3)


        # Победа, для проверки нужно проверить терминал

        print("Phone rebooted at"+ip)

     except Exception as e:
        print(ip+"An error occurred:", str(e))
    # Закрываем окно браузера
    driver.close()


# Запуск скрипта, для выбора достаточно убрать комменты
if __name__ == "__main__":
    automate_phone_settings()
    #automate_phone_reboot()
    #automate_phone_update()
