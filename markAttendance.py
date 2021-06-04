from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.delete_all_cookies()
driver.get('https://lms-practice-school.bits-pilani.ac.in/login/index.php')

EMAIL = 'mail here'
PASSWORD = 'password here'

google = driver.find_element_by_xpath("//a[@title='Google']").click()
driver.implicitly_wait(10)
driver.find_element_by_name('identifier').send_keys(EMAIL)
driver.find_element_by_name('identifier').send_keys(Keys.RETURN)

driver.implicitly_wait(10)
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "password")))
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)
driver.implicitly_wait(10)

psStation = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "coursename"))
)
psStation.click()

button = driver.find_element_by_xpath("//span[@class='instancename' and contains(text(),'Attendance')]")
button.click()

