from browser import driver, logger
from Action import Action
import time

def checkNetwork():
    action = Action()
    driver.activate_app('com.apple.Preferences') # 설정 앱 들어가기
    time.sleep(1)
    action.click("com.apple.settings.wifi") # 와이파이 설정 탭으로 들어가기
    logger.info("[iOS Settings > WIFI]")

    try:
        if action.find("checkmark"):
            logger.info("[iOS Settings > WIFI] activated WIFI")
            return True
    except:
        logger.info("[iOS Settings > WIFI] deactivated WIFI")
        return False











