# -*- coding: utf-8 -*-
from automation import logger
from automation import id
from Action import Action
import time


class Filter:
    def __init__(self):
        self.action = Action()
        self.action.click("browser_my_button")
        time.sleep(1)
        logger.info("tap My browser")

        self.action.click("menu_current_project")
        time.sleep(1)
        logger.info("tap current project")


    # ID는 있으나 찾지를 못하는 경우
    def filter_all_items(self):
        self.action.click("current_project_filter_button")
        time.sleep(1)
        logger.info("tap project filter")

        self.action.click("all_item")
        time.sleep(1)
        logger.info("tap filter 모든 클립")


    def filter_single_clip(self):
        self.action.click("current_project_filter_button")
        time.sleep(1)
        logger.info("tap project filter")

        self.action.click("single_clip")
        time.sleep(1)
        logger.info("tap filter 단일 클립")


    def filter_folder(self):
        self.action.click("current_project_filter_button")
        time.sleep(1)
        logger.info("tap project filter")

        self.action.click("folder")
        time.sleep(1)
        logger.info("tap filter 폴더")




if __name__ == "__main__":
    filter = Filter()
    filter.filter_all_items()
    filter.filter_single_clip()
    filter.filter_folder()
