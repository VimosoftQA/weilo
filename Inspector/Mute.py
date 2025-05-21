from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import Inspector
import time

class MuteAction:
    def __init__(self):
        self.driver = Inspector.initialize_driver()
        self.action = ActionChains(self.driver)
        self.logger = Inspector.setup_logger()

    # ID로 값 탭하기
    def tap_element(self,id):
        self.driver.find_element(by=By.ID, value=id).click()

class Mute:
    def __init__(self):
        self.mute_action = MuteAction()

    # 음소거 인스펙터 열기
    def open_mute_inspector(self):
        self.mute_action.tap_element("inspector_mute")
        self.mute_action.logger.info("[Mute] Open Mute Inspector")

    # 음소거 활성화
    def activate_mute(self):
        self.mute_action.tap_element("mute_mute_toggle_switch")
        self.mute_action.logger.info("[Mute] Activate Mute")

    # 음소거 비활성화
    def deactivate_mute(self):
        self.mute_action.tap_element("mute_mute_toggle_switch")
        self.mute_action.logger.info("[Mute] Deactivate Mute")

    # 음소거 인스펙터 닫기
    def close_mute_inspector(self):
        self.mute_action.tap_element("inspector_mute")
        self.mute_action.logger.info("[Mute] Close Mute Inspector")


if __name__ == '__main__':
    mute = Mute()
    mute.open_mute_inspector()
    mute.activate_mute()
    mute.deactivate_mute()
    mute.close_mute_inspector()
