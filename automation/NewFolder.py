# 새 폴더를 생성
# -*- coding: utf-8 -*-
from automation import logger
from automation import id
from Action import Action
import time

class NewFolder:
    def __init__(self):
        self.action = Action()
        self.action.click("browser_my_button")
        time.sleep(1)
        logger.info("tap My browser")

        self.action.click("current_project_create_folder_button")
        time.sleep(1)
        logger.info("create new folder")


if __name__ == "__main__":
    newFolder = NewFolder()


