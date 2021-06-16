from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
import time

config = ConfigParser()
config.read('./Library/Configuration.ini')
email = config.get('Login', 'email')
password = config.get('Login', 'password')
searchbar = config.get('search', 'product')
product = config.get('search', 'product name')

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

path = "F:\\cdweb\\chromedriver.exe"
driver = Chrome(options=option, executable_path= path)

driver.get("http://www.flipkart.com")
driver.maximize_window()
time.sleep(0.7)
driver.find_element_by_xpath('//*[@class="_2IX_2- VJZDxU"]').send_keys(email)
driver.find_element_by_xpath('//*[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@class="_2KpZ6l _2HKlqd _3AWRsL"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@type="text"]').send_keys(searchbar)
driver.find_element_by_xpath('//*[@type="submit"]').click()
time.sleep(3)
act = ActionChains(driver)
act.click(driver.find_element_by_xpath("//div[contains(text(),'" + product + "')]")).perform()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
act = ActionChains(driver)
act.click(driver.find_element_by_xpath('//*[@class="_2KpZ6l _2U9uOA _3v1-ww"]')).perform()
time.sleep(5)
driver.quit()
