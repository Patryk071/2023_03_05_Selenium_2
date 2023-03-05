from selenium import webdriver
import time

#Jeśli import z selenium nie zadziała to trzeba w terminalu
#wpisać pip install selenium

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
time.sleep(10)

#driver.set_window_size(1200, 1000)
driver.maximize_window()

accept = driver.find_element("id", "accept-choices")
accept.click()

menu = driver.find_element("id", "navbtn_tutorials")
#Tutaj dopiero najeżdżamy na "Tutorials"
webdriver.ActionChains(driver).move_to_element(menu).perform()
#A tutaj klikamy
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

HTMLtutu = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[1]')
HTMLtutu.click()
# HTMLAtributs = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[64]')
# HTMLAtributs.click()

driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[64]').click()
driver.find_element('xpath', '//*[@id="main"]/div[3]/table/tbody/tr[32]/td[1]/a').click()
driver.find_element('xpath', '//*[@id="main"]/div[5]/a').click()

print(driver.title)

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles

for window in windowNames:
    if window != currentWindowName:
        driver.switch_to.window(window)

print(driver.title)
driver.find_element('xpath', '//*[@id="runbtn"]').click()

firstName = driver.find_element("id", "fname")

if firstName.is_enabled():
    firstName.send_keys("Kleopatra")
else:
    print("Nie da się wpisać tekstu")

firstName.clear()

#driver.find_element("id", "fname").send_keys("Natalia")

time.sleep(15)
driver.close()
