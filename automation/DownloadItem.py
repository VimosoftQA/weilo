import time
from automation import logger, driver
from Action import Action
from Network import checkNetwork
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

def download_item():

    action = Action()
    isConnection = checkNetwork()

    driver.activate_app(os.getenv("APP_NAME"))
    action.click("inspector_download_ic")

    if isConnection:
        logger.info("Success to download item")

    else:
        time.sleep(1)
        action.find("네트워크 연결 상태를 확인하세요")
        logger.info("Failed to download item")


if __name__ == '__main__':
    download_item()

