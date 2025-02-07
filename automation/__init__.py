from appium import webdriver
from appium.options.ios import XCUITestOptions
import json
import logging
from datetime import datetime

# 로거 셋업
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        today = datetime.now().strftime("%Y-%m-%d")
        file_handler = logging.FileHandler(f"{today}.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# 자동화에 필요한 driver를 초기화
def initialize_driver():
    with open('capabilities.json', 'r', encoding='utf-8') as f:
        capabilities = json.load(f)

    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

    logger.info("initialize appium driver settings")
    return driver


logger = setup_logger()
driver = initialize_driver()
__all__ = ['driver']
