from Action import Action
import json
from browser import logger,driver
import time


class Voiceover:
    def __init__(self):
        self.action = Action()

    def tap_voiceover_button(self):
        self.action.click("voiceover_button")
        logger.info("[Browser > Voiceover] Tap voiceover")

    def allow_access_microphone(self):
        self.action.click("Allow")
        logger.info('[Browser > Voiceover] Allow access to Microphone')

    def dont_allow_access_microphone(self):
        self.action.click("Don’t Allow")
        logger.info("[Browser > Voiceover] Don't allow access to Microphone")

    def setting_voiceover(self):
        self.action.click("top setting ic")
        logger.info("[Browser > Voiceover] Setting voiceover")

    def back_setting_voiceover(self):
        self.action.click("inspector chevron left ic")
        logger.info("[Browser > Voiceover] Back setting voiceover")

    def close_voiceover(self):
        self.action.click("inspector close line ic")
        logger.info("[Browser > Voiceover] Close voiceover")

    # def rename_voiceover(self):
    #     self.setting_voiceover()
    #     element = self.action.find("Untitled") #TODO 이름을 입력하는 박스의 ID 필요함
    #     driver.execute_script('mobile: doubleTap', {'element': element.id})
    #     logger.info("[Browser > Voiceover] Rename voiceover clip")

    def start_voiceover(self):
        self.action.click("timeline mic ic")
        logger.info("[Browser > Voiceover] Start voiceover")
        self.action.screenshot("Voiceover")
        time.sleep(5)
        self.action.click("timeline mic ic")



if __name__ == '__main__':
    voiceover = Voiceover()
    voiceover.tap_voiceover_button()
    # voiceover.setting_voiceover()
    # voiceover.rename_voiceover()