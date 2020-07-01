from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "mrbond1"
accessKey = "SBcceAmgx2r9xtFkGELs"
desired_cap = {
  'device': 'Google Pixel 3',
  'os_version': '9.0'
}
desired_cap['project'] = 'My First Project'
desired_cap['build'] = 'My First Build'
desired_cap['name'] = 'Bstack-[Python] Sample Test'
desired_cap['app'] = "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c"

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)

search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()
