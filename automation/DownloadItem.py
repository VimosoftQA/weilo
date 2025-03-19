import time
from automation import logger, driver
from Action import Action
from Network import checkNetwork
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
action = Action()
isConnection = checkNetwork()
driver.activate_app(os.getenv("APP_NAME"))

def download_item():

    if isConnection:
        icon = "inspector_download_ic"
        coordinate = action.find_element_coordinate(icon)
        action.click_coordinate(coordinate)
        logger.info("Success to download item")
        return  coordinate
    else:
        time.sleep(1)
        action.find("네트워크 연결 상태를 확인하세요")
        logger.info("Failed to download item")
        return False

if __name__ == '__main__':
    result = download_item()

