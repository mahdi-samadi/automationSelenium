from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service= service)
actions = ActionChains(driver= driver)
driver.maximize_window()

driver.get('http://google.com')
search_box = driver.find_element('name', 'q')
# search_box.send_keys('selenium' + Keys.ENTER)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# actions.key_down(Keys.SHIFT).send_keys_to_element(search_box, 'selenium').perform()
actions.key_down(Keys.SHIFT).send_keys_to_element(search_box, 'selenium').key_up(Keys.SHIFT).send_keys(' selenium').perform()
sleep(2)
# search_box.clear()
search_box.click()
actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()

sleep(4)