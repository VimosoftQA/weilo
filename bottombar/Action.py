from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from bottombar import driver
import time

class Action:
    """
    자동화 동작에 필요한 기능들을 정의한 클래스
    """

    action_chain = ActionChains(driver)

    def click(self,value):
        driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = value).click()

    def click_name(self,value):
        driver.find_element(by = AppiumBy.NAME , value = value).click()

    def click_class_name(self,value):
        driver.find_element(by = AppiumBy.CLASS_NAME, value = value).click()

    def click_coordinate(self,value : dict): #{x : n , y : m}
        X = value.get("x")
        Y = value.get("y")
        driver.tap([(X,Y)])

    def double_click(self,value):
        element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
        params = { 'elementId': element.id, 'count': 2 } # 탭 횟수
        driver.execute_script('mobile: doubleTap', params)

    def find(self,value):
        element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
        return element
    
    def find_name(self,value):
        element = driver.find_element(by=AppiumBy.NAME, value=value)
        return element

    def find_class_name(self,value):
        element = driver.find_element(by=AppiumBy.CLASS_NAME, value = value)
        return element

    def long_press(self,value):
        driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = value).long_click()

    def long_press_name(self,value):
        driver.find_element(by = AppiumBy.NAME , value = value).long_click()

    def swipe(self,sx, sy, ex, ey):
        driver.swipe(start_x=sx, start_y=sy, end_x= ex, end_y= ey)

    def screenshot(self,route):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"screenshot_{route}_{timestamp}"
        driver.save_screenshot(f'screenshot/{screenshot_name}.png')

    def find_element_coordinate(self,value) -> dict:
        # 임의의 요소의 좌표를 리턴
        element_location = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value).location
        return element_location # location이 dictionary 의 형태로 반환됨

    def drag_and_drop(self,draggable_id,droppable_id):
        draggable = driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = draggable_id)
        droppable = driver.find_element(by = AppiumBy.ACCESSIBILITY_ID , value = droppable_id)

        actions = ActionChains(driver)
        actions.click_and_hold(draggable).pause(1).move_to_element(droppable).perform()

