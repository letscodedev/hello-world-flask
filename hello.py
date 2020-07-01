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
desired_cap['app'] = "bs://<hashed app-id>"
 
driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)

//Write your code here

driver.quit()
