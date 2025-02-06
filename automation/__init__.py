from appium import webdriver
from appium.options.ios import XCUITestOptions
import json
# 자동화에 필요한 driver를 초기화

def initalize_driver():
    with open('capabilities.json', 'r', encoding='utf-8') as f:
        capabilities = json.load(f)

    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

    return driver


driver = initalize_driver()
__all__ = ['driver']
