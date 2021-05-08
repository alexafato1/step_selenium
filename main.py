from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
from bs4 import BeautifulSoup
from math import  sin
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="/Users/alexafato/Desktop/step_selenium/chrome/chromedriver")
driver.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    """
    html = driver.page_source
    # print(html)
    with open(f"projectslink.html", "w") as file:
        file.write(html)

    with open(f"projectslink.html") as file:
        src = file.read()
        soup = BeautifulSoup(src, "lxml")
    """
    #staleness_of
    driver.implicitly_wait(2)
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    button = driver.find_element_by_id("book")
    button.click()

    x = driver.find_element_by_id('input_value').text
    #
    print(x)
    # num2 = driver.find_element_by_id('num2').text

    num = math.log((abs(12 * sin(int(x)))))

    driver.find_element_by_id("answer").send_keys(str(num))
    button1 = driver.find_element_by_id("solve")
    button1.click()

    """
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    rc = driver.find_element_by_id('robotCheckbox')
    print(rc)  # robotsRule"  # robotCheckbox
    rc.click()
    rr = driver.find_element_by_id('robotsRule')
    rr.click()  # robotsRule
    
    button = driver.find_element_by_tag_name("button")
    button.click()
    driver.switch_to.window(first_window)

       #alert = driver.switch_to.alert
       #alert.accept()

       new_window = driver.window_handles[1]
       first_window = driver.window_handles[0]
       driver.switch_to.window(new_window)
       
        inputs = driver.find_element_by_class_name('form-group').find_elements_by_tag_name('input')
    for i in inputs:
        i.send_keys('Hello')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = driver.find_element_by_id('file')
    element.send_keys(file_path)
       """


finally:
    time.sleep(30)
    driver.quit()