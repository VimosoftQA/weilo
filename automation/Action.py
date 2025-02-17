from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from automation import driver
import time


class Action:
    """
    자동화 동작에 필요한 기능들을 정의한 클래스
    """

    # def __init__(self,driver):
    #     self.driver = driver

    def click(self,value):
        driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = value).click()
        return value

    def click_xpath(self,value):
        driver.find_element(by = AppiumBy.XPATH , value = value).click()

    def click_name(self,value):
        driver.find_element(by = AppiumBy.NAME , value = value).click()

    def click_class_name(self,value):
        driver.find_element(by = AppiumBy.CLASS_NAME, value = value).click()
    
    def click_ios_class_chain(self,value):
        driver.find_element(by = AppiumBy.IOS_CLASS_CHAIN, value = value).click()
        return value

    def find(self,value):
        element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
        return element
    
    def find_xpath(self,value):
        element = driver.find_element(by=AppiumBy.XPATH, value=value)
        return element
    
    def find_name(self,value):
        element = driver.find_element(by=AppiumBy.NAME, value=value)
        return element

    def find_class_name(self,value):
        element = driver.find_element(by=AppiumBy.CLASS_NAME, value = value)
        return element

    def double_click(self,value):
        driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = value).double_click()

    def double_click_name(self,value):
        driver.find_element(by = AppiumBy.NAME , value = value).double_click()

    def double_click_xpath(self,value):
        driver.find_element(by = AppiumBy.XPATH , value = value).double_click()

    def long_press(self,value):
        driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = value).long_click()

    def long_press_name(self,value):
        driver.find_element(by = AppiumBy.NAME , value = value).long_click()

    def long_press_xpath(self,value):
        driver.find_element(by = AppiumBy.XPATH , value = value).long_click()

    def swipe(self,sx, sy, ex, ey):
        driver.swipe(start_x=sx, start_y=sy, end_x= ex, end_y= ey)

    def tap_coordinate(self, X,Y,sec) : 
        driver.tap([(X,Y)],sec)

    def screenshot(self,route):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"screenshot_{route}_{timestamp}"
        driver.save_screenshot(f'screenshot/{screenshot_name}.png')


    # def scroll_by_ios_predicate(driver, text):
    #     """
    #     iOS Predicate String을 사용한 스크롤 (iOS 전용)
    #     :param driver: Appium 드라이버
    #     :param text: 찾고자 하는 텍스트
    #     :return: 찾은 요소 또는 None
    #     """
    #     try:
    #         return driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                                    f'label == "{text}" OR name == "{text}" OR value == "{text}"')
    #     except:
    #         return None



    



