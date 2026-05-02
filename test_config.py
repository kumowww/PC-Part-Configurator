from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_incompatible_socket():
    driver = webdriver.Chrome()
    driver.get("file:///твоя_папка/index.html") # Укажи путь к файлу
    time.sleep(1)

    # Выбираем AMD CPU
    Select(driver.find_element(By.ID, "cpu-select")).select_by_value("1") 
    # Выбираем Intel Motherboard
    Select(driver.find_element(By.ID, "mobo-select")).select_by_value("2") 

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    if "Incompatible" in result:
        print("Test Passed: Incompatibility detected correctly.")
    else:
        print("Test Failed!")
    
    driver.quit()

if __name__ == "__main__":
    test_incompatible_socket()